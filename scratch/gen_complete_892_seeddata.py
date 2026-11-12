import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Load AZ-900 questions (452)
with open('scratch/lotes_parsed.json', 'r', encoding='utf-8') as f:
    az900_qs = json.load(f)

# 2. Load AZ-104 questions (440)
with open('scratch/az104_parsed.json', 'r', encoding='utf-8') as f:
    az104_qs = json.load(f)

print(f"Loaded {len(az900_qs)} AZ-900 questions and {len(az104_qs)} AZ-104 questions.")
print(f"Total to seed: {len(az900_qs) + len(az104_qs)}")

def escape_cs(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\r', '').replace('\n', ' ').strip()

def gen_guid(prefix, n):
    return f"{prefix:08x}-0000-0000-0000-{n:012x}"

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
lines.append('        // ==========================================')
lines.append('        // 1. EXAME AZ-900: MICROSOFT AZURE FUNDAMENTALS')
lines.append('        // ==========================================')
lines.append('        var exam900Id = Guid.Parse("00000000-0000-0000-0000-000000000001");')
lines.append('        var domain900_1Id = Guid.Parse("10000000-0000-0000-0000-000000000001");')
lines.append('        var domain900_2Id = Guid.Parse("20000000-0000-0000-0000-000000000002");')
lines.append('        var domain900_3Id = Guid.Parse("30000000-0000-0000-0000-000000000003");')
lines.append('')
lines.append('        var exam900 = new Exam')
lines.append('        {')
lines.append('            Id = exam900Id,')
lines.append('            Code = "AZ-900",')
lines.append('            Name = "Microsoft Azure Fundamentals",')
lines.append('            TimeLimitMinutes = 45,')
lines.append('            PassingScore = 700,')
lines.append('            MaxScore = 1000')
lines.append('        };')
lines.append('')
lines.append('        var domain900_1 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain900_1Id,')
lines.append('            Name = "Descrever os conceitos de nuvem",')
lines.append('            WeightPercent = 25,')
lines.append('            ExamId = exam900Id')
lines.append('        };')
lines.append('')
lines.append('        var domain900_2 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain900_2Id,')
lines.append('            Name = "Descrever a arquitetura e os serviços do Azure",')
lines.append('            WeightPercent = 40,')
lines.append('            ExamId = exam900Id')
lines.append('        };')
lines.append('')
lines.append('        var domain900_3 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain900_3Id,')
lines.append('            Name = "Descrever o gerenciamento e a governança no Azure",')
lines.append('            WeightPercent = 35,')
lines.append('            ExamId = exam900Id')
lines.append('        };')
lines.append('')
lines.append('        // ==========================================')
lines.append('        // 2. EXAME AZ-104: MICROSOFT AZURE ADMINISTRATOR')
lines.append('        // ==========================================')
lines.append('        var exam104Id = Guid.Parse("00000000-0000-0000-0000-000000000104");')
lines.append('        var domain104_1Id = Guid.Parse("10400000-0000-0000-0000-000000000001");')
lines.append('        var domain104_2Id = Guid.Parse("10400000-0000-0000-0000-000000000002");')
lines.append('        var domain104_3Id = Guid.Parse("10400000-0000-0000-0000-000000000003");')
lines.append('        var domain104_4Id = Guid.Parse("10400000-0000-0000-0000-000000000004");')
lines.append('        var domain104_5Id = Guid.Parse("10400000-0000-0000-0000-000000000005");')
lines.append('')
lines.append('        var exam104 = new Exam')
lines.append('        {')
lines.append('            Id = exam104Id,')
lines.append('            Code = "AZ-104",')
lines.append('            Name = "Microsoft Azure Administrator",')
lines.append('            TimeLimitMinutes = 100,')
lines.append('            PassingScore = 700,')
lines.append('            MaxScore = 1000')
lines.append('        };')
lines.append('')
lines.append('        var domain104_1 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain104_1Id,')
lines.append('            Name = "Gerenciar identidades e governança do Azure",')
lines.append('            WeightPercent = 25,')
lines.append('            ExamId = exam104Id')
lines.append('        };')
lines.append('')
lines.append('        var domain104_2 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain104_2Id,')
lines.append('            Name = "Implementar e gerenciar armazenamento",')
lines.append('            WeightPercent = 20,')
lines.append('            ExamId = exam104Id')
lines.append('        };')
lines.append('')
lines.append('        var domain104_3 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain104_3Id,')
lines.append('            Name = "Implantar e gerenciar recursos de computação do Azure",')
lines.append('            WeightPercent = 25,')
lines.append('            ExamId = exam104Id')
lines.append('        };')
lines.append('')
lines.append('        var domain104_4 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain104_4Id,')
lines.append('            Name = "Configurar e gerenciar redes virtuais",')
lines.append('            WeightPercent = 20,')
lines.append('            ExamId = exam104Id')
lines.append('        };')
lines.append('')
lines.append('        var domain104_5 = new SkillDomain')
lines.append('        {')
lines.append('            Id = domain104_5Id,')
lines.append('            Name = "Monitorar e manter recursos do Azure",')
lines.append('            WeightPercent = 10,')
lines.append('            ExamId = exam104Id')
lines.append('        };')
lines.append('')
lines.append('        context.Exams.AddRange(exam900, exam104);')
lines.append('        context.SkillDomains.AddRange(')
lines.append('            domain900_1, domain900_2, domain900_3,')
lines.append('            domain104_1, domain104_2, domain104_3, domain104_4, domain104_5')
lines.append('        );')
lines.append('        await context.SaveChangesAsync();')
lines.append('')
lines.append('        var questions = new List<Question>')
lines.append('        {')

def get_az900_domain_var(domain_name):
    if "conceito" in domain_name.lower():
        return "domain900_1Id"
    elif "arquitetura" in domain_name.lower():
        return "domain900_2Id"
    else:
        return "domain900_3Id"

# Append AZ-900 (452)
for q in az900_qs:
    qtype = q['type']
    stmt = escape_cs(q['statement'])
    expl = escape_cs(q['explanation'])
    domain_var = get_az900_domain_var(q['domain'])
    qguid = gen_guid(0x900, q['number'])
    
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
    lines.append('            },')

# Append AZ-104 (440)
for q in az104_qs:
    qtype = q['type']
    stmt = escape_cs(q['statement'])
    expl = escape_cs(q['explanation'])
    domain_var = f"domain104_{q['domainId']}Id"
    qguid = gen_guid(0x104, q['number'])
    
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
    lines.append('            },')

lines.append('        };')
lines.append('')
lines.append('        await context.Questions.AddRangeAsync(questions);')
lines.append('        await context.SaveChangesAsync();')
lines.append('    }')
lines.append('}')

target_path = r'c:\Users\gabri\OneDrive\Desktop\Projetos\simulados\src\CertifyHub.Infrastructure\Data\SeedData.cs'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Generated SeedData.cs successfully with {len(az900_qs) + len(az104_qs)} questions ({len(az900_qs)} AZ-900 + {len(az104_qs)} AZ-104).")
