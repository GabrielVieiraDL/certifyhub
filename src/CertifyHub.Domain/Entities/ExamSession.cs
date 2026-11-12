using CertifyHub.Domain.Enums;

namespace CertifyHub.Domain.Entities;

public class ExamSession
{
    public Guid Id { get; set; }
    public ExamMode Mode { get; set; }
    public SessionStatus Status { get; set; }
    public DateTime StartedAt { get; set; }
    public DateTime? ExpiresAt { get; set; }
    public DateTime? CompletedAt { get; set; }
    public int? FinalScore { get; set; }
    public bool? Passed { get; set; }
    public int Seed { get; set; }

    /// <summary>
    /// Comma-separated list of Question GUIDs selected for this session (50 out of the full pool).
    /// </summary>
    public string SelectedQuestionIds { get; set; } = string.Empty;

    public Guid ExamId { get; set; }
    public Exam Exam { get; set; } = null!;

    public List<UserAnswer> Answers { get; set; } = [];
}
