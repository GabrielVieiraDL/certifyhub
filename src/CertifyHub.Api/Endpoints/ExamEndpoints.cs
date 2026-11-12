using CertifyHub.Api.DTOs;
using CertifyHub.Domain.Entities;
using CertifyHub.Domain.Enums;
using CertifyHub.Infrastructure.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace CertifyHub.Api.Endpoints;

public static class ExamEndpoints
{
    private const int QuestionsPerSession = 50;

    public static void MapExamEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/exams").WithTags("Exams");

        // Listar exames disponíveis
        group.MapGet("/", async (AppDbContext db) =>
        {
            var exams = await db.Exams
                .Include(e => e.Domains)
                .ThenInclude(d => d.Questions)
                .Select(e => new ExamDto(
                    e.Id,
                    e.Code,
                    e.Name,
                    e.TimeLimitMinutes,
                    e.PassingScore,
                    e.MaxScore,
                    e.Domains.Select(d => new SkillDomainDto(d.Id, d.Name, d.WeightPercent, d.Questions.Count)).ToList()
                ))
                .ToListAsync();

            return Results.Ok(exams);
        });

        // Detalhes do exame por código (ex: AZ-900)
        group.MapGet("/{code}", async (string code, AppDbContext db) =>
        {
            var exam = await db.Exams
                .Include(e => e.Domains)
                .ThenInclude(d => d.Questions)
                .FirstOrDefaultAsync(e => e.Code.ToUpper() == code.ToUpper());

            if (exam is null) return Results.NotFound();

            var dto = new ExamDto(
                exam.Id,
                exam.Code,
                exam.Name,
                exam.TimeLimitMinutes,
                exam.PassingScore,
                exam.MaxScore,
                exam.Domains.Select(d => new SkillDomainDto(d.Id, d.Name, d.WeightPercent, d.Questions.Count)).ToList()
            );

            return Results.Ok(dto);
        });

        // Estatísticas globais: quantas questões únicas o usuário já respondeu
        group.MapGet("/stats", async (AppDbContext db) =>
        {
            var totalPool = await db.Questions.CountAsync();

            // Questões únicas já respondidas em qualquer sessão finalizada
            var completedSessions = await db.ExamSessions
                .Where(s => s.Status == SessionStatus.Completed || s.Status == SessionStatus.Expired)
                .CountAsync();

            var totalAnswered = await db.UserAnswers.CountAsync();

            var uniqueQuestionsAnswered = await db.UserAnswers
                .Select(a => a.QuestionId)
                .Distinct()
                .CountAsync();

            var uniqueCorrect = await db.UserAnswers
                .Where(a => a.IsCorrect)
                .Select(a => a.QuestionId)
                .Distinct()
                .CountAsync();

            return Results.Ok(new ExamStatsDto(
                totalPool,
                QuestionsPerSession,
                completedSessions,
                totalAnswered,
                uniqueQuestionsAnswered,
                uniqueCorrect
            ));
        });

        // Estatísticas específicas de um exame (ex: AZ-900 ou AZ-104)
        group.MapGet("/{code}/stats", async (string code, AppDbContext db) =>
        {
            var exam = await db.Exams.FirstOrDefaultAsync(e => e.Code.ToUpper() == code.ToUpper());
            if (exam is null) return Results.NotFound();

            var totalPool = await db.Questions.CountAsync(q => q.Domain.ExamId == exam.Id);

            var completedSessions = await db.ExamSessions
                .Where(s => s.ExamId == exam.Id && (s.Status == SessionStatus.Completed || s.Status == SessionStatus.Expired))
                .CountAsync();

            var totalAnswered = await db.UserAnswers
                .Where(a => a.Session.ExamId == exam.Id)
                .CountAsync();

            var uniqueQuestionsAnswered = await db.UserAnswers
                .Where(a => a.Session.ExamId == exam.Id)
                .Select(a => a.QuestionId)
                .Distinct()
                .CountAsync();

            var uniqueCorrect = await db.UserAnswers
                .Where(a => a.Session.ExamId == exam.Id && a.IsCorrect)
                .Select(a => a.QuestionId)
                .Distinct()
                .CountAsync();

            return Results.Ok(new ExamStatsDto(
                totalPool,
                Math.Min(QuestionsPerSession, totalPool),
                completedSessions,
                totalAnswered,
                uniqueQuestionsAnswered,
                uniqueCorrect
            ));
        });
    }

    public static void MapSessionEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/sessions").WithTags("Sessions");

        // Criar nova sessão de simulado (Exame ou Estudo)
        // Seleciona 50 questões aleatórias do pool total
        group.MapPost("/", async ([FromBody] CreateSessionRequest req, AppDbContext db) =>
        {
            var exam = await db.Exams.FirstOrDefaultAsync(e => e.Code.ToUpper() == req.ExamCode.ToUpper());
            if (exam is null) return Results.NotFound("Exame não encontrado");

            // Buscar todas as questões do exame
            var allQuestionIds = await db.Questions
                .Where(q => q.Domain.ExamId == exam.Id)
                .Select(q => q.Id)
                .ToListAsync();

            // Selecionar 50 aleatórias (ou todas se o pool for menor)
            var rng = new Random();
            var selectedIds = allQuestionIds
                .OrderBy(_ => rng.Next())
                .Take(QuestionsPerSession)
                .ToList();

            var now = DateTime.UtcNow;
            var session = new ExamSession
            {
                Id = Guid.NewGuid(),
                ExamId = exam.Id,
                Mode = req.Mode,
                Status = SessionStatus.InProgress,
                StartedAt = now,
                ExpiresAt = req.Mode == ExamMode.Exam ? now.AddMinutes(exam.TimeLimitMinutes) : null,
                Seed = Random.Shared.Next(1, 1000000),
                SelectedQuestionIds = string.Join(",", selectedIds)
            };

            db.ExamSessions.Add(session);
            await db.SaveChangesAsync();

            return Results.Created($"/api/sessions/{session.Id}", new ExamSessionDto(
                session.Id,
                exam.Code,
                exam.Name,
                session.Mode,
                session.Status,
                session.StartedAt,
                session.ExpiresAt,
                selectedIds.Count,
                0
            ));
        });

        // Buscar dados da sessão
        group.MapGet("/{id:guid}", async (Guid id, AppDbContext db) =>
        {
            var session = await db.ExamSessions
                .Include(s => s.Exam)
                .Include(s => s.Answers)
                .FirstOrDefaultAsync(s => s.Id == id);

            if (session is null) return Results.NotFound();

            var sessionQuestionCount = session.SelectedQuestionIds
                .Split(',', StringSplitOptions.RemoveEmptyEntries)
                .Length;

            return Results.Ok(new ExamSessionDto(
                session.Id,
                session.Exam.Code,
                session.Exam.Name,
                session.Mode,
                session.Status,
                session.StartedAt,
                session.ExpiresAt,
                sessionQuestionCount,
                session.Answers.Count
            ));
        });

        // Retorna questões da sessão com embaralhamento determinístico e anti-cheating
        // Agora retorna apenas as 50 questões selecionadas para esta sessão
        group.MapGet("/{id:guid}/questions", async (Guid id, AppDbContext db) =>
        {
            var session = await db.ExamSessions
                .Include(s => s.Exam)
                .FirstOrDefaultAsync(s => s.Id == id);

            if (session is null) return Results.NotFound("Sessão não encontrada");

            // Parse the selected question IDs for this session
            var selectedIds = session.SelectedQuestionIds
                .Split(',', StringSplitOptions.RemoveEmptyEntries)
                .Select(Guid.Parse)
                .ToHashSet();

            var questions = await db.Questions
                .Include(q => q.Domain)
                .Include(q => q.Options)
                .Where(q => selectedIds.Contains(q.Id))
                .ToListAsync();

            // Embaralhamento determinístico usando o Seed da sessão (Fisher-Yates)
            var rng = new Random(session.Seed);
            var shuffledQuestions = questions.OrderBy(_ => rng.Next()).ToList();

            var isExam = session.Mode == ExamMode.Exam;

            var dtoList = shuffledQuestions.Select(q =>
            {
                var optRng = new Random(session.Seed + q.Number);
                var shuffledOptions = q.Options.OrderBy(_ => optRng.Next()).ToList();

                return new QuestionDto(
                    q.Id,
                    q.Number,
                    q.Domain.Name,
                    q.Type,
                    q.Statement,
                    shuffledOptions.Select(o => new OptionDto(
                        o.Id,
                        o.Letter,
                        o.Text,
                        isExam ? null : o.IsCorrect // Proteção anti-cheating no Modo Exame
                    )).ToList(),
                    isExam ? null : q.Explanation // Oculta explicação no Modo Exame
                );
            }).ToList();

            return Results.Ok(dtoList);
        });

        // Submeter resposta de uma questão
        group.MapPost("/{id:guid}/answer", async (Guid id, [FromBody] SubmitAnswerRequest req, AppDbContext db) =>
        {
            var session = await db.ExamSessions
                .Include(s => s.Exam)
                .Include(s => s.Answers)
                .FirstOrDefaultAsync(s => s.Id == id);

            if (session is null) return Results.NotFound("Sessão não encontrada");
            if (session.Status != SessionStatus.InProgress) return Results.BadRequest("Sessão já finalizada ou expirada");

            // Verifica se expirou o tempo
            if (session.ExpiresAt.HasValue && DateTime.UtcNow > session.ExpiresAt.Value)
            {
                session.Status = SessionStatus.Expired;
                await db.SaveChangesAsync();
                return Results.BadRequest("Tempo de exame esgotado");
            }

            var question = await db.Questions
                .Include(q => q.Options)
                .FirstOrDefaultAsync(q => q.Id == req.QuestionId);

            if (question is null) return Results.NotFound("Questão não encontrada");

            var correctIds = question.Options.Where(o => o.IsCorrect).Select(o => o.Id).ToHashSet();
            var userIds = req.SelectedOptionIds.ToHashSet();

            var isCorrect = correctIds.SetEquals(userIds);

            var existingAnswer = await db.UserAnswers
                .FirstOrDefaultAsync(a => a.SessionId == session.Id && a.QuestionId == req.QuestionId);

            if (existingAnswer is not null)
            {
                existingAnswer.SelectedOptionIds = string.Join(",", req.SelectedOptionIds);
                existingAnswer.IsCorrect = isCorrect;
                existingAnswer.AnsweredAt = DateTime.UtcNow;
            }
            else
            {
                var answer = new UserAnswer
                {
                    Id = Guid.NewGuid(),
                    SessionId = session.Id,
                    QuestionId = req.QuestionId,
                    SelectedOptionIds = string.Join(",", req.SelectedOptionIds),
                    IsCorrect = isCorrect,
                    AnsweredAt = DateTime.UtcNow
                };
                db.UserAnswers.Add(answer);
            }

            await db.SaveChangesAsync();

            // Count based on session's 50 questions, not total pool
            var sessionQuestionCount = session.SelectedQuestionIds
                .Split(',', StringSplitOptions.RemoveEmptyEntries)
                .Length;

            var answeredCount = await db.UserAnswers.CountAsync(a => a.SessionId == session.Id);

            return Results.Ok(new AnswerFeedbackDto(
                isCorrect,
                correctIds.ToList(),
                question.Explanation,
                answeredCount,
                sessionQuestionCount
            ));
        });

        // Finalizar sessão e calcular pontuação oficial
        group.MapPost("/{id:guid}/submit", async (Guid id, AppDbContext db) =>
        {
            var session = await db.ExamSessions
                .Include(s => s.Exam)
                .ThenInclude(e => e.Domains)
                .Include(s => s.Answers)
                .FirstOrDefaultAsync(s => s.Id == id);

            if (session is null) return Results.NotFound("Sessão não encontrada");

            // Parse selected question IDs for this session
            var selectedIds = session.SelectedQuestionIds
                .Split(',', StringSplitOptions.RemoveEmptyEntries)
                .Select(Guid.Parse)
                .ToHashSet();

            // Load only the questions that were part of this session
            var sessionQuestions = await db.Questions
                .Include(q => q.Domain)
                .Where(q => selectedIds.Contains(q.Id))
                .ToListAsync();

            var domains = session.Exam.Domains;
            double weightedScore = 0;
            int totalCorrect = 0;
            int totalQuestions = 0;

            foreach (var domain in domains)
            {
                var domainQuestionIds = sessionQuestions
                    .Where(q => q.DomainId == domain.Id)
                    .Select(q => q.Id)
                    .ToHashSet();

                var domainAnswers = session.Answers.Where(a => domainQuestionIds.Contains(a.QuestionId)).ToList();
                var domainCorrect = domainAnswers.Count(a => a.IsCorrect);
                var domainTotal = domainQuestionIds.Count;

                totalCorrect += domainCorrect;
                totalQuestions += domainTotal;

                if (domainTotal > 0)
                {
                    var domainPercentage = (double)domainCorrect / domainTotal;
                    weightedScore += domainPercentage * (domain.WeightPercent / 100.0) * session.Exam.MaxScore;
                }
            }

            var finalScore = (int)Math.Round(weightedScore);
            var passed = finalScore >= session.Exam.PassingScore;

            session.Status = SessionStatus.Completed;
            session.CompletedAt = DateTime.UtcNow;
            session.FinalScore = finalScore;
            session.Passed = passed;

            await db.SaveChangesAsync();

            return Results.Ok(new { message = "Exame finalizado com sucesso", finalScore, passed });
        });

        // Resultado completo e revisão de questões
        group.MapGet("/{id:guid}/result", async (Guid id, AppDbContext db) =>
        {
            var session = await db.ExamSessions
                .Include(s => s.Exam)
                .ThenInclude(e => e.Domains)
                .Include(s => s.Answers)
                .FirstOrDefaultAsync(s => s.Id == id);

            if (session is null) return Results.NotFound("Sessão não encontrada");
            if (session.Status != SessionStatus.Completed && session.Status != SessionStatus.Expired)
            {
                return Results.BadRequest("O exame ainda não foi finalizado");
            }

            // Parse selected question IDs for this session
            var selectedIds = session.SelectedQuestionIds
                .Split(',', StringSplitOptions.RemoveEmptyEntries)
                .Select(Guid.Parse)
                .ToHashSet();

            // Load only the questions that were part of this session
            var sessionQuestions = await db.Questions
                .Include(q => q.Domain)
                .Include(q => q.Options)
                .Where(q => selectedIds.Contains(q.Id))
                .ToListAsync();

            var duration = (session.CompletedAt ?? DateTime.UtcNow) - session.StartedAt;
            var domains = session.Exam.Domains;
            var domainScores = new List<DomainScoreDto>();
            var reviews = new List<QuestionReviewDto>();

            var answersMap = session.Answers.ToDictionary(a => a.QuestionId, a => a);

            foreach (var domain in domains)
            {
                var domainQuestions = sessionQuestions
                    .Where(q => q.DomainId == domain.Id)
                    .OrderBy(q => q.Number)
                    .ToList();

                var domainCorrect = 0;

                foreach (var q in domainQuestions)
                {
                    answersMap.TryGetValue(q.Id, out var ans);

                    var userSelected = ans?.SelectedOptionIds?
                        .Split(',', StringSplitOptions.RemoveEmptyEntries)
                        .Select(Guid.Parse)
                        .ToList() ?? [];

                    var correctOptions = q.Options.Where(o => o.IsCorrect).Select(o => o.Id).ToList();
                    var isCorrect = ans?.IsCorrect ?? false;
                    if (isCorrect) domainCorrect++;

                    reviews.Add(new QuestionReviewDto(
                        q.Number,
                        domain.Name,
                        q.Statement,
                        q.Options.Select(o => new OptionDto(o.Id, o.Letter, o.Text, o.IsCorrect)).ToList(),
                        userSelected,
                        correctOptions,
                        isCorrect,
                        q.Explanation
                    ));
                }

                var domainTotal = domainQuestions.Count;
                var percentage = domainTotal > 0 ? ((double)domainCorrect / domainTotal) * 100 : 0;

                domainScores.Add(new DomainScoreDto(
                    domain.Name,
                    domain.WeightPercent,
                    domainCorrect,
                    domainTotal,
                    Math.Round(percentage, 1)
                ));
            }

            var totalQuestions = reviews.Count;
            var totalCorrect = reviews.Count(r => r.IsCorrect);

            var result = new ExamResultDto(
                session.Id,
                session.Exam.Code,
                session.Exam.Name,
                session.Mode,
                session.FinalScore ?? 0,
                session.Exam.PassingScore,
                session.Passed ?? false,
                duration,
                totalQuestions,
                totalCorrect,
                domainScores,
                reviews.OrderBy(r => r.Number).ToList()
            );

            return Results.Ok(result);
        });
    }
}
