# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 7 (Questões 301 a 350)

Esta base de conhecimento contém as questões 301 a 350 do exame **AZ-104: Microsoft Azure Administrator** formatadas para ingestão e automação no Antigravity.

---

### Questão 301
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Sua empresa possui uma sub-rede contendo dez máquinas virtuais e uma instância de Azure Firewall. Você precisa garantir que todo o tráfego de saída da sub-rede com destino à Internet seja roteado exclusivamente através da instância do Azure Firewall. O que você deve configurar?
**Opções:**
- A) Uma regra de Grupo de Segurança de Rede (NSG) de saída com prioridade 100
- B) Uma Tabela de Rotas (Route Table) com uma Rota Definida pelo Usuário (UDR) para 0.0.0.0/0 direcionada ao Virtual Appliance (Azure Firewall)
- C) Uma conexão de Peering de Rede Virtual (VNet Peering) com a opção Gateway Transit habilitada
- D) Um Ponto de Extremidade Privado (Private Endpoint) associado à sub-rede
**Resposta Correta:** B
**Explicação Técnica:** Para forçar o tráfego de saída de uma sub-rede a passar por um firewall ou Virtual Network Appliance (NVA), cria-se uma Tabela de Rotas (Route Table) contendo uma Rota Definida pelo Usuário (UDR) para o destino `0.0.0.0/0` com o próximo salto (*next hop*) configurado como *Virtual Appliance* e o endereço IP privado do Azure Firewall.

### Questão 302
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa garantir que todos os dados armazenados em uma Conta de Armazenamento do Azure sejam criptografados utilizando chaves gerenciadas pelo próprio cliente (Customer-Managed Keys - CMK) armazenadas no Azure Key Vault. O que deve ser configurado no Key Vault antes de associar a chave à Conta de Armazenamento?
**Opções:**
- A) Habilitar o Soft Delete e a Proteção contra Purga (Purge Protection) no Key Vault
- B) Configurar um Ponto de Extremidade de Serviço (Service Endpoint) para a sub-rede da Conta de Armazenamento
- C) Alterar o nível de preços do Key Vault para Premium
- D) Criar um contrato de SLA estendido no portal do Azure
**Resposta Correta:** A
**Explicação Técnica:** Para utilizar Chaves Gerenciadas pelo Cliente (CMK) no Azure Key Vault para criptografia do Azure Storage, é requisito obrigatório que o Key Vault tenha habilitadas as propriedades de *Soft Delete* e *Purge Protection* para evitar a perda irrevogável das chaves de criptografia.

### Questão 303
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma aplicação Web hospedada em um Conjunto de Escalonamento de Máquinas Virtuais (VMSS) necessita acessar um banco de dados Azure SQL sem armazenar credenciais ou cadeias de conexão em código fonte ou arquivos de configuração. Qual recurso deve ser configurado na VMSS?
**Opções:**
- A) Uma Identidade Gerenciada atribuída pelo sistema ou pelo usuário (Managed Identity)
- B) Uma chave SAS com permissões de leitura e gravação
- C) Um Ponto de Extremidade de Serviço (Service Endpoint)
- D) Uma regra de entrada de NSG permitindo a porta 1433
**Resposta Correta:** A
**Explicação Técnica:** As Identidades Gerenciadas (Managed Identities) para recursos do Azure fornecem ao recurso uma identidade gerada automaticamente no Microsoft Entra ID. As aplicações podem usar a identidade para obter tokens de acesso sem a necessidade de armazenar credenciais no código.

### Questão 304
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador precisa conceder a um grupo de analistas permissão para reiniciar e parar máquinas virtuais em um Grupo de Recursos específico, impedindo qualquer modificação em configurações de rede ou disco. Qual função de Controle de Acesso Baseado em Função (RBAC) deve ser atribuída?
**Opções:**
- A) Colaborador (Contributor)
- B) Colaborador de Máquina Virtual (Virtual Machine Contributor)
- C) Operador de Máquina Virtual (Virtual Machine Operator)
- D) Leitor (Reader)
**Resposta Correta:** B
**Explicação Técnica:** A função nativa *Virtual Machine Contributor* permite gerenciar máquinas virtuais (incluindo ligar, desligar e reiniciar), mas não concede acesso para alterar a rede virtual ou a conta de armazenamento associada, respeitando a separação de deveres.

### Questão 305
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar o envio automático de alertas via SMS e e-mail para a equipe de infraestrutura sempre que a utilização média de CPU de qualquer máquina virtual de um grupo ultrapassar 85% por mais de 10 minutos. Qual recurso do Azure Monitor coordena os canais de notificação?
**Opções:**
- A) Regra de Coleta de Dados (Data Collection Rule - DCR)
- B) Grupo de Ação (Action Group)
- C) Log Analytics Workspace
- D) Alerta do Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** Os Grupos de Ação (Action Groups) no Azure Monitor definem uma lista de preferências de notificação (e-mail, SMS, notificação push no aplicativo do Azure, chamadas de voz) e ações automatizadas (Runbooks, Azure Functions, Webhooks) acionadas por regras de alerta.

### Questão 306
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa possui duas Redes Virtuais: VNet1 (10.1.0.0/16) localizada na região East US e VNet2 (10.2.0.0/16) na região West Europe. Você configura o Peering de Rede Virtual Global (Global VNet Peering) entre VNet1 e VNet2. Quais tipos de recursos podem se comunicar através dessa conexão privada?
**Opções:**
- A) Apenas máquinas virtuais da mesma zona de disponibilidade
- B) Qualquer recurso com endereço IP privado válido em VNet1 e VNet2 sem passar pela Internet pública
- C) Apenas recursos da camada PaaS que possuem IP público
- D) Apenas instâncias do Azure Kubernetes Service (AKS)
**Resposta Correta:** B
**Explicação Técnica:** O Peering de Rede Virtual Global conecta VNets entre diferentes regiões do Azure. O tráfego flui diretamente através da rede backbone privada da Microsoft, permitindo comunicação de baixíssima latência entre recursos com IPs privados nas duas redes.

### Questão 307
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa transferir 45 TB de dados históricos de um servidor de arquivos local para uma Conta de Armazenamento do Azure Blob. A conexão de Internet local possui uma largura de banda restrita de apenas 10 Mbps. Qual é o método mais eficiente e rápido para realizar essa migração?
**Opções:**
- A) Executar o utilitário AzCopy via linha de comando
- B) Solicitante e utilizar o dispositivo físico Azure Data Box
- C) Configurar o Azure File Sync com Cloud Tiering
- D) Usar o Azure Storage Explorer com transferência em lote
**Resposta Correta:** B
**Explicação Técnica:** Para grandes volumes de dados (dezenas de Terabytes) e conexões de Internet lentas ou limitadas, o *Azure Data Box* é o dispositivo físico seguro enviado pela Microsoft para cópia local rápida e envio posterior ao data center do Azure.

### Questão 308
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Um administrador precisa atualizar o sistema operacional de uma máquina virtual crítica sem alterar seu endereço IP privado estático nem perder a configuração de sub-rede associada. Qual é o procedimento adequado para a interface de rede (NIC)?
**Opções:**
- A) Excluir a NIC e criar uma nova na mesma sub-rede
- B) Desassociar a NIC da VM, recriar a VM a partir do disco atualizado e reassociar a NIC existente
- C) Alterar a alocação de IP na NIC de Estática para Dinâmica antes da atualização
- D) Mover a NIC para uma nova VNet temporária
**Resposta Correta:** B
**Explicação Técnica:** As interfaces de rede (NICs) no Azure são recursos independentes. É possível desassociar uma NIC de uma VM e associá-la a outra VM (ou recriar a VM a partir do disco mantendo a NIC), preservando o endereço IP privado, configurações de IP e associações de NSG.

### Questão 309
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma corporação deseja aplicar o princípio do menor privilégio para concessões de acesso temporárias. Os administradores devem solicitar permissões de Administrador Global ou de Colaborador apenas quando necessário, por um período máximo de 4 horas com aprovação prévia. Qual recurso do Microsoft Entra ID atende ao requisito?
**Opções:**
- A) Unidades Administrativas (AU)
- B) Microsoft Entra Privileged Identity Management (PIM)
- C) Políticas de Acesso Condicional
- D) Controle de Acesso Baseado em Função (RBAC) estático
**Resposta Correta:** B
**Explicação Técnica:** O Microsoft Entra PIM (Privileged Identity Management) permite gerenciar, controlar e monitorar o acesso a recursos críticos. Ele oferece concessão Just-In-Time (JIT), expiração baseada em tempo, fluxos de aprovação e auditoria de elevação de privilégios.

### Questão 310
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa consultar logs de auditoria e métricas de desempenho de várias máquinas virtuais armazenadas em um Log Analytics Workspace. Qual linguagem de consulta padrão do Azure deve ser utilizada?
**Opções:**
- A) SQL (Structured Query Language)
- B) KQL (Kusto Query Language)
- C) JSONPath
- D) PowerShell Scripting
**Resposta Correta:** B
**Explicação Técnica:** A linguagem KQL (Kusto Query Language) é a linguagem de consulta somente leitura utilizada para analisar grandes volumes de dados no Azure Log Analytics, Azure Data Explorer, Application Insights e Microsoft Sentinel.

### Questão 311
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa possui uma sub-rede contendo servidores Web que precisam receber tráfego HTTP/HTTPS distribuído com suporte a encerramento SSL, afinidade de sessão baseada em cookie e inspeção WAF contra ataques de SQL Injection. Qual serviço de balanceamento de carga deve ser implantado?
**Opções:**
- A) Azure Load Balancer Standard (Camada 4)
- B) Azure Application Gateway com WAF (Camada 7)
- C) Azure Traffic Manager
- D) Azure Network Watcher
**Resposta Correta:** B
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego web de Camada 7 que inclui roteamento baseado em URL, encerramento TLS/SSL, afinidade de sessão por cookie e proteção WAF (Web Application Firewall) contra vulnerabilidades OWASP.

### Questão 312
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você deseja configurar uma regra de Gerenciamento do Ciclo de Vida (Lifecycle Management) em um Azure Blob Storage. A regra deve mover arquivos que não foram modificados há mais de 30 dias para o nível Frio (Cool) e arquivos não modificados há mais de 180 dias para o nível de Arquivamento (Archive). Qual tipo de dado suporta essa automação?
**Opções:**
- A) Blobs de Bloco (Block Blobs)
- B) Discos Gerenciados (Managed Disks)
- C) Tabelas do Azure Table Storage
- D) Filas do Azure Queue Storage
**Resposta Correta:** A
**Explicação Técnica:** As políticas de Gerenciamento de Ciclo de Vida do Azure Storage aplicam-se a Blobs de Bloco (Block Blobs) e Blobs de Anexo (Append Blobs) em contas de armazenamento de uso geral v2 (General Purpose v2) e Blob Storage.

### Questão 313
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma aplicação baseada em contêiner Docker precisa ser executada de forma isolada, sem a necessidade de provisionar máquinas virtuais subjacentes ou orquestrar um cluster Kubernetes completo. Qual serviço do Azure oferece essa capacidade serverless?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Serviço de Kubernetes do Azure (AKS)
- C) Conjunto de Escalonamento de Máquinas Virtuais (VMSS)
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Instances (ACI) é a solução serverless mais rápida e simples para executar contêineres no Azure sem a necessidade de gerenciar máquinas virtuais ou adotar orquestradores complexos.

### Questão 314
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma organização necessita impedir que qualquer usuário (incluindo administradores de subscrição) exclua um Grupo de Recursos contendo bancos de dados de produção. Qual recurso de governança deve ser aplicado?
**Opções:**
- A) Bloqueio de Recurso do tipo CanNotDelete (Delete Lock)
- B) Bloqueio de Recurso do tipo ReadOnly
- C) Azure Policy com efeito Deny
- D) Regra de NSG bloqueando a porta 443
**Resposta Correta:** A
**Explicação Técnica:** O Bloqueio de Recurso (Resource Lock) do tipo *CanNotDelete* permite que usuários autorizados leiam e modifiquem os recursos, mas os impede de excluir o recurso ou o grupo de recursos até que o bloqueio seja removido.

### Questão 315
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa restaurar uma máquina virtual do Azure que foi acidentalmente corrompida. O backup mais recente está armazenado em um Cofre dos Serviços de Recuperação (Recovery Services Vault). Quais são as duas opções de restauração oferecidas pelo serviço? (Escolha duas opções)
**Opções:**
- A) Criar uma nova Máquina Virtual a partir do ponto de restauração
- B) Restaurar os discos da VM e criar uma VM manualmente via modelo ARM/Bicep
- C) Converter o backup diretamente em uma conta do AWS S3
- D) Substituir automaticamente o sistema operacional de máquinas virtuais locais no Hyper-V
- E) Exportar a imagem para um contêiner ACI imediatamente sem disco
**Resposta Correta:** A, B
**Explicação Técnica:** Ao restaurar uma VM do Azure pelo Recovery Services Vault, é possível optar por: (1) Criar uma nova VM diretamente com os parâmetros configurados no backup, ou (2) Restaurar os discos gerenciados (VHDs) para que o administrador os anexe a uma VM existente ou monte uma nova via ARM/Bicep/PowerShell.

### Questão 316
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa permitir que máquinas virtuais em uma sub-rede privada acessem com segurança um banco de dados Azure SQL utilizando o endereço IP privado do banco dentro da sub-rede, eliminando o acesso via IP público. Qual tecnologia deve ser adotada?
**Opções:**
- A) Ponto de Extremidade Privado (Private Endpoint / Azure Private Link)
- B) Ponto de Extremidade de Serviço (Service Endpoint)
- C) Azure ExpressRoute Direct
- D) NAT Gateway
**Resposta Correta:** A
**Explicação Técnica:** O Private Endpoint utiliza uma interface de rede privada (NIC) na sua sub-rede para conectar de forma privada e segura a serviços PaaS do Azure (como Azure SQL, Storage, Cosmos DB) via Azure Private Link, atribuindo um IP privado interno da VNet ao serviço.

### Questão 317
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa exige que os dados gravados em um contêiner de Blob Storage permaneçam inalteráveis e protegidos contra exclusão ou sobrescrita durante um período de retenção legal obrigatório de 5 anos (WORM - Write Once, Read Many). Qual recurso deve ser habilitado?
**Opções:**
- A) Armazenamento Imutável de Blobs com Política de Retenção Baseada no Tempo (Time-Based Retention Policy)
- B) Replicação de Armazenamento com Redundância Geo-Zonal (GZRS)
- C) Soft Delete para Contêineres
- D) Criptografia AES-256 no nível de disco
**Resposta Correta:** A
**Explicação Técnica:** O Armazenamento Imutável para o Azure Blob Storage permite que os dados sejam armazenados no formato WORM (Write Once, Read Many). Quando uma política baseada em tempo é bloqueada, os blobs podem ser criados e lidos, mas não modificados ou excluídos até o término do período estipulado.

### Questão 318
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um aplicativo web em um Plano do Serviço de Aplicativo do Azure (Azure App Service Plan). O aplicativo precisa suportar domínio personalizado, certificado SSL próprio e ter a capacidade de alternar entre ambientes de Preparação (Staging) e Produção sem tempo de inatividade. Qual nível de preço mínimo é necessário?
**Opções:**
- A) Gratuito (F1 - Free)
- B) Compartilhado (D1 - Shared)
- C) Padrão (S1 - Standard)
- D) Básico (B1 - Basic)
**Resposta Correta:** C
**Explicação Técnica:** Os slots de implantação (*Deployment Slots*), como o ambiente de Staging para troca (*swap*) sem downtime, estão disponíveis a partir do nível de preço **Padrão (Standard - S1)** do App Service. O nível Básico suporta domínios personalizados e SSL, mas não suporta slots.

### Questão 319
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa possui três subscrições do Azure e deseja garantir que todas sigam os mesmos padrões de conformidade e definições de segurança centralizadas. O administrador deseja aplicar políticas sobre o conjunto de subscrições de uma só vez. Onde essas políticas devem ser atribuídas?
**Opções:**
- A) Em um Grupo de Gerenciamento (Management Group) pai das subscrições
- B) No nível do Grupo de Recursos de cada subscrição separadamente
- C) No portal do Microsoft Entra ID como uma função do aplicativo
- D) Dentro de cada máquina virtual via script do PowerShell
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento (Management Groups) fornecem um escopo de governança acima das assinaturas do Azure. Ao atribuir Azure Policies ou controles RBAC em um Grupo de Gerenciamento, as configurações são herdadas automaticamente por todas as assinaturas contidas nele.

### Questão 320
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual ferramenta do Azure Network Watcher permite diagnosticar se o tráfego entre duas máquinas virtuais em sub-redes distintas está sendo bloqueado por uma regra de Grupo de Segurança de Rede (NSG)?
**Opções:**
- A) Verificação de Fluxo de IP (IP Flow Verify)
- B) Diagnóstico de Roteamento (Next Hop)
- C) Captura de Pacotes (Packet Capture)
- D) Exibição de Topologia (Topology)
**Resposta Correta:** A
**Explicação Técnica:** A ferramenta *IP Flow Verify* do Azure Network Watcher verifica se um pacote de dados é permitido ou negado para ou de uma VM com base nas regras ativas de NSG de entrada ou saída, informando a regra exata responsável pelo bloqueio.

### Questão 321
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa integrar a resolução de nomes de domínio privados da sua rede local (on-premises) com os nomes de domínio das Redes Virtuais do Azure. Qual serviço do Azure gerencia zonas DNS privadas e resolução em duas vias?
**Opções:**
- A) Zonas DNS Privadas do Azure (Azure Private DNS Zones) com Azure DNS Private Resolver
- B) Azure Front Door Private Links
- C) Azure Traffic Manager
- D) Servidor WINS no Active Directory
**Resposta Correta:** A
**Explicação Técnica:** O *Azure Private DNS Resolver* permite consultar e resolver zonas DNS Privadas do Azure a partir do ambiente local (on-premises) e vice-versa, sem a necessidade de implantar servidores DNS IaaS dedicados baseados em máquinas virtuais.

### Questão 322
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Um administrador precisa sincronizar o conteúdo de um servidor de arquivos Windows Server local com um Compartilhamento de Arquivos do Azure (Azure File Share). Qual recurso de armazenamento híbrido deve ser configurado?
**Opções:**
- A) Azure File Sync
- B) AzCopy v10 com Agendador de Tarefas
- C) Importação/Exportação do Azure
- D) Azure Data Factory
**Resposta Correta:** A
**Explicação Técnica:** O *Azure File Sync* permite centralizar os compartilhamentos de arquivos da sua organização no Azure Files, mantendo a flexibilidade, o desempenho e a compatibilidade de um servidor de arquivos Windows local (com suporte a Cloud Tiering).

### Questão 323
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você cria uma máquina virtual no Azure e precisa executar um script PowerShell de pós-implantação para instalar a função de Servidor Web (IIS) sem efetuar login remoto via RDP. Qual recurso deve ser utilizado?
**Opções:**
- A) Extensão de Script Personalizado (Custom Script Extension)
- B) Azure Bastion
- C) Console Serial
- D) Regra de entrada no NSG para a porta 5985
**Resposta Correta:** A
**Explicação Técnica:** A *Custom Script Extension* do Azure permite baixar e executar scripts em máquinas virtuais do Azure sem a necessidade de fazer login na VM via RDP/SSH. É ideal para automação de configuração pós-implantação e instalação de softwares.

### Questão 324
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual ferramenta de Governança como Código (IaC) nativa e declarativa da Microsoft simplifica a sintaxe para criação e implantação de recursos no Azure em comparação aos modelos JSON tradicionais do ARM?
**Opções:**
- A) Azure Bicep
- B) Terraform
- C) Ansible
- D) PowerShell Desired State Configuration (DSC)
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bicep é uma linguagem de domínio específico (DSL) declarativa desenvolvida pela Microsoft que utiliza sintaxe limpa e legível para implantar recursos no Azure de forma transparente sobre o mecanismo do Azure Resource Manager (ARM).

### Questão 325
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa coletar eventos de log de segurança do sistema operacional e métricas de desempenho de alta frequência de 50 máquinas virtuais executando Windows e Linux. Qual agente moderno unificado do Azure Monitor deve ser instalado nas VMs?
**Opções:**
- A) Agente do Azure Monitor (Azure Monitor Agent - AMA) com Regras de Coleta de Dados (DCR)
- B) Agente Log Analytics legado (MMA / OMS)
- C) Agente de Diagnóstico do Azure (WAD)
- D) Agente do Dependency Agent isolado
**Resposta Correta:** A
**Explicação Técnica:** O Agente do Azure Monitor (AMA) substitui os agentes legados (Log Analytics / MMA / WAD) e utiliza as Regras de Coleta de Dados (DCR - Data Collection Rules) para definir de forma simplificada e centralizada quais dados devem ser coletados e para onde devem ser enviados.

### Questão 326
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma máquina virtual na VNetA precisa enviar tráfego para a VNetB. O Peering entre VNetA e VNetB está configurado com o status "Connected". No entanto, os pings entre as VMs falham. Qual é a causa mais provável para a falha do ICMP?
**Opções:**
- A) O firewall do sistema operacional (Windows Firewall / iptables) ou o NSG está bloqueando o tráfego ICMP de entrada
- B) O VNet Peering não suporta tráfego privado entre VMs
- C) É necessário reiniciar as duas máquinas virtuais após configurar o Peering
- D) O Peering exige a compra de um circuito ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O VNet Peering fornece conectividade total de rede privada L3. Falhas em testes de ping (ICMP) ocorrem frequentemente devido a bloqueios no firewall do sistema operacional convidado da VM ou por regras do Grupo de Segurança de Rede (NSG) que negam o tráfego ICMP.

### Questão 327
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa conceder acesso temporário e delimitado a um arquivo específico contido em uma Conta de Armazenamento a um cliente externo por um período de 2 horas. O acesso deve ser estritamente de leitura sem expor a chave primária da conta. O que deve ser gerado?
**Opções:**
- A) Uma Assinatura de Acesso Compartilhado (Shared Access Signature - SAS) no nível de Serviço ou Objeto
- B) Uma nova Chave de Acesso Primária
- C) Uma regra de firewall para o IP do cliente no Key Vault
- D) Uma politica de RBAC atribuindo o papel de Proprietário
**Resposta Correta:** A
**Explicação Técnica:** As Assinaturas de Acesso Compartilhado (SAS) fornecem acesso delegado seguro a recursos na sua conta de armazenamento com controle granular sobre o tipo de recurso, permissões (leitura, gravação, exclusão), intervalo de IP permitido e tempo de expiração.

### Questão 328
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Um administrador precisa implementar alta disponibilidade para uma aplicação em duas máquinas virtuais na mesma região do Azure. As VMs devem ser isoladas contra falhas em nível de rack físico (energia, rede e hardware) dentro do mesmo data center. Qual recurso de resiliência deve ser utilizado?
**Opções:**
- A) Conjunto de Disponibilidade (Availability Set) configurado com Domínios de Falha (Fault Domains)
- B) Zonas de Disponibilidade (Availability Zones)
- C) Grupo de Recursos Distribuído
- D) Instâncias do Azure Functions
**Resposta Correta:** A
**Explicação Técnica:** Os Conjuntos de Disponibilidade (Availability Sets) garantem que as VMs sejam distribuídas entre múltiplos nós de hardware físicos, racks e comutadores de rede (Domínios de Falha - Fault Domains) dentro de um mesmo data center do Azure.

### Questão 329
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa deseja restringir os tipos de recursos que os desenvolvedores podem criar em uma subscrição de desenvolvimento (ex.: proibir a criação de VMs de tamanhos M-Series de alto custo). Qual serviço do Azure impõe essa restrição de conformidade?
**Opções:**
- A) Azure Policy (utilizando a definição Allowed Virtual Machine SKUs)
- B) Bloqueio de Recursos (Resource Locks)
- C) Alertas de Orçamento (Azure Budgets)
- D) Grupos de Gerenciamento
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy avalia recursos comparando-os com regras de negócios declaradas em formato JSON. Políticas nativas como *Allowed Virtual Machine SKUs* impedem a implantação de máquinas virtuais de famílias ou tamanhos não autorizados.

### Questão 330
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual funcionalidade do Azure Monitor permite visualizar a topologia de dependências de componentes, o fluxo de comunicação entre microsserviços e os tempos de resposta de requisições em tempo real para aplicações Web?
**Opções:**
- A) Mapa de Aplicativos (Application Map) no Application Insights
- B) Verificação de Rota (Next Hop) no Network Watcher
- C) Azure Activity Log
- D) Azure Service Health
**Resposta Correta:** A
**Explicação Técnica:** O Mapa de Aplicativos (*Application Map*) no Application Insights apresenta visualmente a estrutura e topologia das aplicações distribuídas, destacando dependências, gargalos de latência e taxas de erro em cada componente do sistema.

### Questão 331
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma sub-rede de máquinas virtuais precisa acessar a Internet para baixar atualizações de pacotes Linux. No entanto, por razões de segurança, as VMs não devem possuir endereços IP públicos individuais e a sub-rede não deve aceitar nenhuma conexão de entrada da Internet. Qual recurso de rede deve ser configurado?
**Opções:**
- A) Gateway NAT do Azure (Azure NAT Gateway) associado à sub-rede
- B) Azure Load Balancer Interno
- C) Azure ExpressRoute
- D) Peering de Rede Virtual
**Resposta Correta:** A
**Explicação Técnica:** O Azure NAT Gateway fornece conectividade de saída de Internet segura e escalável para sub-redes privadas. Ele utiliza IPs públicos estáticos de saída enquanto impede que conexões de entrada indesejadas originadas na Internet alcancem as VMs.

### Questão 332
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa configurar a replicação de uma Conta de Armazenamento para garantir proteção contra desastres regionais completos, mantendo os dados síncronos entre três zonas de disponibilidade na região primária e assíncronos em uma região secundária remota. Qual opção de redundância deve ser selecionada?
**Opções:**
- A) Armazenamento com Redundância Geo-Zonal (GZRS - Geo-Zone-Redundant Storage)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância Zonal (ZRS)
- D) Armazenamento com Redundância Geográfica (GRS)
**Resposta Correta:** A
**Explicação Técnica:** O GZRS (Geo-Zone-Redundant Storage) combina a alta disponibilidade da replicação síncrona em três Zonas de Disponibilidade na região primária com a replicação assíncrona para uma região geográfica secundária distante.

### Questão 333
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa necessita migrar uma aplicação web legada executada em IIS de um servidor local para o Azure App Service. Qual ferramenta oficial da Microsoft analisa o aplicativo local e automatiza o processo de migração para a nuvem?
**Opções:**
- A) Assistente de Migração do Azure App Service (App Service Migration Assistant)
- B) AzCopy v10
- C) Azure Storage Explorer
- D) Azure Data Box
**Resposta Correta:** A
**Explicação Técnica:** O *Azure App Service Migration Assistant* é uma ferramenta gratuita que avalia aplicações Web locais (ASP.NET ou Java/IIS) e automatiza a migração do site e das configurações para o Azure App Service.

### Questão 334
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa deseja organizar suas 20 subscrições do Azure por departamentos (Financeiro, TI, Recursos Humanos) para consolidar a cobrança e aplicar controles corporativos padronizados. Qual estrutura hierárquica deve ser implementada?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups) estruturados por Departamento
- B) Grupos de Recursos dentro de uma única subscrição
- C) Unidades Administrativas no Microsoft Entra ID
- D) Tags de ambiente no Key Vault
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento fornecem níveis de escopo acima das assinaturas. Organizar assinaturas em uma estrutura de árvore de Grupos de Gerenciamento permite aplicar políticas de governança, RBAC e visualização de custos unificada por departamento.

### Questão 335
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa garantir que todos os backups efetuados pelo Recovery Services Vault fiquem imunes a modificações ou exclusões acidentais/maliciosas acionadas por contas comprometidas de administradores. Qual configuração deve ser habilitada no Vault?
**Opções:**
- A) Imutabilidade do Cofre (Vault Immutability / Soft Delete para Backup)
- B) Bloqueio de Recurso ReadOnly na subscrição
- C) Criptografia TLS 1.3 obrigatória
- D) Regra de NSG de bloqueio da porta 443
**Resposta Correta:** A
**Explicação Técnica:** A Imutabilidade do Cofre de Backup (Vault Immutability) impede a alteração de políticas de retenção e a exclusão de pontos de restauração de backup por usuários ou atacantes, garantindo resiliência contra ataques de ransomware.

### Questão 336
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você cria um Grupo de Segurança de Rede (NSG) e o associa a uma interface de rede (NIC). O NSG possui uma regra personalizada de entrada: Prioridade 200, Ação: Deny, Origem: Any, Porta: 80. Existe outra regra: Prioridade 150, Ação: Allow, Origem: 192.168.1.0/24, Porta: 80. O tráfego HTTP vindo do IP 192.168.1.5 será permitido ou negado?
**Opções:**
- A) Permitido, pois a regra com prioridade 150 tem precedência sobre a regra de prioridade 200
- B) Negado, pois a regra de prioridade 200 é mais abrangente
- C) Negado, pois a ação Deny sempre substitui a ação Allow em NSGs
- D) O tráfego será descartado por falta de rota UDR
**Resposta Correta:** A
**Explicação Técnica:** No Azure NSG, as regras são processadas em ordem de prioridade (números menores indicam maior prioridade). A regra com prioridade 150 (Allow) é avaliada antes da regra de prioridade 200 (Deny), permitindo o tráfego do IP especificado.

### Questão 337
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa montar um compartilhamento de arquivos nativo do Azure diretamente em máquinas virtuais Linux locais via protocolo NFS v3.0. Qual tipo de conta de armazenamento e configuração são necessários?
**Opções:**
- A) Conta Premium File Storage (FileStorage) com suporte a protocolo NFS v3.0 e rede privada
- B) Conta Standard General Purpose v1 via SMB 2.1
- C) Azure Blob Storage com acesso público anônimo
- D) Table Storage com autenticação por chave primária
**Resposta Correta:** A
**Explicação Técnica:** O suporte ao protocolo NFS (Network File System) v3.0 no Azure Files exige uma conta de armazenamento do tipo *FileStorage* de nível Premium (baseada em SSD) e a conexão deve ser estabelecida via VNet / Private Endpoint.

### Questão 338
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa planeja executar um cluster Kubernetes (AKS) para microsserviços. Eles exigem que cada Pod receba um endereço IP privado real pertencente à sub-rede da Rede Virtual do Azure (VNet), permitindo comunicação direta entre Pods e VMs da rede. Qual plug-in de rede deve ser selecionado na criação do cluster?
**Opções:**
- A) Azure CNI (Container Network Interface)
- B) Kubenet (Rede Básica)
- C) Overlay Network isolada
- D) DNS Privado Nativo
**Resposta Correta:** A
**Explicação Técnica:** Com o plug-in de rede *Azure CNI*, cada Pod no cluster AKS obtém um endereço IP privado diretamente da sub-rede da VNet configurada, permitindo que os Pods se comuniquem com outros recursos da VNet sem necessidade de tradução de endereços (NAT).

### Questão 339
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** O departamento financeiro exige um relatório consolidador de custos do Azure detalhado por projeto. Como os administradores devem organizar a identificação dos recursos para permitir a filtragem exata de custos na Gestão de Custos do Azure (Azure Cost Management)?
**Opções:**
- A) Aplicar Tags (chaves e valores como Projeto=Alfa) nos recursos e grupos de recursos
- B) Mover todos os recursos para subscrições separadas
- C) Alterar o nome das máquinas virtuais com um prefixo numérico
- D) Criar rotas UDR separadas para cada projeto
**Resposta Correta:** A
**Explicação Técnica:** As Tags do Azure são pares de chave-valor que ajudam a organizar e categorizar os recursos para fins de gerenciamento, governança e relatórios de custos detalhados no Azure Cost Management & Billing.

### Questão 340
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você configura um Log Analytics Workspace para receber logs de várias instâncias do Azure Firewall e máquinas virtuais. Você deseja receber alertas em tempo real quando o número de eventos de erro ultrapassar 50 em um intervalo de 5 minutos. Qual tipo de sinal de alerta deve ser criado?
**Opções:**
- A) Alerta de Pesquisa de Log (Log Search Alert) baseado em consulta KQL
- B) Alerta de Métrica de CPU
- C) Alerta de Integridade do Serviço (Service Health)
- D) Alerta de Cota de Assinatura
**Resposta Correta:** A
**Explicação Técnica:** Os Alertas de Pesquisa de Log (*Log Search Alerts*) no Azure Monitor executam uma consulta KQL em intervalos definidos sobre o Log Analytics Workspace e disparam um alerta quando o número de resultados atinge o limite configurado.

### Questão 341
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa possui um servidor DNS local no endereço 192.168.1.10. As máquinas virtuais criadas em uma VNet do Azure precisam resolver nomes de domínio locais através desse servidor. Onde a configuração de DNS personalizado deve ser aplicada?
**Opções:**
- A) Nas configurações de Servidores DNS (DNS Servers) da própria Rede Virtual (VNet)
- B) No Grupo de Segurança de Rede (NSG) da sub-rede
- C) No arquivo de configuração hosts de cada VM individualmente
- D) No Azure Key Vault
**Resposta Correta:** A
**Explicação Técnica:** A opção de alterar os Servidores DNS nas propriedades da VNet permite substituir o DNS padrão fornecido pelo Azure (168.63.129.16) pelos endereços IP dos seus servidores DNS personalizados (on-premises ou em VMs IaaS).

### Questão 342
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa conceder ao aplicativo web da empresa permissão para ler arquivos em uma Conta de Armazenamento utilizando identidades sem senhas baseadas no Microsoft Entra ID. Qual função RBAC nativa deve ser atribuída à Identidade Gerenciada do aplicativo?
**Opções:**
- A) Leitor de Dados do Blob de Armazenamento (Storage Blob Data Reader)
- B) Colaborador da Conta de Armazenamento (Storage Account Contributor)
- C) Leitor (Reader) no nível da assinatura
- D) Proprietário dos Dados do Blob
**Resposta Correta:** A
**Explicação Técnica:** A função nativa *Storage Blob Data Reader* concede acesso de leitura no nível de plano de dados aos contêineres e blobs do Azure Storage, permitindo que a aplicação se autentique via Microsoft Entra ID sem usar chaves de conta.

### Questão 343
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa deseja implantar uma aplicação web baseada em Linux no Azure App Service com suporte a escalonamento automático de 2 a 10 instâncias durante horários de pico comercial. Qual métrica do Azure Monitor é recomendada para acionar a regra de Auto Scale?
**Opções:**
- A) Percentual de utilização de CPU (CPU Percentage) ou Contagem de Requisições (Http Queue Length)
- B) Espaço livre em disco no servidor SQL
- C) Número de usuários cadastrados no Microsoft Entra ID
- D) Latência do ping ICMP na NIC
**Resposta Correta:** A
**Explicação Técnica:** As regras de Auto Scale no Azure App Service permitem escalar instâncias horizontalmente com base em métricas de desempenho em tempo real, como uso de CPU, memória ou comprimento da fila de requisições HTTP.

### Questão 344
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador precisa transferir a propriedade e o controle de faturamento de uma assinatura do Azure para outro usuário na organização sem interromper os recursos ativos. Qual ação deve ser executada no portal do Azure?
**Opções:**
- A) Alterar o Proprietário do Faturamento (Billing Owner / Administrator) no Azure Cost Management & Billing
- B) Excluir a assinatura e criar uma nova
- C) Recriar todas as máquinas virtuais em uma nova subscrição
- D) Atribuir o papel de Global Admin no Entra ID
**Resposta Correta:** A
**Explicação Técnica:** A transferência de propriedade de faturamento de uma assinatura do Azure é realizada através do centro de Gestão de Custos e Cobrança do Azure, alterando a conta responsável pelo pagamento sem afetar a execução dos recursos técnicos.

### Questão 345
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa proteger uma máquina virtual Linux contra alterações de arquivos de sistema não autorizadas e monitorar vulnerabilidades de segurança do sistema operacional. Qual serviço integrado da Microsoft fornece essa proteção e relatórios de conformidade?
**Opções:**
- A) Microsoft Defender para Nuvem (Microsoft Defender for Cloud)
- B) Azure Network Watcher
- C) Azure Advisor
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** O *Microsoft Defender for Cloud* é a solução de gerenciamento de postura de segurança em nuvem (CPSM) e proteção de cargas de trabalho (CWPP) que analisa continuamente o estado de segurança de VMs, contêineres e bancos de dados.

### Questão 346
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa precisa implantar uma arquitetura Hub-and-Spoke de Redes Virtuais no Azure. A VNet Hub contém uma instância de Azure Firewall. Como garantir que todo o tráfego entre as VNets Spoke (Spoke1 e Spoke2) passe obrigatoriamente pelo Azure Firewall no Hub?
**Opções:**
- A) Configurar Peering entre as Spokes e a Hub habilitando Use Remote Gateways / Allow Gateway Transit e adicionar UDRs nas Spokes apontando para o IP privado do Firewall
- B) Criar Peering direto entre Spoke1 e Spoke2
- C) Adicionar uma regra de NSG bloqueando portas altas
- D) Configurar o Azure Traffic Manager entre as Spokes
**Resposta Correta:** A
**Explicação Técnica:** Em uma topologia Hub-and-Spoke, para que o tráfego entre VNets Spoke seja inspecionado pelo Firewall no Hub, as sub-redes Spoke devem possuir Tabelas de Rotas (UDRs) definindo o IP privado do Azure Firewall como o próximo salto (*next hop*).

### Questão 347
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma conta de armazenamento de uso geral v2 possui 10 TB de dados acessados raramente. Você altera o nível de acesso padrão da conta de Frio (Cool) para Arquivamento (Archive). Qual será o efeito imediato nos blobs existentes no contêiner?
**Opções:**
- A) O nível de acesso dos blobs existentes não é alterado automaticamente; a mudança do nível padrão afeta apenas novos blobs criados sem nível explícito
- B) Todos os blobs existentes são movidos imediatamente para o nível Archive
- C) Os blobs são excluídos permanentemente após 24 horas
- D) Os blobs tornam-se inacessíveis para leitura via HTTPS
**Resposta Correta:** A
**Explicação Técnica:** Alterar o nível de acesso padrão no nível da Conta de Armazenamento afeta apenas os novos blobs que forem gravados sem uma especificação explícita de nível. Os blobs já existentes mantêm o nível de acesso atribuído a eles anteriormente.

### Questão 348
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa garantir que um grupo de máquinas virtuais de banco de dados no Azure utilize discos de estado sólido com a menor latência possível (sub-milisegundo) e altíssimo desempenho de IOPS (até 160.000 IOPS). Qual tipo de Disco Gerenciado deve ser selecionado?
**Opções:**
- A) Discos Gerenciados Ultra (Ultra Disks)
- B) SSD Premium v1
- C) SSD Padrão (Standard SSD)
- D) HDD Padrão (Standard HDD)
**Resposta Correta:** A
**Explicação Técnica:** Os *Ultra Disks* do Azure fornecem armazenamento em bloco de alto rendimento, alta taxa de IOPS (até 160.000 IOPS) e latência inferior a um milissegundo para cargas de trabalho extremamente exigentes orientadas a dados (como SQL Server, SAP HANA).

### Questão 349
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma corporação precisa criar um relatório mensal que liste todas as alterações de configuração e atividades administrativas realizadas nas subscrições do Azure nos últimos 90 dias. Qual registro central do Azure deve ser consultado?
**Opções:**
- A) Registro de Atividades do Azure (Azure Activity Log)
- B) Logs de Entrada do Microsoft Entra ID (Sign-in Logs)
- C) Azure Network Watcher Traffic Analytics
- D) Azure Advisor Metrics
**Resposta Correta:** A
**Explicação Técnica:** O *Azure Activity Log* registra eventos do plano de controle (subscription-level events), fornecendo insights sobre operações de criação, atualização ou exclusão de recursos efetuadas por usuários ou serviços no Azure.

### Questão 350
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Um administrador precisa monitorar a disponibilidade global de um ponto de extremidade de API HTTP público hospedado no Azure. O teste deve ser realizado a partir de múltiplos locais geográficos ao redor do mundo a cada 5 minutos. Qual recurso do Azure Monitor atende a esse requisito?
**Opções:**
- A) Testes de Disponibilidade Padrão (Standard Availability Tests / URL Ping Tests) no Application Insights
- B) Azure Network Watcher Connection Troubleshooter
- C) Azure Activity Log Alerts
- D) Log Analytics KQL Summarize
**Resposta Correta:** A
**Explicação Técnica:** Os Testes de Disponibilidade (*Availability Tests*) no Application Insights permitem disparar solicitações web sintéticas regulares (ping de URL ou teste padrão) de múltiplos data centers ao redor do mundo para validar tempo de resposta e uptime de aplicações web.
