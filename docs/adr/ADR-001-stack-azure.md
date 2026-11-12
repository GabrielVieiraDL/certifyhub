# ADR-001: Escolha da Stack Tecnológica — Ecossistema Azure & Microsoft

## Contexto
O objetivo é desenvolver uma plataforma de alta fidelidade para simulados de certificações de TI (focando em exames reais como AZ-900, AZ-104, AZ-204, SC-900, AI-900, AWS, CompTIA, etc.), permitindo que o desenvolvedor aprenda e utilize na prática as tecnologias e boas práticas do ecossistema Azure e Microsoft.

## Decisão
Adotaremos uma arquitetura nativa com ferramentas e serviços compatíveis com o ecossistema Azure:

1. **Backend / API:**
   - **.NET 9 / ASP.NET Core Web API** (ou **Azure Functions Isolated Worker**) com C#.
   - Modelagem com Clean Architecture / Domain-Driven Design (Domain, Application, Infrastructure, API).
   - **Entity Framework Core (EF Core)** com Migrations.
   - Padrão **Repository** e **DTOs (Records)** para contratos estritos.

2. **Frontend:**
   - **React / Next.js com TypeScript e Tailwind CSS** (preparado para deploy no **Azure Static Web Apps**).
   - Componentes visuais com Shadcn UI / Radix primitives.

3. **Banco de Dados & Persistência:**
   - Em desenvolvimento local: **SQLite** ou **SQL Server Express / LocalDB**.
   - Alvo em nuvem: **Azure SQL Database** ou **Azure Cosmos DB** (NoSQL / SQL API).
   - Armazenamento de diagramas/mídias das questões: **Azure Blob Storage** (ou Azurite para emulação local).

4. **Autenticação & Segurança:**
   - **Microsoft Entra ID (Azure AD / Azure AD B2C)** ou JWT seguro com Identity Core, preparando o terreno para SSO corporativo e exames oficiais.

## Consequências
- Excelente alinhamento com os próprios exames de certificação da Microsoft (AZ-900, AZ-204, DP-900).
- Alta performance (.NET 9 + C# compilado e tipagem estática do TypeScript no front).
- Integração facilitada com pipelines Azure DevOps / GitHub Actions para CI/CD direto no Azure.
