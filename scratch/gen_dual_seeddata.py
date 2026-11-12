import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Load the 452 AZ-900 questions
with open('scratch/lotes_parsed.json', 'r', encoding='utf-8') as f:
    az900_qs = json.load(f)

print(f"Loaded {len(az900_qs)} AZ-900 questions.")

# 2. Define AZ-104 Starter Questions
az104_questions = [
    # Domínio 1: Gerenciar identidades e governança do Azure (25%)
    {
        "number": 1,
        "domain": 1, # Domínio 1 AZ-104
        "type": "SingleChoice",
        "statement": "Você precisa criar um grupo no Microsoft Entra ID cuja associação seja atualizada automaticamente quando os funcionários forem contratados ou mudarem de departamento. Qual tipo de associação de grupo deve ser configurado?",
        "options": [
            {"letter": "A", "text": "Atribuído (Assigned)", "isCorrect": False},
            {"letter": "B", "text": "Usuário Dinâmico (Dynamic User)", "isCorrect": True},
            {"letter": "C", "text": "Dispositivo Dinâmico (Dynamic Device)", "isCorrect": False},
            {"letter": "D", "text": "Sincronizado via Entra Connect sem regras", "isCorrect": False}
        ],
        "explanation": "Os grupos de Usuários Dinâmicos utilizam regras baseadas em atributos de usuário (como 'user.department -eq \"Vendas\"') para adicionar ou remover membros automaticamente conforme os perfis são atualizados."
    },
    {
        "number": 2,
        "domain": 1,
        "type": "SingleChoice",
        "statement": "Sua organização precisa conceder a um administrador acesso de privilégio elevado (como Administrador de Usuários) apenas durante o horário de plantão e exigindo justificativa prévia e aprovação por e-mail. Qual recurso do Microsoft Entra ID Governance atende a esse requisito?",
        "options": [
            {"letter": "A", "text": "Acesso Condicional (Conditional Access)", "isCorrect": False},
            {"letter": "B", "text": "Privileged Identity Management (PIM)", "isCorrect": True},
            {"letter": "C", "text": "Bloqueio de Recurso (Resource Lock)", "isCorrect": False},
            {"letter": "D", "text": "Redefinição de Senha de Autoatendimento (SSPR)", "isCorrect": False}
        ],
        "explanation": "O Privileged Identity Management (PIM) fornece ativação de função baseada em tempo e aprovação just-in-time (JIT) para mitigar os riscos de permissões de acesso excessivas e desnecessárias."
    },
    {
        "number": 3,
        "domain": 1,
        "type": "SingleChoice",
        "statement": "Qual ferramenta de governança do Azure deve ser utilizada para impedir estritamente que os administradores criem máquinas virtuais que não utilizem um SKU de tamanho aprovado pela empresa, aplicando a regra em nível de grupo de gerenciamento?",
        "options": [
            {"letter": "A", "text": "Azure Policy com efeito Deny", "isCorrect": True},
            {"letter": "B", "text": "Bloqueio de Recurso ReadOnly", "isCorrect": False},
            {"letter": "C", "text": "Controle de Acesso Baseado em Função (RBAC) com função Reader", "isCorrect": False},
            {"letter": "D", "text": "Microsoft Defender for Cloud", "isCorrect": False}
        ],
        "explanation": "O Azure Policy permite definir e aplicar padrões organizacionais de conformidade na criação e atualização de recursos, utilizando a regra nativa de SKUs de VM permitidos com o efeito 'Deny' para bloquear solicitações não autorizadas."
    },

    # Domínio 2: Implementar e gerenciar armazenamento (20%)
    {
        "number": 4,
        "domain": 2,
        "type": "SingleChoice",
        "statement": "Uma empresa armazena terabytes de logs no Azure Blob Storage. Os logs devem permanecer acessíveis imediatamente durante os primeiros 30 dias após a criação. Após 30 dias, os dados raramente são consultados, e após 180 dias devem ser retidos pelo menor custo possível por 7 anos. Como você deve automatizar essa retenção com o menor esforço administrativo?",
        "options": [
            {"letter": "A", "text": "Executar um script do PowerShell agendado no Azure Automation para mover os blobs", "isCorrect": False},
            {"letter": "B", "text": "Configurar uma regra de Gerenciamento do Ciclo de Vida (Lifecycle Management) na conta de armazenamento", "isCorrect": True},
            {"letter": "C", "text": "Usar o AzCopy em um trabalho diário do Azure DevOps", "isCorrect": False},
            {"letter": "D", "text": "Alterar manualmente o nível de acesso da conta de armazenamento a cada trimestre", "isCorrect": False}
        ],
        "explanation": "As regras de gerenciamento do ciclo de vida (Lifecycle Management) no Azure Blob Storage automatizam a transição entre camadas (Hot -> Cool -> Archive) e exclusão com base na idade dos dados sem necessidade de scripts externos."
    },
    {
        "number": 5,
        "domain": 2,
        "type": "SingleChoice",
        "statement": "Você precisa conceder a uma aplicação de parceiro externo permissão temporária de leitura para um único contêiner de blob no Azure Storage durante 4 horas, sem compartilhar a chave de acesso mestre da conta. O que você deve gerar?",
        "options": [
            {"letter": "A", "text": "Uma Assinatura de Acesso Compartilhado (SAS) de serviço com expiração em 4 horas", "isCorrect": True},
            {"letter": "B", "text": "Uma nova Chave de Acesso Secundária", "isCorrect": False},
            {"letter": "C", "text": "Um token de acesso mestre de assinatura", "isCorrect": False},
            {"letter": "D", "text": "Um certificado SSL privado", "isCorrect": False}
        ],
        "explanation": "A Shared Access Signature (SAS) fornece acesso delegado seguro e com privilégios limitados (permissões, intervalo de datas e endereços IP permitidos) a recursos específicos de armazenamento sem expor as chaves da conta."
    },

    # Domínio 3: Implantar e gerenciar recursos de computação do Azure (25%)
    {
        "number": 6,
        "domain": 3,
        "type": "SingleChoice",
        "statement": "Você planeja implantar um conjunto de máquinas virtuais de missão crítica na região Leste dos EUA. Você precisa garantir que a solução tenha um SLA de 99,99% contra interrupções físicas de data centers inteiros dentro da mesma região. Qual configuração de alta disponibilidade deve ser utilizada?",
        "options": [
            {"letter": "A", "text": "Conjunto de Disponibilidade (Availability Set)", "isCorrect": False},
            {"letter": "B", "text": "Zonas de Disponibilidade (Availability Zones)", "isCorrect": True},
            {"letter": "C", "text": "Instâncias Spot do Azure", "isCorrect": False},
            {"letter": "D", "text": "Grupo de Recursos Dedicado", "isCorrect": False}
        ],
        "explanation": "As Zonas de Disponibilidade distribuem cargas de trabalho entre locais físicos exclusivos com energia, refrigeração e rede independentes na mesma região do Azure, fornecendo o SLA mais alto (99,99%) para duas ou mais instâncias."
    },
    {
        "number": 7,
        "domain": 3,
        "type": "SingleChoice",
        "statement": "Você precisa implantar um aplicativo web em contêiner Linux no Azure de maneira simplificada, sem precisar gerenciar clusters, nós de VMs subjacentes ou orquestração complexa de Kubernetes. Qual serviço deve ser escolhido?",
        "options": [
            {"letter": "A", "text": "Instâncias de Contêiner do Azure (Azure Container Instances - ACI)", "isCorrect": True},
            {"letter": "B", "text": "Serviço de Kubernetes do Azure (AKS)", "isCorrect": False},
            {"letter": "C", "text": "Azure Batch", "isCorrect": False},
            {"letter": "D", "text": "Azure Virtual Machines com Docker CE instalado", "isCorrect": False}
        ],
        "explanation": "O Azure Container Instances (ACI) é a solução serverless mais rápida e simples para executar contêineres sob demanda no Azure sem precisar provisionar servidores ou adotar uma plataforma de orquestração completa como o AKS."
    },

    # Domínio 4: Configurar e gerenciar redes virtuais (20%)
    {
        "number": 8,
        "domain": 4,
        "type": "SingleChoice",
        "statement": "Você possui duas redes virtuais chamadas VNet1 e VNet2 na mesma região do Azure. Máquinas virtuais na VNet1 precisam se comunicar com máquinas virtuais na VNet2 através de endereços IP privados com latência mínima e sem passar pela Internet pública. O que você deve configurar?",
        "options": [
            {"letter": "A", "text": "Emparelhamento de Rede Virtual (Virtual Network Peering)", "isCorrect": True},
            {"letter": "B", "text": "Gateway de VPN Site-to-Site", "isCorrect": False},
            {"letter": "C", "text": "Azure ExpressRoute", "isCorrect": False},
            {"letter": "D", "text": "Azure Front Door", "isCorrect": False}
        ],
        "explanation": "O VNet Peering conecta diretamente duas VNets através do backbone de alta velocidade da Microsoft, permitindo que o tráfego flua por IPs privados com a menor latência e sem a sobrecarga de gateways de VPN."
    },
    {
        "number": 9,
        "domain": 4,
        "type": "SingleChoice",
        "statement": "Você precisa permitir que administradores de TI conectem-se via RDP e SSH às máquinas virtuais do Azure de forma altamente segura diretamente pelo navegador web no Portal do Azure, sem que as VMs possuam endereços IP públicos nem portas abertas na Internet. Qual serviço deve ser implantado na rede virtual?",
        "options": [
            {"letter": "A", "text": "Azure Bastion", "isCorrect": True},
            {"letter": "B", "text": "Azure Firewall", "isCorrect": False},
            {"letter": "C", "text": "Network Security Group (NSG) com porta 3389 permitida para Any", "isCorrect": False},
            {"letter": "D", "text": "Balanceador de Carga Interno", "isCorrect": False}
        ],
        "explanation": "O Azure Bastion é um serviço PaaS totalmente gerenciado que fornece acesso RDP e SSH contínuo e seguro via TLS diretamente do Portal do Azure sem expor as VMs à Internet com IPs públicos."
    },
    {
        "number": 10,
        "domain": 4,
        "type": "SingleChoice",
        "statement": "Qual serviço de rede do Azure opera na Camada 7 (Layer 7 - Camada de Aplicação) do modelo OSI e suporta roteamento baseado em caminho de URL (/imagens, /videos), terminação TLS/SSL e integração com Web Application Firewall (WAF)?",
        "options": [
            {"letter": "A", "text": "Azure Application Gateway", "isCorrect": True},
            {"letter": "B", "text": "Azure Load Balancer (Standard SKU)", "isCorrect": False},
            {"letter": "C", "text": "Azure Traffic Manager", "isCorrect": False},
            {"letter": "D", "text": "Azure NAT Gateway", "isCorrect": False}
        ],
        "explanation": "O Azure Application Gateway é um balanceador de carga de tráfego web de camada 7 que toma decisões de roteamento com base em atributos como URI e cabeçalhos HTTP, incluindo suporte nativo a WAF."
    },

    # Domínio 5: Monitorar e manter recursos do Azure (10%)
    {
        "number": 11,
        "domain": 5,
        "type": "SingleChoice",
        "statement": "Você precisa consultar e analisar logs de eventos de várias máquinas virtuais e contas de armazenamento em um repositório centralizado utilizando a linguagem Kusto Query Language (KQL). Onde esses logs devem ser agregados?",
        "options": [
            {"letter": "A", "text": "Em um Workspace do Log Analytics do Azure Monitor", "isCorrect": True},
            {"letter": "B", "text": "Em uma Conta de Armazenamento de Arquivo (Azure Files)", "isCorrect": False},
            {"letter": "C", "text": "No Histórico de Atividades do Azure Advisor", "isCorrect": False},
            {"letter": "D", "text": "No Painel de Governança do Azure Policy", "isCorrect": False}
        ],
        "explanation": "O Log Analytics Workspace é o ambiente de análise central do Azure Monitor onde dados de telemetria e logs são consolidados e pesquisados com consultas ricas em KQL (Kusto Query Language)."
    },
    {
        "number": 12,
        "domain": 5,
        "type": "SingleChoice",
        "statement": "Você precisa configurar o backup diário automatizado de máquinas virtuais do Azure executando Windows e Linux com suporte a retenção de longo prazo e restauração pontual. Qual recurso deve ser provisionado?",
        "options": [
            {"letter": "A", "text": "Cofre dos Serviços de Recuperação (Recovery Services Vault)", "isCorrect": True},
            {"letter": "B", "text": "Área de Trabalho do Azure Monitor", "isCorrect": False},
            {"letter": "C", "text": "Conta de Armazenamento LRS", "isCorrect": False},
            {"letter": "D", "text": "Instância do Azure Site Recovery sem cofre", "isCorrect": False}
        ],
        "explanation": "O Recovery Services Vault armazena dados de backup do Azure Backup para vários serviços, como máquinas virtuais, bancos de dados SQL em VMs do Azure e compartilhamentos de arquivos do Azure."
    }
]

print(f"Defined {len(az104_questions)} AZ-104 starter questions across all 5 domains.")

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

# Add AZ-900 questions
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

# Add AZ-104 questions
for q in az104_questions:
    qtype = q['type']
    stmt = escape_cs(q['statement'])
    expl = escape_cs(q['explanation'])
    domain_var = f"domain104_{q['domain']}Id"
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

print(f"Generated SeedData.cs with {len(az900_qs)} AZ-900 questions + {len(az104_questions)} AZ-104 questions.")
