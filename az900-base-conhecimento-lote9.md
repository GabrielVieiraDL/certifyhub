# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals - Lote 9 (Questões 401 a 452)

Esta base de conhecimento contém o lote final (questões 401 a 452) do exame **AZ-900: Microsoft Azure Fundamentals** formatadas para ingestão e automação no Antigravity.

---

### Questão 401
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa precisa migrar suas aplicações locais para a nuvem. Ela deseja manter o controle total sobre a configuração do sistema operacional e o gerenciamento das máquinas virtuais. Qual modelo de serviço de nuvem atende a este requisito?
**Opções:**
- A) Software como Serviço (SaaS)
- B) Plataforma como Serviço (PaaS)
- C) Infraestrutura como Serviço (IaaS)
- D) Função como Serviço (FaaS)
**Resposta Correta:** C
**Explicação Técnica:** O modelo Infraestrutura como Serviço (IaaS) fornece controle total sobre os sistemas operacionais, configurações de rede, armazenamento e máquinas virtuais, enquanto a Microsoft gerencia apenas a infraestrutura física e o hipervisor.

### Questão 402
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual ferramenta de gerenciamento do Azure permite executar comandos administrativos interativos via navegador web utilizando Bash ou PowerShell sem necessidade de instalar ferramentas locais?
**Opções:**
- A) CLI do Azure (Azure CLI)
- B) Azure Cloud Shell
- C) Azure Portal
- D) PowerShell do Azure
**Resposta Correta:** B
**Explicação Técnica:** O Azure Cloud Shell é um terminal interativo acessível pelo navegador que permite gerenciar recursos do Azure usando Bash ou PowerShell configurados previamente.

### Questão 403
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Azure permite organizar geograficamente ou por centro de custos as faturas de múltiplas assinaturas sob um único contrato comercial corporativo?
**Opções:**
- A) Grupos de Recursos (Resource Groups)
- B) Contas de Cobrança / Contratos de Cliente do Azure (Billing Accounts / Azure Customer Agreement)
- C) Grupos de Gerenciamento (Management Groups)
- D) Azure Policy
**Resposta Correta:** B
**Explicação Técnica:** As Contas de Cobrança e os escopos do Azure Cost Management agrupam a faturação de múltiplas assinaturas para consolidar relatórios de custos e conformidade financeira por departamento ou região.

### Questão 404
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa deseja garantir que o acesso aos dados em uma Conta de Armazenamento do Azure seja permitido apenas a partir de endereços IP específicos da rede corporativa local. Qual recurso de segurança de rede deve ser configurado?
**Opções:**
- A) Peering de Rede Virtual
- B) Firewalls e Redes Virtuais da Conta de Armazenamento
- C) Grupo de Segurança de Rede (NSG)
- D) Azure ExpressRoute
**Resposta Correta:** B
**Explicação Técnica:** O recurso de Firewall e Redes Virtuais em Contas de Armazenamento do Azure permite restringir o acesso público filtrando por faixas de IP estáticas da rede local corporativa ou sub-redes VNet autorizadas.

### Questão 405
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a principal finalidade da funcionalidade de Tags no Azure?
**Opções:**
- A) Criptografar arquivos armazenados nas contas de armazenamento
- B) Agrupar e categorizar recursos logicamente através de pares chave-valor para automação e relatórios de faturamento
- C) Bloquear a exclusão acidental de recursos essenciais
- D) Impor regras de validação de conformidade sobre os recursos
**Resposta Correta:** B
**Explicação Técnica:** As Tags (marcas) consistem em pares chave-valor associados aos recursos para organizar a visualização, consolidar relatórios de custos por departamento e facilitar scripts de automação.

### Questão 406
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Uma aplicação exige um banco de dados relacional totalmente gerenciado com suporte nativo ao motor PostgreSQL. Qual serviço do Azure deve ser implantado?
**Opções:**
- A) Azure Cosmos DB
- B) Banco de Dados do Azure para PostgreSQL (Azure Database for PostgreSQL)
- C) Instância Gerenciada do SQL do Azure
- D) Azure Synapse Analytics
**Resposta Correta:** B
**Explicação Técnica:** O Azure Database for PostgreSQL é um serviço de banco de dados relacional como serviço (PaaS) gerenciado pela Microsoft, que oferece alta disponibilidade, backups automáticos e escala com base na engine de código aberto do PostgreSQL.

### Questão 407
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que é o benefício de Economia de Escala na computação em nuvem?
**Opções:**
- A) A capacidade de executar código serverless sem pagar por infraestrutura ociosa
- B) A redução no custo operacional unitário obtida pelos grandes provedores de nuvem (como a Microsoft), que repassam essa economia em preços menores aos clientes
- C) A garantia de que os dados serão replicados para três data centers independentes
- D) A possibilidade de converter contratos OpEx em investimentos CapEx no final do ano fiscal
**Resposta Correta:** B
**Explicação Técnica:** Economia de Escala significa que provedores como a Microsoft compram infraestrutura massiva a custos unitários muito mais baixos, repassando eficiências e redução de tarifas aos clientes de nuvem.

### Questão 408
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite armazenar segredos, chaves de criptografia e certificados SSL/TLS em um repositório centralizado protegido por módulos de segurança de hardware (HSM)?
**Opções:**
- A) Microsoft Entra ID
- B) Azure Key Vault
- C) Microsoft Defender for Cloud
- D) Azure Policy
**Resposta Correta:** B
**Explicação Técnica:** O Azure Key Vault é a solução para gerenciar centralidamente e com segurança segredos de aplicação, chaves criptográficas e certificados digitais.

### Questão 409
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual painel no Portal do Azure informa o status atual de integridade dos serviços globais do Azure e alerta sobre paralisações planejadas ou incidentes de serviço em andamento que possam afetar seus recursos?
**Opções:**
- A) Azure Advisor
- B) Azure Service Health
- C) Azure Monitor
- D) Log Analytics Workspace
**Resposta Correta:** B
**Explicação Técnica:** O Azure Service Health fornece uma visão personalizada do status operacional dos serviços do Azure nas regiões onde seus recursos estão implantados, alertando sobre paralisações, manutenções programadas e avisos de integridade.

### Questão 410
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de redundância de armazenamento do Azure copia os dados de forma síncrona três vezes dentro de um único data center na região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS - Locally Redundant Storage)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância de Zona Geo-Resiliente (GZRS)
**Resposta Correta:** A
**Explicação Técnica:** O LRS (Locally Redundant Storage) replica seus dados três vezes dentro de uma única instalação/data center físico na região primária, oferecendo proteção contra falhas de hardware no nível de rack e disco.

### Questão 411
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa precisa garantir que nenhum desenvolvedor consiga excluir acidentalmente uma Conta de Armazenamento de produção. Qual recurso deve ser aplicado?
**Opções:**
- A) Bloqueio de Recurso do tipo CanNotDelete (Delete Lock)
- B) Política do Azure (Azure Policy) com efeito Deny
- C) Função RBAC de Leitor (Reader)
- D) Tag de Proteção de Dados
**Resposta Correta:** A
**Explicação Técnica:** O bloqueio de recursos do tipo *CanNotDelete* (Delete) impede a exclusão acidental do recurso por qualquer usuário, independentemente de suas permissões de acesso RBAC.

### Questão 412
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é uma plataforma de integração de workflows como serviço (PaaS serverless) que permite conectar aplicações e serviços através de conectores pré-construídos sem codificação complexa?
**Opções:**
- A) Azure Logic Apps
- B) Azure Functions
- C) Azure Event Grid
- D) Azure Service Bus
**Resposta Correta:** A
**Explicação Técnica:** O Azure Logic Apps permite automatizar e orquestrar fluxos de trabalho, processos de negócios e integrações de dados entre serviços de nuvem e locais através de uma interface visual com centenas de conectores.

### Questão 413
**Domínio:** Conceitos de Nuvem
**Enunciado:** Em um modelo de Infraestrutura como Serviço (IaaS), quem é o responsável pela aplicação de patches de segurança e atualizações do sistema operacional de uma máquina virtual no Azure?
**Opções:**
- A) A Microsoft exclusivamente
- B) O cliente exclusivamente
- C) Compartilhado igualmente entre o cliente e a Microsoft
- D) O parceiro de hardware de rede
**Resposta Correta:** B
**Explicação Técnica:** No modelo IaaS, o sistema operacional, atualizações, patches de segurança e a pilha de software instalada na máquina virtual são de responsabilidade exclusiva do cliente.

### Questão 414
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa necessita implantar contêineres Docker de forma rápida sem ter que gerenciar máquinas virtuais ou orquestradores complexos como o Kubernetes. Qual serviço é o mais adequado?
**Opções:**
- A) Instâncias de Contêiner do Azure (ACI - Azure Container Instances)
- B) Serviço de Kubernetes do Azure (AKS)
- C) Conjuntos de Escalabilidade de Máquinas Virtuais (VMSS)
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Instances (ACI) permite rodar contêineres Docker isolados sob demanda sem a necessidade de gerenciar VMs subjacentes ou configurar cluster/orquestrador.

### Questão 415
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta permite estimar o custo mensal esperado de implantar uma nova arquitetura no Azure antes de criar qualquer recurso?
**Opções:**
- A) Calculadora de TCO
- B) Calculadora de Preços do Azure (Pricing Calculator)
- C) Azure Cost Management
- D) Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** A Calculadora de Preços do Azure permite aos usuários estimar seus custos operacionais mensais combinando diferentes produtos, regiões e configurações de uso hipotéticos.

### Questão 416
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece inteligência artificial generativa corporativa com acesso a modelos avançados como GPT-4, DALL-E e modelos de linguagem de grande escala (LLM) com governança da Microsoft?
**Opções:**
- A) Serviço do Azure OpenAI (Azure OpenAI Service)
- B) Azure AI Search
- C) Azure Bot Service
- D) Azure Machine Learning
**Resposta Correta:** A
**Explicação Técnica:** O Azure OpenAI Service integra os modelos de IA da OpenAI (GPT-4, DALL-E, etc.) com a segurança, conformidade e infraestrutura de nuvem corporativa da Microsoft.

### Questão 417
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta é utilizada para realizar consultas em tempo real usando a linguagem KQL sobre as propriedades e inventário de milhões de recursos em múltiplos grupos de gerenciamento e assinaturas no Azure?
**Opções:**
- A) Azure Resource Graph
- B) Azure Log Analytics
- C) Azure Monitor
- D) Azure Data Explorer
**Resposta Correta:** A
**Explicação Técnica:** O Azure Resource Graph permite realizar consultas eficientes e rápidas sobre todo o inventário de recursos das suas assinaturas utilizando a linguagem Kusto Query Language (KQL).

### Questão 418
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual camada de acesso do Azure Blob Storage possui o menor custo de armazenamento por gigabyte, mas cobra o maior custo de recuperação e exige horas para restaurar os dados?
**Opções:**
- A) Camada Frequente (Hot)
- B) Camada Esporádica (Cool)
- C) Camada Fria (Cold)
- D) Camada de Arquivamento (Archive)
**Resposta Correta:** D
**Explicação Técnica:** A camada de Arquivamento (Archive) é otimizada para retenção de longo prazo de dados raramente acessados, oferecendo a menor tarifa de armazenamento e maior latência de reidratação (várias horas).

### Questão 419
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma organização quer padronizar o provisionamento de novos ambientes fornecendo um pacote completo com modelos ARM, atribuições de RBAC e políticas do Azure. Qual serviço legado de governança cumpre este papel?
**Opções:**
- A) Azure Blueprints
- B) Azure Arc
- C) Azure Automation
- D) Azure Developer CLI
**Resposta Correta:** A
**Explicação Técnica:** O Azure Blueprints permite definir um conjunto repetível de recursos do Azure (modelos ARM, políticas, atribuições de função RBAC) para garantir a governança em novas assinaturas.

### Questão 420
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure fornece um balanceador de carga de tráfego web de Camada 7 que inclui recursos de firewall de aplicação web (WAF) e descarregamento SSL?
**Opções:**
- A) Gateway de Aplicativo do Azure (Azure Application Gateway)
- B) Azure Load Balancer (Camada 4)
- C) Azure Traffic Manager
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway atua na Camada 7 (HTTP/HTTPS), oferecendo roteamento baseado em URL, SSL offloading e firewall de aplicação web (WAF).

### Questão 421
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual o termo que descreve a capacidade da nuvem de garantir que as aplicações permaneçam acessíveis mesmo durante falhas de componentes de hardware ou software?
**Opções:**
- A) Agilidade
- B) Alta Disponibilidade / Tolerância a Falhas
- C) Elasticidade
- D) Governança
**Resposta Correta:** B
**Explicação Técnica:** Alta Disponibilidade e Tolerância a Falhas garantem que a infraestrutura redundante assuma a carga de trabalho sem causar indisponibilidade perceptível para os usuários finais.

### Questão 422
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço de segurança centraliza o gerenciamento de postura de segurança (CSPM) e a proteção contra ameaças para recursos no Azure, na nuvem híbrida e em outras nuvens?
**Opções:**
- A) Microsoft Defender for Cloud
- B) Azure Key Vault
- C) Microsoft Sentinel
- D) Azure Policy
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Defender for Cloud avalia a postura de segurança dos recursos, calcula a Pontuação de Segurança (Secure Score) e fornece proteção contra ameaças em ambientes multicloud e híbridos.

### Questão 423
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de computação sem servidor (serverless) é orientado a eventos e executa pequenas unidades de código sob demanda sem requerer o gerenciamento de infraestrutura?
**Opções:**
- A) Azure Functions
- B) Máquinas Virtuais do Azure
- C) Azure App Service
- D) Conjuntos de Disponibilidade
**Resposta Correta:** A
**Explicação Técnica:** O Azure Functions permite executar código em resposta a eventos (triggers) com escalabilidade automática e custos baseados apenas no tempo de execução.

### Questão 424
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual portal oficial da Microsoft publica relatórios de auditoria independente, certificações ISO/SOC e documentação sobre como os serviços de nuvem da Microsoft cumprem regulamentações internacionais de privacidade?
**Opções:**
- A) Service Trust Portal (Portal de Confiança do Serviço)
- B) Microsoft Privacy Dashboard
- C) Azure Advisor
- D) Microsoft Learn
**Resposta Correta:** A
**Explicação Técnica:** O Service Trust Portal é a central da Microsoft onde clientes e auditores consultam certificados de conformidade, relatórios SOC, ISO e whitepapers de privacidade.

### Questão 425
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual componente do Azure permite estender a governança, políticas e serviços do Azure para servidores e clusters de Kubernetes localizados fora do Azure (on-premises ou em outras nuvens)?
**Opções:**
- A) Azure Arc
- B) Azure ExpressRoute
- C) Azure Migrate
- D) Azure Site Recovery
**Resposta Correta:** A
**Explicação Técnica:** O Azure Arc estende o painel de controle do Azure ARM para gerenciar e governar recursos físicos e virtuais localizados em data centers locais ou em concorrentes de nuvem.

### Questão 426
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que acontece quando duas políticas do Azure (Azure Policy) entram em conflito, onde uma restrição explicita o efeito Deny (Negar) e outra o efeito Audit (Auditar)?
**Opções:**
- A) A ação é permitida e apenas auditada
- B) O efeito Deny tem precedência e a ação de criação é bloqueada
- C) O sistema escolhe aleatoriamente a regra mais recente
- D) O recurso é criado mas marcado como aviso no Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** Na avaliação de conformidade do Azure Policy, qualquer regra de bloqueio explícito (*Deny*) se sobressai sobre avaliações menos restritivas (*Audit* ou *Disabled*).

### Questão 427
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual modelo de banco de dados relacional gerenciado oferece compatibilidade quase 100% com o motor SQL Server local, permitindo migrações de aplicações legadas com mínimo esforço de reengenharia?
**Opções:**
- A) Instância Gerenciada do SQL do Azure (Azure SQL Managed Instance)
- B) Banco de Dados SQL do Azure (Azure SQL Database - Single Database)
- C) Azure Cosmos DB
- D) Azure Synapse Analytics
**Resposta Correta:** A
**Explicação Técnica:** A Instância Gerenciada do SQL do Azure (SQL Managed Instance) combina a compatibilidade de recursos do SQL Server tradicional com os benefícios operacionais de um serviço PaaS totalmente gerenciado.

### Questão 428
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta é recomendada pela Microsoft para automatizar o provisionamento de infraestrutura como código (IaC) de forma nativa e declarativa no Azure com sintaxe simplificada em comparação aos modelos ARM JSON?
**Opções:**
- A) Azure Bicep
- B) Terraform
- C) Ansible
- D) PowerShell Desired State Configuration (DSC)
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bicep é uma linguagem de domínio específico (DSL) declarativa desenvolvida pela Microsoft que simplifica o desenvolvimento e compilação nativa para modelos ARM.

### Questão 429
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure oferece proteção contra ataques de Negação de Serviço Distribuída (DDoS) na camada de rede de forma contínua para todas as VNets?
**Opções:**
- A) Proteção Contra DDoS do Azure (Azure DDoS Protection)
- B) Firewall do Azure
- C) Grupo de Segurança de Rede (NSG)
- D) Azure Application Gateway
**Resposta Correta:** A
**Explicação Técnica:** O Azure DDoS Protection monitora o tráfego de rede e mitiga automaticamente ataques de inundação DDoS antes que afetem a disponibilidade das aplicações.

### Questão 430
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função dos Grupos de Gerenciamento (Management Groups) no Azure?
**Opções:**
- A) Agrupar máquinas virtuais para formar um cluster de alta disponibilidade
- B) Fornecer um escopo de governança acima de múltiplas Assinaturas do Azure para aplicar políticas, RBAC e conformidade de forma hierárquica
- C) Gerenciar os acessos de usuários ao Microsoft 365
- D) Agrupar conexões de rede privada entre VNets
**Resposta Correta:** B
**Explicação Técnica:** Os Grupos de Gerenciamento oferecem um nível de organização acima das assinaturas, permitindo aplicar políticas do Azure e atribuições de acesso RBAC de forma consistente em dezenas ou centenas de assinaturas.

### Questão 431
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de nuvem do Azure é projetado especificamente para atuar como um warehouse de dados de grande escala e plataforma de análise integrada que combina Big Data e armazenamento de dados empresarial?
**Opções:**
- A) Azure Synapse Analytics
- B) Azure Data Lake Storage
- C) Azure Stream Analytics
- D) Azure Data Factory
**Resposta Correta:** A
**Explicação Técnica:** O Azure Synapse Analytics unifica a ingestão de dados, data warehousing empresarial e análise de Big Data em um único serviço integrado.

### Questão 432
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é o recurso do Microsoft Entra ID que exige que os usuários forneçam uma verificação secundária (como um código enviado ao celular ou aprovação em aplicativo) durante o processo de login?
**Opções:**
- A) Autenticação Multifator do Microsoft Entra (MFA)
- B) Acesso Condicional (Conditional Access)
- C) Login Único (SSO)
- D) Proteção de Identidade (Identity Protection)
**Resposta Correta:** A
**Explicação Técnica:** A Autenticação Multifator (MFA) adiciona uma camada de segurança exigindo duas ou mais formas de verificação de identidade antes de conceder acesso.

### Questão 433
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de nuvem do Azure fornece instâncias de desktop virtual totalmente gerenciadas no Azure para permitir que os funcionários trabalhem remotamente com segurança?
**Opções:**
- A) Área de Trabalho Virtual do Azure (Azure Virtual Desktop - AVD)
- B) Azure DevTest Labs
- C) Conjuntos de Escalabilidade de Máquinas Virtuais
- D) Azure Bastion
**Resposta Correta:** A
**Explicação Técnica:** O Azure Virtual Desktop (AVD) é um serviço de virtualização de desktop e aplicativos totalmente gerenciado que roda na nuvem.

### Questão 434
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta é utilizada para monitorar o histórico completo de operações no nível de plano de controle realizadas em seus recursos do Azure (por exemplo, quem criou, modificou ou excluiu um recurso)?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Azure Application Insights
- C) Azure Metrics
- D) Azure Service Health
**Resposta Correta:** A
**Explicação Técnica:** O Log de Atividades (Activity Log) registra todos os eventos ocorridos no plano de gerenciamento (ARM) do Azure, permitindo auditorias detalhadas sobre quem realizou cada ação.

### Questão 435
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual tipo de IP público no Azure garante que o endereço IP associado a uma placa de rede de máquina virtual nunca mude durante o ciclo de vida do recurso, mesmo que a VM seja descalculada e reiniciada?
**Opções:**
- A) Endereço IP Público Estático
- B) Endereço IP Público Dinâmico
- C) Endereço IP de Loopback
- D) Endereço IP de Sub-rede Privada
**Resposta Correta:** A
**Explicação Técnica:** Um Endereço IP Público Estático permanece alocado fixamente à interface de rede até ser explicitamente desassociado ou excluído.

### Questão 436
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure avalia proativamente seus recursos para fornecer recomendações de otimização de custos, segurança, confiabilidade, desempenho e excelência operacional?
**Opções:**
- A) Azure Advisor
- B) Azure Monitor
- C) Azure Security Center
- D) Azure Inspector
**Resposta Correta:** A
**Explicação Técnica:** O Azure Advisor é um consultor personalizado de nuvem que analisa a telemetria dos seus recursos e emite recomendações alinhadas às boas práticas da Microsoft.

### Questão 437
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite gerenciar, implantar e escalar aplicações de microsserviços sem estado (stateless) e com estado (stateful) usando contêineres sem necessidade de administrar a infraestrutura subjacente de servidores?
**Opções:**
- A) Aplicativos de Contêiner do Azure (Azure Container Apps)
- B) Azure Functions
- C) Azure Virtual Machines
- D) Azure Logic Apps
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Apps é um serviço gerenciado serverless para microsserviços baseado em contêineres construído sobre Kubernetes e Dapr.

### Questão 438
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Como é chamada a garantia percentual da Microsoft sobre o tempo de atividade operacional e disponibilidade dos serviços de nuvem?
**Opções:**
- A) Contrato de Nível de Serviço (SLA - Service Level Agreement)
- B) Acordo de Governança Híbrida
- C) Indicador de Performance de TI (KPI)
- D) Acordo de Responsabilidade Compartilhada
**Resposta Correta:** A
**Explicação Técnica:** O SLA (Service Level Agreement) formaliza os compromissos da Microsoft quanto ao tempo de atividade, desempenho e créditos financeiros em caso de descumprimento de metas.

### Questão 439
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de banco de dados NoSQL do Azure oferece suporte a múltiplas APIs (como MongoDB, Cassandra, Gremlin e SQL) com latências de leitura e gravação de um dígito em milissegundos e distribuição global simplificada?
**Opções:**
- A) Azure Cosmos DB
- B) Banco de Dados SQL do Azure
- C) Azure Table Storage
- D) Azure Managed Redis
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cosmos DB é um banco de dados NoSQL multimodelo e distribuído globalmente que oferece latência garantida de milissegundos e distribuição global com um clique.

### Questão 440
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa possui licenças locais do Windows Server e SQL Server com Software Assurance. Qual benefício de precificação do Azure permite reutilizar essas licenças na nuvem para economizar significativamente no custo de VMs?
**Opções:**
- A) Benefício Híbrido do Azure (Azure Hybrid Benefit)
- B) Instâncias Reservadas do Azure
- C) Desconto por Volume Corporativo
- D) Créditos Dev/Test
**Resposta Correta:** A
**Explicação Técnica:** O Benefício Híbrido do Azure permite aplicar suas licenças locais existentes do Windows Server e SQL Server cobertas por Software Assurance para pagar tarifas reduzidas de computação em VMs no Azure.

### Questão 441
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual recurso do Azure permite criar uma conexão RDP/SSH totalmente segura e criptografada para uma Máquina Virtual do Azure diretamente através do navegador sem expor um IP público na VM?
**Opções:**
- A) Azure Bastion
- B) Azure ExpressRoute
- C) VPN Gateway
- D) Azure Application Gateway
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bastion é um serviço PaaS que fornece acesso RDP e SSH seguro e direto às suas máquinas virtuais através do Portal do Azure utilizando TLS na porta 443.

### Questão 442
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure é uma solução SIEM (Gerenciamento de Eventos e Informações de Segurança) e SOAR (Resposta Automatizada de Orquestração de Segurança) nativa da nuvem para análise de ameaças em toda a organização?
**Opções:**
- A) Microsoft Sentinel
- B) Microsoft Defender for Cloud
- C) Azure Key Vault
- D) Azure Monitor
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Sentinel é a solução SIEM/SOAR nativa de nuvem da Microsoft para coleta de dados de telemetria, detecção de ameaças, visibilidade de incidentes e resposta automatizada.

### Questão 443
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de replicação de dados do Azure Storage distribui cópias de dados de forma síncrona em três Zonas de Disponibilidade na região primária e de forma assíncrona para uma região secundária?
**Opções:**
- A) Armazenamento com Redundância de Zona Geo-Resiliente (GZRS - Geo-Zone-Redundant Storage)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância de Zona (ZRS)
- D) Armazenamento com Redundância Geográfica (GRS)
**Resposta Correta:** A
**Explicação Técnica:** O GZRS combina a alta disponibilidade de Zonas de Disponibilidade na região primária com a proteção contra desastres em nível regional replicando os dados para uma região secundária.

### Questão 444
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função do Controle de Acesso Baseado em Função (RBAC) do Azure?
**Opções:**
- A) Criptografar automaticamente os dados armazenados em disco
- B) Garantir o gerenciamento refinado de permissões de acesso aos recursos do Azure concedendo apenas as permissões necessárias para cada função
- C) Monitorar a saúde dos data centers físicos da Microsoft
- D) Fornecer roteamento de tráfego de rede privado
**Resposta Correta:** B
**Explicação Técnica:** O RBAC (Role-Based Access Control) permite conceder acessos granulares com base no princípio do menor privilégio, atribuindo funções (como Leitor, Colaborador, Proprietário) a usuários em escopos definidos.

### Questão 445
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual solução do Azure permite transferir petabytes de dados brutos para o armazenamento do Azure de forma offline através da entrega física de um dispositivo de armazenamento robusto fornecido pela Microsoft?
**Opções:**
- A) Azure Data Box
- B) Azure ExpressRoute
- C) Azure Import/Export
- D) Azure Migrate
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Box é um dispositivo físico seguro enviado pela Microsoft para transportar terabytes ou petabytes de dados de forma offline e rápida para o Azure.

### Questão 446
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual portal do Azure deve ser acessado por uma empresa para configurar alertas que notificam administradores quando o custo da assinatura ultrapassar 80% do limite mensal estipulado?
**Opções:**
- A) Gerenciamento de Custos do Azure (Azure Cost Management + Billing)
- B) Calculadora de TCO
- C) Azure Advisor
- D) Azure Service Health
**Resposta Correta:** A
**Explicação Técnica:** No Azure Cost Management, os administradores podem criar orçamentos e configurar alertas de limite de custo automatizados por e-mail ou webhook.

### Questão 447
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de computação em nuvem do Azure permite agendar e executar tarefas de processamento em lote em grande escala utilizando milhares de máquinas virtuais de alta performance?
**Opções:**
- A) Azure Batch
- B) Azure Functions
- C) Azure Logic Apps
- D) Azure App Service
**Resposta Correta:** A
**Explicação Técnica:** O Azure Batch automatiza o agendamento, gerenciamento e dimensionamento de trabalhos de computação de alto desempenho (HPC) e cargas de trabalho em lote pesadas.

### Questão 448
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a finalidade principal do serviço Microsoft Purview no ecossistema Azure?
**Opções:**
- A) Governança de dados, mapeamento de linhagem e catálogo unificado de dados
- B) Monitoramento de tráfego de rede e mitigação de DDoS
- C) Criptografia de discos e gerenciamento de segredos
- D) Execução de código serverless
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Purview é uma solução abrangente de governança e conformidade de dados que ajuda a gerenciar, catalogar e rastrear a linhagem de dados em fontes locais, multicloud e SaaS.

### Questão 449
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é a função de uma Rede Virtual (VNet) no Azure?
**Opções:**
- A) Fornecer uma rede isolada e privada na nuvem do Azure para que os recursos se comuniquem com segurança entre si, com a Internet e com redes locais
- B) Conectar computadores locais ao Microsoft 365
- C) Armazenar arquivos de vídeo não estruturados
- D) Executar scripts em lote em servidores físicos
**Resposta Correta:** A
**Explicação Técnica:** A Rede Virtual (VNet) é o bloco fundamental de construção para sua rede privada no Azure, permitindo o isolamento, comunicação e filtragem de tráfego entre recursos.

### Questão 450
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que acontece com os recursos dentro de um Grupo de Recursos do Azure quando o próprio Grupo de Recursos é excluído?
**Opções:**
- A) Todos os recursos contidos no grupo são excluídos automaticamente em cascata
- B) Os recursos são movidos automaticamente para o grupo de recursos padrão
- C) A exclusão falha se houver recursos ativos
- D) Os recursos são desativados mas continuam gerando custos de armazenamento
**Resposta Correta:** A
**Explicação Técnica:** Quando um Grupo de Recursos é excluído, a exclusão é aplicada em cascata para todos os recursos contidos dentro dele.

### Questão 451
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite implementar um cache em memória de altíssimo desempenho baseado na tecnologia open-source Redis para acelerar aplicações com alto volume de leituras?
**Opções:**
- A) Azure Managed Redis (antigo Azure Cache for Redis)
- B) Azure Cosmos DB
- C) Azure Table Storage
- D) Azure Blob Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Managed Redis (anteriormente denominado Azure Cache for Redis) fornece um repositório de dados em memória altamente escalável e de baixa latência para melhorar a performance de aplicações.

### Questão 452
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja garantir que todas as suas assinaturas do Azure sigam os padrões de conformidade da lei LGPD/GDPR sem depender de auditorias manuais. Qual serviço do Azure é o mais indicado para auditar e impor essas regras continuamente?
**Opções:**
- A) Azure Policy (Iniciativas e Definições de Política)
- B) Bloqueios de Recursos
- C) Tags do Azure
- D) Azure Cost Management
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy permite atribuir Iniciativas de Política (conjuntos de regras como a iniciativa de conformidade regulatória LGPD/GDPR) para avaliar e impor automaticamente padrões de conformidade em toda a organização.
