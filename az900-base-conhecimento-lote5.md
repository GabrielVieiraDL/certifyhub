# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals - Lote 5 (Questões 201 a 250)

Esta base de conhecimento contém as questões 201 a 250 do exame **AZ-900: Microsoft Azure Fundamentals** formatadas para ingestão e automação no Antigravity.

---

### Questão 201
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Sua empresa precisa garantir que todas as máquinas virtuais implantadas em uma assinatura do Azure estejam em conformidade com as diretrizes de segurança da informação da organização. Qual ferramenta permite criar e atribuir definições para impor a conformidade automaticamente?
**Opções:**
- A) Azure Policy
- B) Grupos de Gerenciamento (Management Groups)
- C) Bloqueios de Recursos (Resource Locks)
- D) Tags do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy avalia seus recursos no Azure comparando-os com as propriedades desejadas de conformidade (regras de política) e impede a criação de recursos fora dos padrões ou sinaliza os recursos não conformes.

### Questão 202
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Uma empresa planeja migrar seu banco de dados relacional para o Azure mantendo a compatibilidade de 100% com o código de SQL Server local e permitindo recursos como suporte a transações distribuídas e backup automatizado. Qual serviço deve ser recomendado?
**Opções:**
- A) Instância Gerenciada do Banco de Dados SQL do Azure (Azure SQL Managed Instance)
- B) Banco de Dados SQL do Azure (Azure SQL Database)
- C) Azure Cosmos DB
- D) Banco de Dados do Azure para PostgreSQL
**Resposta Correta:** A
**Explicação Técnica:** A Instância Gerenciada do Banco de Dados SQL do Azure (Azure SQL Managed Instance) oferece quase 100% de compatibilidade com o mecanismo do SQL Server (Enterprise Edition) local, facilitando migrações lift-and-shift de aplicações legadas.

### Questão 203
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual benefício da computação em nuvem permite que uma empresa aloque dinamicamente mais capacidade de processamento ou memória durante picos de tráfego e reduza essa capacidade quando o tráfego diminuir?
**Opções:**
- A) Elasticidade
- B) Alta Disponibilidade
- C) Alcance Global
- D) Previsibilidade
**Resposta Correta:** A
**Explicação Técnica:** Elasticidade refere-se à capacidade de expandir e contrair recursos computacionais de forma automatizada e sob demanda, acompanhando as variações de carga de trabalho e otimizando os custos.

### Questão 204
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite gerenciar, integrar e executar fluxos de trabalho automatizados que conectam aplicativos, dados, sistemas e serviços em empresas usando um designer visual base em low-code/no-code?
**Opções:**
- A) Azure Logic Apps
- B) Azure Functions
- C) Azure Batch
- D) Azure Event Grid
**Resposta Correta:** A
**Explicação Técnica:** O Azure Logic Apps é uma plataforma em nuvem sem código/baixo código baseada em servidor (serverless) que ajuda a criar e executar fluxos de trabalho automatizados que integram seus aplicativos e dados entre serviços em nuvem e sistemas locais.

### Questão 205
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma organização precisa garantir que determinados recursos críticos, como um banco de dados de produção, não sejam excluídos acidentalmente por nenhum administrador da assinatura. Qual recurso do Azure atende a esse requisito?
**Opções:**
- A) Bloqueio de Exclusão (CanNotDelete Resource Lock)
- B) Atribuição de Função de Leitor no RBAC
- C) Azure Policy do tipo Deny
- D) Grupo de Gerenciamento Restrito
**Resposta Correta:** A
**Explicação Técnica:** O Bloqueio de Exclusão (CanNotDelete) impede que usuários, mesmo aqueles com privilégios de Administrador ou Proprietário (Owner) no RBAC, excluam o recurso sem remover a trava previamente.

### Questão 206
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de armazenamento do Azure é mais adequada para armazenar dados em arquivos compartilhados acessíveis simultaneamente por meio do protocolo padrão de mercado SMB (Server Message Block) ou NFS?
**Opções:**
- A) Azure Files
- B) Azure Blob Storage
- C) Azure Disk Storage
- D) Azure Table Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files oferece compartilhamentos de arquivos totalmente gerenciados na nuvem acessíveis por meio do protocolo SMB padrão do setor e NFS (Network File System), permitindo a substituição ou extensão de file servers locais.

### Questão 207
**Domínio:** Conceitos de Nuvem
**Enunciado:** Em um modelo de Infraestrutura como Serviço (IaaS), qual das seguintes responsabilidades permanece exclusivamente sob o controle do cliente?
**Opções:**
- A) Instalação de patches no sistema operacional e configuração do firewall do SO
- B) Manutenção dos servidores físicos e hipervisores
- C) Segurança física do data center
- D) Fornecimento de energia e refrigeração dos racks
**Resposta Correta:** A
**Explicação Técnica:** No modelo IaaS, o provedor de nuvem (Microsoft) cuida do hardware físico, energia, rede física e hipervisor. O cliente é totalmente responsável pelo sistema operacional, instalação de atualizações/patches, middleware e dados.

### Questão 208
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure deve ser consultada para verificar se há interrupções ativas de serviços do Azure, eventos de manutenção planejada e avisos de integridade que afetam diretamente a sua assinatura?
**Opções:**
- A) Azure Service Health
- B) Azure Status
- C) Azure Monitor
- D) Application Insights
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Health fornece um painel personalizado que mostra o status dos serviços e regiões do Azure que você utiliza especificamente em sua assinatura, alertando sobre incidentes, manutenções e avisos de integridade personalizados.

### Questão 209
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual das seguintes opções de redundância do Azure Storage replica seus dados de maneira síncrona três vezes dentro de um único data center na região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS)
**Resposta Correta:** A
**Explicação Técnica:** O Armazenamento com Redundância Local (LRS) copia seus dados de forma síncrona três vezes em uma única localização física (data center) dentro da região primária, oferecendo a opção de redundância de menor custo.

### Questão 210
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual solução de gerenciamento do Azure permite estender a governança, as políticas e o gerenciamento de serviços do Azure para servidores físicos ou virtuais localizados fora do Azure (ex.: on-premises ou em outras nuvens)?
**Opções:**
- A) Azure Arc
- B) Azure Lighthouse
- C) Azure Blueprints
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Arc simplifica a governança e o gerenciamento ao projetar seus recursos não-Azure (servidores locais, clusters Kubernetes e bancos de dados) no Azure Resource Manager (ARM).

### Questão 211
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Uma empresa deseja implantar contêineres Docker no Azure sem a necessidade de gerenciar nós de cluster ou orchestradores complexos como o Kubernetes. Qual serviço do Azure é o mais indicado?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Serviço de Kubernetes do Azure (AKS)
- C) Máquinas Virtuais do Azure
- D) Serviço de Aplicativo do Azure (Azure App Service)
**Resposta Correta:** A
**Explicação Técnica:** As Instâncias de Contêiner do Azure (ACI) oferecem a maneira mais rápida e simples de executar um contêiner no Azure de forma isolada e serverless, sem requerer o provisionamento de máquinas virtuais ou o gerenciamento de clusters.

### Questão 212
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta é utilizada para estimar os custos mensais hipotéticos de implantação de uma nova arquitetura no Azure antes de criar qualquer recurso?
**Opções:**
- A) Calculadora de Preços do Azure (Azure Pricing Calculator)
- B) Calculadora do Custo Total de Propriedade (TCO Calculator)
- C) Gerenciamento de Custos do Azure (Azure Cost Management)
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** A Calculadora de Preços do Azure é uma ferramenta web pública que permite aos usuários configurar e estimar os custos estimados de produtos e serviços do Azure para diferentes cenários arquiteturais.

### Questão 213
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual tipo de rede virtual permite que o tráfego de dados entre duas VNets do Azure trafegue de forma privada e segura pela rede backbone global da Microsoft sem passar pela Internet aberta?
**Opções:**
- A) Peering de Rede Virtual (VNet Peering)
- B) Conexão VPN Ponto a Site (Point-to-Site VPN)
- C) Azure ExpressRoute
- D) Gateways NAT
**Resposta Correta:** A
**Explicação Técnica:** O Peering de Rede Virtual (VNet Peering) conecta redes virtuais dentro da mesma região ou entre regiões do Azure, permitindo o tráfego privado através da rede backbone global dedicada da Microsoft.

### Questão 214
**Domínio:** Conceitos de Nuvem
**Enunciado:** Quando uma empresa migra seus data centers para o Azure e passa a pagar apenas pelos minutos ou horas de utilização dos recursos computacionais sem comprar novos hardware físicos, qual modelo financeiro ela está adotando?
**Opções:**
- A) Despesas Operacionais (OpEx)
- B) Despesas de Capital (CapEx)
- C) Custos Fixos de Infraestrutura
- D) Modelo de Amortização Direta
**Resposta Correta:** A
**Explicação Técnica:** O modelo de Despesas Operacionais (OpEx) caracteriza-se pelo pagamento sob demanda por serviços ou produtos utilizados continuamente, sem investimentos iniciais vultosos na aquisição de bens duráveis (hardware/edificações).

### Questão 215
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função primária do Microsoft Entra ID (anteriormente Azure Active Directory)?
**Opções:**
- A) Gerenciamento corporativo de identidades e controle de acesso baseado em nuvem
- B) Resolução de nomes de domínio DNS para redes virtuais
- C) Armazenamento seguro de chaves de criptografia e segredos de aplicação
- D) Firewall de inspeção profunda de pacotes de rede
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Entra ID é o serviço em nuvem de gerenciamento de identidade e acesso (IAM) da Microsoft que ajuda os funcionários a entrarem e acessarem recursos internos e externos.

### Questão 216
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa precisa implantar uma solução que analise grandes fluxos de dados de telemetria em tempo real provenientes de milhões de dispositivos IoT. Qual serviço do Azure é projetado para ingestion de eventos em tempo real?
**Opções:**
- A) Hubs de Eventos do Azure (Azure Event Hubs)
- B) Azure Service Bus
- C) Azure Storage Queues
- D) Azure Data Factory
**Resposta Correta:** A
**Explicação Técnica:** O Azure Event Hubs é uma plataforma de streaming de dados de Big Data e serviço de ingestão de eventos altamente escalável, capaz de receber e processar milhões de eventos por segundo.

### Questão 217
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Azure permite aplicar atribuições de permissões do RBAC e políticas corporativas do Azure Policy em escopo hierárquico acima de múltiplas assinaturas do Azure?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups)
- B) Grupos de Recursos (Resource Groups)
- C) Unidades Administrativas do Microsoft Entra ID
- D) Tenants (Locatários) do Azure
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento fornecem um nível de escopo acima das assinaturas. Você organiza as assinaturas em recipientes chamados grupos de gerenciamento e aplica suas condições de governança a todos os recursos contidos.

### Questão 218
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O que é uma Zona de Disponibilidade (Availability Zone) no Azure?
**Opções:**
- A) Um local físico isolado composto por um ou mais data centers com energia, refrigeração e rede independentes dentro de uma região
- B) Um par de regiões localizadas a pelo menos 300 milhas de distância para recuperação de desastres
- C) Um grupo de servidores dentro do mesmo rack compartilhando a mesma fonte de alimentação
- D) Uma rede virtual privada isolada geograficamente
**Resposta Correta:** A
**Explicação Técnica:** Zonas de Disponibilidade são locais físicos exclusivos dentro de uma região do Azure. Cada zona é composta por um ou mais data centers equipados com infraestrutura independente de energia, resfriamento e rede.

### Questão 219
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Um administrador precisa consultar visualmente a recomendação de redução de custos para desligar máquinas virtuais subutilizadas em seu ambiente Azure. Onde essa informação pode ser encontrada?
**Opções:**
- A) Azure Advisor
- B) Azure Security Center
- C) Azure Monitor
- D) Central de Serviços da Microsoft
**Resposta Correta:** A
**Explicação Técnica:** O Azure Advisor fornece recomendações proativas e personalizadas de melhores práticas para Custo, Desempenho, Confiabilidade, Segurança e Excelência Operacional, identificando recursos ociosos.

### Questão 220
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite armazenar chaves de criptografia, segredos de aplicação (como cadeias de conexão) e certificados digitais com alto nível de segurança e integração HSM?
**Opções:**
- A) Azure Key Vault
- B) Microsoft Entra ID
- C) Azure Storage Account
- D) Azure Information Protection
**Resposta Correta:** A
**Explicação Técnica:** O Azure Key Vault é um serviço de nuvem para armazenar com segurança e controlar o acesso a segredos, chaves de criptografia e certificados.

### Questão 221
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa deseja executar uma aplicação em que o código é executado somente quando disparado por eventos e cobra apenas pelo tempo exato de execução em milissegundos. Qual modelo computacional é esse?
**Opções:**
- A) Computação Sem Servidor (Serverless)
- B) Infraestrutura como Serviço (IaaS)
- C) Computação em Grids de Máquinas Físicas
- D) Servidores Dedicados
**Resposta Correta:** A
**Explicação Técnica:** A computação Serverless (Sem Servidor) permite que os desenvolvedores criem aplicativos mais rapidamente, eliminando a necessidade de gerenciar infraestrutura. O provedor executa o código sob demanda e cobra apenas pelo consumo.

### Questão 222
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual camada de acesso do Azure Blob Storage possui o menor custo de armazenamento por gigabyte, mas cobra taxas mais altas para recuperação de dados e exige um tempo de reidratação de várias horas?
**Opções:**
- A) Camada de Arquivamento (Archive Tier)
- B) Camada Fria (Cool Tier)
- C) Camada Quente (Hot Tier)
- D) Camada Premium
**Resposta Correta:** A
**Explicação Técnica:** A camada Archive (Arquivamento) é otimizada para armazenar dados raramente acessados com retenção de pelo menos 180 dias. Ela oferece o custo de armazenamento mais baixo, mas a recuperação exige reidratação que leva horas.

### Questão 223
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Um grupo de administradores precisa controlar quais usuários têm autorização para reiniciar máquinas virtuais em um determinado grupo de recursos sem conceder acesso total à assinatura. O que deve ser configurado?
**Opções:**
- A) Controle de Acesso Baseado em Função (RBAC do Azure)
- B) Azure Policy
- C) Trava de Recursos (Resource Lock)
- D) Grupos de Gerenciamento
**Resposta Correta:** A
**Explicação Técnica:** O Azure RBAC (Role-Based Access Control) permite gerenciar quem tem acesso aos recursos do Azure, o que eles podem fazer com esses recursos e a quais áreas têm acesso.

### Questão 224
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual ferramenta de gerenciamento do Azure pode ser executada diretamente no navegador via Portal do Azure, fornecendo um ambiente de shell interativo com suporte para Bash e PowerShell pré-instalados?
**Opções:**
- A) Azure Cloud Shell
- B) Azure CLI local
- C) Azure PowerShell no Windows
- D) Visual Studio Code Web
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cloud Shell é um shell interativo, acessível pelo navegador, para gerenciar recursos do Azure. Ele dá a liberdade de escolher a experiência de shell que melhor se adapta à sua forma de trabalhar (Bash ou PowerShell).

### Questão 225
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço de segurança SIEM (Gerenciamento de Eventos e Informações de Segurança) e SOAR nativo de nuvem da Microsoft analisa logs e fornece alertas inteligentes de ameaças em toda a empresa?
**Opções:**
- A) Microsoft Sentinel
- B) Microsoft Defender for Cloud
- C) Azure Firewall
- D) Azure Network Security Group (NSG)
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Sentinel é uma solução escalável e nativa da nuvem de SIEM (Gerenciamento de Eventos de Informações de Segurança) e SOAR (Orquestração de Segurança, Automação e Resposta).

### Questão 226
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de banco de dados NoSQL do Azure é totalmente gerenciado, oferece suporte a múltiplas APIs (como MongoDB, Cassandra e Gremlin) e garante latência de leitura e gravação de um dígito em milissegundos em escala global?
**Opções:**
- A) Azure Cosmos DB
- B) Banco de Dados SQL do Azure
- C) Azure Cache for Redis
- D) Banco de Dados do Azure para MySQL
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cosmos DB é um banco de dados NoSQL e relacional totalmente gerenciado para o desenvolvimento de aplicativos modernos com replicação global e resposta em milissegundos.

### Questão 227
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Como é chamada a garantia percentual formal dada pela Microsoft sobre o tempo de atividade operacional e disponibilidade de um determinado serviço no Azure?
**Opções:**
- A) Contrato de Nível de Serviço (SLA - Service Level Agreement)
- B) Acordo de Desempenho do Cliente (CPA)
- C) Garantia de Tempo de Resposta (RTO)
- D) Indicador Chave de Desempenho (KPI)
**Resposta Correta:** A
**Explicação Técnica:** O SLA (Service Level Agreement) descreve os compromissos da Microsoft com em relação ao tempo de atividade e conectividade dos serviços oferecidos.

### Questão 228
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de conectividade privada conecta com segurança a rede local da sua empresa diretamente à nuvem do Azure sem que o tráfego transite pela Internet pública comercial?
**Opções:**
- A) Azure ExpressRoute
- B) VPN de Site a Site (Site-to-Site VPN)
- C) Peering de Rede Virtual
- D) Azure Bastion
**Resposta Correta:** A
**Explicação Técnica:** O Azure ExpressRoute permite criar conexões privadas entre os datacenters do Azure e a infraestrutura local ou em um ambiente de colocalização, sem trafegar pela Internet pública.

### Questão 229
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que define o conceito de "Soberania dos Dados" na nuvem?
**Opções:**
- A) A obrigação de que os dados coletados estejam sujeitos às leis e estruturas de conformidade do país em que estão fisicamente armazenados
- B) A capacidade dos administradores de alterar permissões sem a aprovação da Microsoft
- C) O direito exclusivo do cliente de excluir todos os dados do data center
- D) A garantia de que a Microsoft é dona dos dados no data center
**Resposta Correta:** A
**Explicação Técnica:** Soberania dos dados refere-se à ideia de que os dados estão sujeitos às leis e governança regulatória do país ou jurisdição em que a infraestrutura de armazenamento está fisicamente localizada.

### Questão 230
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite criar e gerenciar um conjunto de máquinas virtuais idênticas com balanceamento de carga e dimensionamento automático baseado no uso de CPU ou regras de agendamento?
**Opções:**
- A) Conjuntos de Dimensionamento de Máquinas Virtuais (Virtual Machine Scale Sets - VMSS)
- B) Conjuntos de Disponibilidade (Availability Sets)
- C) Zonas de Disponibilidade (Availability Zones)
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** Os Conjuntos de Dimensionamento de Máquinas Virtuais (VMSS) permitem criar e gerenciar um grupo de VMs idênticas com balanceamento de carga que dimensionam automaticamente para cima ou para baixo.

### Questão 231
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é o nível de escopo mais alto na hierarquia de recursos do Azure?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups)
- B) Assinaturas (Subscriptions)
- C) Grupos de Recursos (Resource Groups)
- D) Recursos Individuais
**Resposta Correta:** A
**Explicação Técnica:** A hierarquia do Azure é organizada em quatro níveis: Grupos de Gerenciamento (no topo), Assinaturas, Grupos de Recursos e Recursos.

### Questão 232
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite aos desenvolvedores criar aplicativos Web RESTful e APIs no idioma de sua escolha sem gerenciar os servidores subjacentes?
**Opções:**
- A) Serviço de Aplicativo do Azure (Azure App Service)
- B) Máquinas Virtuais do Azure
- C) Azure Functions
- D) Azure Container Registry
**Resposta Correta:** A
**Explicação Técnica:** O Azure App Service é um serviço baseado em HTTP para hospedagem de aplicativos Web, APIs REST e back-ends móveis na modalidade PaaS.

### Questão 233
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que acontece com os recursos dentro de um Grupo de Recursos se o Grupo de Recursos for excluído?
**Opções:**
- A) Todos os recursos contidos no Grupo de Recursos são excluídos permanentemente
- B) Os recursos são movidos automaticamente para o grupo de recursos padrão da assinatura
- C) A exclusão falha até que todos os recursos sejam excluídos manualmente um a um
- D) Os recursos são desativados, mas não excluídos
**Resposta Correta:** A
**Explicação Técnica:** Quando um Grupo de Recursos é excluído, o Azure remove automaticamente todos os recursos associados contidos naquele grupo.

### Questão 234
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure fornece uma solução de gerenciamento de tráfego de rede de camada 7 (HTTP/HTTPS) com suporte a SSL termination, suporte a cookies de afinidade de sessão e firewall de aplicativo Web (WAF)?
**Opções:**
- A) Azure Application Gateway
- B) Azure Load Balancer
- C) Azure Traffic Manager
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego da Web (Camada 7) que permite gerenciar o tráfego para seus aplicativos Web com recursos avançados como inspeção WAF.

### Questão 235
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual das alternativas descreve uma arquitetura de Nuvem Híbrida?
**Opções:**
- A) Um ambiente que combina infraestrutura privada local (on-premises) conectada com serviços de nuvem pública
- B) Um ambiente que utiliza múltiplos provedores de nuvem pública simultaneamente sem conexões locais
- C) Uma nuvem dedicada exclusivamente a um consórcio de várias empresas do mesmo setor
- D) Um data center local tradicional sem nenhuma integração com a nuvem
**Resposta Correta:** A
**Explicação Técnica:** A nuvem híbrida combina infraestrutura local (ou nuvem privada) com a nuvem pública, permitindo que dados e aplicativos sejam compartilhados entre elas.

### Questão 236
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja centralizar a análise de registros (logs) e métricas de desempenho coletados de múltiplos recursos do Azure em um único repositório para realizar consultas SQL analíticas usando a linguagem KQL. O que deve ser criado?
**Opções:**
- A) Workspace do Log Analytics (Log Analytics Workspace)
- B) Conta de Armazenamento de Blobs
- C) Azure SQL Database
- D) Azure Event Grid
**Resposta Correta:** A
**Explicação Técnica:** Um Workspace do Log Analytics é o ambiente de armazenamento para os dados de log coletados pelo Azure Monitor e outros serviços do Azure, consultáveis por meio da Kusto Query Language (KQL).

### Questão 237
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de segurança do Azure fornece proteção contra ataques de Negação de Serviço Distribuída (DDoS) para recursos implantados em redes virtuais do Azure?
**Opções:**
- A) Proteção Contra DDoS do Azure (Azure DDoS Protection)
- B) Azure Firewall
- C) Grupo de Segurança de Rede (NSG)
- D) Azure Information Protection
**Resposta Correta:** A
**Explicação Técnica:** O Azure DDoS Protection fornece recursos aprimorados de mitigação de DDoS para proteger seus recursos do Azure contra ataques de negação de serviço volumétricos.

### Questão 238
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual portal oficial é disponibilizado pela Microsoft para consultar relatórios de auditoria SOC, certificações ISO/IEC, e documentação detalhada sobre como a Microsoft cumpre regulamentações globais de conformidade?
**Opções:**
- A) Portal de Confiança do Serviço (Service Trust Portal)
- B) Portal do Azure
- C) Azure Service Health
- D) Microsoft Learn
**Resposta Correta:** A
**Explicação Técnica:** O Service Trust Portal da Microsoft disponibiliza relatórios de auditoria independentes, guias de conformidade, avaliações de risco e documentos sobre práticas de privacidade e segurança da nuvem Microsoft.

### Questão 239
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o objetivo primário de usar o Azure Traffic Manager?
**Opções:**
- A) Distribuição e roteamento de tráfego DNS para endpoints em todo o mundo para otimizar desempenho e disponibilidade
- B) Balanceamento de carga de pacotes de camada de rede 4 dentro de uma única sub-rede
- C) Filtragem de tráfego malicioso de entrada com inspeção profunda de pacotes HTTP
- D) Conexão criptografada por túnel VPN entre datacenters
**Resposta Correta:** A
**Explicação Técnica:** O Azure Traffic Manager é um balanceador de carga de tráfego baseado em DNS que permite distribuir o tráfego para aplicativos globais nas regiões do Azure.

### Questão 240
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual modelo de serviço de nuvem é exemplificado pelo Microsoft 365 (anteriormente Office 365), onde o usuário utiliza a aplicação pronta via web sem gerenciar infraestrutura, código ou sistemas operacionais?
**Opções:**
- A) Software como Serviço (SaaS)
- B) Plataforma como Serviço (PaaS)
- C) Infraestrutura como Serviço (IaaS)
- D) Função como Serviço (FaaS)
**Resposta Correta:** A
**Explicação Técnica:** O Software como Serviço (SaaS) fornece um aplicativo de software completo gerenciado pelo provedor de nuvem, onde os usuários se conectam e usam o aplicativo pela Internet.

### Questão 241
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual recurso permite acesso remoto direto e seguro via RDP/SSH a máquinas virtuais do Azure através do Portal do Azure usando TLS (porta 443), sem expor IP público na VM?
**Opções:**
- A) Azure Bastion
- B) VPN Gateway
- C) Azure ExpressRoute
- D) Azure Firewall
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bastion é um serviço PaaS totalmente gerenciado que fornece acesso RDP e SSH seguro e contínuo às suas máquinas virtuais diretamente pelo Portal do Azure sobre TLS, sem a necessidade de um IP público na VM.

### Questão 242
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Se o SLA de um serviço individual no Azure é de 99,9% e o SLA de outro serviço dependente na mesma solução é de 99,9%, qual é o SLA composto da aplicação completa?
**Opções:**
- A) 99,8% (calculado multiplicando 99,9% x 99,9%)
- B) 99,9%
- C) 100%
- D) 99,99%
**Resposta Correta:** A
**Explicação Técnica:** Quando uma solução depende de múltiplos serviços em série, o SLA composto é o produto das SLAs individuais (0,999 * 0,999 = 0,998001 ou aproximadamente 99,8%), representando uma probabilidade de falha ligeiramente maior.

### Questão 243
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é uma plataforma de integração de dados e ETL (Extração, Transformação e Carga) baseada em nuvem para criar fluxos de trabalho de dados automatizados?
**Opções:**
- A) Azure Data Factory
- B) Azure Synapse Analytics
- C) Azure Stream Analytics
- D) Azure Databricks
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Factory é o serviço de integração de dados gerenciado em nuvem para criar, agendar e orquestrar fluxos de trabalho ETL/ELT.

### Questão 244
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função de uma Marcação (Tag) no Azure?
**Opções:**
- A) Associar pares de chave-valor aos recursos do Azure para fins de organização, categorização de custos e faturamento
- B) Bloquear a exclusão acidental do recurso por administradores
- C) Imprimir uma regra de restrição de segurança no firewall
- D) Conceder permissão de leitura ao usuário no recurso
**Resposta Correta:** A
**Explicação Técnica:** As Tags (marcas) aplicam metadados aos seus recursos na forma de pares chave-valor para organizar e consolidar dados de faturamento e gerenciamento.

### Questão 245
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite gerenciar políticas de firewall de maneira centralizada e filtrar o tráfego de rede em nível de aplicativo e rede para toda uma Rede Virtual do Azure?
**Opções:**
- A) Azure Firewall
- B) Grupo de Segurança de Rede (NSG)
- C) Azure Key Vault
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** O Azure Firewall é um serviço de segurança de rede gerenciado e baseado em nuvem que protege seus recursos de Rede Virtual do Azure com suporte a filtragem de tráfego stateful.

### Questão 246
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual o termo utilizado para descrever a facilidade e rapidez com que os desenvolvedores podem provisionar novos ambientes de teste e produção na nuvem em questão de minutos?
**Opções:**
- A) Agilidade
- B) Tolerância a Falhas
- C) Alta Disponibilidade
- D) Escalabilidade Vertical
**Resposta Correta:** A
**Explicação Técnica:** A agilidade no contexto da nuvem é a capacidade de implantar e iterar recursos computacionais rapidamente com o mínimo de esforço manual ou burocrático.

### Questão 247
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja enviar notificações por e-mail e disparar automações sempre que o consumo de custos de uma assinatura atingir 80% do orçamento mensal definido. O que deve ser configurado no Azure Cost Management?
**Opções:**
- A) Alertas de Orçamento (Budget Alerts)
- B) Azure Policy
- C) Regra do Azure Advisor
- D) Bloqueio de Orçamento
**Resposta Correta:** A
**Explicação Técnica:** Os Alertas de Orçamento (Budget Alerts) no Azure Cost Management notificam os usuários quando os custos acumulados ou previstos excederem os limites definidos.

### Questão 248
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de armazenamento do Azure é otimizado para armazenar mensagens curtas (até 64 KB) que podem ser lidas por aplicações desacopladas para processamento assíncrono?
**Opções:**
- A) Azure Queue Storage
- B) Azure Blob Storage
- C) Azure Files
- D) Azure Table Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Queue Storage armazena grandes quantidades de mensagens acessíveis de qualquer lugar via chamadas autenticadas via HTTP ou HTTPS, ideal para desacoplamento de componentes.

### Questão 249
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que é o Azure Resource Manager (ARM)?
**Opções:**
- A) A camada de gerenciamento e implantação consistente do Azure que permite criar, atualizar e excluir recursos
- B) O motor de banco de dados por trás de todas as contas do Azure
- C) O hipervisor físico executado nos datacenters do Azure
- D) O painel de monitoramento de tráfego de rede
**Resposta Correta:** A
**Explicação Técnica:** O Azure Resource Manager (ARM) é o serviço de gerenciamento do Azure. Ele fornece uma camada de gerenciamento que permite criar, atualizar e excluir recursos em sua assinatura do Azure.

### Questão 250
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de inteligência artificial da Microsoft permite incorporar recursos pré-construídos de visão computacional, processamento de linguagem natural e fala diretamente em aplicativos via APIs REST?
**Opções:**
- A) Serviços de IA do Azure (Azure AI Services / Cognitive Services)
- B) Azure Machine Learning
- C) Azure Bot Service
- D) Azure Databricks
**Resposta Correta:** A
**Explicação Técnica:** Os Serviços de IA do Azure (anteriormente Serviços Cognitivos) trazem a inteligência de IA ao alcance dos desenvolvedores sem exigir conhecimentos profundos em ciência de dados ou ML.
