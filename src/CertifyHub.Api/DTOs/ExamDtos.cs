using CertifyHub.Domain.Enums;

namespace CertifyHub.Api.DTOs;

public record ExamDto(Guid Id, string Code, string Name, int TimeLimitMinutes, int PassingScore, int MaxScore, List<SkillDomainDto> Domains);

public record SkillDomainDto(Guid Id, string Name, int WeightPercent, int QuestionCount);

public record CreateSessionRequest(string ExamCode, ExamMode Mode);

public record ExamSessionDto(
    Guid Id,
    string ExamCode,
    string ExamName,
    ExamMode Mode,
    SessionStatus Status,
    DateTime StartedAt,
    DateTime? ExpiresAt,
    int TotalQuestions,
    int AnsweredQuestions
);

public record QuestionDto(
    Guid Id,
    int Number,
    string DomainName,
    QuestionType Type,
    string Statement,
    List<OptionDto> Options,
    string? Explanation = null // Nulo no Modo Exame até finalização
);

public record OptionDto(Guid Id, string Letter, string Text, bool? IsCorrect = null); // Nulo no Modo Exame

public record SubmitAnswerRequest(Guid QuestionId, List<Guid> SelectedOptionIds);

public record AnswerFeedbackDto(
    bool IsCorrect,
    List<Guid> CorrectOptionIds,
    string Explanation,
    int AnsweredCount,
    int TotalCount
);

public record ExamResultDto(
    Guid SessionId,
    string ExamCode,
    string ExamName,
    ExamMode Mode,
    int FinalScore,
    int PassingScore,
    bool Passed,
    TimeSpan Duration,
    int TotalQuestions,
    int CorrectQuestions,
    List<DomainScoreDto> DomainScores,
    List<QuestionReviewDto> Reviews
);

public record DomainScoreDto(string DomainName, int WeightPercent, int Correct, int Total, double Percentage);

public record QuestionReviewDto(
    int Number,
    string DomainName,
    string Statement,
    List<OptionDto> Options,
    List<Guid> UserSelectedOptionIds,
    List<Guid> CorrectOptionIds,
    bool IsCorrect,
    string Explanation
);

public record ExamStatsDto(
    int TotalQuestionPool,
    int QuestionsPerSession,
    int CompletedSessions,
    int TotalAnswered,
    int UniqueQuestionsAnswered,
    int UniqueQuestionsCorrect
);
