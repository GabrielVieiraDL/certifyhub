# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 9 (Questões 401 a 440)

Esta base de conhecimento contém as questões 401 a 440 do exame **AZ-104: Microsoft Azure Administrator** formatadas para ingestão e automação no Antigravity.

---

### Questão 401
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Sua empresa possui um Log Analytics Workspace centralizado. Você precisa criar uma consulta KQL para identificar todas as falhas de login de máquinas virtuais Windows nas últimas 24 horas. Qual tabela e filtro KQL devem ser utilizados?
**Opções:**
- A) Syslog | where EventID == 4625
- B) Event | where EventID == 4625 and TimeGenerated > ago(24h)
- C) AzureActivity | where OperationName == 'LoginFailed'
- D) Heartbeat | where Status == 'Failed'
**Resposta Correta:** B
**Explicação Técnica:** No Log Analytics Workspace, os eventos do Log de Eventos do Windows são armazenados na tabela Event. O Event ID 4625 representa uma falha de logon e a função ago(24h) filtra os registros dentro da janela de 24 horas.

### Questão 402
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa configurar uma solução de resolução de nomes que permita que máquinas virtuais em uma Rede Virtual (VNet) privada resolvam os nomes de domínio públicos da Internet, além de registrar automaticamente seus próprios FQDNs em uma zona privada. Qual recurso do Azure atende a esse requisito?
**Opções:**
- A) Azure Public DNS
- B) Azure Private DNS Zone com Auto-registration habilitado
- C) DNS Privado On-Premises via VPN
- D) Azure Firewall DNS Proxy
**Resposta Correta:** B
**Explicação Técnica:** As Zonas Privadas do Azure DNS (Azure Private DNS Zones) com a funcionalidade de Auto-Registration (Registro Automático) vinculada a uma VNet permitem que o Azure registre automaticamente os registros A para as VMs e resolva nomes internos e externos.

### Questão 403
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma organização requer que os dados gravados no Azure Blob Storage permaneçam inalteráveis por um período de 7 anos para conformidade regulatória. Qual recurso deve ser habilitado na conta de armazenamento?
**Opções:**
- A) Bloqueio de Recursos (Resource Lock CanNotDelete)
- B) Criptografia Azure Disk Encryption
- C) Armazenamento Imutável com Política baseada em Tempo (Time-based Retention Policy em modo Compliance)
- D) Azure Backup com GRS
**Resposta Correta:** C
**Explicação Técnica:** O Armazenamento Imutável para o Azure Blob Storage com retenção baseada em tempo no modo Compliance garante o modelo WORM (Write Once, Read Many), onde os dados não podem ser modificados nem excluídos nem mesmo por administradores globais até o término do período estipulado.

### Questão 404
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você está implantando uma aplicação contêinerizada leve que precisa ser executada rapidamente em segundo plano sob demanda, sem a necessidade de provisionar um cluster Kubernetes completo. Qual serviço é o mais adequado?
**Opções:**
- A) Azure Kubernetes Service (AKS)
- B) Azure Container Instances (ACI)
- C) Azure Virtual Machine Scale Sets (VMSS)
- D) Azure App Service Plan dedicado
**Resposta Correta:** B
**Explicação Técnica:** O Azure Container Instances (ACI) é a solução serverless mais rápida e simples para executar contêineres sob demanda no Azure sem gerenciar infraestrutura de cluster ou planos de nós.

### Questão 405
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Você precisa garantir que um administrador possa assumir a função de 'Administrador de Segurança' apenas quando necessário e por um período máximo de 4 horas, exigindo aprovação prévia. Qual recurso do Microsoft Entra ID atende a esse requisito?
**Opções:**
- A) Microsoft Entra Identity Protection
- B) Microsoft Entra Privileged Identity Management (PIM)
- C) Azure Policy
- D) Grupos de Gerenciamento
**Resposta Correta:** B
**Explicação Técnica:** O Microsoft Entra PIM permite acesso Just-In-Time (JIT) elegível para funções de privilégio elevado, impondo limites de tempo, fluxos de aprovação e autenticação multifator antes da ativação.

### Questão 406
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa precisa interceptar e inspecionar todo o tráfego de saída da Internet originado de VMs em uma sub-rede do Azure. Qual componente de rede deve ser configurado na Tabela de Roteamento (UDR)?
**Opções:**
- A) Rota Padrão (0.0.0.0/0) com Próximo Salto apontando para Virtual Appliance / Azure Firewall
- B) VNet Peering com gateway transit
- C) Grupo de Segurança de Rede (NSG) com regra Inbound Deny
- D) Azure Application Gateway WAF
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída da sub-rede através de um dispositivo de segurança (NVA ou Azure Firewall), define-se uma User-Defined Route (UDR) para 0.0.0.0/0 com o campo Next Hop configurado como Virtual Appliance ou IP Privado do Azure Firewall.

### Questão 407
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua equipe precisa sincronizar arquivos de um servidor local Windows Server com o Azure Files de forma contínua, utilizando o recurso de 'Cloud Tiering' para economizar espaço em disco local. Qual serviço do Azure possibilita essa arquitetura?
**Opções:**
- A) Azure Data Box
- B) AzCopy v10
- C) Azure File Sync
- D) Azure Storage Explorer
**Resposta Correta:** C
**Explicação Técnica:** O Azure File Sync permite centralizar os compartilhamentos de arquivos da sua empresa no Azure Files, mantendo a flexibilidade, o desempenho e a compatibilidade de um servidor de arquivos local. O Cloud Tiering mantém arquivos acessados frequentemente no servidor local enquanto move o restante para a nuvem.

### Questão 408
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um grupo de Máquinas Virtuais no Azure garantindo que, em caso de falha física em um rack de servidor ou atualização de hardware de um host, pelo menos uma instância permaneça online. Onde as VMs devem ser alocadas?
**Opções:**
- A) Em um mesmo Grupo de Recursos
- B) Em um Conjunto de Disponibilidade (Availability Set) configurado com Domínios de Falha e Atualização
- C) Em sub-redes diferentes da mesma VNet
- D) Em uma conta de armazenamento ZRS
**Resposta Correta:** B
**Explicação Técnica:** Um Conjunto de Disponibilidade (Availability Set) distribui as VMs entre múltiplos domínios de falha (Fault Domains) e domínios de atualização (Update Domains) no mesmo datacenter, garantindo resiliência contra falhas de hardware e manutenções agendadas.

### Questão 409
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Sua empresa deseja receber notificações instantâneas via SMS e acionar uma Azure Function sempre que a utilização de CPU de uma VM ultrapassar 90%. Qual combinação de recursos do Azure Monitor deve ser criada?
**Opções:**
- A) Regra de Alerta de Métrica e um Grupo de Ações (Action Group)
- B) Consulta KQL em Log Analytics Workspace
- C) Regra de Azure Policy com efeito DeployIfNotExists
- D) Alerta do Azure Service Health
**Resposta Correta:** A
**Explicação Técnica:** Uma Regra de Alerta de Métrica no Azure Monitor monitora o percentual de uso de CPU e, ao atingir o limite estipulado (90%), dispara um Grupo de Ações (Action Group) configurado com receptores SMS e Webhook/Azure Function.

### Questão 410
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Qual tipo de objeto do Microsoft Entra ID deve ser utilizado para delegar a administração de usuários e grupos de um departamento específico (ex.: Recursos Humanos) sem conceder permissões em toda a subscrição?
**Opções:**
- A) Grupo de Gerenciamento (Management Group)
- B) Unidade Administrativa (Administrative Unit)
- C) Grupo de Segurança Dinâmico
- D) Função Personalizada RBAC de Subscrição
**Resposta Correta:** B
**Explicação Técnica:** As Unidades Administrativas (Administrative Units - AU) no Microsoft Entra ID permitem delimitar permissões administrativas a um subconjunto de usuários, grupos ou dispositivos de uma organização.

### Questão 411
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa conectar com segurança duas Redes Virtuais (VNets) em regiões diferentes do Azure (ex.: East US e West Europe). As VMs devem se comunicar diretamente via IP privado sem passar pela Internet pública. Qual solução deve ser aplicada?
**Opções:**
- A) VPN Site-to-Site IPsec
- B) Peering de Rede Virtual Global (Global VNet Peering)
- C) Azure Application Gateway
- D) ExpressRoute Direct
**Resposta Correta:** B
**Explicação Técnica:** O Global VNet Peering conecta VNets em diferentes regiões do Azure através do backbone privado da Microsoft, proporcionando alta velocidade, baixa latência e tráfego totalmente criptografado na rede interna.

### Questão 412
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual ferramenta de linha de comando da Microsoft é otimizada para cópia e transferência de dados em massa de e para Contas de Armazenamento do Azure, suportando sincronização e retomada de downloads interrompidos?
**Opções:**
- A) Azure CLI (az vm create)
- B) AzCopy v10
- C) PowerShell Get-AzResource
- D) Robocopy nativo sem extensão
**Resposta Correta:** B
**Explicação Técnica:** O AzCopy v10 é o utilitário de linha de comando oficial de alta performance projetado para copiar blobs ou arquivos de/para uma conta de armazenamento do Azure com suporte a concorrência e resiliência a falhas.

### Questão 413
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Sua empresa precisa migrar uma máquina virtual local que utiliza um disco de 3 TB. Você precisa garantir que o disco virtual no Azure ofereça o menor tempo de resposta e capacidade de ajustar IOPS e throughput sob demanda sem reiniciar a VM. Qual tipo de disco deve ser selecionado?
**Opções:**
- A) Standard HDD
- B) Standard SSD
- C) Premium SSD v2 ou Ultra Disk
- D) Blob Storage de página
**Resposta Correta:** C
**Explicação Técnica:** Os discos Ultra Disk e Premium SSD v2 oferecem a capacidade de ajustar IOPS e throughput dinamicamente sem interromper a execução da VM, sendo ideais para cargas de trabalho de alto desempenho como bancos de dados transacionais.

### Questão 414
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar o backup automatizado de um conjunto de Máquinas Virtuais no Azure. Qual recurso centralizado deve ser provisionado para gerenciar as políticas de retenção e os pontos de recuperação de backup?
**Opções:**
- A) Log Analytics Workspace
- B) Cofre dos Serviços de Recuperação (Recovery Services Vault)
- C) Conta de Armazenamento com ZRS
- D) Azure Key Vault
**Resposta Correta:** B
**Explicação Técnica:** O Cofre dos Serviços de Recuperação (Recovery Services Vault) é o recurso do Azure Backup utilizado para armazenar dados de backup, pontos de restauração e gerenciar políticas de retenção para VMs e cargas de trabalho.

### Questão 415
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Qual recurso do Azure Policy deve ser utilizado quando você precisa agrupar várias definições de políticas relacionadas (ex.: conformidade com o padrão PCI-DSS) em um único conjunto de governança atribuível?
**Opções:**
- A) Função RBAC Customizada
- B) Iniciativa de Política (Policy Set Definition / Initiative)
- C) Grupo de Gerenciamento
- D) Trava de Recurso
**Resposta Correta:** B
**Explicação Técnica:** Uma Iniciativa de Política (Policy Initiative ou Policy Set) agrupa várias definições de política do Azure em uma única unidade lógica para simplificar a atribuição e o monitoramento de conformidade com padrões organizacionais.

### Questão 416
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual serviço do Azure atua como um Load Balancer de Camada 7 (HTTP/HTTPS) e inclui suporte a terminação TLS/SSL, afinidade de sessão baseada em cookie e Web Application Firewall (WAF)?
**Opções:**
- A) Azure Load Balancer Standard
- B) Azure Application Gateway
- C) Azure Traffic Manager
- D) Azure NAT Gateway
**Resposta Correta:** B
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego web (Camada 7) que oferece recursos avançados como roteamento baseado em URL, terminação SSL/TLS, afinidade de sessão e proteção WAF.

### Questão 417
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua empresa possui dados de auditoria arquivados no Blob Storage na camada Archive (Arquivo morto). O tempo de resposta para reidratação de urgência aceitável é de menos de 1 hora. Qual nível de prioridade de reidratação deve ser selecionado?
**Opções:**
- A) Prioridade Standard (Padrão)
- B) Prioridade High (Alta Prioridade / Expedited)
- C) Reidratação Automática em Tempo Real
- D) Leitura Direta sem Reidratação
**Resposta Correta:** B
**Explicação Técnica:** A prioridade de reidratação High (Alta) permite recuperar um blob da camada Archive para a camada Hot ou Cool em menos de 1 hora para blobs menores que 10 GB, enquanto a prioridade Standard pode levar até 15 horas.

### Questão 418
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você está provisionando uma aplicação Web no Azure App Service e deseja garantir zero tempo de inatividade (Zero Downtime) durante a implantação de novas versões do código. Qual recurso do App Service habilita essa capacidade?
**Opções:**
- A) Slots de Implantação (Deployment Slots)
- B) Auto Scaling Horizontal
- C) Integração com VNet
- D) Certificado SSL Gratuito
**Resposta Correta:** A
**Explicação Técnica:** Os Slots de Implantação (Deployment Slots) são ambientes de homologação vinculados ao App Service que permitem testar alterações e realizar a troca (Swap) imediata com o slot de produção sem queda no serviço.

### Questão 419
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual agente do Azure Monitor deve ser instalado em máquinas virtuais Windows e Linux para coletar métricas de desempenho detalhadas, logs do sistema operacional e enviar os dados para regras de coleta DCR?
**Opções:**
- A) Agente Log Analytics legado (MMA)
- B) Agente do Azure Monitor (Azure Monitor Agent - AMA)
- C) Network Watcher Agent
- D) Azure Diagnostics Extension apenas
**Resposta Correta:** B
**Explicação Técnica:** O Azure Monitor Agent (AMA) substitui os agentes legados e consolida a coleta de logs e métricas do sistema operacional usando Regras de Coleta de Dados (Data Collection Rules - DCR).

### Questão 420
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Você precisa conceder acesso a um desenvolvedor para gerenciar apenas os recursos dentro de um Grupo de Recursos de teste específico, impedindo que ele visualize ou altere recursos em outros grupos da subscrição. Onde a função RBAC deve ser atribuída?
**Opções:**
- A) No Grupo de Gerenciamento raiz
- B) No escopo da Subscrição
- C) No escopo do Grupo de Recursos específico
- D) No perfil de usuário do Entra ID
**Resposta Correta:** C
**Explicação Técnica:** As atribuições de Controle de Acesso Baseado em Função (RBAC) seguem o princípio do menor privilégio e herança. Atribuir a função no escopo do Grupo de Recursos específico limita as permissões do usuário apenas àquele contêiner.

### Questão 421
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual ferramenta do Network Watcher permite testar e verificar se uma regra de Grupo de Segurança de Rede (NSG) está bloqueando ou permitindo o tráfego IP de/para uma máquina virtual específica?
**Opções:**
- A) Network Performance Monitor
- B) IP Flow Verify
- C) Connection Troubleshoot
- D) Packet Capture
**Resposta Correta:** B
**Explicação Técnica:** O IP Flow Verify do Azure Network Watcher analisa os pacotes de rede com base em 5 tuplas (origem, destino, porta de origem, porta de destino e protocolo) e indica qual regra de NSG permitiu ou bloqueou o tráfego.

### Questão 422
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua empresa precisa transferir 150 TB de dados de um datacenter local para o Azure Blob Storage, mas a conexão de Internet local é limitada a 10 Mbps. Qual é o método mais eficiente e rápido para essa transferência?
**Opções:**
- A) Envio contínuo via AzCopy v10
- B) Solicitar um dispositivo físico Azure Data Box
- C) Sincronização via Azure File Sync
- D) Upload direto pelo Portal do Azure
**Resposta Correta:** B
**Explicação Técnica:** O Azure Data Box é um dispositivo físico fornecido pela Microsoft para transporte offline de grandes volumes de dados (acima de 40 TB) quando a largura de banda de rede é insuficiente.

### Questão 423
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa executar uma aplicação contêinerizada em um cluster Kubernetes gerenciado no Azure. Qual serviço elimina a necessidade de gerenciar o plano de controle (Control Plane / Master Nodes) do Kubernetes?
**Opções:**
- A) Azure Container Instances (ACI)
- B) Azure Kubernetes Service (AKS)
- C) Azure Virtual Machines
- D) Red Hat OpenShift no Azure
**Resposta Correta:** B
**Explicação Técnica:** O Azure Kubernetes Service (AKS) é o serviço Kubernetes totalmente gerenciado da Microsoft, no qual o Azure gerencia gratuitamente o plano de controle (Control Plane), ficando o usuário responsável apenas pela administração dos nós de trabalho (Worker Nodes).

### Questão 424
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual serviço do Azure coleta e consolida logs do plano de controle e das operações de gerenciamento realizadas em recursos do Azure (como criação de VMs, alteração de NSG e exclusão de Storage Accounts)?
**Opções:**
- A) Azure Activity Log
- B) Application Insights
- C) Azure Service Health
- D) Network Watcher Flow Logs
**Resposta Correta:** A
**Explicação Técnica:** O Azure Activity Log registra todas as operações realizadas na camada de gerenciamento (Resource Manager / ARM) da sua subscrição, permitindo determinar 'quem', 'o quê' e 'quando' uma ação de controle foi executada.

### Questão 425
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Sua organização deseja impor uma regra onde nenhuma nova máquina virtual possa ser implantada sem que a tag 'Environment' esteja configurada com um valor válido. Qual recurso garante que a criação seja bloqueada se a tag não for fornecida?
**Opções:**
- A) Azure Policy com efeito 'Deny'
- B) Trava de Recurso (Resource Lock)
- C) Regra de Alerta do Azure Monitor
- D) Controle de Acesso RBAC
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy com o efeito 'Deny' impede que solicitações de criação ou atualização de recursos sejam concluídas se não atenderem aos critérios definidos na política, como a presença obrigatória de uma tag especificada.

### Questão 426
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa estabelecer uma conexão privada altamente segura entre os servidores locais da sua empresa e a infraestrutura do Azure com largura de banda garantida de até 10 Gbps e bypass completo da Internet pública. Qual serviço atende a essa exigência?
**Opções:**
- A) VPN Site-to-Site IPsec
- B) Azure ExpressRoute
- C) Azure Application Gateway
- D) VNet Peering
**Resposta Correta:** B
**Explicação Técnica:** O Azure ExpressRoute cria conexões privadas dedicadas entre datacenters locais e a nuvem da Microsoft através de provedores de conectividade, oferecendo maior confiabilidade, velocidades mais altas, menor latência e segurança reforçada sem trafegar pela Internet.

### Questão 427
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual opção de redundância de Armazenamento do Azure replica síncronamente três cópias dos seus dados dentro de três Zonas de Disponibilidade separadas na mesma região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância Geográfica Somente Leitura (RA-GRS)
**Resposta Correta:** B
**Explicação Técnica:** O Armazenamento com Redundância de Zona (ZRS) replica síncronamente os dados em três Zonas de Disponibilidade dentro da região primária, protegendo contra falhas físicas em datacenters individuais.

### Questão 428
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa automatizar o provisionamento idempotente de um ambiente complexo com 50 VMs, redes virtuais e bancos de dados usando linguagem declarativa nativa do Azure com sintaxe limpa e suporte a autocompletar. Qual tecnologia deve ser utilizada?
**Opções:**
- A) Azure CLI em scripts Bash
- B) Arquivos JSON ARM Templates
- C) Azure Bicep
- D) Azure Automation PowerShell
**Resposta Correta:** C
**Explicação Técnica:** O Azure Bicep é a linguagem declarativa de última geração desenvolvida pela Microsoft para implantar recursos no Azure como código (IaC), oferecendo sintaxe mais concisa e simples em comparação aos modelos JSON ARM Templates.

### Questão 429
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa visualizar graficamente o mapa de conexões de rede ativas e processos em execução que se comunicam entre suas Máquinas Virtuais no Azure. Qual recurso do Azure Monitor deve ser ativado?
**Opções:**
- A) VM Insights (com o recurso Map habilitado)
- B) Application Insights
- C) Azure Activity Log
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** O recurso Map do VM Insights coleta automaticamente dados sobre processos em execução, conexões de entrada e saída de rede nas suas VMs Windows e Linux, gerando um mapa visual interativo da arquitetura em tempo real.

### Questão 430
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Qual é a função do recurso 'Identidade Gerenciada' (Managed Identity) no Microsoft Entra ID quando atribuído a uma Máquina Virtual do Azure?
**Opções:**
- A) Permitir que administradores façam login na VM via MFA
- B) Fornecer uma identidade no Entra ID para a aplicação na VM autenticar-se em serviços como Key Vault sem armazenar credenciais no código
- C) Criptografar automaticamente o disco do sistema operacional
- D) Gerenciar atualizações do Windows Update automaticamente
**Resposta Correta:** B
**Explicação Técnica:** As Identidades Gerenciadas (Managed Identities) fornecem aos aplicativos uma identidade gerenciada automaticamente no Microsoft Entra ID. As aplicações podem usar a identidade para se conectar a recursos que suportam autenticação Entra ID sem guardar segredos ou senhas em arquivos de configuração.

### Questão 431
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa precisa permitir que funcionários remotos conectados de seus laptops pessoais acessem com segurança os recursos de uma VNet privada no Azure. Qual tipo de solução VPN deve ser configurada no Azure VPN Gateway?
**Opções:**
- A) VPN Site-to-Site (S2S)
- B) VPN Ponto a Site (Point-to-Site - P2S)
- C) VNet Peering Global
- D) Azure ExpressRoute
**Resposta Correta:** B
**Explicação Técnica:** A VPN Ponto a Site (Point-to-Site - P2S) permite criar uma conexão criptografada segura entre um computador cliente individual remoto e a Rede Virtual do Azure.

### Questão 432
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa conceder acesso temporário e restrito a um arquivo específico no Azure Blob Storage para um parceiro externo por 2 horas, limitando as permissões apenas para leitura. Qual mecanismo deve ser gerado?
**Opções:**
- A) Chave de Acesso da Conta de Armazenamento (Account Key 1)
- B) Assinatura de Acesso Compartilhado de Serviço (Service SAS) com data de expiração e permissão Read
- C) Função RBAC de Proprietário no Grupo de Recursos
- D) Política de Acesso Público no Contêiner
**Resposta Correta:** B
**Explicação Técnica:** Uma Assinatura de Acesso Compartilhado (SAS) concede acesso delegado e seguro aos recursos da sua conta de armazenamento com controle granular de tempo de expiração, intervalo de IPs permitidos e permissões mínimas necessárias.

### Questão 433
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Sua equipe deseja executar comandos de configuração ou scripts PowerShell diretamente dentro de uma VM Windows no Azure sem precisar abrir uma sessão RDP ou ter IP público. Qual extensão deve ser executada?
**Opções:**
- A) Custom Script Extension ou Run Command
- B) VMAccess Extension
- C) Azure Monitor Agent Extension
- D) Network Watcher Agent
**Resposta Correta:** A
**Explicação Técnica:** O recurso Run Command ou a extensão Custom Script Extension permitem executar scripts dentro de máquinas virtuais do Azure utilizando o agente de VM nativo, sem necessidade de conectividade RDP/SSH direta.

### Questão 434
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa ser informado com antecedência sobre interrupções planejadas de serviço pela Microsoft e problemas conhecidos na infraestrutura global do Azure que afetem diretamente os seus recursos ativas na região East US. Onde essas informações são centralizadas?
**Opções:**
- A) Azure Status público
- B) Azure Service Health
- C) Azure Advisor
- D) Azure Monitor Metrics
**Resposta Correta:** B
**Explicação Técnica:** O Azure Service Health fornece um painel personalizado que informa sobre a saúde dos seus recursos específicos do Azure, incidentes de serviço ativos, manutenções planejadas e avisos de integridade.

### Questão 435
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Você deseja impedir que uma máquina virtual crítica seja excluída por engano por qualquer administrador, permitindo ainda que ela seja modificada e reiniciada. Qual Trava de Recurso (Resource Lock) deve ser aplicada?
**Opções:**
- A) ReadOnly
- B) CanNotDelete (Delete)
- C) WriteLock
- D) ServiceLock
**Resposta Correta:** B
**Explicação Técnica:** A trava de recurso CanNotDelete (ou Delete) permite que usuários autorizados leiam e modifiquem os recursos do Azure, mas impede categoricamente que o recurso seja excluído.

### Questão 436
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual componente do Azure permite conectar instâncias em uma VNet diretamente a serviços PaaS do Azure (como Azure Storage ou Azure SQL) via IP Privado interno, isolando totalmente o tráfego da Internet?
**Opções:**
- A) Private Endpoint (Azure Private Link)
- B) Service Endpoint apenas
- C) Azure Public Load Balancer
- D) NAT Gateway
**Resposta Correta:** A
**Explicação Técnica:** Um Private Endpoint é uma interface de rede que usa um endereço IP privado da sua VNet para conectar você com segurança e privacidade a um serviço alimentado pelo Azure Private Link.

### Questão 437
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua empresa possui um compartilhamento de arquivos no Azure Files e precisa restaurar arquivos excluídos por engano nas últimas 24 horas. Qual recurso nativo do Azure Files permite tirar instantâneos pontuais do compartilhamento?
**Opções:**
- A) Snapshots do Compartilhamento de Arquivos (Share Snapshots)
- B) Cópia Geográfica síncrona
- C) AzCopy Sync
- D) Azure Disk Encryption
**Resposta Correta:** A
**Explicação Técnica:** Os Snapshots do Compartilhamento de Arquivos (Share Snapshots) fornecem cópias de trechos em tempo leitura somente de compartilhamentos do Azure Files, permitindo a recuperação rápida de arquivos de versões anteriores.

### Questão 438
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa configurar uma aplicação web no Azure App Service para que ela aumente automaticamente o número de instâncias (Scale Out) quando o consumo médio de memória ultrapassar 80%. Qual tipo de escalonamento deve ser configurado?
**Opções:**
- A) Escalonamento Vertical (Scale Up)
- B) Escalonamento Horizontal Automático (Autoscale baseado em regras de métrica)
- C) Escalonamento Manual de slots
- D) Balanceamento de carga estático
**Resposta Correta:** B
**Explicação Técnica:** O Escalonamento Horizontal Automático (Autoscale) ajusta dinamicamente o número de instâncias de execução do App Service ou VMSS com base em regras de métricas predefinidas (como CPU ou memória).

### Questão 439
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Em uma consulta Log Analytics KQL, qual operador é utilizado para filtrar os resultados retornados com base em uma condição lógica (ex.: extrair apenas registros onde o código de status seja 500)?
**Opções:**
- A) project
- B) where
- C) summarize
- D) render
**Resposta Correta:** B
**Explicação Técnica:** No Kusto Query Language (KQL), o operador 'where' filtra uma tabela para o subconjunto de linhas que atendem a um determinado predicado ou condição lógica.

### Questão 440
**Domínio:** Identidades e Governança no Azure
**Enunciado:** Sua empresa gerencia 20 subscrições do Azure e deseja garantir que uma política de segurança corporativa seja aplicada de maneira centralizada e uniforme a todas elas. Em qual nível da hierarquia o Azure Policy deve ser atribuído?
**Opções:**
- A) Em cada Grupo de Recursos individualmente
- B) No nível do Grupo de Gerenciamento (Management Group) pai que contém todas as subscrições
- C) No nível de cada recurso individual
- D) No Microsoft Entra ID Domain Service
**Resposta Correta:** B
**Explicação Técnica:** Atribuir políticas e permissões no nível de um Grupo de Gerenciamento (Management Group) garante que as definições de governança sejam herdadas automaticamente por todas as subscrições contidas dentro daquele grupo.

