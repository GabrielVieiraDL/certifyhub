# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 2 (Questões 051 a 100)

Esta base de conhecimento contém as questões 051 a 100 do exame **AZ-104: Microsoft Azure Administrator** formatadas para ingestão e automação no Antigravity, traduzidas para o Português do Brasil (pt-BR) com a nomenclatura oficial da Microsoft.

---

### Questão 051
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa possui uma assinatura do Azure e deseja garantir que novos recursos criados em um Grupo de Recursos herdem automaticamente as tags do grupo de recursos pai caso não possuam tags próprias. Qual recurso do Azure Policy deve ser configurado?
**Opções:**
- A) Uma regra de política com o efeito `Modify` ou `Append` para adicionar as tags ausentes
- B) Uma política do tipo `Deny` para bloquear qualquer recurso sem tag
- C) Um Bloqueio de Recurso (Resource Lock) do tipo `ReadOnly`
- D) Uma Unidade Administrativa no Microsoft Entra ID
**Resposta Correta:** A
**Explicação Técnica:** O efeito `Modify` ou `Append` no Azure Policy permite criar ou atualizar tags em recursos existentes ou durante a implantação, garantindo que as tags de governança sejam herdadas dinamicamente sem bloquear o provisionamento.

### Questão 052
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você possui uma conta de armazenamento do Azure do tipo `StorageV2 (general purpose v2)`. É necessário configurar uma regra de Gerenciamento de Ciclo de Vida (Lifecycle Management) para mover automaticamente objetos blob que não foram modificados nos últimos 30 dias para a camada Cool, e após 90 dias para a camada Archive. Como a regra deve ser definida no Azure Portal?
**Opções:**
- A) Definir uma ação de transição baseada em `Days after modification` (30 dias para Cool, 90 dias para Archive)
- B) Criar um script do Azure PowerShell que execute diariamente via Azure Automation
- C) Configurar a replicação de objetos para outra conta de armazenamento na camada Archive
- D) Alterar a camada de acesso padrão da Conta de Armazenamento para Archive
**Resposta Correta:** A
**Explicação Técnica:** O Azure Blob Lifecycle Management permite definir políticas baseadas em regras com condições como `daysAfterModificationGreaterThan` para automatizar a transição de camada de acesso (Hot -> Cool -> Archive) reduzindo os custos de armazenamento.

### Questão 053
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa realizar o backup de uma máquina virtual (VM1) hospedada no Azure. Qual tipo de replicação deve ser configurado no Cofre dos Serviços de Recuperação (Recovery Services Vault) para garantir que os dados de backup permaneçam disponíveis mesmo se duas zonas de disponibilidade da região primária falharem?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância Geográfica (GRS) ou Redundância Geozonal (GZRS)
- C) Armazenamento com Redundância de Zona (ZRS)
- D) Armazenamento de Bloco de Alto Desempenho
**Resposta Correta:** B
**Explicação Técnica:** O GRS ou GZRS replica os dados para uma região secundária pareada a centenas de quilômetros de distância, garantindo resiliência mesmo diante de uma falha catastrófica regional ou perda total de múltiplas zonas de disponibilidade.

### Questão 054
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Sua empresa planeja implantar um aplicativo web em contêineres Linux de forma rápida e sem a necessidade de gerenciar nós de cluster ou Kubernetes. Qual serviço de computação serverless do Azure é o mais adequado?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Serviço de Kubernetes do Azure (AKS)
- C) Conjuntos de Dimensionamento de Máquinas Virtuais (VMSS)
- D) Registro de Contêiner do Azure (ACR)
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Instances (ACI) permite executar contêineres Docker isolados sob demanda em ambiente serverless, sem a complexidade de provisionar máquinas virtuais ou gerenciar orquestradores como o AKS.

### Questão 055
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa permitir que máquinas virtuais em uma Rede Virtual (VNET1) acessem com segurança uma Conta de Armazenamento do Azure (storage1) utilizando endereços IP privados internos, sem expor o tráfego à Internet pública. Qual recurso deve ser implantado na VNET1?
**Opções:**
- A) Ponto de Extremidade Privado (Private Endpoint)
- B) Gateway de VPN Ponto a Site (Point-to-Site VPN)
- C) Conexão do Azure ExpressRoute
- D) Regra de Inbound em um Grupo de Segurança de Rede (NSG)
**Resposta Correta:** A
**Explicação Técnica:** O Private Endpoint cria uma interface de rede virtual com um IP privado da VNET atribuído ao serviço do Azure (como o Storage), garantindo que todo o tráfego permaneça exclusivamente dentro da rede privada da Microsoft.

### Questão 056
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador precisa conceder permissão a um usuário para reiniciar e parar máquinas virtuais em um Grupo de Recursos específico, mas sem permitir a alteração das configurações de rede ou exclusão das VMs. Qual função do RBAC deve ser atribuída?
**Opções:**
- A) Colaborador de Máquina Virtual (Virtual Machine Contributor)
- B) Operador de Máquina Virtual ou uma Função Personalizada (Custom Role) com permissão `Microsoft.Compute/virtualMachines/restart/action`
- C) Leitor (Reader)
- D) Proprietário (Owner)
**Resposta Correta:** B
**Explicação Técnica:** Aplicando o princípio do menor privilégio, uma função personalizada ou de operador específico restringe as ações do usuário estritamente ao reinício/parada de instâncias sem conceder privilégios excessivos de modificação na infraestrutura.

### Questão 057
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa coletar logs de eventos do sistema operacional de 50 máquinas virtuais Windows e Linux e centralizá-los para consultas analíticas utilizando a linguagem KQL. Qual recurso do Azure Monitor deve ser configurado e associado às VMs?
**Opções:**
- A) Regra de Coleta de Dados (Data Collection Rule - DCR) e um Log Analytics Workspace
- B) Azure Advisor
- C) Contas de Armazenamento com retenção de 90 dias
- D) Mapa de Rede do Network Watcher
**Resposta Correta:** A
**Explicação Técnica:** O Agente do Azure Monitor (AMA) utiliza Regras de Coleta de Dados (DCR) para definir quais eventos e métricas serão filtrados e enviados diretamente para o Log Analytics Workspace para consultas KQL.

### Questão 058
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Duas Redes Virtuais, VNET-A (na região East US) e VNET-B (na região West Europe), possuem espaços de endereçamento IP não sobrepostos (10.1.0.0/16 e 10.2.0.0/16). Qual recurso permite a comunicação de baixíssima latência entre as VMs dessas redes sem tráfego pela Internet pública?
**Opções:**
- A) Peering Global de Rede Virtual (Global VNet Peering)
- B) Gateway de VPN Site a Site
- C) Azure Application Gateway
- D) Servidor DNS Privado
**Resposta Correta:** A
**Explicação Técnica:** O Peering de VNet (mesmo entre regiões diferentes - Global Peering) conecta redes virtuais diretamente através da rede de backbone privada de alta velocidade da Microsoft com criptografia na camada física.

### Questão 059
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa garantir que uma aplicação Web hospedada no Conjunto de Dimensionamento de Máquinas Virtuais (VMSS) aumente o número de instâncias de 2 para 10 quando a média de uso de CPU ultrapassar 80% por 10 minutos. Onde essa regra deve ser configurada?
**Opções:**
- A) Configuração de Dimensionamento Automático (Autoscale Setting) no VMSS
- B) Modelo ARM declarativo estático
- C) Regra do Azure Policy
- D) Alertas de Orçamento do Azure Cost Management
**Resposta Correta:** A
**Explicação Técnica:** O recurso de Autoscale no VMSS permite configurar regras métricas (ex.: % de CPU, memória ou fila) com limites e ações de escala horizontal (*Scale-out* / *Scale-in*) automáticas.

### Questão 060
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual utilitário de linha de comando oficial da Microsoft é recomendado para transferência massiva e sincronização de arquivos locais para o Azure Blob Storage e Azure Files com suporte a autenticação via Microsoft Entra ID?
**Opções:**
- A) AzCopy
- B) Robocopy nativo do Windows
- C) Azure CLI `az disk`
- D) FTP Standard
**Resposta Correta:** A
**Explicação Técnica:** O AzCopy v10 é a ferramenta de linha de comando otimizada para cópia e sincronização de dados de alta performance de/para contas de armazenamento do Azure, suportando tokens SAS e identidades do Microsoft Entra ID.

### Questão 061
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Um administrador precisa analisar por que os pacotes de uma máquina virtual não estão conseguindo alcançar um endereço IP de destino na porta 443. Qual ferramenta do Azure Network Watcher permite verificar a regra de NSG responsável pelo bloqueio?
**Opções:**
- A) Verificação de Fluxo IP (IP Flow Verify)
- B) Próximo Salto (Next Hop)
- C) Diagnóstico de Conexão (Connection Troubleshoot)
- D) Captura de Pacotes (Packet Capture)
**Resposta Correta:** A
**Explicação Técnica:** A ferramenta IP Flow Verify do Network Watcher aceita a direção do tráfego, protocolo, IP de origem/destino e porta, informando se o tráfego é permitido ou negado e indicando exatamente qual regra de NSG aplicou a ação.

### Questão 062
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma organização precisa isolar a administração dos usuários do departamento financeiro sem conceder privilégios globais sobre todo o diretório. Qual recurso do Microsoft Entra ID deve ser utilizado?
**Opções:**
- A) Unidade Administrativa (Administrative Unit - AU)
- B) Grupo de Gerenciamento (Management Group)
- C) Assinatura do Azure separada
- D) Bloqueio de Exclusão (Delete Lock)
**Resposta Correta:** A
**Explicação Técnica:** As Unidades Administrativas (AU) no Microsoft Entra ID permitem subdividir a organização e delegar permissões administrativas de RBAC sobre um conjunto específico de usuários, grupos ou dispositivos.

### Questão 063
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual serviço do Azure Monitor permite simular a disponibilidade de uma aplicação Web de múltiplos locais geográficos ao redor do mundo enviando solicitações HTTP/HTTPS periódicas?
**Opções:**
- A) Testes de Disponibilidade (Availability Tests) no Azure Application Insights
- B) Network Watcher Topology
- C) Log Analytics Workspace
- D) Azure Service Health
**Resposta Correta:** A
**Explicação Técnica:** Os Testes de Disponibilidade do Application Insights executam testes de ping de URL ou testes de múltiplos passos a partir de pontos globais para monitorar o tempo de resposta e tempo de atividade (*uptime*) das aplicações.

### Questão 064
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você está configurando um Balanceador de Carga do Azure (Azure Load Balancer) do SKU Standard. Quais tipos de endereços IP de destino podem ser adicionados ao Pool de Backend (Backend Pool)?
**Opções:**
- A) Endereços IP privados pertencentes a qualquer máquina virtual na mesma Rede Virtual ou redes emparelhadas (VNet Peering)
- B) Apenas endereços IP públicos estáticos
- C) Qualquer endereço IP na Internet pública
- D) Apenas instâncias de máquinas virtuais na mesma subrede
**Resposta Correta:** A
**Explicação Técnica:** O Azure Load Balancer Standard permite configurar pools de backend baseados em endereço IP, permitindo associar NICs e VMs em subredes e VNets emparelhadas dentro da mesma região.

### Questão 065
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa possui máquinas virtuais locais no VMware e deseja migrá-las para o Azure sem reconfigurar aplicações. Qual serviço de migração é a ferramenta centralizada recomendada pela Microsoft?
**Opções:**
- A) Azure Migrate
- B) Azure Data Box
- C) Serviço de Migração de Banco de Dados do Azure (DMS)
- D) AzCopy
**Resposta Correta:** A
**Explicação Técnica:** O Azure Migrate é o hub central para descoberta, avaliação de prontidão e migração sem interrupção de servidores locais (VMware, Hyper-V, físicos) para a infraestrutura do Azure.

### Questão 066
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa configurar o serviço de arquivos compartilhados do Azure (Azure Files) para que usuários locais possam acessar os compartilhamentos de arquivos através do protocolo SMB corporativo com autenticação baseada em identidade. Qual integração é necessária?
**Opções:**
- A) Autenticação via Microsoft Entra Domain Services (DS) ou AD DS local
- B) Apenas chaves de acesso da Conta de Armazenamento (Storage Account Key)
- C) Conexão anônima HTTP
- D) Tokens SAS individuais
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files suporta autenticação SMB baseada em identidade integrando-se ao Active Directory Domain Services (AD DS) local ou ao Microsoft Entra Domain Services para controle de permissões no nível de arquivo/pasta (NTFS/ACLs).

### Questão 067
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um usuário relata que não consegue criar máquinas virtuais em uma assinatura do Azure, recebendo a mensagem "Quota Exceeded". Qual é a ação adequada que o administrador deve realizar no Portal do Azure?
**Opções:**
- A) Solicitar o aumento de cota (Quota Increase) no menu `Help + support` ou `Usages + quotas`
- B) Criar um novo Grupo de Recursos
- C) Alterar o plano do Microsoft Entra ID de P1 para P2
- D) Reinstalar o Azure CLI
**Resposta Correta:** A
**Explicação Técnica:** As cotas de recursos do Azure (como número de vCPUs por região) são limites configurados pela Microsoft para proteger contra estouros operacionais e podem ser ampliadas mediante solicitação de suporte sem custo adicional.

### Questão 068
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual recurso do Azure permite inspecionar, filtrar e bloquear tráfego HTTP/HTTPS de entrada em nível de aplicação (Camada 7) utilizando regras de Firewall de Aplicativo Web (WAF)?
**Opções:**
- A) Azure Application Gateway com WAF
- B) Azure Load Balancer Basic
- C) Grupo de Segurança de Rede (NSG)
- D) Azure Route Table
**Resposta Correta:** A
**Explicação Técnica:** O Application Gateway é um balanceador de carga de camada 7 que oferece a funcionalidade de Web Application Firewall (WAF) para proteger aplicações contra vulnerabilidades comuns como SQL Injection e Cross-Site Scripting (XSS).

### Questão 069
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você deseja criar um alerta no Azure Monitor que envie uma notificação por SMS e e-mail para a equipe de infraestrutura sempre que o uso de memória de um servidor ultrapassar 90%. O que deve ser configurado para gerenciar essas ações de notificação?
**Opções:**
- A) Grupo de Ação (Action Group)
- B) Grupo de Gerenciamento (Management Group)
- C) Regra de Alerta de Orçamento
- D) Tabela do KQL
**Resposta Correta:** A
**Explicação Técnica:** Um Grupo de Ação (Action Group) no Azure Monitor define uma coleção de preferências de notificação (SMS, e-mail, push, chamadas telefônicas) e ações automatizadas (webhooks, Azure Functions, Runbooks) disparadas por alertas.

### Questão 070
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um grupo de máquinas virtuais de modo a garantir que em caso de manutenção planejada no data center da Microsoft, no máximo 20% das instâncias sejam reiniciadas por vez. Qual configuração deve ser utilizada em um Conjunto de Disponibilidade (Availability Set)?
**Opções:**
- A) Configurar Domínios de Atualização (Update Domains - até 20 domínios)
- B) Configurar Domínios de Falha (Fault Domains)
- C) Criar subredes separadas para cada VM
- D) Atribuir um Private Endpoint para cada VM
**Resposta Correta:** A
**Explicação Técnica:** Os Domínios de Atualização (Update Domains) determinam quais grupos de máquinas virtuais e hardware subjacente podem ser reiniciados simultaneamente durante manutenções planejadas na infraestrutura física do Azure.

### Questão 071
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa exige que os dados armazenados em uma Conta de Armazenamento do Azure não possam ser alterados ou excluídos por ninguém (nem mesmo administradores) durante um período de retenção de 5 anos por exigências regulatórias. Qual recurso deve ser habilitado no Blob Storage?
**Opções:**
- A) Armazenamento Imutável com Política de Retenção Baseada em Tempo (Immutable Blob Storage)
- B) Criptografia com Chave Gerenciada pelo Cliente (CMK)
- C) Bloqueio de Recurso do tipo ReadOnly
- D) Soft Delete para Blobs
**Resposta Correta:** A
**Explicação Técnica:** O Armazenamento Imutável do Azure Blob permite aplicar políticas WORM (Write Once, Read Many) bloqueadas que impedem modificações ou exclusões de arquivos durante o período configurado para conformidade legal.

### Questão 072
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual recurso de rede do Azure permite conectar de forma segura um usuário remoto trabalhando em home office diretamente à sua Rede Virtual do Azure a partir do seu laptop pessoal através de um cliente VPN?
**Opções:**
- A) Gateway de VPN Ponto a Site (Point-to-Site / P2S VPN)
- B) Gateway de VPN Site a Site (Site-to-Site / S2S VPN)
- C) Peering de VNet
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** A VPN Ponto a Site (P2S) estabelece um túnel criptografado individual a partir de um dispositivo cliente remoto (Windows, macOS, Linux) para a Rede Virtual do Azure via SSTP, OpenVPN ou IKEv2.

### Questão 073
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa visualizar o histórico completo de operações administrativas (como quem criou, modificou ou excluiu um recurso) executadas na sua assinatura do Azure nos últimos 90 dias. Qual log deve ser consultado no Portal do Azure?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Logs de Conectividade do Network Watcher
- C) Logs de Diagnóstico do Storage Account
- D) Microsoft Entra Audit Logs exclusivamente
**Resposta Correta:** A
**Explicação Técnica:** O Log de Atividades do Azure (Activity Log) registra todos os eventos do plano de controle (ARM) executados nas assinaturas, incluindo criação, atualização e exclusão de recursos com detalhes do chamador e data/hora.

### Questão 074
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa deseja executar uma aplicação baseada em contêineres gerenciada via orquestrador Kubernetes completo com integração a redes virtuais, controle RBAC e escalabilidade automática. Qual serviço do Azure é o recomendado?
**Opções:**
- A) Serviço de Kubernetes do Azure (Azure Kubernetes Service - AKS)
- B) Instâncias de Contêiner do Azure (ACI)
- C) Conjunto de Dimensionamento de VMs
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O Azure Kubernetes Service (AKS) é a solução gerenciada de Kubernetes da Microsoft que reduz a complexidade operacional do plano de controle (*control plane*), oferecendo integração nativa com o ecossistema Azure.

### Questão 075
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você deseja permitir que um parceiro externo faça upload de arquivos para um contêiner do Azure Blob Storage durante 4 horas sem fornecer a chave mestra da Conta de Armazenamento nem criar um usuário no Microsoft Entra ID. O que deve ser gerado?
**Opções:**
- A) Uma Assinatura de Acesso Compartilhado (Shared Access Signature - SAS)
- B) Um Bloqueio de Recurso
- C) Uma Chave de Acesso Primária
- D) Um certificado X.509
**Resposta Correta:** A
**Explicação Técnica:** A Assinatura de Acesso Compartilhado (SAS) fornece acesso delegado seguro com privilégios refinados (ex.: apenas gravação) e tempo de expiração estrito sobre recursos específicos de armazenamento sem expor as chaves da conta.

### Questão 076
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa rotear todo o tráfego de saída da Internet de uma subrede da VNET1 para passar obrigatoriamente por uma solução de Firewall hospedada em uma máquina virtual (NVA - Network Virtual Appliance). Qual recurso de rede deve ser associado à subrede?
**Opções:**
- A) Tabela de Roteamento (Route Table / User-Defined Route - UDR)
- B) Grupo de Segurança de Rede (NSG)
- C) Azure DNS Privado
- D) VNet Peering
**Resposta Correta:** A
**Explicação Técnica:** As Tabelas de Roteamento personalizadas (UDRs) permitem sobrescrever o roteamento padrão do Azure criando rotas personalizadas (ex.: `0.0.0.0/0` apontando para o IP privado da NVA como Próximo Salto).

### Questão 077
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa possui 50 assinaturas do Azure e precisa aplicar uma regra de segurança em todas elas para bloquear a criação de endereços IP públicos. Como essa regra pode ser aplicada centralizadamente de forma mais eficiente?
**Opções:**
- A) Atribuir uma definição do Azure Policy a um Grupo de Gerenciamento (Management Group) contendo todas as assinaturas
- B) Configurar o Azure Policy manualmente em cada assinatura uma por uma
- C) Criar 50 tabelas de roteamento
- D) Aplicar Bloqueios de Exclusão em cada Grupo de Recursos
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento fornecem um escopo de governança acima das assinaturas. Atribuir uma política a um Grupo de Gerenciamento garante a herança automática das regras para todas as assinaturas e recursos contidos abaixo dele.

### Questão 078
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual funcionalidade do Azure Monitor permite visualizar um mapa visual interativo mostrando os relacionamentos de dependência e conexões de rede entre máquinas virtuais e seus processos em execução?
**Opções:**
- A) VM Insights (Dependency Map)
- B) Log Analytics KQL Workspace
- C) Azure Advisor Cost Map
- D) Activity Log Search
**Resposta Correta:** A
**Explicação Técnica:** O VM Insights utiliza o mapa de dependências para descobrir automaticamente componentes de aplicação e conexões de rede de entrada/saída em servidores Windows e Linux em tempo real.

### Questão 079
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um aplicativo web em Python no Serviço de Aplicativo do Azure (Azure App Service). Qual plano de serviço de aplicativo (App Service Plan) garante suporte a slots de implantação (*Deployment Slots*) para testes em staging sem tempo de inatividade?
**Opções:**
- A) Camada Padrão (Standard) ou superior
- B) Camada Gratuita (Free)
- C) Camada Compartilhada (Shared)
- D) Camada Básica (Basic)
**Resposta Correta:** A
**Explicação Técnica:** Os Slots de Implantação (Deployment Slots), que permitem realizar trocas (*swaps*) de código sem downtime entre staging e produção, estão disponíveis a partir da camada Standard (Padrão) do App Service Plan.

### Questão 080
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa conectar um data center local ao Azure através de uma conexão de alta velocidade dedicada de até 10 Gbps ou 100 Gbps que não trafegue pela Internet pública e ofereça latência ultra-baixa. Qual serviço deve ser contratado?
**Opções:**
- A) Azure ExpressRoute
- B) Gateway de VPN Site a Site
- C) Peering de VNet
- D) Azure Bastion
**Resposta Correta:** A
**Explicação Técnica:** O Azure ExpressRoute permite criar conexões privadas e diretas entre as instalações locais da empresa e os data centers da Microsoft através de provedores de conectividade dedicados.

### Questão 081
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa deseja sincronizar arquivos de um servidor de arquivos Windows local (Windows Server 2022) com o Azure Files, mantendo os arquivos acessados com maior frequência em cache no servidor local. Qual serviço atende a esse requisito?
**Opções:**
- A) Sincronização de Arquivos do Azure (Azure File Sync)
- B) AzCopy
- C) Azure Import/Export Service
- D) Gerenciamento de Ciclo de Vida do Blob Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure File Sync centraliza os compartilhamentos de arquivos da organização no Azure Files mantendo o desempenho e a compatibilidade de um servidor de arquivos local com o recurso de Tiering em Nuvem (*Cloud Tiering*).

### Questão 082
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual recurso do Microsoft Entra ID permite exigir que os usuários alterem periodicamente suas senhas ou utilizem a Autenticação Multifator (MFA) caso o sistema detecte um login suspeito vindo de um local não habitual?
**Opções:**
- A) Proteção de Identidade do Microsoft Entra (Microsoft Entra ID Protection) e Acesso Condicional
- B) Grupos de Gerenciamento do Azure
- C) Bloqueios de Recursos
- D) Azure Policy
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Entra ID Protection analisa sinais de risco de usuário e de entrada (*sign-in risk*), integrando-se às políticas de Acesso Condicional para automatizar respostas como exigir MFA ou bloqueio de conta.

### Questão 083
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar o backup de máquinas virtuais do Azure para que os pontos de recuperação diários sejam mantidos por 30 dias, os semanais por 12 semanas e os anuais por 5 anos. Onde essas retenções são definidas?
**Opções:**
- A) Política de Backup (Backup Policy) associada ao Cofre dos Serviços de Recuperação
- B) Configurações de Diagnóstico da VM
- C) Regras do Azure Policy
- D) Log Analytics Workspace
**Resposta Correta:** A
**Explicação Técnica:** As Políticas de Backup no Recovery Services Vault especificam a frequência de disparo do backup e o período de retenção dos pontos de restauração (diário, semanal, mensal e anual).

### Questão 084
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual serviço gerenciado do Azure permite que administradores se conectem com segurança a máquinas virtuais Linux e Windows via SSH ou RDP diretamente através do Portal do Azure sem expor endereços IP públicos nas VMs?
**Opções:**
- A) Azure Bastion
- B) Azure Application Gateway
- C) Azure ExpressRoute
- D) Peering de VNet
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bastion é um serviço de PaaS provisionado dentro de uma subrede dedicada (`AzureBastionSubnet`) que fornece conectividade RDP/SSH segura via TLS diretamente no navegador web sem necessidade de IP público nas VMs.

### Questão 085
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar uma máquina virtual no Azure garantindo que ela utilize um disco gerenciado criptografado usando uma chave de criptografia de sua própria autoria armazenada no Azure Key Vault. Qual tecnologia de criptografia de disco é utilizada?
**Opções:**
- A) Criptografia no Nível do Host ou Azure Disk Encryption (ADE) com Chaves Gerenciadas pelo Cliente (CMK)
- B) Criptografia Padrão do BitLocker sem Key Vault
- C) Criptografia SSL/TLS em trânsito
- D) Criptografia no nível de arquivo NTFS
**Resposta Correta:** A
**Explicação Técnica:** O Azure Disk Encryption (ADE) ou a Criptografia do Lado do Servidor (SSE) com Chaves Gerenciadas pelo Cliente (CMK) permite proteger os discos de VMs utilizando chaves guardadas sob controle total do cliente no Azure Key Vault.

### Questão 086
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual opção de replicação de dados em uma Conta de Armazenamento do Azure grava três cópias dos dados de forma síncrona em três zonas de disponibilidade separadas dentro da mesma região primária?
**Opções:**
- A) Armazenamento com Redundância de Zona (ZRS)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento de Leitura com Redundância Geográfica (RA-GRS)
**Resposta Correta:** A
**Explicação Técnica:** O ZRS (Zone-Redundant Storage) replica os dados de forma síncrona em três instalações fisicamente isoladas (Availability Zones) na região primária, oferecendo tolerância à falha de um data center completo.

### Questão 087
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um desenvolvedor precisa criar uma aplicação no Azure que acesse com segurança uma Conta de Armazenamento sem codificar senhas ou credenciais no código-fonte. Qual funcionalidade do Microsoft Entra ID deve ser habilitada na aplicação/VM?
**Opções:**
- A) Identidade Gerenciada (Managed Identity - atribuída pelo sistema ou pelo usuário)
- B) Conta de usuário local com senha de 20 caracteres
- C) Token SAS estático no repositório Git
- D) Registro de aplicativo anônimo
**Resposta Correta:** A
**Explicação Técnica:** As Identidades Gerenciadas (Managed Identities) fornecem uma identidade gerenciada automaticamente no Microsoft Entra ID para que os recursos do Azure se autentiquem em outros serviços suportados sem necessidade de gerenciar credenciais.

### Questão 088
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você possui uma máquina virtual com duas interfaces de rede (NIC1 e NIC2). Ambas estão associadas a subredes da VNET1. O que é correto afirmar sobre a movimentação da NIC2 para outra subrede da mesma VNET1?
**Opções:**
- A) É possível alterar a subrede associada a uma NIC sem precisar excluir a placa de rede ou a máquina virtual
- B) Não é possível alterar a subrede de uma NIC depois de criada
- C) É necessário reformatar o sistema operacional da VM
- D) A VM precisa ser movida para outra assinatura
**Resposta Correta:** A
**Explicação Técnica:** O Azure permite alterar a subrede de uma interface de rede (NIC) existente dentro da mesma VNET através do Portal do Azure, PowerShell ou CLI, ajustando as configurações de IP conforme necessário.

### Questão 089
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual ferramenta de linguagem de consulta é utilizada no Azure Monitor Log Analytics para filtrar, agregar e analisar petabytes de dados de logs estruturados?
**Opções:**
- A) Linguagem de Consulta Kusto (KQL - Kusto Query Language)
- B) SQL Server Transact-SQL (T-SQL)
- C) GraphQL
- D) Python Pandas
**Resposta Correta:** A
**Explicação Técnica:** KQL (Kusto Query Language) é a linguagem de consulta otimizada utilizada no Log Analytics, Azure Data Explorer, Microsoft Sentinel e Resource Graph para pesquisa de alta performance em logs.

### Questão 090
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa garantir que uma máquina virtual crítica no Azure tenha um SLA de disponibilidade de 99,99%. Qual arquitetura de implantação atende a esse requisito oficial da Microsoft?
**Opções:**
- A) Implantar pelo menos duas instâncias da VM em duas ou mais Zonas de Disponibilidade (Availability Zones) na mesma região do Azure
- B) Implantar uma única VM com disco HDD Padrão
- C) Usar um Conjunto de Disponibilidade em uma única zona com discos Standard
- D) Configurar o desligamento automático diário da VM
**Resposta Correta:** A
**Explicação Técnica:** A Microsoft oferece SLA de 99,99% para máquinas virtuais no Azure quando pelo menos duas instâncias são implantadas em Zonas de Disponibilidade separadas na mesma região.

### Questão 091
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa possui 50 TB de dados locais e precisa transferi-los para o Azure Blob Storage, mas a conexão de Internet corporativa é de apenas 10 Mbps. Qual solução física de migração é a mais indicada?
**Opções:**
- A) Solicitar um dispositivo físico do Azure Data Box à Microsoft
- B) Executar o comando `azcopy` via Internet
- C) Fazer upload manual pelo navegador no Portal do Azure
- D) Utilizar um Gateway de VPN P2S
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Box é um dispositivo de armazenamento resistente enviado pela Microsoft para cópia local de terabytes/petabytes de dados, sendo devolvido via transporte físico para carregamento direto nos data centers do Azure.

### Questão 092
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual função interna do RBAC do Azure permite que um usuário leia todos os recursos da assinatura e gerencie permissões de acesso (atribuir/remover papéis a outros usuários), mas sem permissão de criar ou modificar recursos de infraestrutura diretamente?
**Opções:**
- A) Administrador de Acesso Baseado em Função (Role Based Access Control Administrator) ou Administrador de Acesso do Usuário (User Access Administrator)
- B) Proprietário (Owner)
- C) Colaborador (Contributor)
- D) Leitor (Reader)
**Resposta Correta:** A
**Explicação Técnica:** A função User Access Administrator (ou RBAC Administrator) permite gerenciar atribuições de controle de acesso de usuários sobre os recursos do Azure sem conceder permissões de escrita no plano de controle dos recursos.

### Questão 093
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** O que ocorre com os endereços IP privados atribuídos dinamicamente a uma máquina virtual do Azure quando a VM é parada e desalocada (*Stopped (deallocated)*)?
**Opções:**
- A) O endereço IP privado dinâmico é liberado e pode ser atribuído a outro recurso caso não tenha sido configurado como estático
- B) O endereço IP privado é mantido para sempre
- C) A máquina virtual é excluída permanentemente
- D) O endereço IP privado converte-se automaticamente em IP público
**Resposta Correta:** A
**Explicação Técnica:** Endereços IP privados dinâmicos no Azure são liberados quando a VM é desalocada. Para garantir que a VM mantenha o mesmo IP privado após ser reiniciada, a alocação do IP na NIC deve ser alterada para Estática.

### Questão 094
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa ser notificado proativamente se houver uma interrupção nos serviços do Azure que afete a região onde suas máquinas virtuais estão hospedadas. Qual serviço fornece essa visão personalizada do status dos seus serviços?
**Opções:**
- A) Azure Service Health
- B) Azure Monitor Metrics
- C) Azure Advisor Cost Tab
- D) Network Watcher IP Flow
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Health fornece painéis personalizados informando sobre incidentes de serviço oficiais da Microsoft, manutenções planejadas e avisos de integridade especificamente relacionados às suas assinaturas e regiões em uso.

### Questão 095
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você deseja criar um modelo declarativo em formato JSON para implantar repetidamente uma infraestrutura contendo uma VNet, duas subredes e três VMs no Azure. Qual tecnologia nativa do Azure é utilizada?
**Opções:**
- A) Modelos do Azure Resource Manager (ARM Templates) ou arquivos Bicep
- B) Scripts Bash sem validação
- C) Arquivos de configuração XML legados
- D) Dockerfiles
**Resposta Correta:** A
**Explicação Técnica:** Os ARM Templates (em JSON) e o Azure Bicep são as linguagens declarativas nativas de Infraestrutura como Código (IaC) para definir e implantar recursos no Azure de maneira consistente e repetível.

### Questão 096
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual tipo de Conta de Armazenamento do Azure é a recomendada pela Microsoft para a maioria dos cenários de produção, oferecendo suporte a Blobs, Files, Queues e Tables com todas as opções de redundância (LRS, ZRS, GRS, GZRS)?
**Opções:**
- A) `StorageV2 (general purpose v2)`
- B) `BlobStorage (legado)`
- C) `Storage (general purpose v1)`
- D) `Premium BlockBlobs` exclusivamente
**Resposta Correta:** A
**Explicação Técnica:** As contas General Purpose v2 (`StorageV2`) são o tipo padrão recomendado que suportam todos os serviços de armazenamento e os recursos mais recentes de camada de acesso, ciclo de vida e replicação.

### Questão 097
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador aplicou um Bloqueio de Recurso (Resource Lock) do tipo `ReadOnly` em um Grupo de Recursos. O que os usuários com a função de `Proprietário` (Owner) conseguirão fazer dentro desse grupo de recursos?
**Opções:**
- A) Eles poderão visualizar os recursos, mas não poderão criar, atualizar ou excluir nenhum recurso até que a trava seja removida
- B) Eles poderão excluir recursos normalmente por serem Proprietários
- C) Eles perderão acesso de leitura ao portal
- D) O bloqueio não afeta usuários com MFA habilitado
**Resposta Correta:** A
**Explicação Técnica:** Os Bloqueios de Recursos substituem qualquer permissão de RBAC. Um bloqueio `ReadOnly` impede qualquer ação de gravação ou exclusão sobre os recursos protegidos, independentemente do nível de privilégio do usuário.

### Questão 098
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual componente de um Grupo de Segurança de Rede (NSG) determina a ordem de avaliação das regras de tráfego de entrada e saída?
**Opções:**
- A) O número da Prioridade (Priority) da regra (quanto menor o número, maior a prioridade)
- B) O nome alfabético da regra
- C) A data de criação da regra
- D) O endereço MAC da placa de rede
**Resposta Correta:** A
**Explicação Técnica:** As regras de NSG são processadas em ordem de prioridade (de 100 a 4096). Assim que uma regra corresponde ao tráfego (Allow ou Deny), o processamento de regras adicionais é interrompido.

### Questão 099
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa analisar a latência de tráfego de rede e a perda de pacotes contínua entre duas máquinas virtuais localizadas em subredes diferentes. Qual recurso do Network Watcher deve ser implantado?
**Opções:**
- A) Monitor de Conexão (Connection Monitor)
- B) IP Flow Verify
- C) Tabela de Roteamento
- D) Azure Policy Diagnostic
**Resposta Correta:** A
**Explicação Técnica:** O Connection Monitor do Network Watcher fornece verificação contínua de conectividade e desempenho de rede (latência e perda de pacotes) entre recursos do Azure e pontos de extremidade locais ou na nuvem.

### Questão 100
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa precisa implantar máquinas virtuais altamente seguras e isoladas onde o hardware físico subjacente seja dedicado exclusivamente a essa única organização por exigências de conformidade regulatória. Qual solução deve ser utilizada?
**Opções:**
- A) Anfitrião Dedicado do Azure (Azure Dedicated Host)
- B) Instâncias Reservadas de VM compartilhadas
- C) Conjunto de Dimensionamento em modo Flexível
- D) Azure App Service Free
**Resposta Correta:** A
**Explicação Técnica:** O Azure Dedicated Host fornece servidores físicos dedicados exclusivos para a sua organização para hospedar suas máquinas virtuais do Azure, atendendo a requisitos rígidos de conformidade e isolamento de hardware.
