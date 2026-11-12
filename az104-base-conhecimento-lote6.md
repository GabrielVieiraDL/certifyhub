# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 6 (Questões 251 a 300)

Esta base de conhecimento contém as questões 251 a 300 do exame **AZ-104: Microsoft Azure Administrator** formatadas para ingestão e automação no Antigravity.

---

### Questão 251
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa precisa configurar o Azure File Sync para sincronizar arquivos entre um servidor Windows local e um compartilhamento de arquivos do Azure (Azure Files). Qual recurso deve ser criado primeiro no Azure para agrupar e gerenciar os serviços de sincronização?
**Opções:**
- A) Serviço de Sincronização de Armazenamento (Storage Sync Service)
- B) Endpoint de Nuvem (Cloud Endpoint)
- C) Grupo de Sincronização (Sync Group)
- D) Endpoint de Servidor (Server Endpoint)
**Resposta Correta:** A
**Explicação Técnica:** O Serviço de Sincronização de Armazenamento (Storage Sync Service) é o recurso do Azure de nível superior que gerencia a topologia do Azure File Sync e deve ser implantado antes da criação dos grupos de sincronização e endpoints.

### Questão 252
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Um administrador do Azure precisa configurar o roteamento de tráfego de rede para garantir que todo o tráfego destinado à Internet a partir de uma sub-rede passe obrigatoriamente por uma solução de firewall de rede (NVA - Network Virtual Appliance). O que deve ser criado e associado à sub-rede?
**Opções:**
- A) Uma Tabela de Rotas (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando para o IP do NVA
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de negação de tráfego de saída
- C) Um Ponto de Extremidade Privado (Private Endpoint)
- D) Um Peering de Rede Virtual (VNet Peering) com gateway de trânsito
**Resposta Correta:** A
**Explicação Técnica:** As Tabelas de Rotas com Rotas Definidas pelo Usuário (UDR) permitem substituir o roteamento padrão do Azure (como a rota padrão 0.0.0.0/0 para a Internet) direcionando o tráfego para um Virtual Appliance (NVA) ou Azure Firewall como próximo salto (Next Hop).

### Questão 253
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa conceder permissão para que um usuário possa criar e gerenciar máquinas virtuais em um Grupo de Recursos específico, sem conceder acesso administrativo total à assinatura nem permissões para gerenciar permissões de acesso (RBAC). Qual função interna (Built-in Role) deve ser atribuída?
**Opções:**
- A) Colaborador de Máquina Virtual (Virtual Machine Contributor)
- B) Leitor (Reader)
- C) Proprietário (Owner)
- D) Colaborador de Rede (Network Contributor)
**Resposta Correta:** A
**Explicação Técnica:** A função Colaborador de Máquina Virtual (Virtual Machine Contributor) permite gerenciar máquinas virtuais (criar, reiniciar, excluir, alterar tamanho), mas não permite conceder acesso a outros usuários no RBAC nem gerenciar a rede ou armazenamento subjacente se não houver permissão.

### Questão 254
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você planeja implantar um conjunto de escala de máquinas virtuais (VMSS) no Azure. Como você deve garantir que as instâncias do conjunto de escala sejam distribuídas em domínios de falha e domínios de atualização físicos separados dentro de um data center?
**Opções:**
- A) Configurar o Modo de Orquestração Flexível (Flexible Orchestration Mode)
- B) Usar um Conjunto de Disponibilidade (Availability Set) associado ao VMSS
- C) Implantar instâncias em uma única Zona de Disponibilidade no modo Uniforme
- D) Habilitar a criptografia de disco de host
**Resposta Correta:** A
**Explicação Técnica:** O Modo de Orquestração Flexível (Flexible Orchestration) do VMSS permite combinar a escalabilidade automática dos conjuntos de escala com o controle refinado sobre instâncias individuais em domínios de falha e zonas de disponibilidade.

### Questão 255
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Um administrador precisa ser notificado por e-mail e SMS sempre que o uso de CPU de qualquer máquina virtual em uma assinatura ultrapassar 85% por mais de 5 minutos. Quais dois componentes do Azure Monitor devem ser configurados?
**Opções:**
- A) Regra de Alerta de Métrica (Metric Alert Rule) e Grupo de Ação (Action Group)
- B) Regra de Coleta de Dados (DCR) e Log Analytics Workspace
- C) Azure Advisor e Service Health
- D) Network Watcher e Connection Monitor
**Resposta Correta:** A
**Explicação Técnica:** As Regras de Alerta de Métrica monitoram métricas numéricas (como CPU %) e disparam ações. Os Grupos de Ação (Action Groups) definem os receptores e canais de comunicação (SMS, e-mail, Webhook, chamadas de voz).

### Questão 256
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa possui duas redes virtuais, VNet1 (10.1.0.0/16) na região Leste dos EUA e VNet2 (10.2.0.0/16) na região Oeste da Europa. O que é necessário para estabelecer comunicação privada entre as duas VNets com o menor tempo de latência e sem tráfego na Internet pública?
**Opções:**
- A) Peering Global de Rede Virtual (Global VNet Peering)
- B) Conexão VPN Site-to-Site
- C) ExpressRoute Direct
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** O Peering Global de Rede Virtual conecta duas redes virtuais localizadas em regiões diferentes do Azure diretamente pela rede backbone privada global da Microsoft.

### Questão 257
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa garantir que os arquivos armazenados em um contêiner de armazenamento de blobs não possam ser modificados ou excluídos por um período de retenção obrigatório de 3 anos para cumprir regulamentações financeiras. Qual recurso deve ser habilitado?
**Opções:**
- A) Armazenamento Imutável com Política de Conformidade Baseada no Tempo (Immutable Blob Storage - Time-based retention)
- B) Bloqueio de Recursos (Resource Lock - ReadOnly)
- C) Identidade Gerenciada Atribuída pelo Usuário
- D) Criptografia de Infraestrutura do Azure Storage
**Resposta Correta:** A
**Explicação Técnica:** O Armazenamento Imutável para Azure Blob Storage (com políticas de retenção baseadas no tempo bloqueadas) garante conformidade no padrão WORM (Write Once, Read Many), impedindo que dados sejam apagados ou alterados até a expiração do prazo.

### Questão 258
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa expor de forma segura um banco de dados SQL do Azure para instâncias de máquinas virtuais residentes em uma sub-rede privada, sem atribuir IP público ao servidor de banco de dados e sem passar pela Internet. O que deve ser implantado?
**Opções:**
- A) Ponto de Extremidade Privado (Private Endpoint)
- B) Azure Bastion
- C) Public IP Address com NAT Gateway
- D) Servidor Proxy NVA
**Resposta Correta:** A
**Explicação Técnica:** O Private Endpoint utiliza um endereço IP privado da própria VNet para conectar os serviços PaaS da Microsoft (como Azure SQL Database) de forma segura através do Azure Private Link.

### Questão 259
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual funcionalidade do Microsoft Entra ID permite atribuir permissões administrativas a usuários com base no escopo de departamentos específicos da empresa (como Vendas ou RH), sem conceder direitos globais no locatário?
**Opções:**
- A) Unidades Administrativas (Administrative Units - AU)
- B) Grupos de Gerenciamento (Management Groups)
- C) Grupos de Segurança Dinâmicos
- D) Registro de Aplicativo (App Registration)
**Resposta Correta:** A
**Explicação Técnica:** As Unidades Administrativas (AUs) no Microsoft Entra ID permitem subdividir a organização para delegar controle administrativo regional ou departamental sobre subconjuntos de usuários, grupos e dispositivos.

### Questão 260
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual serviço do Azure permite auditar e rastrear todas as operações de gerenciamento e alteração de controle efetuadas na infraestrutura (como criação, exclusão ou modificação de recursos)?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Azure Advisor
- C) Azure Application Insights
- D) Network Watcher Flow Logs
**Resposta Correta:** A
**Explicação Técnica:** O Log de Atividades do Azure (Activity Log) registra eventos no plano de controle do Azure Resource Manager (ARM), documentando quem realizou cada operação, quando ela ocorreu e o status do resultado.

### Questão 261
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você implantou uma máquina virtual executando um servidor Web na sub-rede Subnet1. Os usuários relatam que não conseguem acessar a página Web pela porta HTTP 80. Ao verificar o Grupo de Segurança de Rede (NSG), você observa uma regra de Entrada personalizada permitindo a porta 80 com Prioridade 200 e uma regra padrão de Negação de Entrada (DenyAllInbound) com Prioridade 65500. Qual é a causa mais provável do problema?
**Opções:**
- A) Existe um Firewall de Host (SO) na VM bloqueando a porta 80
- B) A regra de negação possui prioridade numérica maior e portanto sobrescreve a permissão
- C) As regras personalizadas do NSG exigem aprovação do Azure Policy
- D) A regra padrão DenyAllInbound ignora o número da prioridade
**Resposta Correta:** A
**Explicação Técnica:** No NSG, prioridades numéricas menores têm precedência (200 é avaliado antes de 65500), portanto a porta 80 está sendo permitida no NSG. O bloqueio provavelmente está no firewall interno do sistema operacional da máquina virtual (como Windows Firewall ou iptables).

### Questão 262
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa precisa transferir 150 TB de dados locais para uma conta de armazenamento do Azure Blob Storage. A largura de banda da conexão de Internet local é limitada a 10 Mbps. Qual solução da Microsoft é a mais recomendada?
**Opções:**
- A) Azure Data Box
- B) AzCopy v10 via linha de comando
- C) Azure File Sync
- D) PowerShell com Start-AzStorageBlobCopy
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Box é um dispositivo físico fornecido pela Microsoft para transferência de dados offline de grande porte (até 100 TB por dispositivo), ideal quando a transferência via rede de baixa velocidade levaria meses.

### Questão 263
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Qual extensão de máquina virtual do Azure permite executar automaticamente scripts PowerShell ou Bash durante a implantação ou pós-implantação da VM para automação de tarefas de configuração?
**Opções:**
- A) Extensão de Script Personalizado (Custom Script Extension)
- B) Extensão do Agente do Azure Monitor
- C) Extensão VMAccess
- D) Extensão do Desempenho de Disco
**Resposta Correta:** A
**Explicação Técnica:** A Custom Script Extension baixa e executa scripts em máquinas virtuais do Azure, sendo útil para pós-configuração de aplicativos e automação de ambiente.

### Questão 264
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você deseja balancear a carga de solicitações de clientes para um pool de servidores Web backend com base na URL da requisição (roteamento baseado em caminho /path). Qual serviço de rede do Azure oferece suporte nativo a este requisito de camada de aplicação?
**Opções:**
- A) Azure Application Gateway
- B) Azure Load Balancer
- C) Azure Traffic Manager
- D) Azure NAT Gateway
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego Web de Camada 7 que suporta roteamento baseado em URL, terminação SSL/TLS e Web Application Firewall (WAF).

### Questão 265
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma organização deseja implantar um modelo padronizado que inclua Grupos de Recursos, atribuições de RBAC, definições de Azure Policy e modelos ARM em múltiplas assinaturas de forma automatizada. Qual recurso clássico/nativo de governança é projetado para essa função?
**Opções:**
- A) Azure Blueprints
- B) Azure Advisor
- C) Azure Resource Graph
- D) Grupos de Ação
**Resposta Correta:** A
**Explicação Técnica:** O Azure Blueprints permite orquestrar a implantação de diversos artefatos de recursos (Resource Groups, RBAC, Policy, ARM Templates) para criar ambientes de conformidade repetíveis.

### Questão 266
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual ferramenta de linha de comando de alto desempenho é recomendada pela Microsoft para copiar e sincronizar arquivos entre sistemas de arquivos locais e contas de armazenamento do Azure Blob ou Files?
**Opções:**
- A) AzCopy
- B) Robocopy
- C) Azure CLI (az storage copy)
- D) FTP Client
**Resposta Correta:** A
**Explicação Técnica:** O AzCopy (versão 10+) é um utilitário de linha de comando altamente otimizado para cópia e movimentação de dados assíncrona entre o Azure Storage e ambientes locais.

### Questão 267
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Ao configurar o backup de máquinas virtuais do Azure em um Cofrinho de Serviços de Recuperação (Recovery Services Vault), qual recurso garante que os pontos de restauração de backup não sejam excluídos acidentalmente por usuários mal-intencionados por até 14 dias após uma tentativa de exclusão?
**Opções:**
- A) Exclusão Reversível (Soft Delete para Backup)
- B) Trava de Leitura (ReadOnly Lock)
- C) Criptografia com Chave Gerenciada pelo Cliente
- D) Diagnóstico de Inicialização
**Resposta Correta:** A
**Explicação Técnica:** O Soft Delete para Azure Backup protege os dados de backup contra exclusões acidentais ou mal-intencionadas, mantendo os dados salvos por 14 dias adicionais após o comando de exclusão ser emitido.

### Questão 268
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa conectar uma sub-rede contendo servidores de banco de dados locais à sua rede virtual do Azure através de uma conexão criptografada via Internet pública. Qual recurso de rede do Azure deve ser configurado na VNet?
**Opções:**
- A) Gateway de Rede Virtual (Virtual Network Gateway / VPN Gateway)
- B) Peering de Rede Virtual (VNet Peering)
- C) Azure ExpressRoute Direct
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** O VPN Gateway estabelece conexões criptografadas ponto a ponto ou site a site (S2S/P2S) pela Internet entre redes locais e VNets no Azure.

### Questão 269
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa precisa implantar uma aplicação web baseada em contêineres Docker sem gerenciar a infraestrutura de servidores virtuais nem criar um cluster complexo como o AKS. Qual serviço PaaS de contêiner serverless é o mais indicado?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Conjunto de Escala de Máquinas Virtuais (VMSS)
- C) Serviço de Máquina Virtual Dedicada
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Instances (ACI) permite executar contêineres isolados sob demanda na nuvem de forma rápida e serverless, sem a necessidade de provisionar máquinas virtuais ou orquestradores complexos.

### Questão 270
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual funcionalidade do Microsoft Entra ID exige que usuários administradores passem por uma verificação adicional (como aplicativo autenticador ou SMS) antes de acessar o portal do Azure?
**Opções:**
- A) Autenticação Multifator (MFA) no Acesso Condicional
- B) Redefinição de Senha de Autoatendimento (SSPR)
- C) Unidades Administrativas
- D) Identidades Gerenciadas Atribuídas pelo Sistema
**Resposta Correta:** A
**Explicação Técnica:** As políticas de Acesso Condicional com Autenticação Multifator (MFA) impõem requisitos adicionais de verificação de identidade com base em condições de risco, usuários ou funções administrativas.

### Questão 271
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual opção de redundância do Azure Storage replica os dados em três Zonas de Disponibilidade dentro da região primária e também replica assincronamente os dados para uma segunda região secundária emparelhada?
**Opções:**
- A) Armazenamento com Redundância de Zona Geográfica (GZRS)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância de Zona (ZRS)
- D) Armazenamento com Redundância Geográfica (GRS)
**Resposta Correta:** A
**Explicação Técnica:** O GZRS (Geo-Zone-Redundant Storage) combina a alta disponibilidade da redundância de zona (ZRS em 3 zonas) na região primária com a tolerância a falhas regionais da replicação geo-redundante (GRS na região secundária).

### Questão 272
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual ferramenta do Azure Network Watcher permite verificar se um pacote IP é permitido ou bloqueado ao trafegar de ou para uma máquina virtual com base nas regras do Grupo de Segurança de Rede (NSG)?
**Opções:**
- A) Verificação de Fluxo IP (IP Flow Verify)
- B) Teste de Conectividade (Connectivity Check)
- C) Captura de Pacotes (Packet Capture)
- D) Exibição de Topologia (Topology)
**Resposta Correta:** A
**Explicação Técnica:** A ferramenta IP Flow Verify do Network Watcher analisa se um pacote de rede (origem/destino IP e porta) é permitido ou negado por regras de NSG aplicadas à interface de rede da VM.

### Questão 273
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Como um administrador pode proibir a criação de novos recursos do tipo Máquina Virtual da série M em toda uma assinatura do Azure para controlar custos?
**Opções:**
- A) Atribuir uma Política do Azure (Azure Policy) configurada com o efeito 'Deny' para o SKU da VM
- B) Criar uma regra de NSG bloqueando a porta 3389
- C) Aplicar um Bloqueio de Recurso (Resource Lock - ReadOnly)
- D) Alterar a função RBAC dos usuários para Leitor
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy impõe regras e restrições de conformidade sobre o provisionamento de recursos, como proibir determinados SKUs de máquinas virtuais ou regiões geográficas.

### Questão 274
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Onde as estatísticas e métricas de desempenho de aplicações (como chamadas de API, exceções e tempo de resposta) são coletadas e analisadas no Azure para identificação de gargalos de desenvolvimento?
**Opções:**
- A) Application Insights
- B) Log de Atividades do Azure
- C) Azure Advisor
- D) Service Health
**Resposta Correta:** A
**Explicação Técnica:** O Application Insights (recurso do Azure Monitor) é um serviço de Gerenciamento de Desempenho de Aplicações (APM) para desenvolvedores e profissionais de DevOps rastrearem métricas de runtime e exceções de código.

### Questão 275
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma aplicação Web hospedada no Azure App Service precisa acessar um banco de dados Azure SQL sem que nenhuma credencial ou senha fique salva em arquivos de configuração ou código fonte. Qual solução de identidade é recomendada?
**Opções:**
- A) Identidade Gerenciada (Managed Identity)
- B) Chave de Acesso da Conta de Armazenamento
- C) Usuário Local de Banco de Dados
- D) Registro de Aplicativo com Segredo de Cliente estático
**Resposta Correta:** A
**Explicação Técnica:** As Identidades Gerenciadas fornecem uma identidade automática no Microsoft Entra ID para recursos do Azure, permitindo autenticação segura em serviços que suportam autenticação Entra sem armazenar credenciais no código.

### Questão 276
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual tipo de regra de associação no Azure DNS permite que instâncias de máquinas virtuais em uma VNet resolvam automaticamente os nomes de host DNS privados de outras VMs na mesma rede virtual?
**Opções:**
- A) Zona DNS Privada do Azure (Azure Private DNS Zone) com Registro Automático (Auto-registration)
- B) Servidor DNS Público da Microsoft
- C) Encaminhador DNS Externo (DNS Forwarder)
- D) Registro CNAME público no GoDaddy
**Resposta Correta:** A
**Explicação Técnica:** As Zonas DNS Privadas do Azure associadas a uma VNet com a opção de Auto-registration habilitada registram e resolvem automaticamente os nomes de domínio internos e endereços IP das VMs da VNet.

### Questão 277
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual camada de acesso do Azure Blob Storage é otimizada para armazenar dados aos quais raramente se acede e permite uma latência de recuperação aceitável de várias horas em troca dos menores custos de armazenamento?
**Opções:**
- A) Camada de Arquivamento (Archive Tier)
- B) Camada Fria (Cool Tier)
- C) Camada Quente (Hot Tier)
- D) Camada Premium
**Resposta Correta:** A
**Explicação Técnica:** A Camada de Arquivamento (Archive) tem o menor custo de armazenamento de dados, mas requer o processo de reidratação (que pode levar várias horas) para tornar os dados legíveis novamente.

### Questão 278
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador do Azure precisa verificar quais atribuições de função RBAC e permissões foram concedidas a um usuário específico em diferentes escopos. Qual ferramenta/painel no Portal do Azure deve ser consultado?
**Opções:**
- A) Controle de Acesso (IAM) do recurso ou assinatura
- B) Painel de Licenciamento do Entra ID
- C) Bloqueios de Recursos
- D) Azure Policy Compliance
**Resposta Correta:** A
**Explicação Técnica:** A lâmina de Controle de Acesso (IAM - Identity and Access Management) permite visualizar, adicionar e remover atribuições de funções RBAC para usuários, grupos e entidades de serviço em qualquer escopo de recurso.

### Questão 279
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual recurso de rede do Azure fornece um IP público estático e tradução de endereço de rede de saída (outbound SNAT) para todas as instâncias de VMs em uma sub-rede sem expor portas de entrada para a Internet?
**Opções:**
- A) Azure NAT Gateway
- B) Ponto de Extremidade do Serviço (Service Endpoint)
- C) Peering de Rede Virtual
- D) Servidor DNS Privado
**Resposta Correta:** A
**Explicação Técnica:** O Azure NAT Gateway simplifica a conectividade de saída para a Internet em redes virtuais, fornecendo endereços IP de saída estáticos totalmente gerenciados e altamente escaláveis.

### Questão 280
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual linguagem de consulta é utilizada no Azure Monitor Log Analytics para pesquisar, filtrar e agregar logs de eventos e métricas de desempenho coletados de recursos do Azure?
**Opções:**
- A) Kusto Query Language (KQL)
- B) T-SQL
- C) GraphQL
- D) JSONPath
**Resposta Correta:** A
**Explicação Técnica:** A Kusto Query Language (KQL) é a linguagem de consulta somente leitura utilizada para analisar grandes volumes de dados no Azure Log Analytics, Azure Data Explorer e Microsoft Sentinel.

### Questão 281
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa garantir que um aplicativo implantado em máquinas virtuais permaneça disponível caso um data center físico inteiro em uma região do Azure sofra uma falha de energia. Como as VMs devem ser implantadas?
**Opções:**
- A) Em Zonas de Disponibilidade (Availability Zones) distintas na mesma região
- B) Em um único Conjunto de Disponibilidade (Availability Set)
- C) Em uma única sub-rede sem NSG
- D) No mesmo domínio de falha física
**Resposta Correta:** A
**Explicação Técnica:** As Zonas de Disponibilidade são locais físicos independentes com energia, refrigeração e rede separadas dentro de uma região do Azure, garantindo proteção contra a falha de um data center completo.

### Questão 282
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa precisa implantar um compartilhamento de arquivos em nuvem acessível via protocolo SMB 3.0 para servidores Windows locais e máquinas virtuais no Azure. Qual serviço do Azure deve ser utilizado?
**Opções:**
- A) Azure Files
- B) Azure Blob Storage
- C) Azure Disk Storage
- D) Azure Table Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files oferece compartilhamentos de arquivos totalmente gerenciados na nuvem acessíveis por meio dos protocolos padrão SMB (Server Message Block) e NFS.

### Questão 283
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual componente é necessário para conectar uma rede local ao Azure através do serviço ExpressRoute por meio de um provedor de conectividade parceiro?
**Opções:**
- A) Circuito ExpressRoute (ExpressRoute Circuit)
- B) Gateway VPN Ponto a Site
- C) Ponto de Extremidade Privado
- D) Peering VNet para VNet
**Resposta Correta:** A
**Explicação Técnica:** Um Circuito ExpressRoute é uma conexão lógica de camada 2 ou camada 3 estabelecida entre as instalações locais do cliente e a infraestrutura do Azure por meio de um fornecedor parceiro de conectividade.

### Questão 284
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma equipe de desenvolvimento precisa criar um grupo dinâmico de usuários no Microsoft Entra ID cujos membros sejam adicionados automaticamente com base no atributo de departamento do perfil do usuário. Qual tipo de licenciamento do Entra ID é exigido para esse recurso?
**Opções:**
- A) Microsoft Entra ID P1 ou P2
- B) Microsoft Entra ID Free
- C) Licença de Conector Local de AD
- D) Licença Basic de Suporte do Azure
**Resposta Correta:** A
**Explicação Técnica:** Os grupos de usuários dinâmicos (Dynamic User Groups) no Microsoft Entra ID exigem licenças premium (Microsoft Entra ID P1 ou P2) para cada membro pertencente ao grupo.

### Questão 285
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Ao configurar o Azure Backup para máquinas virtuais do Azure, qual é o número máximo de backups automáticos por dia suportado nativamente pelo Cofrinho de Serviços de Recuperação para VMs?
**Opções:**
- A) Múltiplos backups por dia (política Enhanced de até 4 horas) ou 1 por dia na política Standard
- B) Apenas 1 backup por semana
- C) No máximo 1 backup a cada 30 dias
- D) Ilimitados a cada 1 minuto sem custo
**Resposta Correta:** A
**Explicação Técnica:** O Azure Backup na política Standard permite 1 backup diário para VMs, enquanto a política Enhanced (Aprimorada) suporta múltiplos backups diários com frequência de até 4 em 4 horas.

### Questão 286
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você tem duas sub-redes em uma VNet: Subnet1 (Web) e Subnet2 (DB). Qual recurso de segurança de rede deve ser aplicado às sub-redes para controlar e filtrar o tráfego de rede com base em endereços IP de origem, destino e portas?
**Opções:**
- A) Grupo de Segurança de Rede (NSG)
- B) Tabela de Rotas Personalizada (UDR)
- C) Peering de Rede Virtual
- D) Registros DNS A
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Segurança de Rede (NSGs) contêm regras de segurança de entrada e saída que permitem ou negam o tráfego de rede para interfaces de rede (NIC) ou sub-redes inteiras.

### Questão 287
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Qual ferramenta de modelo de Infraestrutura como Código (IaC) moderna da Microsoft oferece uma sintaxe mais simples e concisa do que o JSON para declarar e implantar recursos do Azure?
**Opções:**
- A) Bicep
- B) Python SDK
- C) Powershell ISE
- D) Azure CLI Shell Script
**Resposta Correta:** A
**Explicação Técnica:** O Bicep é uma linguagem de domínio específico (DSL) declarativa desenvolvida pela Microsoft que simplifica a criação de modelos ARM para implantação de infraestrutura no Azure.

### Questão 288
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma aplicação precisa acessar uma conta de armazenamento do Azure Blob usando chaves de criptografia gerenciadas pela própria empresa e mantidas em um Azure Key Vault. Qual tipo de criptografia é esse?
**Opções:**
- A) Criptografia com Chaves Gerenciadas pelo Cliente (Customer-Managed Keys - CMK)
- B) Criptografia com Chaves Gerenciadas pela Microsoft (MMK)
- C) Criptografia de Disco BitLocker local
- D) Criptografia Transparente de Dados (TDE)
**Resposta Correta:** A
**Explicação Técnica:** A criptografia do Azure Storage dá suporte a Chaves Gerenciadas pelo Cliente (CMK), permitindo que os clientes criem, importem e gerenciem suas próprias chaves de criptografia armazenadas no Azure Key Vault.

### Questão 289
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** O que acontece com os recursos contidos em um Grupo de Recursos se um Bloqueio de Exclusão (Delete Lock / CanNotDelete) for aplicado diretamente ao Grupo de Recursos pai?
**Opções:**
- A) Todos os recursos filhos herdam o bloqueio e não podem ser excluídos
- B) Os recursos filhos não herdam o bloqueio e podem ser excluídos individualmente
- C) O bloqueio é ignorado pelos administradores
- D) O grupo de recursos é convertido automaticamente para o modo de leitura
**Resposta Correta:** A
**Explicação Técnica:** Os bloqueios de recursos no Azure seguem o princípio de herança do Resource Manager: quando você aplica um bloqueio em um escopo pai (como uma assinatura ou grupo de recursos), todos os recursos filhos herdam esse bloqueio.

### Questão 290
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual componente do Azure Load Balancer distribui o tráfego recebido nas portas públicas para as máquinas virtuais registradas no Pool de Backend?
**Opções:**
- A) Regras de Balanceamento de Carga (Load Balancing Rules)
- B) Peering de Rede
- C) Tabela de Rotas (UDR)
- D) Azure Policy
**Resposta Correta:** A
**Explicação Técnica:** As Regras de Balanceamento de Carga definem como o tráfego de entrada é mapeado a partir de um IP/porta de frontend para um pool de endereços IP de backend.

### Questão 291
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Um administrador precisa enviar logs de auditoria de várias assinaturas do Azure para um sistema SIEM de terceiros externo em tempo real. Qual recurso do Azure Monitor deve ser utilizado para transmitir esses logs?
**Opções:**
- A) Hubs de Eventos do Azure (Azure Event Hubs)
- B) Cofrinho de Serviços de Recuperação
- C) Azure Blob Storage em Camada de Arquivamento
- D) Azure Network Watcher
**Resposta Correta:** A
**Explicação Técnica:** A integração de logs do Azure Monitor com o Azure Event Hubs permite a transmissão de dados de diagnóstico e auditoria para sistemas de terceiros (como QRadar, Splunk ou SIEMs externos).

### Questão 292
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa precisa executar uma carga de trabalho de lote altamente paralela contendo centenas de tarefas computacionais de curta duração. Qual serviço gerenciado do Azure é o mais adequado para agendar e gerenciar esses trabalhos?
**Opções:**
- A) Azure Batch
- B) Instâncias de Máquinas Virtuais Individuais
- C) Azure Functions em consumo
- D) Azure Logic Apps
**Resposta Correta:** A
**Explicação Técnica:** O Azure Batch é um serviço de gerenciamento de trabalhos em lote e agendamento que escala automaticamente computação em nuvem para executar tarefas de computação de alto desempenho (HPC) e paralelas.

### Questão 293
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual ferramenta da Microsoft permite mapear um compartilhamento do Azure Files como uma letra de unidade de disco de rede (ex.: Drive Z:) em computadores locais fora do Azure?
**Opções:**
- A) Comando 'net use' / SMB via porta TCP 445
- B) Conexão RDP padrão
- C) AzCopy sync
- D) FTP no IIS
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files pode ser montado localmente via protocolo SMB 3.0 utilizando o comando  (Windows) ou none on / type overlay (rw,mode=777)
none on /dev type dev (rw,mode=0755)
none on /sys type sysfs (rw,dentry_cache_limit=1000)
none on /proc type proc (rw,dentry_cache_limit=1000)
none on /tmp type tmpfs (rw,mode=1777,uid=0,gid=0)
none on /dev/pts type devpts (rw)
none on /workspace type 9p (rw,trans=fd,rfdno=9,wfdno=9,aname=/workspace,dfltuid=1000,dfltgid=1000,dcache=1000,cache=remote_revalidating,disable_file_handle_sharing) (Linux/macOS), desde que a porta TCP 445 de saída não esteja bloqueada pelo provedor de Internet.

### Questão 294
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Como você pode garantir que o tráfego de saída de máquinas virtuais para serviços PaaS do Azure (como Azure Storage) utilize a rede de backbone otimizada da Microsoft sem passar pela Internet pública e sem necessitar de IPs privados individuais por recurso?
**Opções:**
- A) Pontos de Extremidade do Serviço da VNet (Service Endpoints)
- B) Peering Global de Rede Virtual
- C) Gateway VPN Ponto a Site
- D) Servidor DNS Privado
**Resposta Correta:** A
**Explicação Técnica:** Os Service Endpoints estendem o espaço de endereço privado da sua VNet e sua identidade para os serviços do Azure via conexões diretas na rede backbone da Microsoft.

### Questão 295
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** O que é o escopo mais alto na hierarquia de gerenciamento do Azure Resource Manager, usado para agrupar e aplicar governança (políticas e RBAC) a múltiplas assinaturas corporativas?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups)
- B) Grupos de Recursos (Resource Groups)
- C) Locatário do Entra ID (Tenant)
- D) Regiões do Azure
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento fornecem um nível de escopo acima das assinaturas, permitindo que políticas, conformidade e permissões RBAC sejam herdadas por todas as assinaturas vinculadas ao grupo.

### Questão 296
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual recurso do Azure Monitor permite definir a retenção de dados e o local central onde os logs coletados por agentes são armazenados para análise KQL?
**Opções:**
- A) Log Analytics Workspace
- B) Conta de Armazenamento Blob
- C) Azure Key Vault
- D) Application Insights Profiler
**Resposta Correta:** A
**Explicação Técnica:** O Log Analytics Workspace é o ambiente de armazenamento e gerenciamento centralizado do Azure Monitor no qual dados de log de diversas fontes são estruturados e indexados para consultas.

### Questão 297
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa alterar a quantidade de memória RAM e vCPUs de uma máquina virtual do Azure em execução. O que acontece com a VM durante o processo de alteração de tamanho (Resize)?
**Opções:**
- A) A VM é reiniciada automaticamente para aplicar a nova configuração de tamanho
- B) O tamanho é alterado a quente sem qualquer reinicialização
- C) O disco de SO é formatado e reinstalado
- D) A VM precisa ser excluída e recriada manualmente
**Resposta Correta:** A
**Explicação Técnica:** A alteração de tamanho (Resize) de uma máquina virtual no Azure exige a reinicialização da VM para que o sistema operacional reconheça as novas capacidades de hardware/vCPU e memória alocadas.

### Questão 298
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Qual funcionalidade do Azure DNS permite hospedar registros de nomes de domínio internos de uma empresa sem expô-los para consultas públicas na Internet?
**Opções:**
- A) Zonas DNS Privadas do Azure (Azure Private DNS Zones)
- B) Zonas DNS Públicas
- C) Registros MX do Microsoft 365
- D) Servidores Root do DNS Global
**Resposta Correta:** A
**Explicação Técnica:** As Zonas DNS Privadas do Azure fornecem um serviço de nomes confiável e seguro para gerenciar e resolver nomes de domínio em uma VNet sem a necessidade de implantar soluções DNS personalizadas.

### Questão 299
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual tipo de réplica do Azure Storage mantém 3 cópias síncronas dos seus dados dentro de um único data center físico em uma região do Azure?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância de Zona Geográfica (GZRS)
**Resposta Correta:** A
**Explicação Técnica:** O LRS (Locally Redundant Storage) replica seus dados três vezes dentro de um único data center físico na região primária, oferecendo proteção contra falhas em discos ou racks individuais.

### Questão 300
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa deseja impedir que qualquer usuário (inclusive administradores) exclua uma conta de armazenamento de produção que contém registros fiscais. Qual recurso deve ser aplicado diretamente à Conta de Armazenamento?
**Opções:**
- A) Bloqueio de Recurso do tipo 'CanNotDelete' (Delete Lock)
- B) Função RBAC de Leitor
- C) Política do Azure Policy com efeito audit
- D) Grupo de Gerenciamento Privado
**Resposta Correta:** A
**Explicação Técnica:** O Bloqueio de Recurso do tipo  (Delete Lock) impede que os usuários excluam o recurso, permitindo ainda que leiam e modifiquem as suas configurações ou dados.
