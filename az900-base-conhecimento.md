# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals

Esta base de conhecimento foi estruturada especificamente para ser consumida por agentes de IA, frameworks de *vibe coding* e sistemas de automação (como o Antigravity). Ela organiza as questões representativas do exame **AZ-900: Microsoft Azure Fundamentals** extraídas do banco de dados oficial em blocos padronizados em Português do Brasil (pt-BR), aplicando estritamente a nomenclatura oficial da Microsoft Brasil.

---

## 1. Especificação de Esquema de Parsing para Agentes (Agent Schema Definition)

Para processamento automatizado e extração estruturada por agentes de IA ou ferramentas de parsing no Antigravity, cada entrada de questão segue uma sintaxe Markdown determinística:

```markdown
### Questão [ID]
**Domínio:** [Conceitos de Nuvem | Arquitetura e Serviços | Gerenciamento e Governança]
**Enunciado:** [Texto do problema traduzido para pt-BR]
**Opções:**
- A) [Alternativa A]
- B) [Alternativa B]
- C) [Alternativa C]
- D) [Alternativa D]
**Resposta Correta:** [Letra / Opção Correta]
**Explicação Técnica:** [Justificativa didática fundamentada no Microsoft Learn]
```

---

## 2. Domínio 1: Conceitos de Nuvem (Cloud Concepts)

### Questão 001
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa planeja migrar todas as suas máquinas virtuais locais (atualmente hospedadas em hipervisores Hyper-V) para uma assinatura do Azure do tipo Pague o que Usar (Pay-As-You-Go). Você precisa identificar o modelo de despesas correto aplicado a essa solução de nuvem. Qual modelo deve ser utilizado?
**Opções:**
- A) Modelo de Despesas Operacionais (OpEx)
- B) Modelo de Despesas Elásticas
- C) Modelo de Despesas de Capital (CapEx)
- D) Modelo de Despesas Escaláveis
**Resposta Correta:** A
**Explicação Técnica:** A migração de infraestrutura local para a nuvem pública altera o modelo financeiro de CapEx (investimento prévio em hardware físico e infraestrutura de data center) para OpEx (despesas operacionais), no qual a empresa paga continuamente apenas pelos serviços computacionais consumidos sob demanda.

### Questão 002
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual benefício da computação em nuvem garante o acesso contínuo dos usuários a uma aplicação hospedada na nuvem com o mínimo possível de tempo de inatividade (downtime)?
**Opções:**
- A) Agilidade
- B) Escalabilidade
- C) Elasticidade
- D) Alta Disponibilidade (High Availability)
**Resposta Correta:** D
**Explicação Técnica:** Alta Disponibilidade (High Availability) é o benefício focado em garantir que os sistemas permaneçam operacionais e acessíveis por longos períodos, minimizando paralisações planejadas e não planejadas através de redundância e tolerância a falhas.

### Questão 003
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual modelo de serviço de nuvem minimiza a responsabilidade de gerenciamento por parte do cliente, transferindo a manutenção do sistema operacional, runtime e infraestrutura para o provedor?
**Opções:**
- A) Infraestrutura como Serviço (IaaS)
- B) Plataforma como Serviço (PaaS)
- C) Software como Serviço (SaaS)
- D) Servidor Dedicado Físico
**Resposta Correta:** C
**Explicação Técnica:** No modelo Software como Serviço (SaaS), o provedor de nuvem (Microsoft) gerencia toda a pilha: hardware, rede, virtualização, sistema operacional, middleware e a própria aplicação. O cliente apenas configura e utiliza o software (ex.: Microsoft 365).

### Questão 004
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa deseja implantar máquinas virtuais no Azure. Qual modelo de serviço de nuvem é o mais adequado para essa necessidade?
**Opções:**
- A) Software como Serviço (SaaS)
- B) Plataforma como Serviço (PaaS)
- C) Infraestrutura como Serviço (IaaS)
- D) Função como Serviço (FaaS)
**Resposta Correta:** C
**Explicação Técnica:** Máquinas Virtuais (VMs) pertencem ao modelo Infraestrutura como Serviço (IaaS). O IaaS oferece o maior grau de controle e flexibilidade sobre os servidores e a rede, onde a Microsoft gerencia o hardware físico e o hipervisor, enquanto o cliente gerencia o SO, patches e aplicações.

### Questão 005
**Domínio:** Conceitos de Nuvem
**Enunciado:** No Modelo de Responsabilidade Compartilhada para o serviço Software como Serviço (SaaS), qual das seguintes responsabilidades é compartilhada entre a Microsoft e o cliente?
**Opções:**
- A) Gerenciamento de infraestrutura de identidade e diretório
- B) Gerenciamento da aplicação
- C) Atualizações do sistema operacional
- D) Manutenção física dos servidores
**Resposta Correta:** A
**Explicação Técnica:** Em soluções SaaS, a segurança dos dados e o gerenciamento de contas de usuário/identidades no diretório (como o Microsoft Entra ID) envolvem responsabilidade compartilhada, pois o cliente configura o controle de acesso e usuários, enquanto a Microsoft mantém a infraestrutura global do serviço de identidade.

---

## 3. Domínio 2: Arquitetura e Serviços do Azure (Azure Architecture & Core Services)

### Questão 006
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Você precisa identificar para qual tipo de falha uma Zona de Disponibilidade (Availability Zone) do Azure pode proteger o acesso aos serviços. O que deve ser identificado?
**Opções:**
- A) Falha em um servidor físico individual
- B) Falha em uma região inteira do Azure
- C) Falha de um disco de armazenamento local
- D) Falha em um data center inteiro do Azure
**Resposta Correta:** D
**Explicação Técnica:** As Zonas de Disponibilidade são locais físicos separados e independentes dentro de uma mesma Região do Azure. Cada zona possui alimentações de energia, refrigeração e redes exclusivas. Portanto, protegem contra a falha de um data center completo.

### Questão 007
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Onde as máquinas virtuais do Azure devem obrigatoriamente estar contidas para fins de organização e gerenciamento de ciclo de vida?
**Opções:**
- A) Em uma Conta de Armazenamento (Storage Account)
- B) Em um Grupo de Recursos (Resource Group)
- C) Em uma Unidade Administrativa
- D) Em um Grupo de Aplicativos
**Resposta Correta:** B
**Explicação Técnica:** Todos os recursos criados no Azure devem pertencer a exatamente um Grupo de Recursos (Resource Group). O grupo de recursos serve como um contêiner lógico para implantar, gerenciar e monitorar recursos do Azure como uma unidade.

### Questão 008
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece um ambiente otimizado para o armazenamento de grandes objetos não estruturados, como arquivos de vídeo, imagens e documentos?
**Opções:**
- A) Azure Disk Storage
- B) Azure Files
- C) Azure Blob Storage
- D) Azure Queue Storage
**Resposta Correta:** C
**Explicação Técnica:** O Azure Blob Storage é o serviço de armazenamento de objetos da Microsoft otimizado para guardar dados não estruturados massivos (como imagens, documentos, áudio e vídeo) acessíveis de qualquer lugar via HTTP/HTTPS.

### Questão 009
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure permite estender redes locais (on-premises) para a nuvem da Microsoft através de uma conexão privada dedicada que não trafega pela Internet pública?
**Opções:**
- A) Azure ExpressRoute
- B) Peering de Rede Virtual (VNet Peering)
- C) VPN Gateway
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** O Azure ExpressRoute cria conexões privadas e dedicadas entre os data centers locais da empresa e a infraestrutura do Azure, oferecendo maior confiabilidade, velocidades mais altas e menor latência do que conexões via Internet.

### Questão 010
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de computação sem servidor (serverless) do Azure permite executar código acionado por eventos sem a necessidade de provisionar ou gerenciar infraestrutura?
**Opções:**
- A) Azure DevOps Pipelines
- B) Modelos do Azure Resource Manager (ARM Templates)
- C) Azure Application Gateway
- D) Azure Functions
**Resposta Correta:** D
**Explicação Técnica:** O Azure Functions é um serviço de computação serverless orientado a eventos. Ele permite rodar trechos de código (funções) sob demanda com escalabilidade automática, pagando apenas pelo tempo de execução do código.

---

## 4. Domínio 3: Gerenciamento e Governança no Azure (Azure Management & Governance)

### Questão 011
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Sua empresa possui uma assinatura do Azure com o plano de suporte Basic. Quais planos de suporte do Azure permitem a abertura de novas solicitações de suporte no portal?
**Opções:**
- A) Apenas Premier e Professional Direct
- B) Apenas Premier, Professional Direct e Standard
- C) Apenas Premier, Professional Direct, Standard e Developer
- D) Premier, Professional Direct, Standard, Developer e Basic
**Resposta Correta:** D
**Explicação Técnica:** Todos os planos de suporte do Azure (incluindo o Basic) permitem a abertura de chamados no Portal do Azure. No plano Basic, o suporte é voltado para gerenciamento de conta, faturamento e solicitações de aumento de cotas/limites da assinatura.

### Questão 012
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Azure permite definir regras e padronizações de conformidade para garantir que os recursos implantados sigam os padrões organizacionais da empresa?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks)
- B) Azure Policy
- C) Grupos de Gerenciamento (Management Groups)
- D) Azure Blueprint
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy é o serviço utilizado para criar, atribuir e gerenciar definições de políticas que impõem regras sobre seus recursos, garantindo conformidade com padrões corporativos e SLAs de governança.

### Questão 013
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que deve ser removido ou alterado quando um administrador precisa excluir um Grupo de Recursos que possui uma trava contra exclusão acidental aplicada?
**Opções:**
- A) É necessário alterar a política do Azure (Azure Policy) associada
- B) É necessário remover o Bloqueio de Exclusão (Delete Lock) antes de tentar a exclusão
- C) Apenas um Administrador Global pode excluir sem alterar nada
- D) Adicionar uma Tag específica ao grupo de recursos
**Resposta Correta:** B
**Explicação Técnica:** Os Bloqueios de Recursos (Resource Locks) do tipo *CanNotDelete* (Delete) impedem que qualquer usuário, independentemente de sua função ou privilégio no RBAC, exclua o recurso até que a trava de bloqueio seja explicitamente removida.

### Questão 014
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure fornece recomendações personalizadas e proativas de boas práticas para otimização de custos, desempenho, alta disponibilidade e segurança?
**Opções:**
- A) Azure Advisor
- B) Application Insights
- C) Azure Service Health
- D) Azure Monitor
**Resposta Correta:** A
**Explicação Técnica:** O Azure Advisor analisa as configurações e métricas de uso dos seus recursos e fornece recomendações personalizadas divididas em cinco pilares: Custo, Segurança, Confiabilidade, Excelência Operacional e Desempenho.

### Questão 015
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é o serviço central de gerenciamento de identidades e acessos baseado em nuvem da Microsoft, utilizado para autenticação e autorização no Azure e no Microsoft 365?
**Opções:**
- A) Active Directory Domain Services (AD DS)
- B) Microsoft Entra ID (antigo Azure Active Directory)
- C) Azure Key Vault
- D) Controle de Acesso Baseado em Função (RBAC)
**Resposta Correta:** B
**Explicação Técnica:** O Microsoft Entra ID (anteriormente denominado Azure Active Directory) é a solução multilocatária corporativa baseada em nuvem para gerenciamento de identidades, autenticação e controle de acesso aos recursos do Azure e serviços como Microsoft 365.
