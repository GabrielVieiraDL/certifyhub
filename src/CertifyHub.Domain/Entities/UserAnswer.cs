namespace CertifyHub.Domain.Entities;

public class UserAnswer
{
    public Guid Id { get; set; }
    public string SelectedOptionIds { get; set; } = string.Empty;
    public bool IsCorrect { get; set; }
    public DateTime AnsweredAt { get; set; }

    public Guid SessionId { get; set; }
    public ExamSession Session { get; set; } = null!;

    public Guid QuestionId { get; set; }
    public Question Question { get; set; } = null!;
}
