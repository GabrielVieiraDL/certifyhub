namespace CertifyHub.Domain.Entities;

public class SkillDomain
{
    public Guid Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public int WeightPercent { get; set; }

    public Guid ExamId { get; set; }
    public Exam Exam { get; set; } = null!;

    public List<Question> Questions { get; set; } = [];
}
