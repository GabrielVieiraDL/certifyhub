using CertifyHub.Domain.Enums;

namespace CertifyHub.Domain.Entities;

public class Question
{
    public Guid Id { get; set; }
    public int Number { get; set; }
    public QuestionType Type { get; set; }
    public string Statement { get; set; } = string.Empty;
    public string Explanation { get; set; } = string.Empty;

    public Guid DomainId { get; set; }
    public SkillDomain Domain { get; set; } = null!;

    public List<Option> Options { get; set; } = [];
}
