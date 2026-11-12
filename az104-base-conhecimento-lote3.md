# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 3 (Questões 101 a 150)

Esta base de conhecimento contém as questões 101 a 150 do exame **AZ-104: Microsoft Azure Administrator** formatadas para ingestão e automação no Antigravity.

---

### Questão 101
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua empresa possui um compartilhamento de arquivos no Azure Files chamado `data-share` contido em uma Conta de Armazenamento. Você precisa garantir que todos os dados gravados no `data-share` sejam criptografados em repouso usando chaves gerenciadas pelo cliente (Customer-Managed Keys - CMK) armazenadas no Azure Key Vault. O que você deve configurar primeiro na Conta de Armazenamento?
**Opções:**
- A) Habilitar a Identidade Gerenciada Atribuída pelo Sistema na Conta de Armazenamento
- B) Alterar a camada de desempenho para Premium
- C) Criar um ponto de extremidade privado (Private Endpoint)
- D) Habilitar a replicação Geo-Redundante (GRS)
**Resposta Correta:** A
**Explicação Técnica:** Para utilizar chaves gerenciadas pelo cliente (CMK) no Azure Key Vault para a criptografia do Azure Storage (SSE), a Conta de Armazenamento precisa ter uma Identidade Gerenciada (Atribuída pelo Sistema ou pelo Usuário) ativada para autenticar e acessar o Azure Key Vault com as permissões necessárias.

### Questão 102
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você possui uma Rede Virtual (VNet1) com três sub-redes: Subnet1, Subnet2 e Subnet3. Uma máquina virtual VM1 está conectada à Subnet1. Você precisa garantir que a VM1 possa se comunicar apenas com instâncias na Subnet2, bloqueando todo o tráfego direto para a Subnet3. Qual ação você deve realizar?
**Opções:**
- A) Associar um Grupo de Segurança de Rede (NSG) à Subnet1 com uma regra de saída (Outbound Rule) negando o tráfego para o intervalo de IP da Subnet3
- B) Criar uma tabela de rotas (Route Table) com uma rota de salto com o tipo 'None' para a Subnet2
- C) Remover a interface de rede (NIC) da VM1 e recriá-la na Subnet3
- D) Habilitar o Peering de VNet entre a Subnet1 e a Subnet2
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Segurança de Rede (NSG) controlam o tráfego de entrada e saída. Para impedir que a VM1 acesse a Subnet3, aplica-se uma regra de segurança de saída no NSG associado à Subnet1 (ou à NIC da VM1) bloqueando o destino correspondente ao préfixo IP da Subnet3.

### Questão 103
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Sua organização tem múltiplos Grupos de Recursos no Azure. Você precisa aplicar uma regra de governança que proíba a criação de qualquer máquina virtual da série 'M' em todas as assinaturas do grupo corporativo. Qual recurso do Azure deve ser implantado?
**Opções:**
- A) Uma atribuição de política do Azure Policy direcionada ao Grupo de Gerenciamento (Management Group) principal
- B) Um Bloqueio de Recurso do tipo 'ReadOnly' no nível da Assinatura
- C) Uma função personalizada do Azure RBAC atribuída a todos os administradores
- D) Um plano do Microsoft Defender for Cloud
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy é a ferramenta oficial para aplicar regras de conformidade e restrições de recursos (como SKUs de VMs não autorizados). Ao atribuir a política no nível do Grupo de Gerenciamento (Management Group), a regra é herdada automaticamente por todas as assinaturas e grupos de recursos contidos abaixo dele.

### Questão 104
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você planeja implantar um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. O conjunto de escala deve ajustar automaticamente o número de instâncias de VM com base na utilização de CPU das instâncias existentes. O que você deve configurar no VMSS?
**Opções:**
- A) Regras de Dimensionamento Automático (Autoscale Rules) baseadas em métricas
- B) Um Grupo de Disponibilidade com 3 domínios de falha
- C) Um Bloqueio de Recurso do tipo CanNotDelete
- D) Um Azure Load Balancer na camada Básica
**Resposta Correta:** A
**Explicação Técnica:** Os Conjuntos de Escala de Máquinas Virtuais (VMSS) suportam Autoscale baseado em métricas de desempenho (como porcentagem média de CPU). Quando os limites (thresholds) definidos são atingidos, o Azure adiciona (scale-out) ou remove (scale-in) instâncias de VM automaticamente.

### Questão 105
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa coletar logs de eventos de segurança de 50 máquinas virtuais Windows no Azure e centralizá-los em um workspace do Log Analytics. Qual é o agente recomendado e o recurso de configuração necessário para realizar essa coleta no modelo moderno do Azure Monitor?
**Opções:**
- A) Instalar o Agente do Azure Monitor (AMA) nas VMs e criar uma Regra de Coleta de Dados (Data Collection Rule - DCR)
- B) Instalar o agente Log Analytics legado (MMA) e configurar a extensão do Diagnóstico do Azure (WAD)
- C) Configurar o Azure Network Watcher em cada região
- D) Habilitar o Azure Serial Console em cada VM
**Resposta Correta:** A
**Explicação Técnica:** A arquitetura moderna de monitoramento da Microsoft utiliza o Agente do Azure Monitor (AMA - Azure Monitor Agent) em conjunto com Regras de Coleta de Dados (DCR - Data Collection Rules) para definir exatamente quais eventos e logs devem ser coletados e para qual workspace do Log Analytics devem ser enviados.

### Questão 106
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa fornecer acesso remoto seguro via navegador Web (HTTPS) a máquinas virtuais Linux e Windows hospedadas em uma VNet do Azure, sem expor os endereços IP públicos das VMs à Internet e sem necessitar de cliente VPN instalado. Qual serviço você deve implementar?
**Opções:**
- A) Azure Bastion
- B) VPN Gateway Ponto a Site (P2S)
- C) Azure ExpressRoute
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bastion é um serviço PaaS totalmente gerenciado que fornece acesso RDP e SSH seguro e contínuo às suas máquinas virtuais diretamente pelo Portal do Azure via TLS/HTTPS, sem expor IPs públicos nas VMs e sem a necessidade de agentes ou clientes adicionais.

### Questão 107
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa migrar 40 TB de dados locais não estruturados para uma Conta de Armazenamento do Azure Blob. A conexão de Internet da sua empresa é limitada e lenta. Qual é o método mais eficiente e rápido recomendado para realizar essa transferência?
**Opções:**
- A) Solicitar um dispositivo físico do Azure Data Box
- B) Executar o utilitário AzCopy via linha de comando sobre a Internet pública
- C) Utilizar o Azure Storage Explorer com transferência em segundo plano
- D) Configurar o Azure File Sync
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Box é um dispositivo de armazenamento físico seguro enviado pela Microsoft. Ele é ideal para transferências massivas de dados (acima de 10-20 TB) quando as conexões de rede locais são limitadas ou lentas, permitindo que a Microsoft importe os dados diretamente no data center.

### Questão 108
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador precisa conceder a um usuário permissão para gerenciar todas as máquinas virtuais em um Grupo de Recursos, mas o usuário não deve ter permissão para conceder acesso a outros usuários ou alterar políticas do grupo. Qual função nativa do Azure RBAC deve ser atribuída?
**Opções:**
- A) Colaborador de Máquina Virtual (Virtual Machine Contributor)
- B) Proprietário (Owner)
- C) Leitor (Reader)
- D) Administrador de Acesso Baseado em Função (Role Based Access Control Administrator)
**Resposta Correta:** A
**Explicação Técnica:** A função nativa 'Colaborador de Máquina Virtual' permite gerenciar totalmente as máquinas virtuais (criar, reiniciar, excluir, alterar tamanho), mas não permite conceder permissões a outros usuários (função reservada ao Proprietário ou Administrador de Acesso de Usuário).

### Questão 109
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Duas Redes Virtuais no Azure (VNetA na região East US e VNetB na região West Europe) precisam ser conectadas. Os recursos nas duas VNets devem comunicar-se com baixíssima latência e tráfego criptografado pela rede backbone da Microsoft. Qual recurso deve ser configurado?
**Opções:**
- A) Peering de Rede Virtual Global (Global VNet Peering)
- B) Conexão VPN Site a Site (S2S) com VPN Gateways
- C) Azure ExpressRoute Direct
- D) Azure Application Gateway
**Resposta Correta:** A
**Explicação Técnica:** O Peering de Rede Virtual Global (Global VNet Peering) conecta redes virtuais entre diferentes regiões do Azure. O tráfego flui inteiramente através da rede privada backbone de alta velocidade da Microsoft, oferecendo baixa latência e sem passar pela Internet pública.

### Questão 110
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa deseja executar contêineres Docker de forma rápida e simplificada no Azure, sem a necessidade de gerenciar nós, cluster ou orquestradores complexos como o Kubernetes. Qual serviço é o mais recomendado?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Serviço do Azure Kubernetes (AKS)
- C) Conjunto de Escala de Máquinas Virtuais (VMSS)
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Instances (ACI) é a solução serverless mais rápida e simples para executar contêineres isolados sob demanda no Azure, sem a necessidade de provisionar máquinas virtuais ou gerenciar clusters complexos de orquestração.

### Questão 111
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa ser notificado por SMS e e-mail sempre que a utilização de CPU de uma máquina virtual crítica ultrapassar 90% por mais de 5 minutos. Qual combinação de recursos do Azure Monitor deve ser criada?
**Opções:**
- A) Uma Regra de Alerta de Métrica (Metric Alert Rule) associada a um Grupo de Ação (Action Group)
- B) Um painel do Azure Dashboard exportado em PDF
- C) Um relatório do Azure Advisor
- D) Uma consulta KQL salva no Log Analytics sem alertas ativados
**Resposta Correta:** A
**Explicação Técnica:** No Azure Monitor, as Regras de Alerta de Métrica monitoram limites numéricos (como CPU > 90%). Quando a condição é satisfeita, a regra dispara um Grupo de Ação (Action Group), que gerencia as notificações (SMS, e-mail, Webhook, push).

### Questão 112
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você possui uma Conta de Armazenamento usada para guardar arquivos de auditoria que devem ser mantidos por 7 anos sem possibilidade de alteração ou exclusão, mesmo por administradores globais. O que você deve aplicar nos contêineres de Blob?
**Opções:**
- A) Uma política de retenção baseada em tempo no recurso de Imutabilidade (WORM / Immutable Blob Storage)
- B) Um Bloqueio de Recurso do tipo CanNotDelete no Portal do Azure
- C) Uma política do Azure Policy atribuída à assinatura
- D) Habilitar a exclusão temporária (Soft Delete) por 7 anos
**Resposta Correta:** A
**Explicação Técnica:** O armazenamento imutável (Immutable Storage / WORM) para o Azure Blob Storage permite definir políticas de retenção baseadas em tempo travadas (*locked retention policy*). Uma vez bloqueada, os dados não podem ser modificados ou excluídos por ninguém até que o período expire.

### Questão 113
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa solucionar um problema onde o tráfego de rede de uma VM no Azure está sendo bloqueado de forma inesperada ao tentar acessar um banco de dados em outra sub-rede. Qual ferramenta do Azure Network Watcher permite testar e verificar qual regra de NSG está permitindo ou bloqueando esse tráfego?
**Opções:**
- A) Verificação de Fluxo de IP (IP Flow Verify)
- B) Próximo Salto (Next Hop)
- C) Diagnóstico de Roteamento (Route Diagnostics)
- D) Captura de Pacotes (Packet Capture)
**Resposta Correta:** A
**Explicação Técnica:** A ferramenta IP Flow Verify do Azure Network Watcher verifica se um pacote de rede de entrada ou saída é permitido ou negado para uma máquina virtual com base nas regras dos Grupos de Segurança de Rede (NSG) aplicados, indicando a regra exata responsável pelo bloqueio.

### Questão 114
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma organização precisa permitir que um grupo de administradores gerencie usuários apenas em um departamento específico (ex.: departamento Financeiro) dentro do Microsoft Entra ID. Qual recurso deve ser utilizado para agrupar esses usuários e atribuir a função administrativa correspondente?
**Opções:**
- A) Unidade Administrativa (Administrative Unit - AU)
- B) Grupo de Gerenciamento (Management Group)
- C) Grupo de Segurança de Rede (NSG)
- D) Grupo de Recursos (Resource Group)
**Resposta Correta:** A
**Explicação Técnica:** As Unidades Administrativas (AU) no Microsoft Entra ID permitem subdividir a organização e atribuir funções administrativas (como Administrador de Usuários) com escopo restrito aos membros pertencentes apenas àquela unidade específica.

### Questão 115
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um aplicativo Web baseado em contêiner no Azure App Service que deve ser dimensionado automaticamente e ter suporte a certificados SSL personalizados. Qual plano de serviço do App Service (App Service Plan) mínimo suporta autoscaling e certificados personalizados?
**Opções:**
- A) Padrão (Standard)
- B) Gratuito (F1 / Free)
- C) Compartilhado (D1 / Shared)
- D) Básico (B1 / Basic)
**Resposta Correta:** A
**Explicação Técnica:** O nível Padrão (Standard) do Azure App Service Plan é o nível de produção inicial que oferece suporte a escala automática (autoscale), certificados SSL personalizados, domínios personalizados e backups diários automatizados.

### Questão 116
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa distribuir o tráfego de entrada HTTP/HTTPS para três máquinas virtuais de back-end. A solução deve oferecer suporte ao descarregamento SSL (SSL Offloading) e roteamento baseado em caminho de URL (/images, /video). Qual serviço deve ser utilizado?
**Opções:**
- A) Azure Application Gateway
- B) Azure Load Balancer Básico
- C) Azure Traffic Manager
- D) Azure Network Watcher
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego Web de Camada 7. Ele oferece recursos avançados como roteamento baseado em URL, descarregamento SSL (SSL Termination/Offloading) e Firewall de Aplicação Web (WAF).

### Questão 117
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você tem uma Conta de Armazenamento do Azure Blob com milhões de pequenos arquivos. Para reduzir custos, você quer mover automaticamente os blobs não acessados há mais de 30 dias para a camada Cool, e os não acessados há mais de 180 dias para a camada Archive. O que você deve configurar?
**Opções:**
- A) Gerenciamento do Ciclo de Vida (Lifecycle Management Rules)
- B) Replicação de Armazenamento por Objetos (Object Replication)
- C) Azure Storage Sync
- D) Análise de Armazenamento com Log Analytics
**Resposta Correta:** A
**Explicação Técnica:** O recurso Gerenciamento de Ciclo de Vida do Azure Blob Storage permite definir regras automáticas baseadas em condições de tempo (como dias desde a última modificação ou último acesso) para transicionar blobs entre as camadas Hot, Cool e Archive ou excluí-los.

### Questão 118
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você deseja permitir que os usuários da sua empresa utilizem a autenticação de dois fatores (MFA) e login sem senha (Passwordless). Qual solução de gerenciamento de identidades do Azure fornece esses recursos nativos de segurança?
**Opções:**
- A) Microsoft Entra ID
- B) Azure Key Vault
- C) Active Directory Domain Services (AD DS) em VM
- D) Azure Information Protection
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Entra ID (antigo Azure AD) é o serviço de identidade baseado em nuvem que oferece suporte nativo à Autenticação Multifator (MFA), Acesso Condicional, login sem senha (FIDO2, Microsoft Authenticator) e controle de identidade corporativa.

### Questão 119
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma máquina virtual do Azure Windows parou de responder e você não consegue se conectar a ela via RDP nem SSH. Você precisa visualizar a saída do console de inicialização e enviar comandos de depuração diretamente ao sistema operacional. Qual ferramenta nativa deve ser utilizada?
**Opções:**
- A) Console Serial do Azure (Azure Serial Console)
- B) Peering de VNet
- C) Conexão do Azure Bastion
- D) Reinstalação do Agente do VMInsights
**Resposta Correta:** A
**Explicação Técnica:** O Console Serial do Azure (Serial Console) no Portal do Azure fornece uma conexão de texto direta à porta serial (COM1/ttyS0) da máquina virtual, permitindo solucionar problemas de boot e comandos de depuração mesmo quando a rede da VM está indisponível.

### Questão 120
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa executar consultas analíticas complexas nos logs de auditoria e métricas de desempenho armazenados no Log Analytics Workspace do Azure. Qual linguagem de consulta é utilizada nativamente pelo Azure Monitor?
**Opções:**
- A) KQL (Kusto Query Language)
- B) T-SQL
- C) PowerShell
- D) GraphQL
**Resposta Correta:** A
**Explicação Técnica:** A linguagem KQL (Kusto Query Language) é a linguagem de consulta padrão e otimizada utilizada no Azure Monitor, Log Analytics Workspaces, Application Insights e Microsoft Sentinel para analisar grandes volumes de dados de log.

### Questão 121
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você deseja conectar a rede local da matriz da sua empresa à sua VNet no Azure através de um túnel VPN seguro criptografado IPsec/IKE pela Internet pública. Qual tipo de VPN Gateway deve ser configurado?
**Opções:**
- A) VPN Gateway Site a Site (S2S)
- B) VPN Gateway Ponto a Site (P2S)
- C) Conexão dedicada Azure ExpressRoute
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** Uma conexão VPN Site a Site (S2S) liga uma rede local (matriz ou filial) inteira à sua VNet do Azure usando um túnel VPN IPsec/IKE, permitindo a comunicação transparente entre todos os dispositivos locais e os recursos no Azure.

### Questão 122
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma Conta de Armazenamento do Azure precisa permitir que uma aplicação Web externa acesse diretamente arquivos PDF armazenados em um contêiner privado por um período limitado de 2 horas, sem expor as chaves de acesso primárias da conta. Qual recurso deve ser gerado?
**Opções:**
- A) Assinatura de Acesso Compartilhado (Shared Access Signature - SAS)
- B) Chave de Acesso Secundária (Secondary Access Key)
- C) Bloqueio de Recurso do tipo ReadOnly
- D) Certificado de Chave Pública X.509
**Resposta Correta:** A
**Explicação Técnica:** As Assinaturas de Acesso Compartilhado (SAS) fornecem acesso delegado seguro com privilégios limitados a recursos na sua Conta de Armazenamento, especificando as permissões (leitura, escrita), o intervalo de IP permitido e a data/hora exata de expiração.

### Questão 123
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa auditarr quem alterou uma regra de segurança em um Grupo de Segurança de Rede (NSG) às 14:00 de ontem no Azure. Qual log do Azure deve ser consultado?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Log de Entradas do Microsoft Entra (SignIn Logs)
- C) Azure Storage Analytics Log
- D) Log de Diagnóstico do Azure DNS
**Resposta Correta:** A
**Explicação Técnica:** O Log de Atividades do Azure (Azure Activity Log) fornece insights sobre todos os eventos no nível de plano de controle (ARM), registrando quem, quando e qual modificação/operação foi realizada em qualquer recurso da assinatura (ex.: criar, atualizar ou excluir NSG).

### Questão 124
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa garantir que as máquinas virtuais do seu aplicativo Web estejam hospedadas em racks físicos diferentes, com fontes de alimentação e switches de rede separados dentro do mesmo data center do Azure. O que você deve criar e associar às VMs?
**Opções:**
- A) Conjunto de Disponibilidade (Availability Set) configurado com Domínios de Falha (Fault Domains)
- B) Grupo de Gerenciamento (Management Group)
- C) Zonas de Disponibilidade em regiões diferentes
- D) VNet Peering
**Resposta Correta:** A
**Explicação Técnica:** Um Conjunto de Disponibilidade (Availability Set) garante que as VMs implantadas nele sejam distribuídas por múltiplos domínios de falha (racks com energia e conectividade independentes) e domínios de atualização dentro de um único data center do Azure.

### Questão 125
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa implantar um servidor DNS privado no Azure para resolver nomes de domínio personalizados para recursos dentro de suas VNets, sem a necessidade de implantar e gerenciar máquinas virtuais com a função DNS Server. Qual serviço PaaS deve ser utilizado?
**Opções:**
- A) Zonas Privadas do Azure DNS (Azure DNS Private Zones)
- B) Azure Application Gateway
- C) Azure ExpressRoute
- D) Azure Network Watcher Traffic Analytics
**Resposta Correta:** A
**Explicação Técnica:** As Zonas Privadas do Azure DNS fornecem um serviço de nomes seguro e confiável para gerenciar e resolver nomes de nomes de domínio em uma VNet sem a necessidade de configurar e manter soluções de DNS baseadas em máquinas virtuais.

### Questão 126
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa sincronizar os compartilhamentos de arquivos de um servidor de arquivos Windows local (Windows Server On-Premises) com um compartilhamento do Azure Files, mantendo o cache local de arquivos frequentemente acessados. Qual serviço deve ser implementado?
**Opções:**
- A) Azure File Sync
- B) Azure Data Box
- C) Utilitário AzCopy
- D) Azure Import/Export Service
**Resposta Correta:** A
**Explicação Técnica:** O Azure File Sync permite centralizar os compartilhamentos de arquivos da sua empresa no Azure Files, mantendo ao mesmo tempo a flexibilidade, o desempenho e a compatibilidade de um servidor de arquivos local Windows através do recurso de armazenamento em camadas na nuvem (Cloud Tiering).

### Questão 127
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar o backup automatizado diário de 10 máquinas virtuais do Azure, garantindo retenção de 30 dias e capacidade de restauração de arquivos individuais ou da VM inteira. Qual recurso do Azure deve ser implantado?
**Opções:**
- A) Cofre dos Serviços de Recuperação (Recovery Services Vault) com Política de Backup
- B) Log Analytics Workspace com retenção estendida
- C) Cópia de sombras de volume (VSS) local
- D) Azure Storage Explorer
**Resposta Correta:** A
**Explicação Técnica:** O Cofre dos Serviços de Recuperação (Recovery Services Vault) é o recurso no Azure usado para armazenar dados de backup e pontos de recuperação para VMs do Azure, máquinas físicas e bancos de dados, gerenciados por Políticas de Backup (Backup Policies).

### Questão 128
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa deseja forçar que todos os administradores do Azure autentiquem-se obrigatoriamente com MFA apenas quando estiverem acessando o portal fora da rede corporativa da empresa (definida por um intervalo de IP público). Qual recurso do Microsoft Entra ID deve ser configurado?
**Opções:**
- A) Políticas de Acesso Condicional (Conditional Access Policies)
- B) Grupos de Gerenciamento
- C) Azure Policy
- D) Unidades Administrativas
**Resposta Correta:** A
**Explicação Técnica:** O Acesso Condicional (Conditional Access) no Microsoft Entra ID avalia sinais de contexto (como usuário, localização por IP, dispositivo, aplicativo) para tomar decisões de acesso e impor políticas automatizadas (ex.: exigir MFA quando fora do intervalo de IPs confiáveis).

### Questão 129
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual componente de rede do Azure opera na Camada 4 do modelo OSI e distribui o tráfego de entrada não-HTTP/HTTPS (como tráfego TCP/UDP) com baixíssima latência entre instâncias de back-end saudáveis?
**Opções:**
- A) Azure Load Balancer
- B) Azure Application Gateway
- C) Azure Front Door
- D) Web Application Firewall (WAF)
**Resposta Correta:** A
**Explicação Técnica:** O Azure Load Balancer é um balanceador de carga de Camada 4 (TCP/UDP) de altíssimo desempenho e ultra baixa latência que distribui o tráfego entre instâncias de recursos de acordo com regras configuradas e testes de integridade (Health Probes).

### Questão 130
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um aplicativo web em contêineres gerenciado pelo Azure Kubernetes Service (AKS). Qual recurso do Azure é o repositório privado oficial recomendado para armazenar e gerenciar as imagens de contêiner Docker que serão implantadas nos nós do AKS?
**Opções:**
- A) Registro de Contêiner do Azure (Azure Container Registry - ACR)
- B) Conta de Armazenamento com Azure Files
- C) Azure Key Vault
- D) Repositório do Azure Artifacts
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Registry (ACR) é um serviço de registro privado gerenciado baseado no Docker Registry 2.0, usado para armazenar, gerenciar e implantar imagens de contêineres e artefatos em serviços como AKS, ACI e App Service.

### Questão 131
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa garantir que os dados armazenados em uma Conta de Armazenamento continuem disponíveis para leitura mesmo no caso de uma falha completa da região primária e da região secundária emparelhada. Qual tipo de redundância oferece o maior nível de resiliência geográfica e zonal?
**Opções:**
- A) Armazenamento com Redundância Geo-Zonal com Acesso de Leitura (RA-GZRS)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância de Zona (ZRS)
**Resposta Correta:** A
**Explicação Técnica:** O RA-GZRS (Read-Access Geo-Zone-Redundant Storage) copia seus dados de forma síncrona em três Zonas de Disponibilidade na região primária e os replica de forma assíncrona para uma região secundária, fornecendo acesso de leitura na região secundária em caso de desastre na primária.

### Questão 132
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa listar todos os recursos no Azure que estão utilizando mais de 80% de capacidade ou que possuem tags ausentes em 10 assinaturas diferentes da empresa. Qual serviço de consulta rápida deve ser utilizado?
**Opções:**
- A) Azure Resource Graph (usando consultas KQL)
- B) Portal de Confiança do Serviço
- C) Azure Advisor
- D) Leitura do Log de Atividades arquivo por arquivo
**Resposta Correta:** A
**Explicação Técnica:** O Azure Resource Graph é um serviço que oferece exploração de recursos de alto desempenho e em escala, permitindo executar consultas KQL complexas em todas as suas assinaturas para obter informações detalhadas sobre o estado dos recursos.

### Questão 133
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você tem máquinas virtuais em uma sub-rede privada que precisam acessar um banco de dados PaaS (Azure SQL Database) com segurança através da rede privada da Microsoft, impedindo que o tráfego passe pela Internet pública. Qual recurso deve ser criado e associado à VNet?
**Opções:**
- A) Ponto de Extremidade Privado (Private Endpoint)
- B) Rota de Salto Personalizada para a Internet
- C) Azure ExpressRoute Direct
- D) VPN Gateway P2S
**Resposta Correta:** A
**Explicação Técnica:** Um Ponto de Extremidade Privado (Private Endpoint) utiliza um endereço IP privado da sua VNet para se conectar de forma segura e privada a um serviço PaaS do Azure (como Azure SQL ou Storage), trazendo o serviço para dentro da sua rede privada.

### Questão 134
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual funcionalidade do Azure Monitor permite visualizar a topologia de dependências de rede e as conexões de entrada/saída em tempo real de máquinas virtuais e processos ativos?
**Opções:**
- A) Visão Geral do VM Insights (Map Feature)
- B) Azure Activity Log
- C) Métricas da Conta de Armazenamento
- D) Grupos de Ação de Alertas
**Resposta Correta:** A
**Explicação Técnica:** O recurso de Mapa (Map) no VM Insights analisa e exibe graficamente conexões de rede ativas, portas e dependências de processos em tempo real em máquinas virtuais Windows e Linux hospedadas no Azure ou em ambientes híbridos.

### Questão 135
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa automatizar a implantação de uma infraestrutura complexa com 10 VMs, 2 VNets e Load Balancers usando código declarativo que seja nativo, legível e otimizado para o Azure. Qual linguagem de IaC desenvolvida pela Microsoft é a recomendada?
**Opções:**
- A) Bicep
- B) Bash scripts
- C) Python SDK
- D) CLI do Azure legado
**Resposta Correta:** A
**Explicação Técnica:** O Bicep é uma linguagem de Sintaxe Declarativa (IaC) desenvolvida pela Microsoft para implantar recursos do Azure de forma limpa, concisa e com suporte nativo de validação no momento da compilação para os modelos do Azure Resource Manager (ARM).

### Questão 136
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** O que acontece quando você tenta conectar duas Redes Virtuais (VNets) via VNet Peering se os intervalos de endereços IP (CIDR blocks) das duas redes se sobrepuserem (overlapping IP addresses)?
**Opções:**
- A) O Peering falhará e não poderá ser estabelecido
- B) O Azure resolverá o conflito criando um NAT automático
- C) Apenas a primeira sub-rede de cada VNet conseguirá se comunicar
- D) O tráfego será roteado via ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** Para estabelecer o Peering de Rede Virtual (VNet Peering) com sucesso no Azure, os espaços de endereçamento IP (IP address spaces) das duas redes virtuais não podem se sobrepor. Caso haja sobreposição, o Azure impedirá a criação do Peering.

### Questão 137
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual ferramenta nativa de linha de comando da Microsoft é otimizada para copiar e sincronizar dados em alta velocidade entre sistemas de arquivos locais e Contas de Armazenamento do Azure Blob ou Azure Files?
**Opções:**
- A) AzCopy
- B) Robocopy nativo sem extensão
- C) PowerShell Get-Content
- D) FTP Client
**Resposta Correta:** A
**Explicação Técnica:** O AzCopy é um utilitário de linha de comando de altíssimo desempenho projetado especificamente para copiar dados de e para o Azure Blob, Files e Table Storage, suportando sincronização, retentativas e paralelismo de transferência.

### Questão 138
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa garantir que nenhum usuário, inclusive quem possui a função de Proprietário (Owner), consiga excluir acidentalmente uma Conta de Armazenamento crítica de produção. O que você deve aplicar diretamente na Conta de Armazenamento?
**Opções:**
- A) Um Bloqueio de Recurso contra Exclusão (Delete Lock / CanNotDelete)
- B) Uma política no Azure Policy proibindo a exclusão
- C) Uma função personalizada do RBAC
- D) Remover as permissões de gravação do usuário
**Resposta Correta:** A
**Explicação Técnica:** Os Bloqueios de Recursos (Resource Locks) do tipo CanNotDelete impedem que qualquer usuário exclua o recurso. Mesmo usuários com permissão de Proprietário (Owner) devem remover a trava de bloqueio antes de conseguir realizar a exclusão.

### Questão 139
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar o Azure Backup para proteger uma máquina virtual Windows. No entanto, o agente de backup falha ao tentar criar o instantâneo (snapshot) consistente com o aplicativo. O que deve ser verificado na VM?
**Opções:**
- A) O estado do serviço de Cópias de Sombra de Volume (VSS - Volume Shadow Copy Service) no Windows
- B) Se a extensão de criptografia BitLocker está desativada
- C) Se a chave de licença do Windows é válida
- D) O tamanho da tabela de rotas do sistema
**Resposta Correta:** A
**Explicação Técnica:** O Azure Backup utiliza a extensão VSS Snapshot no Windows para garantir que o backup de máquinas virtuais seja consistente com aplicativos (como SQL Server e Exchange). Se o serviço VSS local estiver desativado ou com falha, o instantâneo falhará.

### Questão 140
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa deseja redefinir a senha de administrador local e reconfigurar o serviço de RDP de uma máquina virtual Windows no Azure que perdeu o acesso remoto. Como isso pode ser feito pelo Portal do Azure sem recriar a VM?
**Opções:**
- A) Utilizando a opção 'Redefinir senha' (Reset Password) nas configurações da VM no Portal do Azure
- B) Editando o arquivo de registro do Windows via Azure Storage Explorer
- C) Abrindo um chamado com a Microsoft para reiniciar o data center
- D) Executando uma migração de assinatura
**Resposta Correta:** A
**Explicação Técnica:** O recurso 'Redefinir Senha' (Reset Password) nas configurações de suporte e solução de problemas da VM no Portal do Azure utiliza o VMAccess Extension para redefinir credenciais de administrador e restaurar a configuração padrão do RDP/SSH.

### Questão 141
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa rotear todo o tráfego de saída da Internet vindo de uma sub-rede de VMs através de um Firewall Virtual (NVA - Network Virtual Appliance) hospedado em outra sub-rede. O que você deve criar e associar à sub-rede?
**Opções:**
- A) Uma Tabela de Rotas (Route Table) com uma Rota Definida pelo Usuário (UDR) especificando o NVA como próximo salto (Next Hop)
- B) Um Grupo de Segurança de Rede (NSG) com regra Padrão
- C) Um Peering de VNet
- D) Um Azure Load Balancer Básico
**Resposta Correta:** A
**Explicação Técnica:** As Rotas Definidas pelo Usuário (UDR - User-Defined Routes) em uma Tabela de Rotas permitem sobrescrever as rotas padrão do Azure, direcionando o tráfego (ex.: 0.0.0.0/0) para um próximo salto personalizado como um NVA/Firewall.

### Questão 142
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual camada de acesso do Azure Blob Storage oferece o menor custo de armazenamento por gigabyte, mas possui o maior custo de recuperação e exige um tempo de reidratação de dados que pode levar até 15 horas?
**Opções:**
- A) Camada de Arquivamento (Archive Tier)
- B) Camada Fria (Cool Tier)
- C) Camada Quente (Hot Tier)
- D) Camada Premium
**Resposta Correta:** A
**Explicação Técnica:** A camada de Arquivamento (Archive Tier) é otimizada para dados raramente acessados e que exigem retenção de longo prazo. Ela oferece os menores custos de armazenamento, mas os blobs ficam offline e exigem o processo de reidratação (até 15 horas) antes de poderem ser lidos.

### Questão 143
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa atribuir a permissão 'Colaborador de Armazenamento de Dados de Blob' a um grupo de desenvolvedores. O acesso deve ser concedido apenas a um contêiner específico dentro de uma Conta de Armazenamento. Em qual escopo a atribuição de função (Role Assignment) deve ser realizada?
**Opções:**
- A) No escopo do Contêiner específico de Blob
- B) No escopo do Grupo de Recursos
- C) No escopo da Assinatura
- D) No escopo do Grupo de Gerenciamento
**Resposta Correta:** A
**Explicação Técnica:** O Azure RBAC suporta atribuição de funções em quatro escopos hierárquicos: Grupo de Gerenciamento, Assinatura, Grupo de Recursos e Recurso (incluindo níveis filhos como um contêiner específico de Blob Storage). Atribuir no escopo do contêiner garante o princípio do menor privilégio.

### Questão 144
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Qual recurso do Azure permite implantar um cluster de máquinas virtuais Linux pré-configurado para executar cargas de trabalho de computação de alto desempenho (HPC) e tarefas em lote altamente paralelas de forma agendada e escalável?
**Opções:**
- A) Azure Batch
- B) Azure Logic Apps
- C) Instâncias de Contêiner do Azure
- D) Azure Functions
**Resposta Correta:** A
**Explicação Técnica:** O Azure Batch é o serviço da Microsoft projetado para executar tarefas de computação de alto desempenho (HPC) e computação em lote (batch processing) em grande escala, gerenciando automaticamente o provisionamento, escalonamento e execução de nós de VM.

### Questão 145
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** O que é um Ponto de Extremidade de Serviço (Service Endpoint) do Azure VNet e como ele se difere de um Ponto de Extremidade Privado (Private Endpoint)?
**Opções:**
- A) O Service Endpoint otimiza o tráfego fornecendo uma rota direta para o IP público do serviço PaaS através do backbone da Microsoft, enquanto o Private Endpoint aloca um IP privado interno dentro da sua VNet
- B) O Service Endpoint cria uma VPN, enquanto o Private Endpoint exige ExpressRoute
- C) Não há diferença técnica entre eles
- D) O Private Endpoint funciona apenas para VMs Windows
**Resposta Correta:** A
**Explicação Técnica:** Os Service Endpoints mantêm o IP público do serviço PaaS no destino, mas garantem que o tráfego seja roteado de forma otimizada pela rede interna do Azure. Já os Private Endpoints alocam uma interface de rede virtual (NIC) com IP privado da sub-rede local para o serviço PaaS.

### Questão 146
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa exportar continuamente todas as métricas de desempenho e logs de diagnósticos de um Azure Application Gateway para uma Conta de Armazenamento externa para fins de arquivamento legal. O que deve ser configurado no Application Gateway?
**Opções:**
- A) Configurações de Diagnóstico (Diagnostic Settings)
- B) Azure Network Watcher Traffic Analytics
- C) Grupo de Ação de Alertas
- D) Azure Advisor Recommendation
**Resposta Correta:** A
**Explicação Técnica:** As Configurações de Diagnóstico (Diagnostic Settings) em recursos do Azure definem para onde enviar métricas e logs de recursos (Resource Logs). Os destinos suportados incluem workspaces do Log Analytics, Contas de Armazenamento e Event Hubs.

### Questão 147
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma Conta de Armazenamento do Azure possui dois tipos de chaves de acesso (Key1 e Key2). A equipe de segurança exige que as chaves de acesso sejam rotacionadas a cada 90 dias sem causar tempo de inatividade para os aplicativos que consomem o serviço. Qual é a estratégia recomendada?
**Opções:**
- A) Atualizar os aplicativos para usar a Key2, regenerar a Key1, atualizar os aplicativos de volta para a Key1 e regenerar a Key2
- B) Excluir a Conta de Armazenamento e recriá-la com novas chaves
- C) Regenerar Key1 e Key2 simultaneamente no Portal
- D) Converter a Conta de Armazenamento em um Azure Data Box
**Resposta Correta:** A
**Explicação Técnica:** As duas chaves de acesso (Key1 e Key2) permitem a rotação de chaves sem downtime: você altera a configuração das aplicações para a Key2, regenera a Key1, altera as aplicações para a nova Key1 e, por fim, regenera a Key2.

### Questão 148
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa atribuir automaticamente uma tag 'Ambiente: Produção' a todos os novos recursos criados em uma determinada assinatura do Azure. Qual componente deve ser utilizado?
**Opções:**
- A) Definição de política do Azure Policy com efeito 'Modify' ou 'Append'
- B) Bloqueio de Recurso do tipo ReadOnly
- C) Atribuição de função do RBAC
- D) Script de inicialização do Azure Bastion
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy permite criar regras com efeitos 'Modify' ou 'Append' para adicionar automaticamente tags ou propriedades aos recursos durante a implantação, garantindo a conformidade e a padronização das informações de governança.

### Questão 149
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual funcionalidade de segurança integrada ao Azure Application Gateway permite proteger aplicativos Web contra ataques comuns da OWASP (como SQL Injection e Cross-Site Scripting - XSS)?
**Opções:**
- A) Firewall de Aplicação Web (Web Application Firewall - WAF)
- B) Grupo de Segurança de Rede (NSG)
- C) Azure ExpressRoute Direct
- D) Filtro de DNS Privado
**Resposta Correta:** A
**Explicação Técnica:** O Web Application Firewall (WAF) no Azure Application Gateway fornece proteção centralizada para seus aplicativos Web contra vulnerabilidades e explorações comuns baseadas nos conjuntos de regras da OWASP (Open Web Application Security Project).

### Questão 150
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Uma empresa possui um Cofre dos Serviços de Recuperação usado para fazer backup de máquinas virtuais. Para evitar que backups antigos sejam excluídos por um ataque cibernético de ransomware ou por um administrador mal intencionado, qual recurso de proteção avançada deve ser ativado no cofre?
**Opções:**
- A) Soft Delete (Exclusão Temporária) e Imutabilidade do Vault (Vault Immutability)
- B) Azure Key Vault Auto-Rotation
- C) Desativar o agente do Azure Monitor
- D) Excluir o grupo de recursos do cofre
**Resposta Correta:** A
**Explicação Técnica:** O recurso Soft Delete para Azure Backup mantém os dados de backup excluídos retidos por 14 dias adicionais sem custo. Quando combinado com a Imutabilidade do Cofre (Vault Immutability), impede a alteração ou exclusão prematura de pontos de recuperação mesmo sob tentativas maliciosas.
