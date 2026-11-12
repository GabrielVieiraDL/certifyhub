import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/lotes_parsed.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total questions to seed: {len(qs)}")

def escape_cs(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\r', '').replace('\n', ' ').strip()

def gen_guid(n):
    return f"{n:08x}-0000-0000-0000-{n:012x}"

lines = []
lines.append('using CertifyHub.Domain.Entities;')
lines.append('using CertifyHub.Domain.Enums;')
lines.append('using Microsoft.EntityFrameworkCore;')
lines.append('')
lines.append('namespace CertifyHub.Infrastructure.Data;')
lines.append('')
lines.append('public static class SeedData')
lines.append('{')
lines.append('    public static async Task InitializeAsync(AppDbContext context)')
lines.append('    {')
lines.append('        await context.Database.EnsureCreatedAsync();')
lines.append('')
lines.append('        if (await context.Exams.AnyAsync())')
lines.append('        {')
lines.append('            return;')
lines.append('        }')
lines.append('')
lines.append('        var examId = Guid.Parse("00000000-0000-0000-0000-000000000001");')
lines.append('        var domain1Id = Guid.Parse("10000000-0000-0000-0000-000000000001");')
lines.append('        var domain2Id = Guid.Parse("20000000-0000-0000-0000-000000000002");')
lines.append('        var domain3Id = Guid.Parse("30000000-0000-0000-0000-000000000003");')
lines.append('')
lines.append('        var exam = new Exam')
lines.append('        {')
lines.append('            Id = examId,')
lines.append('            Code = "AZ-900",')
lines.append('            Name = "Microsoft Azure Fundamentals",')
lines.append('            TimeLimitMinutes = 45,')
lines.append('            PassingScore = 700,')
lines.append('            MaxScore = 1000')
lines.append('        };')
lines.append('')
lines.append('        var domain1 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain1Id,')
lines.append('            Name = "Descrever os conceitos de nuvem",')
lines.append('            WeightPercent = 25,')
lines.append('            ExamId = examId')
lines.append('        };')
lines.append('')
lines.append('        var domain2 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain2Id,')
lines.append('            Name = "Descrever a arquitetura e os serviços do Azure",')
lines.append('            WeightPercent = 40,')
lines.append('            ExamId = examId')
lines.append('        };')
lines.append('')
lines.append('        var domain3 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain3Id,')
lines.append('            Name = "Descrever o gerenciamento e a governança no Azure",')
lines.append('            WeightPercent = 35,')
lines.append('            ExamId = examId')
lines.append('        };')
lines.append('')
lines.append('        context.Exams.Add(exam);')
lines.append('        context.SkillDomains.AddRange(domain1, domain2, domain3);')
lines.append('        await context.SaveChangesAsync();')
lines.append('')
lines.append('        var questions = new List<Question>')
lines.append('        {')

def get_domain_var(domain_name):
    if "conceito" in domain_name.lower():
        return "domain1Id"
    elif "arquitetura" in domain_name.lower():
        return "domain2Id"
    else:
        return "domain3Id"

for i, q in enumerate(qs):
    qtype = q['type']
    stmt = escape_cs(q['statement'])
    expl = escape_cs(q['explanation'])
    domain_var = get_domain_var(q['domain'])
    qguid = gen_guid(q['number'])
    
    lines.append('            new()')
    lines.append('            {')
    lines.append(f'                Id = Guid.Parse("{qguid}"),')
    lines.append(f'                Number = {q["number"]},')
    lines.append(f'                DomainId = {domain_var},')
    lines.append(f'                Type = QuestionType.{qtype},')
    lines.append(f'                Statement = "{stmt}",')
    lines.append(f'                Explanation = "{expl}",')
    lines.append('                Options =')
    lines.append('                [')
    
    for o in q['options']:
        letter = o['letter']
        otext = escape_cs(o['text'])
        correct = 'true' if o['isCorrect'] else 'false'
        lines.append(f'                    new() {{ Id = Guid.NewGuid(), Letter = "{letter}", Text = "{otext}", IsCorrect = {correct} }},')
    
    lines.append('                ]')
    
    if i < len(qs) - 1:
        lines.append('            },')
    else:
        lines.append('            }')

lines.append('        };')
lines.append('')
lines.append('        await context.Questions.AddRangeAsync(questions);')
lines.append('        await context.SaveChangesAsync();')
lines.append('    }')
lines.append('}')

target_path = r'c:\Users\gabri\OneDrive\Desktop\Projetos\simulados\src\CertifyHub.Infrastructure\Data\SeedData.cs'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Generated {len(qs)} questions in {target_path}")
