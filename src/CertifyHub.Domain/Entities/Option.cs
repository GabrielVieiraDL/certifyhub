namespace CertifyHub.Domain.Entities;

public class Option
{
    public Guid Id { get; set; }
    public string Letter { get; set; } = string.Empty;
    public string Text { get; set; } = string.Empty;
    public bool IsCorrect { get; set; }

    public Guid QuestionId { get; set; }
    public Question Question { get; set; } = null!;
}
