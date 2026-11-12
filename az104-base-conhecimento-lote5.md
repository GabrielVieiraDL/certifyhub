# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 5 (Questões 201 a 250)

Esta base de conhecimento contém as questões 201 a 250 do exame **AZ-104: Microsoft Azure Administrator** formatadas em pt-BR com nomenclatura oficial para automação e ingestão no Antigravity.

---

### Questão 201
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você possui uma assinatura do Azure contendo 100 máquinas virtuais. Você precisa garantir que todas as novas máquinas virtuais implantadas na assinatura tenham uma tag chamada "Departamento" com um valor padrão. O que você deve usar?
**Opções:**
- A) Um bloqueio de recurso (Resource Lock)
- B) Uma atribuição de Azure Policy com o efeito Append ou Modify
- C) Uma regra de Grupo de Segurança de Rede (NSG)
- D) Um grupo de gerenciamento
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com efeito Modify ou Append permite adicionar ou modificar tags automaticamente durante a implantação de recursos para garantir conformidade de governança.

### Questão 202
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua empresa precisa armazenar 50 TB de dados de backup no Azure Blob Storage. Os dados raramente serão acessados, mas quando solicitados, devem estar disponíveis em poucos segundos. Qual camada de acesso (access tier) deve ser configurada?
**Opções:**
- A) Hot Tier (Frequente)
- B) Cool Tier (Pouco Frequente)
- C) Cold Tier (Frio)
- D) Archive Tier (Aquivo)
**Resposta Correta:** B
**Explicação Técnica:** A camada Cool (Pouco Frequente) é otimizada para dados acessados raramente com retenção mínima de 30 dias, oferecendo acesso imediato (em milissegundos), ao contrário da camada Archive, que exige horas para reidratação.

### Questão 203
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você planeja implantar uma aplicação web no Azure App Service que requer alta disponibilidade em múltiplas Zonas de Disponibilidade dentro da mesma região. Qual plano de serviço do App Service (App Service Plan) mínimo é necessário?
**Opções:**
- A) Free (F1)
- B) Basic (B1)
- C) Standard (S1)
- D) Premium v3 (P1v3)
**Resposta Correta:** D
**Explicação Técnica:** O suporte a Zonas de Disponibilidade no Azure App Service exige um plano de serviço na camada Premium v2/v3 ou Isolated v2, permitindo distribuir instâncias entre zonas de disponibilidade.

### Questão 204
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você tem duas Redes Virtuais chamadas VNet1 e VNet2 na região Leste dos EUA. Você configura o Peering de Rede Virtual entre elas. Os recursos na VNet1 conseguem se comunicar com os recursos na VNet2, mas o tráfego não passa pela Internet pública. Qual backbone de rede é utilizado?
**Opções:**
- A) Rede de longa distância (WAN) da operadora de telecomunicações
- B) Backbone privado global da Microsoft
- C) Conexão VPN IPSec via Internet
- D) Roteamento de gateway público
**Resposta Correta:** B
**Explicação Técnica:** O VNet Peering conecta redes virtuais diretamente através da rede de backbone privada da Microsoft, oferecendo altíssima largura de banda e baixa latência sem trafegar pela Internet.

### Questão 205
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Sua empresa possui um Log Analytics Workspace no Azure. Você precisa criar um alerta que notifique a equipe de TI sempre que uma máquina virtual crítica ultrapassar 90% de uso de CPU por mais de 10 minutos. Qual recurso deve ser configurado?
**Opções:**
- A) Regra de Alerta do Azure Monitor vinculada a um Grupo de Ação (Action Group)
- B) Bloqueio de Recurso do tipo ReadOnly
- C) Recomendação do Azure Advisor
- D) Regra de Política do Azure (Azure Policy)
**Resposta Correta:** A
**Explicação Técnica:** As Regras de Alerta no Azure Monitor avaliam métricas ou consultas KQL e acionam Grupos de Ação (Action Groups) para enviar e-mails, SMS, webhooks ou chamadas de automação.

### Questão 206
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador precisa conceder a um grupo de usuários a capacidade de reiniciar máquinas virtuais em um Resource Group específico, sem permitir que alterem configurações de rede ou excluam as VMs. Qual função de RBAC deve ser atribuída?
**Opções:**
- A) Proprietário (Owner)
- B) Colaborador (Contributor)
- C) Colaborador de Máquina Virtual (Virtual Machine Contributor)
- D) Leitor (Reader)
**Resposta Correta:** C
**Explicação Técnica:** A função built-in Virtual Machine Contributor permite gerenciar máquinas virtuais (incluindo reiniciar e iniciar), mas não concede acesso à gestão de rede ou atribuição de direitos de acesso.

### Questão 207
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa configurar uma Conta de Armazenamento do Azure para que todas as tentativas de acesso via HTTP não criptografado sejam automaticamente rejeitadas. Qual configuração deve ser habilitada?
**Opções:**
- A) Transferência segura exigida (Secure transfer required / Require secure transfer)
- B) Habilitar armazenamento hierárquico (Data Lake Storage Gen2)
- C) Bloqueio de exclusão de recurso
- D) Armazenamento com redundância de zona (ZRS)
**Resposta Correta:** A
**Explicação Técnica:** A opção "Secure transfer required" força o uso de HTTPS para todas as chamadas de API da Conta de Armazenamento, bloqueando conexões HTTP não seguras.

### Questão 208
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa criar um conjunto de escala de máquinas virtuais (VMSS) que aumente o número de instâncias de VM automaticamente quando o uso médio de CPU ultrapassar 75%. Qual funcionalidade é responsável por isso?
**Opções:**
- A) Regra de Autoescala (Autoscale Settings / Rules)
- B) Disponibilidade em Zonas (Availability Zones)
- C) Conjunto de Disponibilidade (Availability Set)
- D) Extensão de Diagnóstico de VM
**Resposta Correta:** A
**Explicação Técnica:** As regras de Autoscale no VMSS ajustam dinamicamente a contagem de instâncias com base em métricas de desempenho (como uso de CPU ou memória) ou agendamento temporal.

### Questão 209
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma empresa deseja restringir todo o tráfego de saída de uma sub-rede para que passe por uma solução de Firewall virtual (NVA). O que deve ser criado e associado à sub-rede?
**Opções:**
- A) Uma Tabela de Rotas (Route Table) com uma Rota Definida pelo Usuário (UDR)
- B) Um Grupo de Segurança de Aplicação (ASG)
- C) Um Peering de VNet
- D) Uma regra de Azure DNS
**Resposta Correta:** A
**Explicação Técnica:** Uma Route Table contendo uma User-Defined Route (UDR) direcionando o tráfego 0.0.0.0/0 para o IP privado do Firewall (NVA) força o tunelamento de tráfego de saída.

### Questão 210
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar o Backup do Azure para proteger máquinas virtuais IaaS. Onde os pontos de recuperação de backup ficam armazenados com retenção de longo prazo e criptografia?
**Opções:**
- A) Cofre dos Serviços de Recuperação (Recovery Services Vault)
- B) Disco Gerenciado do Azure
- C) Azure Key Vault
- D) Workspace do Log Analytics
**Resposta Correta:** A
**Explicação Técnica:** O Recovery Services Vault é o repositório de gerenciamento e armazenamento de backups do Azure para VMs, bancos de dados e cargas de trabalho locais.

### Questão 211
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Sua empresa utiliza o Microsoft Entra ID. Você precisa garantir que administradores globais devam solicitar justificativa e aprovação por tempo limitado antes de assumir privilégios elevados. Qual recurso do Entra ID atende ao requisito?
**Opções:**
- A) Microsoft Entra Privileged Identity Management (PIM)
- B) Grupos de Segurança do Entra ID
- C) Políticas de Acesso Condicional
- D) Unidades Administrativas
**Resposta Correta:** A
**Explicação Técnica:** O PIM (Privileged Identity Management) permite gerenciar, controlar e monitorar o acesso a recursos críticos, oferecendo ativação de funções Just-In-Time (JIT) com aprovação.

### Questão 212
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa garantir que os arquivos armazenados em um compartilhamento do Azure Files estejam sincronizados continuamente com um servidor Windows local (on-premises). Qual serviço deve ser implantado?
**Opções:**
- A) Azure File Sync
- B) AzCopy
- C) Azure Data Box
- D) Azure Data Factory
**Resposta Correta:** A
**Explicação Técnica:** O Azure File Sync centraliza os compartilhamentos de arquivos da sua organização no Azure Files, mantendo a flexibilidade, o desempenho e a compatibilidade de um servidor de arquivos local.

### Questão 213
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma VM do Azure não consegue ser inicializada devido a uma corrupção no sistema operacional. Você precisa acessar o console da máquina para solucionar o problema sem recriar a VM. Qual ferramenta do Portal do Azure deve ser usada?
**Opções:**
- A) Console Serial (Serial Console)
- B) Bastion do Azure
- C) Conexão RDP padrão
- D) Executar Comando (Run Command)
**Resposta Correta:** A
**Explicação Técnica:** O Serial Console do Azure fornece acesso de terminal baseado em texto direto à porta serial de VMs Linux e Windows, independente do estado da rede ou SO.

### Questão 214
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa conectar com segurança os desenvolvedores remotos de sua empresa à VNet do Azure usando conexões criptografadas a partir de seus notebooks pessoais. Qual tipo de VPN deve ser configurada no Azure VPN Gateway?
**Opções:**
- A) VPN Ponto a Site (Point-to-Site - P2S)
- B) VPN Site a Site (Site-to-Site - S2S)
- C) ExpressRoute Direct
- D) Peering VNet Global
**Resposta Correta:** A
**Explicação Técnica:** A VPN Point-to-Site (P2S) permite que clientes individuais se conectem com segurança a uma VNet a partir de computadores remotos em qualquer lugar.

### Questão 215
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você quer visualizar graficamente as dependências de rede e comunicação entre máquinas virtuais e processos ativos no Azure Monitor. Qual recurso deve ser habilitado?
**Opções:**
- A) VM Insights (insights de Máquina Virtual)
- B) Azure Advisor
- C) Log de Atividades do Azure
- D) Status do Serviço (Service Health)
**Resposta Correta:** A
**Explicação Técnica:** O VM Insights inclui o mapa de dependências que visualiza conexões de rede entre processos em execução em VMs Windows/Linux e dependências externas.

### Questão 216
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual recurso de governança do Azure é usado para organizar subscrições em uma hierarquia unificada para aplicação centralizada de políticas e controle de custos?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups)
- B) Grupos de Recursos (Resource Groups)
- C) Unidades Administrativas
- D) Rótulos de Sensibilidade
**Resposta Correta:** A
**Explicação Técnica:** Os Management Groups oferecem um nível de escopo acima das assinaturas, permitindo governança centralizada com RBAC e Azure Policy em escala.

### Questão 217
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa precisa implantar uma Conta de Armazenamento com redundância geográfica e acesso de leitura secundário na região par. Qual opção de redundância de armazenamento deve ser selecionada?
**Opções:**
- A) Armazenamento com redundância geográfica e acesso de leitura (RA-GRS)
- B) Armazenamento com redundância local (LRS)
- C) Armazenamento com redundância de zona (ZRS)
- D) Armazenamento com redundância geográfica (GRS)
**Resposta Correta:** A
**Explicação Técnica:** O RA-GRS (Read-Access Geo-Redundant Storage) replica os dados para uma região secundária geograficamente distante e fornece acesso de leitura imediato aos dados secundários.

### Questão 218
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você tem uma aplicação baseada em microsserviços em contêineres e precisa de um orquestrador Kubernetes totalmente gerenciado no Azure. Qual serviço deve utilizar?
**Opções:**
- A) Serviço de Kubernetes do Azure (AKS)
- B) Instâncias de Contêiner do Azure (ACI)
- C) Registro de Contêiner do Azure (ACR)
- D) Azure App Service
**Resposta Correta:** A
**Explicação Técnica:** O AKS (Azure Kubernetes Service) é o serviço gerenciado de orquestração de contêineres Kubernetes na nuvem Azure.

### Questão 219
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa permitir que recursos em uma sub-rede privada acessem com segurança o serviço Azure SQL Database sem expor o tráfego à Internet pública e utilizando um endereço IP privado dentro da própria sub-rede. O que deve ser configurado?
**Opções:**
- A) Endpoint Privado (Private Endpoint / Azure Private Link)
- B) Gateway de NAT (NAT Gateway)
- C) Azure Front Door
- D) Regra de firewall de IP público
**Resposta Correta:** A
**Explicação Técnica:** O Private Endpoint usa um IP privado da sua VNet para conectar com segurança e de forma privada a um serviço PaaS (como Azure SQL) via Azure Private Link.

### Questão 220
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa consultar logs de auditoria e operacionais armazenados em um Log Analytics Workspace. Qual linguagem de consulta deve ser utilizada?
**Opções:**
- A) Kusto Query Language (KQL)
- B) Transact-SQL (T-SQL)
- C) PowerQuery (M)
- D) GraphQL
**Resposta Correta:** A
**Explicação Técnica:** A KQL (Kusto Query Language) é a linguagem de consulta usada no Azure Monitor e Log Analytics para analisar grandes volumes de dados de logs.

### Questão 221
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa automatizar a atribuição de funções RBAC e definições de Azure Policy em múltiplas assinaturas como um pacote de implantação repetível. Qual serviço do Azure é ideal para essa finalidade?
**Opções:**
- A) Azure Blueprints
- B) Azure Advisor
- C) Grupos de Ação
- D) Azure Resource Health
**Resposta Correta:** A
**Explicação Técnica:** O Azure Blueprints permite que engenheiros de nuvem definam um conjunto repetível de recursos do Azure (políticas, RBAC, modelos ARM) que atendem aos padrões organizacionais.

### Questão 222
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual ferramenta de linha de comando da Microsoft é recomendada para transferir terabytes de arquivos locais para o Azure Blob Storage de forma assíncrona, de alto desempenho e com suporte a retomada de download/upload?
**Opções:**
- A) AzCopy (v10)
- B) FTP Client
- C) Robocopy padrão
- D) Azure PowerShell Get-Content
**Resposta Correta:** A
**Explicação Técnica:** O AzCopy v10 é a ferramenta oficial de linha de comando otimizada para cópia de dados de alta performance para/de contas de armazenamento do Azure.

### Questão 223
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma empresa deseja executar scripts Python acionados por eventos sem provisionar servidores ou gerenciar infraestrutura subjacente. Qual serviço de computação serverless atende a essa demanda?
**Opções:**
- A) Funções do Azure (Azure Functions)
- B) Máquinas Virtuais do Azure
- C) Conjuntos de Escala de Máquinas Virtuais
- D) Host Dedicado do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Functions é a plataforma serverless orientada a eventos para execução de trechos de código sob demanda.

### Questão 224
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você quer distribuir o tráfego de entrada da Web entre um grupo de máquinas virtuais com base na URL da requisição (roteamento baseado em caminho / path-based routing). Qual balanceador deve ser usado?
**Opções:**
- A) Gateway de Aplicativo do Azure (Azure Application Gateway)
- B) Balanceador de Carga do Azure (Azure Load Balancer)
- C) Servidor DNS Privado do Azure
- D) Peering de VNet
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego da camada 7 (HTTP/HTTPS) que suporta roteamento baseado em URL e terminação TLS/SSL.

### Questão 225
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você deseja acompanhar e ser notificado sobre interrupções de serviço planejadas e não planejadas que afetem a região do Azure onde seus recursos estão implantados. Qual recurso você deve consultar?
**Opções:**
- A) Azure Service Health (Status do Serviço)
- B) Azure Advisor
- C) Azure Security Center
- D) Log Analytics Workspace
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Health fornece um painel personalizado com informações sobre a integridade dos serviços do Azure na sua região e assinaturas especificamente.

### Questão 226
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Como parte da conformidade de segurança, sua empresa exige a alteração da propriedade de recursos quando um funcionário sai da organização. Qual nível de acesso do RBAC permite gerenciar a atribuição de permissões a outros usuários?
**Opções:**
- A) Proprietário (Owner) e Administrador de Acesso Baseado em Função
- B) Colaborador (Contributor)
- C) Leitor (Reader)
- D) Usuário de Suporte
**Resposta Correta:** A
**Explicação Técnica:** A função Owner e a função Role Based Access Control Administrator permitem conceder e revogar permissões RBAC para outros usuários e identidades.

### Questão 227
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua empresa precisa impor uma política de imutabilidade em uma Conta de Armazenamento para que dados gravados não possam ser excluídos ou alterados por um período legal de 7 anos. Qual funcionalidade do Blob Storage deve ser ativada?
**Opções:**
- A) Armazenamento Imutável com Política de Retenção Baseada no Tempo (Time-Based Retention)
- B) Criptografia Server-Side com SSE
- C) Replicação LRS
- D) Redundância ZRS
**Resposta Correta:** A
**Explicação Técnica:** O armazenamento imutável para o Azure Blob Storage permite guardar dados no estado WORM (Write Once, Read Many) protegido contra exclusão e modificação durante o período definido.

### Questão 228
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você implantou um conjunto de escala de VMs (VMSS) e precisa atualizar a imagem do sistema operacional de todas as instâncias em lotes sem interromper totalmente a aplicação. Qual estratégia de atualização deve ser usada?
**Opções:**
- A) Modo de Atualização Rolante (Rolling Upgrade Policy)
- B) Recriação Manual Manual Upgrade
- C) Parada Total de Serviço
- D) Backup e Restauração em outra região
**Resposta Correta:** A
**Explicação Técnica:** A política de atualização Rolling no VMSS atualiza as instâncias em lotes/fases, garantindo que o restante das instâncias continue processando requisições.

### Questão 229
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa criar um registro DNS no Azure DNS que aponte o domínio personalizado da empresa para o endereço IP público de uma máquina virtual. Qual tipo de zona DNS deve ser criada?
**Opções:**
- A) Zona DNS Pública (Public DNS Zone)
- B) Zona DNS Privada (Private DNS Zone)
- C) Zona Inversa PTR
- D) Encaminhador Condicional
**Resposta Correta:** A
**Explicação Técnica:** As Zonas DNS Públicas no Azure DNS hospedam registros de nomes de domínio resolvidos publicamente na Internet.

### Questão 230
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Sua equipe de TI precisa automatizar tarefas de rotina no Azure usando PowerShell. Qual módulo oficial deve ser instalado nos computadores administradores?
**Opções:**
- A) Módulo Az do PowerShell (Az PowerShell module)
- B) Módulo AzureRM antigo
- C) Módulo MSOnline
- D) Azure CLI Python package
**Resposta Correta:** A
**Explicação Técnica:** O módulo Az é o conjunto de cmdlets oficial e recomendado da Microsoft para gerenciar recursos do Azure diretamente via PowerShell.

### Questão 231
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa garantir que recursos criados dentro de um Grupo de Recursos herdem automaticamente a tag de centro de custo definida no Grupo de Recursos. Como isso pode ser configurado?
**Opções:**
- A) Usando uma Azure Policy com o efeito Modify e a regra Inherit a tag from the resource group
- B) Usando um bloqueio ReadOnly
- C) Atribuindo a função Reader no escopo do grupo de recursos
- D) Através do Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** Uma regra do Azure Policy pode ser estruturada para copiar/herdar automaticamente tags do grupo de recursos pai para novos recursos criados dentro dele.

### Questão 232
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa precisa migrar 150 TB de arquivos de vídeo locais para o Azure Blob Storage, mas a conexão de Internet local possui largura de banda limitada a 10 Mbps. Qual é a solução mais rápida e eficiente?
**Opções:**
- A) Solicitar o dispositivo físico Azure Data Box
- B) Fazer upload via AzCopy pela Internet
- C) Criar uma VPN Ponto a Site
- D) Enviar arquivos via e-mail em anexos
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Box é um dispositivo robusto e seguro enviado pela Microsoft para transferência offline de grandes volumes de dados (terabytes/petabytes) para a nuvem.

### Questão 233
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você deseja garantir que as máquinas virtuais em uma sub-rede sejam distribuídas em domínios de falha físicos separados para proteger o ambiente contra falhas de rack e energia dentro do mesmo data center. O que deve ser configurado?
**Opções:**
- A) Conjunto de Disponibilidade (Availability Set)
- B) Grupo de Gerenciamento
- C) Peering de VNet Global
- D) Tabela de Rotas
**Resposta Correta:** A
**Explicação Técnica:** Um Availability Set garante que as VMs implantadas nele sejam separadas em múltiplos domínios de falha (racks/energia) e domínios de atualização no mesmo data center.

### Questão 234
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa filtrar o tráfego de entrada e saída em nível de sub-rede ou de interface de rede (NIC) de uma máquina virtual usando regras com prioridade, IP de origem/destino e portas. Qual recurso deve ser associado?
**Opções:**
- A) Grupo de Segurança de Rede (Network Security Group - NSG)
- B) Tabela de Rotas (UDR)
- C) Azure DNS
- D) ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O NSG (Network Security Group) contém regras de segurança que permitem ou negam o tráfego de rede de entrada e saída para adaptadores de rede (NIC) ou sub-redes.

### Questão 235
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual ferramenta do Azure permite estimar a redução de custos de carga de trabalho antes de migrar de um ambiente local para a nuvem Azure?
**Opções:**
- A) Calculadora de Custo Total de Propriedade (TCO Calculator)
- B) Calculadora de Preços do Azure
- C) Gerenciamento de Custos do Azure (Cost Management)
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** A Calculadora de TCO (Total Cost of Ownership) ajuda a comparar os custos de manter a infraestrutura local vs. migrar para o Azure.

### Questão 236
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual é o termo utilizado no Microsoft Entra ID para um diretório dedicado que representa uma organização específica no ecossistema de nuvem?
**Opções:**
- A) Tenant (Locatário)
- B) Subscrição
- C) Grupo de Recursos
- D) Unidade Organizacional
**Resposta Correta:** A
**Explicação Técnica:** Um Tenant (Locatário) é uma instância reservada do Microsoft Entra ID que uma organização recebe quando assina serviços de nuvem da Microsoft.

### Questão 237
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa permitir que uma aplicação web rodando em um servidor externo acesse temporariamente arquivos em um contêiner do Blob Storage sem compartilhar as chaves de acesso mestres da conta. O que deve ser gerado?
**Opções:**
- A) Assinatura de Acesso Compartilhado (Shared Access Signature - SAS)
- B) Chave Primária da Conta
- C) Certificado SSL
- D) Chave Pública RSA
**Resposta Correta:** A
**Explicação Técnica:** Uma SAS (Shared Access Signature) fornece acesso delegado seguro a recursos na sua conta de armazenamento com permissões refinadas e prazo de expiração.

### Questão 238
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um contêiner Docker isolado em segundos sem a necessidade de gerenciar nós de servidor ou clusters de orquestração. Qual serviço é o mais simples para este cenário?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Serviço de Kubernetes do Azure (AKS)
- C) Conjunto de Escala de VMs
- D) Máquinas Virtuais IaaS
**Resposta Correta:** A
**Explicação Técnica:** O ACI (Azure Container Instances) é a solução mais rápida para executar contêineres isolados sob demanda no Azure sem provisionar infraestrutura.

### Questão 239
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Sua empresa precisa de uma conexão de rede dedicada, de alta velocidade e com latência ultra-baixa entre a rede local corporativa e o data center do Azure que bypassa a Internet pública. Qual serviço atende ao requisito?
**Opções:**
- A) Azure ExpressRoute
- B) VPN Site a Site (S2S)
- C) VNet Peering
- D) Gateway de NAT
**Resposta Correta:** A
**Explicação Técnica:** O Azure ExpressRoute cria conexões privadas e dedicadas de alta velocidade entre a infraestrutura local e os data centers do Azure sem trafegar pela Internet.

### Questão 240
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa analisar os custos históricos do Azure, criar previsões de gastos e definir alertas de orçamento. Qual recurso no Portal do Azure deve utilizar?
**Opções:**
- A) Gerenciamento de Custos e Faturamento (Azure Cost Management + Billing)
- B) Azure Advisor
- C) Azure Monitor
- D) Log Analytics
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cost Management + Billing é a suíte de ferramentas para monitoramento de custos, análise de faturamento e configuração de orçamentos e alertas.

### Questão 241
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa atribuir permissões para que um usuário possa ler e gravar arquivos em uma conta de armazenamento, mas não possa alterar as configurações de rede ou excluir a conta. Qual função RBAC deve ser concedida?
**Opções:**
- A) Colaborador de Dados do Blob de Armazenamento (Storage Blob Data Contributor)
- B) Colaborador de Conta de Armazenamento (Storage Account Contributor)
- C) Leitor (Reader)
- D) Proprietário (Owner)
**Resposta Correta:** A
**Explicação Técnica:** A função Storage Blob Data Contributor concede acesso de leitura, gravação e exclusão ao plano de dados dos blobs, sem conceder controle de gerenciamento na conta.

### Questão 242
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual opção de redundância de armazenamento do Azure copia os dados de maneira síncrona três vezes dentro de três Zonas de Disponibilidade separadas na região primária?
**Opções:**
- A) Armazenamento com Redundância de Zona (ZRS)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Read-Access GRS
**Resposta Correta:** A
**Explicação Técnica:** O ZRS (Zone-Redundant Storage) replica seus dados síncronamente em três zonas de disponibilidade do Azure na mesma região primária.

### Questão 243
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você tem 5 Máquinas Virtuais no Azure e deseja garantir que o tráfego de entrada HTTP/HTTPS seja distribuído igualmente entre elas com verificação de integridade (health probe). Qual recurso de camada 4 deve ser utilizado?
**Opções:**
- A) Balanceador de Carga do Azure (Azure Load Balancer)
- B) Azure Application Gateway
- C) Azure DNS
- D) Tabela de Rotas
**Resposta Correta:** A
**Explicação Técnica:** O Azure Load Balancer opera na Camada 4 do modelo OSI (TCP/UDP) e distribui o tráfego de entrada entre instâncias em um pool de back-end com verificações de integridade.

### Questão 244
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa restringir que máquinas virtuais de uma sub-rede acessem a Internet pública para download de atualizações, enquanto permite tráfego de entrada apenas de IPs confiáveis. Qual componente gerencia essas regras?
**Opções:**
- A) Grupo de Segurança de Rede (NSG)
- B) Peering de VNet
- C) ExpressRoute
- D) Tabela de Rotas Padrão
**Resposta Correta:** A
**Explicação Técnica:** O NSG permite criar regras inbound e outbound refinadas com base em IP, porta e protocolo para controlar o tráfego de rede.

### Questão 245
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual funcionalidade do Azure Monitor permite coletar logs de desempenho e eventos do sistema operacional de máquinas virtuais e enviá-los para um Log Analytics Workspace?
**Opções:**
- A) Agente do Azure Monitor (Azure Monitor Agent - AMA) com Regras de Coleta de Dados (DCR)
- B) Extension Network Watcher
- C) Azure Advisor
- D) Azure Security Center
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA) utiliza Data Collection Rules (DCR) para definir com precisão quais dados coletar do sistema operacional e para onde enviá-los.

### Questão 246
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual recurso do Microsoft Entra ID permite estender a autenticação para usuários externos (clientes ou parceiros) usando suas próprias identidades sociais ou corporativas (como Google, Facebook ou SAML)?
**Opções:**
- A) Microsoft Entra External ID (B2B / B2C)
- B) Unidades Administrativas
- C) PIM
- D) Identidades Gerenciadas
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Entra External ID (B2B/B2C) permite colaborar com usuários externos e clientes gerenciando autenticação com identidades externas.

### Questão 247
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma empresa precisa garantir que o armazenamento de logs no Blob Storage seja automaticamente movido para a camada Archive após 90 dias e excluído após 365 dias. Qual recurso automatiza esse ciclo?
**Opções:**
- A) Gerenciamento do Ciclo de Vida do Armazenamento (Lifecycle Management)
- B) AzCopy
- C) Azure Backup
- D) Soft Delete
**Resposta Correta:** A
**Explicação Técnica:** As regras de Lifecycle Management automatizam a transição de dados entre as camadas Hot, Cool e Archive e a exclusão final com base na idade dos arquivos.

### Questão 248
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa executar um contêiner de longa duração que requer suporte a múltiplos nós e balanceamento de carga automático no Kubernetes. Qual serviço é mais adequado?
**Opções:**
- A) Serviço de Kubernetes do Azure (AKS)
- B) Instâncias de Contêiner do Azure (ACI)
- C) Azure Functions
- D) App Service Plan Free
**Resposta Correta:** A
**Explicação Técnica:** O AKS é o orquestrador nativo recomendado para aplicações de contêiner complexas, de alta disponibilidade e grande escala.

### Questão 249
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa de uma solução que resolva nomes de domínio de máquinas virtuais internas dentro de uma Rede Virtual sem expor os registros à Internet. O que deve usar?
**Opções:**
- A) Zona DNS Privada do Azure (Azure Private DNS Zone)
- B) Zona DNS Pública
- C) Servidor DNS externo
- D) Arquivo Hosts local
**Resposta Correta:** A
**Explicação Técnica:** As Zonas DNS Privadas do Azure fornecem um serviço DNS confiável e seguro para gerenciar e resolver nomes de domínio em uma VNet sem necessidade de servidores DNS personalizados.

### Questão 250
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você deseja visualizar o histórico de todas as alterações administrativas e operacionais (como criação, modificação e exclusão de recursos) realizadas na sua assinatura do Azure nos últimos 90 dias. Qual log deve consultar?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Log de Diagnóstico da VM
- C) Log do Entra ID
- D) Log de Segurança do Windows
**Resposta Correta:** A
**Explicação Técnica:** O Azure Activity Log registra todos os eventos no nível de plano de controle (ARM), incluindo quem criou, modificou ou excluiu recursos na assinatura.

