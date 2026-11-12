# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals - Lote 4 (Questões 151 a 200)

Esta base de conhecimento contém as questões 151 a 200 do exame **AZ-900: Microsoft Azure Fundamentals** formatadas para ingestão e automação de agentes de IA no Antigravity.

---

### Questão 151
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma organização deseja implantar recursos no Azure garantindo que nenhum recurso seja criado fora das regiões geográficas autorizadas na Europa. Qual recurso do Azure deve ser utilizado para aplicar essa restrição de conformidade?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks)
- B) Azure Policy
- C) Grupos de Segurança de Rede (NSG)
- D) Grupos de Gerenciamento (Management Groups)
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy permite definir e aplicar políticas corporativas que restringem os locais (regiões) onde os recursos podem ser criados, garantindo a conformidade regulatória e de governança.

### Questão 152
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de banco de dados relacional gerenciado do Azure oferece compatibilidade total com o mecanismo do SQL Server, suporte a transações distribuídas e isolamento completo de rede em uma instância dedicada?
**Opções:**
- A) Banco de Dados SQL do Azure (Azure SQL Database - Instância Única)
- B) Instância Gerenciada do SQL do Azure (Azure SQL Managed Instance)
- C) Azure Cosmos DB
- D) Banco de Dados do Azure para PostgreSQL
**Resposta Correta:** B
**Explicação Técnica:** A Instância Gerenciada do SQL do Azure (Azure SQL Managed Instance) oferece quase 100% de compatibilidade com o mecanismo do SQL Server local (on-premises), incluindo recursos como SQL Server Agent, Service Broker e transações entre bancos, combinados com os benefícios de um serviço PaaS totalmente gerenciado.

### Questão 153
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual benefício da nuvem descreve a capacidade de um sistema de recuperar serviços e dados após um desastre natural ou falha catastrófica de infraestrutura com o mínimo de perda de dados?
**Opções:**
- A) Alta Disponibilidade
- B) Recuperação de Desastres (Disaster Recovery)
- C) Agilidade
- D) Escala Horizontal
**Resposta Correta:** B
**Explicação Técnica:** A Recuperação de Desastres (Disaster Recovery) refere-se às estratégias e ferramentas (como backup remoto e replicação geográfica) que garantem a restauração de dados e continuidade dos negócios em caso de falhas catastróficas ou eventos desastrosos.

### Questão 154
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta no Portal do Azure permite estimar os custos mensais de uma solução composta por múltiplos serviços antes de realizar qualquer implantação real?
**Opções:**
- A) Calculadora de Custo Total de Propriedade (TCO)
- B) Calculadora de Preços do Azure (Azure Pricing Calculator)
- C) Gerenciamento de Custos do Azure (Azure Cost Management)
- D) Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** A Calculadora de Preços do Azure (Azure Pricing Calculator) é uma ferramenta baseada na web utilizada para estimar os custos operacionais esperados de serviços e recursos do Azure antes que eles sejam provisionados.

### Questão 155
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de redundância de armazenamento do Azure copia seus dados de forma síncrona três vezes dentro de um único data center na região primária?
**Opções:**
- A) Armazenamento com Redundância Geográfica (GRS)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância de Zona (ZRS)
- D) Armazenamento com Redundância Geográfica de Zona (GZRS)
**Resposta Correta:** B
**Explicação Técnica:** O Armazenamento com Redundância Local (LRS) replica os dados três vezes dentro de uma única instalação/data center na região primária, protegendo contra falhas físicas de hardware de servidor e disco.

### Questão 156
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja impedir a alteração ou exclusão acidental de uma conta de armazenamento crítica. Qual funcionalidade do Azure deve ser aplicada ao recurso?
**Opções:**
- A) Azure Policy
- B) Bloqueio de Recurso (Resource Lock - ReadOnly ou Delete)
- C) Controle de Acesso Baseado em Função (RBAC)
- D) Grupo de Segurança de Rede (NSG)
**Resposta Correta:** B
**Explicação Técnica:** Os Bloqueios de Recursos (Resource Locks) do Azure podem ser configurados como `ReadOnly` (somente leitura) ou `Delete` (impedir exclusão) para proteger recursos críticos contra alterações não intencionais ou exclusões acidentais por qualquer usuário.

### Questão 157
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é projetado para centralizar o gerenciamento e o armazenamento seguro de segredos de aplicativos, chaves de criptografia e certificados digitais SSL/TLS?
**Opções:**
- A) Microsoft Entra ID
- B) Azure Key Vault
- C) Azure Information Protection
- D) Microsoft Defender for Cloud
**Resposta Correta:** B
**Explicação Técnica:** O Azure Key Vault armazena e protege centralmente segredos (como senhas e tokens de conexão), chaves de criptografia e certificados SSL/TLS, permitindo acesso seguro e auditável por aplicações.

### Questão 158
**Domínio:** Conceitos de Nuvem
**Enunciado:** No modelo de computação em nuvem, qual termo descreve a alocação flexível de recursos em que você paga apenas pela quantidade exata de capacidade computacional consumida por segundo ou minuto?
**Opções:**
- A) Preço Fixo Anual
- B) Modelo de Preço Baseado em Consumo (Pay-As-You-Go)
- C) Despesa de Capital (CapEx)
- D) Custos Fixos de Infraestrutura
**Resposta Correta:** B
**Explicação Técnica:** O modelo de preço baseado em consumo (Pay-As-You-Go) garante que os clientes paguem apenas pelos recursos que realmente utilizam, sem custos iniciais de capital ou taxas de cancelamento.

### Questão 159
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite que desenvolvedores executem contêineres Docker sob demanda sem a necessidade de gerenciar máquinas virtuais subjacentes ou orquestradores complexos?
**Opções:**
- A) Serviços de Computação Virtualizada do Azure (Azure VMs)
- B) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- C) Serviço do Kubernetes do Azure (AKS)
- D) Serviço de Aplicativo do Azure (Azure App Service)
**Resposta Correta:** B
**Explicação Técnica:** As Instâncias de Contêiner do Azure (ACI) oferecem a maneira mais rápida e simples de executar um contêiner no Azure de forma serverless, sem provisionar máquinas virtuais ou adotar orquestradores avançados.

### Questão 160
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a estrutura de nível superior na hierarquia do Azure que permite organizar e aplicar políticas de governança e conformidade em múltiplas assinaturas do Azure de forma centralizada?
**Opções:**
- A) Grupos de Recursos (Resource Groups)
- B) Grupos de Gerenciamento (Management Groups)
- C) Assinaturas (Subscriptions)
- D) Leiras de Recursos (Resource Arrays)
**Resposta Correta:** B
**Explicação Técnica:** Os Grupos de Gerenciamento (Management Groups) fornecem um escopo de governança acima das assinaturas. Você pode organizar assinaturas em uma hierarquia e aplicar Azure Policies e RBAC que são herdados por todas as assinaturas e recursos filhos.

### Questão 161
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure atua como um balanceador de carga de tráfego da Web (Camada 7) que inclui recursos de firewall de aplicativo Web (WAF) e roteamento baseado em URL?
**Opções:**
- A) Azure Load Balancer
- B) Azure Application Gateway
- C) Azure Traffic Manager
- D) Azure Network Watcher
**Resposta Correta:** B
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego da Web (OSI camada 7) que permite gerenciar o tráfego para suas aplicações Web, oferecendo suporte a terminação SSL, roteamento baseado em caminho de URL e Firewall de Aplicativo Web (WAF).

### Questão 162
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa quer analisar e prever quanto gastará no Azure ao longo do próximo trimestre com base no histórico atual de uso. Qual serviço ou ferramenta do Portal do Azure fornece essa funcionalidade?
**Opções:**
- A) Azure Advisor
- B) Gerenciamento de Custos do Azure (Azure Cost Management)
- C) Monitor do Azure (Azure Monitor)
- D) Azure Service Health
**Resposta Correta:** B
**Explicação Técnica:** O Gerenciamento de Custos do Azure (Azure Cost Management) inclui recursos de análise de custos, orçamentos, alertas de gastos e previsão (forecasting) baseada em padrões de consumo históricos.

### Questão 163
**Domínio:** Conceitos de Nuvem
**Enunciado:** Em qual modelo de nuvem uma organização opera uma infraestrutura computacional compartilhada entre múltiplos clientes (locatários) na internet pública mantida por um provedor parceiro?
**Opções:**
- A) Nuvem Privada
- B) Nuvem Pública
- C) Nuvem Híbrida
- D) Nuvem Local (On-premises)
**Resposta Correta:** B
**Explicação Técnica:** Na Nuvem Pública, os recursos de computação são de propriedade e operados por um provedor de nuvem terceirizado (como a Microsoft) e compartilhados entre múltiplos locatários (multi-tenant) via Internet pública.

### Questão 164
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual solução de análise e IA do Azure oferece um ambiente de Data Lake e plataforma de processamento de Big Data baseada em Apache Spark totalmente gerenciada?
**Opções:**
- A) Azure Databricks
- B) Azure HDInsight
- C) Azure Synapse Analytics
- D) Azure Analysis Services
**Resposta Correta:** A
**Explicação Técnica:** O Azure Databricks é uma plataforma de análise baseada em Apache Spark otimizada para o Azure que simplifica a criação de soluções de Big Data, engenharia de dados e aprendizado de máquina.

### Questão 165
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure deve ser utilizado para coletar, analisar e agir sobre dados de teleometria e métricas de desempenho provenientes de ambientes de nuvem e locais?
**Opções:**
- A) Azure Service Health
- B) Monitor do Azure (Azure Monitor)
- C) Azure Advisor
- D) Microsoft Sentinel
**Resposta Correta:** B
**Explicação Técnica:** O Monitor do Azure (Azure Monitor) coleta, analisa e atua sobre dados de telemetria (métricas e logs) de ambientes de nuvem e locais para maximizar a disponibilidade e o desempenho de suas aplicações.

### Questão 166
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual camada de armazenamento do Azure Blob Storage é otimizada para armazenar dados que são raramente acessados e que exigem um tempo de recuperação de várias horas, oferecendo o menor custo de armazenamento por gigabyte?
**Opções:**
- A) Camada Frequente (Hot)
- B) Camada Esporádica (Cool)
- C) Camada de Arquivamento (Archive)
- D) Camada Fria (Cold)
**Resposta Correta:** C
**Explicação Técnica:** A camada de Arquivamento (Archive tier) do Blob Storage oferece o menor custo de armazenamento, mas tem custos de recuperação mais altos e exige várias horas para descongelar e disponibilizar os dados.

### Questão 167
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual painel no Portal do Azure informa aos clientes sobre interrupções de serviço planejadas e não planejadas, problemas de integridade de serviço e manutenções programadas que afetam sua assinatura?
**Opções:**
- A) Azure Status
- B) Azure Service Health
- C) Monitor do Azure
- D) Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** O Azure Service Health fornece uma visualização personalizada e detalhada sobre o status e a integridade dos serviços do Azure nas regiões em que seus recursos específicos estão implantados, avisando sobre incidentes e manutenções.

### Questão 168
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual ferramenta de linha de comando multiplataforma baseada em shells modernos (como PowerShell ou Bash) permite gerenciar recursos do Azure diretamente no navegador da Web sem instalar programas locais?
**Opções:**
- A) Azure Cloud Shell
- B) CLI do Azure (instalada localmente)
- C) PowerShell do Azure (instalado localmente)
- D) Portal do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cloud Shell é um terminal interativo e acessível via navegador Web que permite gerenciar recursos do Azure usando Bash ou PowerShell com autenticação automática.

### Questão 169
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa deseja migrar para a nuvem mantendo seus bancos de dados confidenciais em seu próprio data center local enquanto executa os servidores de aplicativos Web na nuvem pública. Qual modelo de implantação de nuvem é esse?
**Opções:**
- A) Nuvem Pública
- B) Nuvem Privada
- C) Nuvem Híbrida
- D) Multicloud Exclusiva
**Resposta Correta:** C
**Explicação Técnica:** A Nuvem Híbrida combina ambientes de nuvem pública e nuvem privada (ou infraestrutura local), permitindo que dados e aplicativos sejam compartilhados entre eles de forma integrada.

### Questão 170
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Microsoft Entra ID permite exigir uma segunda forma de identificação (como um código no aplicativo autenticador ou SMS) antes de conceder acesso a uma conta?
**Opções:**
- A) Autenticação Multifator do Microsoft Entra (MFA)
- B) Login Único (SSO)
- C) Controle de Acesso Baseado em Função (RBAC)
- D) Proteção de Identidade (Identity Protection)
**Resposta Correta:** A
**Explicação Técnica:** A Autenticação Multifator (MFA) adiciona uma camada adicional de segurança solicitando dois ou mais elementos de verificação (algo que você sabe + algo que você possui) durante o processo de logon.

### Questão 171
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de integração e fluxo de trabalho sem código (no-code) do Azure permite automatizar tarefas e conectar aplicativos e serviços de terceiros por meio de conectores pré-construídos?
**Opções:**
- A) Azure Functions
- B) Aplicativos Lógicos do Azure (Azure Logic Apps)
- C) Azure Event Grid
- D) Azure Service Bus
**Resposta Correta:** B
**Explicação Técnica:** O Azure Logic Apps é um serviço de nuvem que ajuda a agendar, automatizar e orquestrar tarefas, processos de negócios e fluxos de trabalho quando você precisa integrar aplicativos, dados, sistemas e serviços em empresas.

### Questão 172
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure é uma solução SIEM (Gerenciamento de Eventos e Informações de Segurança) e SOAR (Resposta Automatizada de Orquestração de Segurança) nativa de nuvem?
**Opções:**
- A) Microsoft Defender for Cloud
- B) Microsoft Sentinel
- C) Firewall do Azure
- D) Azure Key Vault
**Resposta Correta:** B
**Explicação Técnica:** O Microsoft Sentinel é uma solução SIEM e SOAR escalável e nativa da nuvem que oferece análise de segurança inteligente e inteligência contra ameaças em toda a empresa.

### Questão 173
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de conectividade permite interconectar duas Redes Virtuais do Azure (VNets) localizadas em regiões diferentes (por exemplo, Leste dos EUA e Europa Setentrional)?
**Opções:**
- A) Peering de VNet Regional
- B) Peering de VNet Global (Global VNet Peering)
- C) Azure ExpressRoute Direct
- D) Gateway de Aplicativo
**Resposta Correta:** B
**Explicação Técnica:** O Peering de VNet Global (Global VNet Peering) permite conectar Redes Virtuais do Azure em diferentes regiões geográficas, permitindo que os recursos se comuniquem com baixa latência pela rede global da Microsoft.

### Questão 174
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual conceito de nuvem se refere à capacidade de aumentar a capacidade computacional adicionando mais recursos (como mais CPU ou RAM) a uma máquina virtual existente?
**Opções:**
- A) Escalabilidade Horizontal (Scale-out)
- B) Escalabilidade Vertical (Scale-up)
- C) Elasticidade Automática
- D) Altíssima Disponibilidade
**Resposta Correta:** B
**Explicação Técnica:** Escalabilidade Vertical (Scale-up) significa adicionar mais recursos (como memória RAM ou processadores CPU) a um servidor existente para lidar com uma carga de trabalho crescente.

### Questão 175
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure avalia continuamente a postura de segurança dos seus recursos e fornece uma pontuação de segurança (Secure Score) com recomendações de endurecimento?
**Opções:**
- A) Azure Policy
- B) Microsoft Defender for Cloud
- C) Monitor do Azure
- D) Azure Information Protection
**Resposta Correta:** B
**Explicação Técnica:** O Microsoft Defender for Cloud calcula o Secure Score (Pontuação de Segurança) da sua infraestrutura e fornece recomendações para mitigar vulnerabilidades e fortalecer a postura de segurança.

### Questão 176
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de banco de dados NoSQL do Azure oferece latência de leitura e gravação de um dígito em milissegundos e suporte a distribuição global imediata com múltiplos modelos de API (como SQL, MongoDB, Cassandra)?
**Opções:**
- A) Banco de Dados SQL do Azure
- B) Azure Cosmos DB
- C) Azure Table Storage
- D) Banco de Dados do Azure para MySQL
**Resposta Correta:** B
**Explicação Técnica:** O Azure Cosmos DB é um banco de dados NoSQL totalmente gerenciado, distribuído globalmente, projetado para oferecer baixa latência de milissegundos e escalabilidade massiva de taxa de transferência.

### Questão 177
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa precisa atribuir a um desenvolvedor a permissão apenas para reiniciar máquinas virtuais, sem poder alterar as configurações de rede ou excluir o servidor. Qual recurso deve ser utilizado?
**Opções:**
- A) Azure Policy
- B) Controle de Acesso Baseado em Função (RBAC) do Azure
- C) Bloqueio de Recursos
- D) Tags do Azure
**Resposta Correta:** B
**Explicação Técnica:** O Controle de Acesso Baseado em Função (RBAC) do Azure permite a gestão granular de acessos, atribuindo funções com permissões específicas (como reiniciar VMs) a usuários ou grupos de usuários.

### Questão 178
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite gerenciar e estender os serviços e governança do Azure para infraestruturas locais, multicloud (como AWS ou GCP) e borda (edge)?
**Opções:**
- A) Azure Arc
- B) Azure DevOps
- C) Azure ExpressRoute
- D) Azure Migrate
**Resposta Correta:** A
**Explicação Técnica:** O Azure Arc simplifica a governança e o gerenciamento ao estender o plano de controle do Azure Resource Manager para servidores, clusters Kubernetes e serviços de dados fora do Azure.

### Questão 179
**Domínio:** Conceitos de Nuvem
**Enunciado:** No Modelo de Responsabilidade Compartilhada na Nuvem, quem é SEMPRE responsável pelo gerenciamento e proteção dos dados e informações do cliente, independentemente do modelo de nuvem (IaaS, PaaS ou SaaS)?
**Opções:**
- A) O Provedor de Nuvem (Microsoft)
- B) O Cliente (Organização)
- C) Compartilhado 50% / 50%
- D) A equipe de Suporte do Azure
**Resposta Correta:** B
**Explicação Técnica:** Em todos os modelos de serviço de nuvem (IaaS, PaaS e SaaS), o cliente mantém sempre a responsabilidade integral pela segurança de seus dados, informações, contas de usuários e identidades.

### Questão 180
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é o objetivo principal do uso de Tags no Azure?
**Opções:**
- A) Aumentar o desempenho da rede entre recursos
- B) Organizar recursos de forma lógica e categorizar custos por departamento ou ambiente
- C) Criptografar automaticamente o disco da máquina virtual
- D) Bloquear a exclusão não autorizada de recursos
**Resposta Correta:** B
**Explicação Técnica:** As Tags no Azure consistem em pares de chave-valor associados aos recursos que ajudam a organizar a infraestrutura de forma lógica, facilitando o gerenciamento, relatórios de faturamento e governança.

### Questão 181
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de firewall com estado (stateful) como serviço gerenciado do Azure inspeciona e filtra o tráfego de rede de entrada e saída para Redes Virtuais?
**Opções:**
- A) Firewall do Azure (Azure Firewall)
- B) Grupo de Segurança de Rede (NSG)
- C) Azure DDoS Protection
- D) Azure Application Gateway
**Resposta Correta:** A
**Explicação Técnica:** O Firewall do Azure é um serviço de segurança de rede gerenciado e baseado em nuvem que protege seus recursos de Rede Virtual com inteligência contra ameaças integrada e regras de filtragem com estado.

### Questão 182
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja garantir que quando o valor gasto no Azure atingir 80% do orçamento mensal definido, uma notificação por e-mail seja enviada aos administradores financeiros. Qual ferramenta deve ser configurada?
**Opções:**
- A) Alertas de Orçamento do Azure (Azure Budget Alerts)
- B) Azure Advisor
- C) Azure Policy
- D) Azure Service Health
**Resposta Correta:** A
**Explicação Técnica:** Os Alertas de Orçamento (Azure Budget Alerts) no Azure Cost Management notificam os administradores quando os custos reais ou previstos ultrapassam limiares definidos em um orçamento de gastos.

### Questão 183
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de armazenamento do Azure fornece compartilhamentos de arquivos gerenciados na nuvem acessíveis por meio dos protocolos padrão da indústria SMB (Server Message Block) ou NFS?
**Opções:**
- A) Azure Blob Storage
- B) Arquivos do Azure (Azure Files)
- C) Azure Table Storage
- D) Azure Disk Storage
**Resposta Correta:** B
**Explicação Técnica:** O Azure Files oferece compartilhamentos de arquivos totalmente gerenciados na nuvem que são acessíveis via protocolos padrão SMB e NFS, permitindo substituir ou complementar servidores de arquivos locais.

### Questão 184
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual termo descreve o benefício da nuvem em que você pode implantar aplicações rapidamente em várias regiões geográficas do mundo para oferecer baixa latência aos usuários finais locais?
**Opções:**
- A) Alcance Global (Global Reach)
- B) Tolerância a Falhas
- C) Alta Disponibilidade Local
- D) Elasticidade de Disco
**Resposta Correta:** A
**Explicação Técnica:** O Alcance Global (Global Reach) permite implantar recursos e aplicar presença de computação em regiões ao redor do mundo, aproximando os dados e aplicações dos seus clientes.

### Questão 185
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual portal corporativo público da Microsoft fornece relatórios de auditoria independente, certificações ISO/SOC e informações sobre conformidade regulatória para os serviços de nuvem da Microsoft?
**Opções:**
- A) Service Trust Portal
- B) Azure Advisor
- C) Microsoft Defender for Cloud
- D) Portal do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Service Trust Portal da Microsoft é a publicação pública que fornece acesso a relatórios de auditoria, certificações de conformidade e documentos de governança e privacidade dos serviços de nuvem da Microsoft.

### Questão 186
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite criar e gerenciar um grupo de máquinas virtuais idênticas com balanceamento de carga automático que pode aumentar ou diminuir o número de instâncias com base na demanda?
**Opções:**
- A) Conjuntos de Disponibilidade (Availability Sets)
- B) Conjuntos de Dimensionamento de Máquinas Virtuais (Virtual Machine Scale Sets - VMSS)
- C) Zonas de Disponibilidade
- D) Serviço de Aplicativo do Azure
**Resposta Correta:** B
**Explicação Técnica:** Os Conjuntos de Dimensionamento de Máquinas Virtuais (VMSS) permitem criar e gerenciar um grupo de VMs idênticas com suporte a auto-scaling (escala automática) de acordo com regras de uso de CPU ou tráfego.

### Questão 187
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual das seguintes afirmações sobre os Grupos de Recursos do Azure é VERDADEIRA?
**Opções:**
- A) Um recurso pode pertencer a múltiplos Grupos de Recursos simultaneamente
- B) Recursos em um Grupo de Recursos devem obrigatoriamente estar na mesma região que o Grupo de Recursos
- C) Se um Grupo de Recursos for excluído, todos os recursos contidos nele também serão excluídos
- D) Não é possível mover um recurso de um Grupo de Recursos para outro
**Resposta Correta:** C
**Explicação Técnica:** A exclusão de um Grupo de Recursos exclui automaticamente todos os recursos contidos nele. Um recurso só pode pertencer a um único grupo de recursos por vez e os recursos podem estar em regiões diferentes do grupo.

### Questão 188
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de IA do Azure oferece modelos pré-treinados para tradução de idiomas, conversão de fala em texto, visão computacional e análise de sentimentos sem exigir conhecimento avançado em Machine Learning?
**Opções:**
- A) Azure Machine Learning
- B) Serviços de IA do Azure (Azure AI Services / Cognitive Services)
- C) Azure Bot Service
- D) Azure Databricks
**Resposta Correta:** B
**Explicação Técnica:** Os Serviços de IA do Azure (anteriormente Cognitive Services) fornecem APIs e modelos de IA/ML pré-treinados que permitem integrar facilmente capacidades de visão, fala, linguagem e tomada de decisão em aplicativos.

### Questão 189
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa planeja parar de adquirir servidores físicos para seu data center e passar a utilizar servidores virtuais provisionados no Azure sob demanda. Qual alteração no tipo de despesa isso representa?
**Opções:**
- A) Mudança de OpEx para CapEx
- B) Mudança de CapEx para OpEx
- C) Eliminação de todos os custos de TI
- D) Aumento permanente de CapEx
**Resposta Correta:** B
**Explicação Técnica:** A substituição de compras físicas de hardware (CapEx - Despesas de Capital) pelo pagamento conforme o uso de recursos de nuvem (OpEx - Despesas Operacionais) reduz o investimento inicial e converte custos fixos em custos variáveis.

### Questão 190
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure permite rastrear visualmente a topologia de rede, diagnosticar problemas de roteamento de pacotes e capturar tráfego de rede para máquinas virtuais?
**Opções:**
- A) Azure Network Watcher
- B) Azure Monitor
- C) Azure ExpressRoute
- D) Grupo de Segurança de Rede
**Resposta Correta:** A
**Explicação Técnica:** O Azure Network Watcher fornece ferramentas para monitorar, diagnosticar, visualizar métricas e habilitar ou desabilitar logs para recursos em uma rede virtual do Azure.

### Questão 191
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual funcionalidade de computação do Azure permite executar tarefas em lote (batch processing) de alto desempenho em milhar de máquinas virtuais paralelas sem gerenciar a infraestrutura?
**Opções:**
- A) Azure Batch
- B) Azure Functions
- C) Azure Logic Apps
- D) Instâncias de Contêiner do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Batch permite executar trabalhos de computação paralela e de alto desempenho (HPC) em grande escala de forma eficiente no Azure, gerenciando a alocação e escalonamento de VMs.

### Questão 192
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço ou recurso do Azure permite criar uma identidade gerenciada para um recurso do Azure (como uma VM) para que ele se autentique em outros serviços (como o Key Vault) sem armazenar credenciais no código?
**Opções:**
- A) Identidades Gerenciadas para Recursos do Azure (Managed Identities)
- B) Microsoft Entra B2C
- C) Chaves de Acesso de Armazenamento
- D) Certificados SSL de Domínio
**Resposta Correta:** A
**Explicação Técnica:** As Identidades Gerenciadas (Managed Identities) no Microsoft Entra ID fornecem aos recursos do Azure uma identidade atribuída automaticamente que pode ser usada para se autenticar em serviços compatíveis sem expor segredos ou senhas em arquivos de configuração.

### Questão 193
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de redundância de armazenamento do Azure garante a replicação dos dados para uma segunda região geográfica secundária distante centenas de quilômetros da região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância Interna
**Resposta Correta:** C
**Explicação Técnica:** O Armazenamento com Redundância Geográfica (GRS) replica seus dados de forma síncrona três vezes na região primária e depois copia os dados assincronamente para uma região secundária distante.

### Questão 194
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que é o SLA (Service Level Agreement) no contexto dos serviços de nuvem da Microsoft?
**Opções:**
- A) O modelo financeiro de tributação dos serviços de nuvem
- B) O compromisso formal da Microsoft sobre o tempo de atividade (uptime) e disponibilidade garantida de um serviço
- C) O manual de instruções para instalação de servidores de nuvem
- D) A licença de uso do software para usuários finais
**Resposta Correta:** B
**Explicação Técnica:** O Contrato de Nível de Serviço (SLA) descreve os compromissos da Microsoft em relação ao tempo de atividade (uptime) e à disponibilidade dos serviços do Azure, além de definir créditos de serviço caso o nível não seja atingido.

### Questão 195
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de computação sem servidor (serverless) do Azure permite executar contêineres microserviços orientados a eventos com suporte a escala zero (scale to zero)?
**Opções:**
- A) Aplicativos de Contêiner do Azure (Azure Container Apps)
- B) Serviço de Aplicativo do Azure
- C) Máquinas Virtuais do Azure
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Apps é um serviço serverless totalmente gerenciado para construir e implantar microserviços e aplicativos baseados em contêineres sem gerenciar infraestruturas complexas ou Kubernetes diretamente.

### Questão 196
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa precisa implantar novos recursos no Azure seguindo um modelo reutilizável declarativo escrito em sintaxe JSON ou Bicep. Qual recurso deve ser utilizado?
**Opções:**
- A) Modelos do Azure Resource Manager (ARM Templates)
- B) Azure Policy
- C) Scripts do PowerShell
- D) Azure Blueprints
**Resposta Correta:** A
**Explicação Técnica:** Os Modelos do Azure Resource Manager (ARM Templates) e arquivos Bicep permitem definir e implantar toda a infraestrutura do Azure usando código declarativo em arquivos JSON/Bicep.

### Questão 197
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure conecta redes locais à Nuvem do Azure usando um túnel criptografado IPsec/IKE pela Internet pública?
**Opções:**
- A) Azure ExpressRoute
- B) Gateway de VPN do Azure (Azure VPN Gateway)
- C) Peering de VNet
- D) Azure Front Door
**Resposta Correta:** B
**Explicação Técnica:** O Gateway de VPN do Azure (Azure VPN Gateway) envia tráfego criptografado entre uma rede virtual do Azure e uma localização local através da Internet pública usando conexões VPN site a site.

### Questão 198
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual das seguintes opções é uma característica EXCLUSIVA do modelo de serviço de nuvem Plataforma como Serviço (PaaS)?
**Opções:**
- A) O cliente gerencia o hardware físico do data center
- B) O cliente gerencia o código e os dados do aplicativo, enquanto a nuvem gerencia o SO, middleware e runtime
- C) O cliente compra licenças diretas de software prontas para consumo do usuário final
- D) O cliente tem controle total sobre o sistema operacional subjacente e patches de kernel
**Resposta Correta:** B
**Explicação Técnica:** No modelo PaaS, o provedor de nuvem cuida do hardware, rede, virtualização, sistema operacional e runtime de desenvolvimento, permitindo que o cliente foque exclusivamente na construção do código e gerenciamento de dados do aplicativo.

### Questão 199
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta no Portal do Azure permite pesquisar recursos por nome, acessar a documentação oficial da Microsoft e abrir solicitações de suporte diretamente da barra superior?
**Opções:**
- A) Barra de Pesquisa Global do Portal do Azure
- B) Azure Cloud Shell
- C) Monitor do Azure
- D) Central de Segurança do Azure
**Resposta Correta:** A
**Explicação Técnica:** A barra de pesquisa global na parte superior do Portal do Azure permite pesquisar serviços, recursos, documentação, tutoriais e navegar rapidamente para a seção de ajuda e suporte.

### Questão 200
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço global da Microsoft atua como uma rede de entrega de conteúdo (CDN) e balanceador de carga HTTP/HTTPS que acelera o acesso dos usuários finais a aplicações Web globais?
**Opções:**
- A) Azure Front Door
- B) Azure Traffic Manager
- C) Azure Load Balancer
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Front Door é uma plataforma global e escalável de rede de entrega de conteúdo (CDN) e balanceamento de carga que usa a rede de borda global da Microsoft para oferecer acesso rápido, confiável e seguro a suas aplicações Web.
