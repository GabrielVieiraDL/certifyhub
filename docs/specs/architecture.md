# CertifyHub — architecture.md

## Visão Arquitetural
Plataforma Full-Stack no ecossistema **Microsoft Azure**, com Clean Architecture e princípios agênticos de menor acoplamento, alta coesão e contratos estritos.

## Estrutura de Pastas e Módulos

```txt
simulados/
├── docs/                      # Especificações, ADRs, planos e relatórios de tarefas
├── .claude/                   # Agentes universais, regras de segurança e skills
├── apps/
│   ├── api/                   # ASP.NET Core 9 Web API (.NET 9 / C#)
│   │   ├── CertifyHub.Domain          # Entidades (Exame, Questão, Alternativa, Tentativa)
│   │   ├── CertifyHub.Application     # Casos de uso, interfaces, DTOs (Records)
│   │   ├── CertifyHub.Infrastructure  # EF Core, Migrations, Repositórios, Azure SDKs
│   │   └── CertifyHub.Api             # Controllers, Middlewares, Filtros, Swagger/OpenAPI
│   └── web/                   # Next.js 14+ / React (TypeScript + TailwindCSS + Shadcn UI)
```

## Serviços Azure Integrados (ou Alvos de Implantação)
- **Azure App Service / Azure Container Apps:** Hospedagem da Web API.
- **Azure Static Web Apps:** Hospedagem do frontend Next.js/React.
- **Azure SQL Database:** Persistência relacional das certificações, domínios e histórico.
- **Azure Blob Storage:** Armazenamento seguro de imagens de topologias e arquiteturas nas questões.
- **Azure Key Vault:** Gerenciamento centralizado de segredos e connection strings em produção.
- **Application Insights / Azure Monitor:** Telemetria, rastreamento distribuído e métricas de erro.

## Estruturas de Dados e Algoritmos do Motor de Simulados
- **Árvore de Domínios:** `Certificação -> Exame (ex: AZ-900) -> Domínio (ex: Descrever conceitos de nuvem) -> Questões`.
- **Embaralhamento Seguro (Fisher-Yates Shuffle):** Sorteio de questões do banco sem repetição e permutação cega de alternativas.
- **Mapeamento O(1) de Respostas:** Lookup das respostas do usuário usando Dicionários/HashMaps para pontuação em tempo real.
- **Anti-Cheating:** O payload entregue ao estudante em modo exame nunca inclui o booleano `isCorrect` ou as justificativas antes do submit final.
