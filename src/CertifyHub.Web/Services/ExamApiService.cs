using System.Net.Http.Json;
using CertifyHub.Api.DTOs;
using CertifyHub.Domain.Enums;

namespace CertifyHub.Web.Services;

public class ExamApiService(HttpClient http)
{
    public async Task<List<ExamDto>> GetExamsAsync()
    {
        return await http.GetFromJsonAsync<List<ExamDto>>("/api/exams") ?? [];
    }

    public async Task<ExamDto?> GetExamAsync(string code)
    {
        return await http.GetFromJsonAsync<ExamDto>($"/api/exams/{code}");
    }

    public async Task<ExamSessionDto?> CreateSessionAsync(string examCode, ExamMode mode)
    {
        var response = await http.PostAsJsonAsync("/api/sessions", new CreateSessionRequest(examCode, mode));
        if (!response.IsSuccessStatusCode) return null;
        return await response.Content.ReadFromJsonAsync<ExamSessionDto>();
    }

    public async Task<ExamSessionDto?> GetSessionAsync(Guid sessionId)
    {
        return await http.GetFromJsonAsync<ExamSessionDto>($"/api/sessions/{sessionId}");
    }

    public async Task<List<QuestionDto>> GetSessionQuestionsAsync(Guid sessionId)
    {
        return await http.GetFromJsonAsync<List<QuestionDto>>($"/api/sessions/{sessionId}/questions") ?? [];
    }

    public async Task<AnswerFeedbackDto?> SubmitAnswerAsync(Guid sessionId, Guid questionId, List<Guid> selectedOptionIds)
    {
        var response = await http.PostAsJsonAsync($"/api/sessions/{sessionId}/answer", new SubmitAnswerRequest(questionId, selectedOptionIds));
        if (!response.IsSuccessStatusCode) return null;
        return await response.Content.ReadFromJsonAsync<AnswerFeedbackDto>();
    }

    public async Task<bool> FinishExamAsync(Guid sessionId)
    {
        var response = await http.PostAsync($"/api/sessions/{sessionId}/submit", null);
        return response.IsSuccessStatusCode;
    }

    public async Task<ExamResultDto?> GetResultAsync(Guid sessionId)
    {
        return await http.GetFromJsonAsync<ExamResultDto>($"/api/sessions/{sessionId}/result");
    }

    public async Task<ExamStatsDto?> GetStatsAsync(string? examCode = null)
    {
        var url = string.IsNullOrWhiteSpace(examCode) ? "/api/exams/stats" : $"/api/exams/{examCode}/stats";
        return await http.GetFromJsonAsync<ExamStatsDto>(url);
    }
}
