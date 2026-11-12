namespace CertifyHub.Domain.Entities;

public class Exam
{
    public Guid Id { get; set; }
    public string Code { get; set; } = string.Empty;
    public string Name { get; set; } = string.Empty;
    public int TimeLimitMinutes { get; set; }
    public int PassingScore { get; set; }
    public int MaxScore { get; set; }

    public List<SkillDomain> Domains { get; set; } = [];
}
