# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals - Lote 8 (Questões 351 a 400)

Esta base de conhecimento contém as questões 351 a 400 do exame **AZ-900: Microsoft Azure Fundamentals** formatadas para ingestão e automação no Antigravity.

---

### Questão 351
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual das seguintes afirmações descreve corretamente a principal vantagem da computação em nuvem em relação aos data centers locais tradicionais no que tange à escalabilidade?
**Opções:**
- A) A nuvem exige pagamento adiantado para reserva de capacidade de armazenamento por 5 anos.
- B) A nuvem permite adicionar e remover recursos de computação quase instantaneamente com base nas demandas de tráfego.
- C) Os data centers locais eliminam totalmente os custos de manutenção de hardware e energia.
- D) A nuvem impede a expansão de servidores em regiões geográficas diferentes do país de origem.
**Resposta Correta:** B
**Explicação Técnica:** A escalabilidade e a agilidade da computação em nuvem permitem que as empresas ajustem a capacidade de infraestrutura quase instantaneamente (horizontal ou verticalmente) para atender a picos ou reduções de demanda, ao contrário do ambiente local que exige aquisição demorada de hardware.

### Questão 352
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Uma empresa precisa criar um repositório centralizado e seguro de chaves de criptografia, segredos de aplicação, senhas de banco de dados e certificados SSL/TLS. Qual serviço do Azure atende a esse requisito?
**Opções:**
- A) Azure Key Vault
- B) Microsoft Entra ID
- C) Azure Security Center
- D) Azure Storage Table
**Resposta Correta:** A
**Explicação Técnica:** O Azure Key Vault é o serviço gerenciado de nuvem para armazenar e proteger com segurança segredos, chaves de criptografia e certificados com controle rigoroso de acesso e criptografia respaldada por HSM (Hardware Security Modules).

### Questão 353
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Você precisa visualizar o impacto de uma manutenção planejada nos data centers do Azure que possa afetar os serviços da sua assinatura. Qual ferramenta do Azure fornece esse painel personalizado de status?
**Opções:**
- A) Azure Service Health
- B) Azure Status (Público)
- C) Azure Advisor
- D) Azure Monitor
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Health fornece um painel personalizado informando sobre o status de integridade dos serviços do Azure implantados na sua assinatura específica, incluindo manutenções planejadas, incidentes em andamento e avisos de segurança.

### Questão 354
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite conectar dispositivos de Internet das Coisas (IoT) à nuvem para comunicação bidirecional segura entre milhões de dispositivos e o backend da aplicação?
**Opções:**
- A) Azure IoT Hub
- B) Azure Event Grid
- C) Azure Logic Apps
- D) Azure Notification Hubs
**Resposta Correta:** A
**Explicação Técnica:** O Azure IoT Hub é um serviço totalmente gerenciado que atua como um hub central de mensagens para comunicação bidirecional segura e confiável entre milhões de dispositivos IoT e a nuvem.

### Questão 355
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Sua empresa precisa impedir a alteração acidental ou a exclusão de uma Conta de Armazenamento crítica do Azure, mesmo que o administrador possua a função de Proprietário (Owner) no RBAC. O que deve ser aplicado à conta?
**Opções:**
- A) Um Bloqueio de Recurso (Resource Lock) do tipo ReadOnly ou Delete
- B) Uma Azure Policy de auditoria
- C) Um Grupo de Gerenciamento exclusivo
- D) Uma regra de marcação de Tag
**Resposta Correta:** A
**Explicação Técnica:** Os Bloqueios de Recursos (Resource Locks) aplicados no nível do recurso suplantam as permissões do RBAC. Um bloqueio de exclusão (*CanNotDelete*) impede que qualquer usuário exclua o recurso até que a trava seja explicitamente removida.

### Questão 356
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece um banco de dados relacional totalmente gerenciado baseado no mecanismo do PostgreSQL com suporte a alta disponibilidade e atualizações automáticas?
**Opções:**
- A) Azure Database for PostgreSQL
- B) Azure Cosmos DB
- C) Azure SQL Database
- D) Azure Synapse Analytics
**Resposta Correta:** A
**Explicação Técnica:** O Azure Database for PostgreSQL é o serviço de banco de dados relacional PaaS da Microsoft focado na tecnologia aberta PostgreSQL, lidando automaticamente com backups, atualizações, patches e alta disponibilidade.

### Questão 357
**Domínio:** Conceitos de Nuvem
**Enunciado:** No Modelo de Responsabilidade Compartilhada da nuvem, de quem é a responsabilidade pela segurança dos dados do cliente e pelo gerenciamento de identidades/acessos em qualquer modelo de nuvem (IaaS, PaaS ou SaaS)?
**Opções:**
- A) Sempre do cliente
- B) Sempre da Microsoft
- C) Compartilhada 50% em IaaS e 100% da Microsoft em SaaS
- D) Exclusiva do provedor de telecomunicações
**Resposta Correta:** A
**Explicação Técnica:** Em todos os modelos de serviço de nuvem (IaaS, PaaS e SaaS), o cliente sempre retém a responsabilidade final pela governança dos seus dados e pelo gerenciamento das contas e identidades de acesso.

### Questão 358
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual tipo de armazenamento em nuvem é mais recomendado para guardar arquivos de registro (logs) que raramente são acessados, mas precisam ser retidos por motivos de conformidade legal por no mínimo 180 dias ao menor custo possível?
**Opções:**
- A) Camada de Acesso Raro / Arquivamento (Archive Tier) do Azure Blob Storage
- B) Camada Frequente (Hot Tier)
- C) Camada Esfria (Cool Tier)
- D) Azure Files Premium
**Resposta Correta:** A
**Explicação Técnica:** A camada de Arquivamento (Archive Tier) do Azure Blob Storage oferece o menor custo de armazenamento para dados não estruturados que podem tolerar várias horas de latência de reidratação e que raramente são consultados.

### Questão 359
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja organizar suas assinaturas do Azure em uma hierarquia unificada para aplicar políticas de conformidade e controle de acesso a múltiplos projetos de forma centralizada. Qual estrutura deve ser usada?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups)
- B) Grupos de Recursos (Resource Groups)
- C) Unidades Administrativas
- D) Regiões emparelhadas
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento fornecem um nível de escopo acima das assinaturas. As assinaturas são organizadas em contêineres chamados grupos de gerenciamento para aplicar governança, Azure Policy e RBAC em escala.

### Questão 360
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece uma solução de balanceamento de carga de tráfego web de Camada 7 que inclui funcionalidade de Firewall de Aplicação Web (WAF) e roteamento baseado em URL?
**Opções:**
- A) Azure Application Gateway
- B) Azure Load Balancer (Camada 4)
- C) Azure Traffic Manager
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego web (Camada 7 OSI) que permite gerenciar o tráfego para aplicações web e inclui recursos como terminação SSL e Web Application Firewall (WAF).

### Questão 361
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que é o Azure Bicep?
**Opções:**
- A) Uma linguagem de sintaxe declarativa específica do Azure utilizada para implantar recursos de infraestrutura como código (IaC) de forma simplificada em relação aos modelos ARM.
- B) Um serviço de firewall de rede gerenciado pela Microsoft.
- C) Um banco de dados NoSQL de ultra-baixa latência.
- D) Um plano de suporte empresarial exclusivo para grandes corporações.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bicep é uma linguagem de domínio específico (DSL) que usa sintaxe declarativa para implantar recursos do Azure como código (IaC), substituindo a complexidade do JSON dos modelos ARM tradicionais.

### Questão 362
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de redundância de armazenamento do Azure replica seus dados de forma síncrona três vezes dentro de um único data center na região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geo-Zonal (GZRS)
- D) Armazenamento com Redundância Geográfica (GRS)
**Resposta Correta:** A
**Explicação Técnica:** O LRS (Locally Redundant Storage) replica os dados três vezes dentro de um único local físico/data center na região primária, oferecendo proteção contra falhas de disco/hardware individual.

### Questão 363
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta online permite simular e estimar os custos mensais hipotéticos de serviços do Azure antes de implantar qualquer infraestrutura na nuvem?
**Opções:**
- A) Calculadora de Preços do Azure (Pricing Calculator)
- B) Calculadora de TCO (Total Cost of Ownership)
- C) Azure Cost Management + Billing
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** A Calculadora de Preços do Azure permite estimar os custos operacionais de arquiteturas planejadas configurando recursos, regiões e volume de uso antes do provisionamento.

### Questão 364
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é um barramento de integração de mensagens corporativas seguro que utiliza filas e tópicos com assinaturas no modelo Publish/Subscribe para desacoplar aplicações?
**Opções:**
- A) Azure Service Bus
- B) Azure Event Grid
- C) Azure Event Hubs
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Bus é um corretor de mensagens corporativo (message broker) totalmente gerenciado com filas de mensagens e tópicos de publicação/assinatura para integração de sistemas e microsserviços.

### Questão 365
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Microsoft Entra ID permite exigir que os usuários forneçam uma segunda forma de identificação (como um código enviado por SMS ou pelo aplicativo autenticador) ao realizar login?
**Opções:**
- A) Autenticação Multifator (MFA) do Microsoft Entra
- B) Controle de Acesso Baseado em Função (RBAC)
- C) Azure Key Vault
- D) Log Analytics Workspace
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Entra MFA adiciona uma camada de proteção ao processo de login, exigindo dois ou mais elementos de verificação (algo que você sabe + algo que você possui).

### Questão 366
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite gerenciar e implantar contêineres Docker sem a necessidade de configurar ou gerenciar instâncias de controle ou nós do Kubernetes?
**Opções:**
- A) Instâncias de Contêiner do Azure (ACI - Azure Container Instances)
- B) Azure Kubernetes Service (AKS)
- C) Azure Virtual Machines
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O ACI (Azure Container Instances) oferece o método mais rápido e simples de executar um contêiner no Azure, sem ter que provisionar máquinas virtuais ou adotar um orquestrador complexo como o AKS.

### Questão 367
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja auditar quem criou, modificou ou excluiu uma máquina virtual específica nos últimos 90 dias. Qual registro deve ser consultado no Azure?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Azure Application Insights
- C) Azure Service Health
- D) Log de Diagnóstico do IIS
**Resposta Correta:** A
**Explicação Técnica:** O Azure Activity Log é um log da plataforma que fornece insights sobre eventos no nível de assinatura (operações do plano de controle, como criação, atualização ou exclusão de recursos).

### Questão 368
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece um data warehouse de nível empresarial de alta escala que combina integração de dados, análise de Big Data e processamento analítico massivamente paralelo (MPP)?
**Opções:**
- A) Azure Synapse Analytics
- B) Azure Databricks
- C) Azure HDInsight
- D) Azure Stream Analytics
**Resposta Correta:** A
**Explicação Técnica:** O Azure Synapse Analytics é um serviço de análise ilimitado que reúne armazenamento de dados corporativos (Enterprise Data Warehousing) e análise de Big Data em uma experiência unificada.

### Questão 369
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual é o benefício de operar em nuvem conhecido como "Economia de Escala"?
**Opções:**
- A) Capacidade de grandes provedores de nuvem como a Microsoft reduzirem custos operacionais e repassarem a economia em forma de preços mais baixos para os clientes.
- B) Capacidade do cliente de executar apenas um único servidor sem gastar energia local.
- C) Garantia de que todos os data centers locais custam metade do valor da nuvem pública.
- D) Eliminação total de regulamentações de governança de dados.
**Resposta Correta:** A
**Explicação Técnica:** Economia de escala é o conceito em que a operação em escala massiva (como a mantida pela Microsoft) reduz os custos de compra e operação de infraestrutura por unidade, permitindo oferecer preços altamente competitivos.

### Questão 370
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual componente do Azure permite conectar recursos em uma VNet do Azure à Internet sem expor os endereços IP privados das máquinas virtuais diretamente para conexões de entrada?
**Opções:**
- A) NAT Gateway da VNet do Azure
- B) Peering de Rede Virtual
- C) Azure ExpressRoute
- D) Tabela de Rotas Personalizada
**Resposta Correta:** A
**Explicação Técnica:** O Azure Virtual Network NAT (Network Address Translation) simplifica a conectividade de saída para a Internet em redes virtuais, fornecendo conectividade SNAT totalmente gerenciada e segura para sub-redes.

### Questão 371
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual solução de conformidade da Microsoft oferece acesso público a relatórios de auditoria independentes, certificações ISO/SOC e documentação sobre como a Microsoft protege a privacidade dos dados na nuvem?
**Opções:**
- A) Portal de Confiança do Serviço (Service Trust Portal)
- B) Azure Advisor
- C) Microsoft Sentinel
- D) Azure Purview
**Resposta Correta:** A
**Explicação Técnica:** O Service Trust Portal (STP) é o portal público da Microsoft que fornece relatórios de auditoria de conformidade, certificações de terceiros (ISO, SOC, HIPAA) e whitepapers sobre privacidade e segurança.

### Questão 372
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Uma empresa deseja executar workloads de Inteligência Artificial usando modelos de linguagem avançados (como modelos GPT) com a segurança, conformidade e integração privada do Azure. Qual serviço atende a essa necessidade?
**Opções:**
- A) Serviço Azure OpenAI
- B) Azure Machine Learning
- C) Azure AI Bot Service
- D) Azure Cognitive Search
**Resposta Correta:** A
**Explicação Técnica:** O Azure OpenAI Service dá aos clientes acesso aos modelos avançados de IA generativa da OpenAI (incluindo GPT-4 e DALL-E) com as capacidades de segurança corporativa, governança e rede do Azure.

### Questão 373
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual tipo de regra do Controle de Acesso Baseado em Função (RBAC) do Azure concede permissão apenas para visualizar todos os recursos de uma assinatura, mas proíbe qualquer alteração ou criação?
**Opções:**
- A) Leitor (Reader)
- B) Colaborador (Contributor)
- C) Proprietário (Owner)
- D) Administrador de Usuários
**Resposta Correta:** A
**Explicação Técnica:** A função interna Leitor (*Reader*) no RBAC permite visualizar tudo em um escopo, mas não autoriza criar, modificar ou excluir nenhum recurso.

### Questão 374
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é a função de uma Região Emparelhada (Paired Region) no Azure?
**Opções:**
- A) Garantir que cada região seja vinculada a outra na mesma geografia a pelo menos 300 milhas de distância para isolamento contra desastres regionais e atualizações sequenciais de plataforma.
- B) Conectar duas regiões locais por cabos de fibra óptica dedicados de alta velocidade sem passar por data centers.
- C) Permitir o compartilhamento de máquinas virtuais entre contas de clientes diferentes.
- D) Garantir o backup automático gratuito de todas as tabelas SQL do Azure.
**Resposta Correta:** A
**Explicação Técnica:** Cada região do Azure é emparelhada com outra região dentro da mesma geografia (a pelo menos 300 milhas de distância), o que permite replicação cruzada e atualização de software sequencial para minimizar downtime em desastres em grande escala.

### Questão 375
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que é o Microsoft Defender for Cloud?
**Opções:**
- A) Uma ferramenta de Gerenciamento de Postura de Segurança na Nuvem (CSPM) e Proteção de Carga de Trabalho (CWPP) que monitora e protege recursos em ambientes Azure, multicloud e locais.
- B) Um serviço exclusivo para prevenção de ataques DDoS em redes virtuais.
- C) Uma solução de armazenamento de backup de longo prazo.
- D) Um plugin para o Visual Studio Code para compilar modelos ARM.
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Defender for Cloud é uma ferramenta de gerenciamento de postura de segurança e proteção contra ameaças para recursos no Azure, AWS, GCP e servidores locais.

### Questão 376
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite implantar um cluster gerenciado do Kubernetes para orquestração automática de contêineres escaláveis?
**Opções:**
- A) Azure Kubernetes Service (AKS)
- B) Azure Container Instances (ACI)
- C) Azure App Service
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O AKS (Azure Kubernetes Service) simplifica a implantação, o gerenciamento e a operação de um cluster Kubernetes gerenciado no Azure.

### Questão 377
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso permite categorizar recursos do Azure associando pares de Chave:Valor (Key:Value) para fins de consolidação de relatórios de faturamento e organização lógica?
**Opções:**
- A) Tags (Etiquetas) do Azure
- B) Bloqueios de Recursos
- C) Azure Policy
- D) Grupos de Gerenciamento
**Resposta Correta:** A
**Explicação Técnica:** As Tags aplicam metadados aos recursos na forma de pares chave-valor para agrupar recursos logicamente, simplificando a visualização de relatórios de custos por departamento ou ambiente.

### Questão 378
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure fornece análises em tempo real e processamento de fluxo de eventos (event-streaming) de dados vindos de dispositivos IoT ou aplicações?
**Opções:**
- A) Azure Stream Analytics
- B) Azure Data Factory
- C) Azure Synapse Analytics
- D) Azure SQL Database
**Resposta Correta:** A
**Explicação Técnica:** O Azure Stream Analytics é um mecanismo de processamento de eventos complexos e análise de dados em tempo real projetado para analisar volumes massivos de streaming de dados.

### Questão 379
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure permite executar consultas analíticas avançadas em grafos para inventariar e mapear rapidamente todos os recursos implantados em suas assinaturas usando KQL (Kusto Query Language)?
**Opções:**
- A) Azure Resource Graph
- B) Azure Advisor
- C) Azure Monitor
- D) Azure Policy
**Resposta Correta:** A
**Explicação Técnica:** O Azure Resource Graph é um serviço que estende o Gerenciamento de Recursos do Azure (ARM) fornecendo exploração de recursos em grande escala com capacidade de consultar de maneira rápida e eficiente milhares de assinaturas com KQL.

### Questão 380
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O que é o Peering de Rede Virtual Global (Global VNet Peering)?
**Opções:**
- A) A capacidade de conectar Redes Virtuais (VNets) do Azure localizadas em regiões geográficas diferentes através da rede backbone privada da Microsoft.
- B) Uma conexão dedicada ponto-a-ponto via satélite.
- C) Um recurso de roteamento de e-mails corporativos no Microsoft 365.
- D) Uma VPN pública criptografada baseada em SSL.
**Resposta Correta:** A
**Explicação Técnica:** O Global VNet Peering permite conectar VNets que estão em regiões diferentes do Azure, permitindo tráfego privado, de alta velocidade e baixa latência através do backbone global da Microsoft.

### Questão 381
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure permite monitorar a disponibilidade e o desempenho de suas aplicações web (APM) coletando telemetria e rastreando exceções em tempo real?
**Opções:**
- A) Application Insights (Recurso do Azure Monitor)
- B) Azure Service Health
- C) Azure Network Watcher
- D) Microsoft Sentinel
**Resposta Correta:** A
**Explicação Técnica:** O Application Insights é um recurso do Azure Monitor que oferece gerenciamento de desempenho de aplicações (APM) para desenvolvedores, monitorando aplicações ativas em tempo real.

### Questão 382
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece um serviço de arquivos de rede totalmente gerenciado que pode ser acessado via protocolo padrão SMB ou NFS?
**Opções:**
- A) Azure Files
- B) Azure Blob Storage
- C) Azure Disk Storage
- D) Azure Data Lake Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files oferece compartilhamentos de arquivos totalmente gerenciados na nuvem acessíveis por meio dos protocolos padrão da indústria Server Message Block (SMB) ou Network File System (NFS).

### Questão 383
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função das Notificações de Alerta de Orçamento (Budget Alerts) no Azure Cost Management?
**Opções:**
- A) Notificar automaticamente os administradores por e-mail quando os gastos reais ou previstos atingirem limites percentuais do orçamento configurado.
- B) Encerrar automaticamente todas as máquinas virtuais quando o limite do cartão de crédito for atingido.
- C) Bloquear a criação de novas contas de armazenamento no final do mês.
- D) Converter a assinatura de Pague o que Usar para Reservada.
**Resposta Correta:** A
**Explicação Técnica:** Os Alertas de Orçamento notificam os envolvidos quando os custos reais ou estimados superam os patamares percentuais definidos (ex.: 80% do orçamento mensal), sem interromper automaticamente os serviços.

### Questão 384
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o nível de SLA padrão de disponibilidade oferecido pela Microsoft para uma única máquina virtual que utiliza Discos SSD Premium no Azure?
**Opções:**
- A) 99,9%
- B) 99,99%
- C) 99,0%
- D) 100%
**Resposta Correta:** A
**Explicação Técnica:** Para qualquer VM de instância única usando armazenamento de disco SSD Premium ou Ultra Disk para todos os discos do SO e de dados, a Microsoft garante SLA de disponibilidade de 99,9%.

### Questão 385
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Azure permite criar ambientes padronizados repetíveis contendo modelos ARM, definições de Azure Policy e atribuições de RBAC para implantação de novas assinaturas corporativas?
**Opções:**
- A) Azure Blueprints
- B) Azure Advisor
- C) Azure Resource Graph
- D) Azure Activity Log
**Resposta Correta:** A
**Explicação Técnica:** O Azure Blueprints permite que engenheiros de nuvem definam um conjunto repetível de recursos do Azure (políticas, modelos ARM, RBAC) que implementa e cumpre os padrões e requisitos de conformidade da organização.

### Questão 386
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual tipo de serviço do Azure permite executar trabalhos em lote de alto desempenho (HPC - High Performance Computing) e computação paralela em escala em milhares de máquinas virtuais sem gerenciamento manual de clusters?
**Opções:**
- A) Azure Batch
- B) Azure Functions
- C) Azure Logic Apps
- D) Azure App Service
**Resposta Correta:** A
**Explicação Técnica:** O Azure Batch é um serviço de agendamento de tarefas e gerenciamento de computação que permite executar trabalhos em lote paralelos e de alto desempenho (HPC) em escala no Azure.

### Questão 387
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que é o Microsoft Purview?
**Opções:**
- A) Uma solução unificada de governança, risco e conformidade de dados que ajuda a gerenciar e governar dados locais, multicloud e SaaS.
- B) Um firewall de borda da rede privada do Azure.
- C) Uma calculadora de previsão de custos de tráfego de saída.
- D) Um serviço de CDN para acelerar imagens estáticas.
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Purview é uma família de soluções de governança de dados que ajuda a catalogar, rastrear, classificar e proteger dados em toda a sua organização (locais, multicloud e SaaS).

### Questão 388
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de segurança do Azure protege seus recursos de rede contra ataques massivos de negação de serviço distribuída na camada de rede (Camadas 3 e 4 OSI)?
**Opções:**
- A) Proteção Contra DDoS do Azure (Azure DDoS Protection)
- B) Azure Web Application Firewall (WAF)
- C) Grupos de Segurança de Rede (NSG)
- D) Azure Key Vault
**Resposta Correta:** A
**Explicação Técnica:** O Azure DDoS Protection fornece recursos aprimorados de mitigação de DDoS para proteger recursos específicos em redes virtuais contra ataques de saturação de volume e rede.

### Questão 389
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual opção do Azure permite pagar antecipadamente por recursos computacionais (como VMs ou bancos de dados) por um período de 1 ou 3 anos em troca de descontos significativos de até 72%?
**Opções:**
- A) Reservas do Azure (Azure Reserved Instances / Reservations)
- B) Compromisso de Consumo do Azure (MACC)
- C) Desconto Pague o que Usar
- D) Plano de Suporte Premier
**Resposta Correta:** A
**Explicação Técnica:** As Reservas do Azure ajudam a economizar dinheiro comprometendo-se com planos de 1 ou 3 anos para máquinas virtuais ou bancos de dados SQL, oferecendo descontos expressivos em relação ao preço sob demanda.

### Questão 390
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite hospedar APIs RESTful com suporte a autenticação, controle de taxa (throttling), transformação de payload e portal do desenvolvedor?
**Opções:**
- A) Gerenciamento de API do Azure (Azure API Management)
- B) Azure Functions
- C) Azure Logic Apps
- D) Azure Event Grid
**Resposta Correta:** A
**Explicação Técnica:** O Gerenciamento de API do Azure (APIM) é uma plataforma de gerenciamento híbrida e multicloud para APIs que inclui portal do desenvolvedor, gateway de API e ferramentas de gerenciamento.

### Questão 391
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que é o Princípio de Menor Privilégio (Principle of Least Privilege)?
**Opções:**
- A) Conceder a um usuário ou serviço apenas os privilégios exatos e mínimos necessários para realizar suas tarefas de trabalho, e nada mais.
- B) Garantir que todos os administradores tenham acesso de Proprietário (Owner) para evitar chamados de suporte.
- C) Desabilitar a autenticação de dois fatores em redes internas.
- D) Limitar a quantidade de máquinas virtuais por grupo de recursos.
**Resposta Correta:** A
**Explicação Técnica:** O princípio de menor privilégio é uma prática fundamental de segurança que exige conceder apenas o nível de acesso estritamente necessário para desempenhar uma determinada função.

### Questão 392
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de redundância de armazenamento do Azure copia seus dados de forma síncrona entre três Zonas de Disponibilidade na região primária e de forma assíncrona para uma segunda região remota?
**Opções:**
- A) Armazenamento com Redundância Geo-Zonal (GZRS)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância de Zona (ZRS)
- D) Armazenamento com Redundância Geográfica (GRS)
**Resposta Correta:** A
**Explicação Técnica:** O GZRS (Geo-Zone-Redundant Storage) combina a alta disponibilidade das Zonas de Disponibilidade na região primária com a proteção contra desastres regionais copiando os dados para uma região secundária.

### Questão 393
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure permite executar comandos PowerShell ou Bash interativos diretamente do navegador no Portal do Azure sem instalar nenhuma CLI local?
**Opções:**
- A) Azure Cloud Shell
- B) Azure Virtual Desktop
- C) Prompt de Comando do Windows
- D) Azure Arc
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cloud Shell é um shell interativo, acessível via navegador e autenticado para gerenciar recursos do Azure usando Bash ou PowerShell com ferramentas pré-instaladas.

### Questão 394
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite provisionar ambientes de desenvolvimento e teste rápidos, seguros e isolados para equipes de software usando modelos pré-configurados?
**Opções:**
- A) Azure DevTest Labs
- B) Azure DevOps Pipelines
- C) Azure App Service
- D) Azure Kubernetes Service
**Resposta Correta:** A
**Explicação Técnica:** O Azure DevTest Labs permite que as equipes criem rapidamente ambientes no Azure minimizando o desperdício e controlando os custos por meio de cota e automação de desligamento.

### Questão 395
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que acontece quando uma iniciativa do Azure Policy (Azure Policy Initiative) é atribuída a um Grupo de Recursos?
**Opções:**
- A) Um conjunto agrupado de múltiplas definições de políticas é aplicado simultaneamente para avaliar a conformidade dos recursos no grupo.
- B) Todos os recursos dentro do grupo são automaticamente convertidos para modelos SaaS.
- C) O grupo de recursos é bloqueado permanentemente contra exclusão.
- D) A assinatura do Azure é pausada até a verificação manual.
**Resposta Correta:** A
**Explicação Técnica:** Uma Iniciativa do Azure Policy é uma coleção ou grupo de definições de política do Azure adaptadas para atingir uma meta ou objetivo de conformidade específico.

### Questão 396
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure atua como um DNS público e privado altamente disponível que permite converter nomes de domínio em endereços IP?
**Opções:**
- A) Azure DNS
- B) Azure Traffic Manager
- C) Azure Front Door
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure DNS é um serviço de hospedagem para domínios DNS que fornece resolução de nomes usando a infraestrutura do Microsoft Azure.

### Questão 397
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual benefício o Benefício Híbrido do Azure (Azure Hybrid Benefit) oferece aos clientes?
**Opções:**
- A) Permite reaproveitar licenças existentes no local de Windows Server e SQL Server com Software Assurance para obter grandes descontos em VMs e SQL no Azure.
- B) Oferece suporte técnico de engenharia gratuito por 5 anos.
- C) Garante SLA de 100% de disponibilidade para máquinas virtuais de camada de entrada.
- D) Isenta a empresa do pagamento de tráfego de dados de saída da nuvem.
**Resposta Correta:** A
**Explicação Técnica:** O Benefício Híbrido do Azure (AHB) permite economizar significativamente usando suas licenças locais existentes do Windows Server e SQL Server com Software Assurance no Azure.

### Questão 398
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o objetivo do Azure ExpressRoute Direct?
**Opções:**
- A) Fornecer conectividade de fibra óptica privada direta de 10 Gbps ou 100 Gbps nos locais de emparelhamento da Microsoft em todo o mundo.
- B) Criar redes VPN banda larga gratuitas para usuários domésticos.
- C) Conectar dispositivos móveis 5G ao Microsoft 365 sem autenticação.
- D) Automatizar os backups locais para fita magnética.
**Resposta Correta:** A
**Explicação Técnica:** O ExpressRoute Direct oferece a capacidade de conectar-se diretamente à rede global da Microsoft em locais de emparelhamento estrategicamente distribuídos ao redor do mundo em velocidades de 10 ou 100 Gbps.

### Questão 399
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure coleta, analisa e age sobre dados de telemetria de seus ambientes de nuvem e locais para otimizar desempenho e disponibilidade?
**Opções:**
- A) Azure Monitor
- B) Azure Policy
- C) Azure Advisor
- D) Microsoft Sentinel
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor maximiza a disponibilidade e o desempenho de suas aplicações e serviços fornecendo uma solução abrangente para coletar, analisar e agir sobre a telemetria (métricas e logs).

### Questão 400
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de nuvem do Azure fornece um banco de dados NoSQL gerenciado de alta velocidade baseado em chave-valor para armazenamento em memória e suporte a cache distribuído?
**Opções:**
- A) Azure Cache for Redis
- B) Azure Cosmos DB
- C) Azure Table Storage
- D) Azure SQL Database
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cache for Redis fornece um armazenamento de dados em memória de alto desempenho baseado no software Redis de código aberto, perfeito para suporte a cache de baixa latência.
