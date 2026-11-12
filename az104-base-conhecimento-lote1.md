# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 1 (Questões 001 a 050)

Esta base de conhecimento contém as questões do exame **AZ-104: Microsoft Azure Administrator** extraídas e adaptadas para o ecossistema de agentes de IA no Antigravity, traduzidas para o Português do Brasil (pt-BR) com a nomenclatura oficial da Microsoft.

---

### Questão 001
**Domínio:** Gerenciar Identidades e Governança do Azure (Gerenciamento de Recursos & Tags)
**Enunciado:** Sua empresa possui vários departamentos e cada departamento possui uma quantidade de máquinas virtuais (VMs). A empresa possui uma assinatura do Azure contendo um grupo de recursos chamado RG1, onde todas as VMs estão localizadas. Você precisa associar cada máquina virtual ao seu respectivo departamento. O que você deve fazer?
**Opções:**
- A) Criar Grupos de Gerenciamento do Azure para cada departamento.
- B) Criar um grupo de recursos para cada departamento.
- C) Atribuir Tags às máquinas virtuais.
- D) Modificar as configurações individuais das máquinas virtuais.
**Resposta Correta:** C
**Explicação Técnica:** As Tags do Azure permitem associar metadados em formato chave-valor (ex.: `Departamento: Financeiro`) aos recursos para organizar a visualização, gestão de custos e agrupamento lógico sem precisar mover os recursos de grupo de recursos ou assinatura.

---

### Questão 002
**Domínio:** Gerenciar Identidades e Governança do Azure (Microsoft Entra ID / Acesso Condicional)
**Enunciado:** Sua empresa possui uma assinatura do Microsoft Entra ID (anteriormente Azure AD). Você deseja implementar uma política de Acesso Condicional exigindo que membros do grupo Administradores Globais utilizem Autenticação Multifator (MFA) e dispositivos ingressados no Entra ID ao se conectarem de locais não confiáveis.
Solução: Você acessa o Portal do Azure para alterar o controle de concessão (grant control) da política de Acesso Condicional do Entra ID.
Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** Os controles de concessão (*grant controls*) nas políticas de Acesso Condicional do Microsoft Entra ID permitem impor requisitos de segurança específicos (como exigir MFA e exigir dispositivo marcado como em conformidade ou ingressado no diretório) para conceder ou bloquear o acesso.

---

### Questão 003
**Domínio:** Gerenciar Identidades e Governança do Azure (Microsoft 365 Groups & Expiração)
**Enunciado:** Você possui um locatário do Microsoft 365 e um locatário do Microsoft Entra ID chamado contoso.com. Você planeja conceder a três usuários (User1, User2 e User3) acesso a uma biblioteca de documentos temporária do SharePoint chamada Library1. Você precisa criar grupos para os usuários garantindo que os grupos sejam excluídos automaticamente após 180 dias. Quais dois tipos de grupo você deve criar? (Cada resposta correta apresenta uma solução completa).
**Opções:**
- A) Um grupo do Microsoft 365 que utiliza o tipo de associação Atribuída (Assigned).
- B) Um grupo de Segurança que utiliza o tipo de associação Atribuída (Assigned).
- C) Um grupo do Microsoft 365 que utiliza o tipo de associação de Usuário Dinâmico (Dynamic User).
- D) Um grupo de Segurança que utiliza o tipo de associação de Usuário Dinâmico (Dynamic User).
- E) Um grupo de Segurança que utiliza o tipo de associação de Dispositivo Dinâmico (Dynamic Device).
**Resposta Correta:** A, C
**Explicação Técnica:** Políticas de expiração automática de grupos baseadas em tempo (como 180 dias) são suportadas exclusivamente em Grupos do Microsoft 365 no Entra ID. Grupos de Segurança tradicionais não suportam políticas de expiração de ciclo de vida automática.

---

### Questão 004
**Domínio:** Monitorar e Proteger Recursos do Azure (Azure Monitor & Alertas ITSM)
**Enunciado:** Você possui uma assinatura do Azure chamada Subscription1 e uma implantação local do Microsoft System Center Service Manager. A Subscription1 contém uma máquina virtual chamada VM1. Você precisa garantir que um alerta seja gerado no Service Manager quando a quantidade de memória disponível na VM1 for inferior a 10 por cento. O que você deve fazer primeiro?
**Opções:**
- A) Criar um runbook de automação.
- B) Implantar um aplicativo de função (Function App).
- C) Implantar o Conector de Gerenciamento de Serviços de TI (ITSM Connector).
- D) Criar uma notificação.
**Resposta Correta:** C
**Explicação Técnica:** O Conector ITSM (IT Service Management Connector) permite conectar o Azure Monitor a ferramentas de ITSM suportadas (como o Microsoft System Center Service Manager), gerando itens de trabalho e tickets de incidente automaticamente com base nos alertas acionados no Azure.

---

### Questão 005
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure DNS & Verificação de Domínio)
**Enunciado:** Você possui um locatário do Microsoft Entra ID chamado contosocloud.onmicrosoft.com e uma zona DNS pública para contoso.com. Você adiciona contoso.com como um nome de domínio personalizado no Entra ID. Você precisa garantir que o Azure consiga verificar a propriedade do nome de domínio. Qual tipo de registro DNS você deve criar na sua zona DNS pública?
**Opções:**
- A) MX
- B) NSEC
- C) PTR
- D) RRSIG
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Entra ID exige a validação da propriedade do domínio personalizado criando um registro DNS do tipo TXT ou do tipo MX na zona DNS pública do domínio. Entre as opções apresentadas, a alternativa A (MX) é o tipo válido para verificação.

---

### Questão 006
**Domínio:** Gerenciar Identidades e Governança do Azure (RBAC & Papéis Integrados)
**Enunciado:** Sua empresa possui um grupo chamado Developers e um grupo de recursos chamado Dev. Você precisa fornecer ao grupo Developers a capacidade de criar aplicativos lógicos (Logic Apps) no grupo de recursos Dev.
Solução: Na Subscription1, você atribui a função "DevTest Labs User" ao grupo Developers.
Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** A função *DevTest Labs User* permite apenas conectar, iniciar, reiniciar e desligar máquinas virtuais dentro do Azure DevTest Labs. Para permitir a criação e gerenciamento de Logic Apps, a função apropriada seria *Logic App Contributor* (ou *Contributor* no escopo do grupo de recursos).

---

### Questão 007
**Domínio:** Implementar e Gerenciar Armazenamento (Azure DNS / Subdomínios)
**Enunciado:** Você possui uma zona DNS do Azure chamada adatum.com. Você precisa delegar um subdomínio chamado research.adatum.com para um servidor DNS diferente hospedado no Azure. O que você deve fazer?
**Opções:**
- A) Criar um registro NS chamado "research" na zona adatum.com.
- B) Criar um registro PTR chamado "research" na zona adatum.com.
- C) Modificar o registro SOA de adatum.com.
- D) Criar um registro A chamado "*.research" na zona adatum.com.
**Resposta Correta:** A
**Explicação Técnica:** Para delegar a autoridade de resolução de um subdomínio (ex.: `research.adatum.com`) para outros servidores de nomes (Name Servers), cria-se um registro do tipo NS (Name Server) na zona DNS pai (`adatum.com`) especificando os servidores DNS do subdomínio.

---

### Questão 008
**Domínio:** Gerenciar Identidades e Governança do Azure (Microsoft Entra ID / Custom Domain)
**Enunciado:** Você possui um locatário do Entra ID com o domínio contoso.onmicrosoft.com e adquiriu o domínio contoso.com em um registrador de terceiros. Você precisa configurar o Entra ID para permitir a criação de usuários com o sufixo @contoso.com. Quais três ações você deve executar em sequência?
**Opções:**
- A) 1. Adicionar nome personalizado no Entra ID -> 2. Adicionar registro DNS no registrador público -> 3. Verificar o domínio no Entra ID.
- B) 1. Criar zona DNS no Azure -> 2. Configurar marca da empresa -> 3. Verificar o domínio.
- C) 1. Adicionar locatário -> 2. Adicionar registro DNS público -> 3. Configurar marca.
- D) 1. Verificar o domínio -> 2. Criar zona DNS -> 3. Adicionar nome personalizado.
**Resposta Correta:** A
**Explicação Técnica:** O fluxo padrão do Microsoft Entra ID para adição de domínios personalizados consiste em: (1) Adicionar o nome do domínio no portal do Entra ID, (2) Criar o registro TXT/MX no registrador DNS do domínio público para provar a posse, e (3) Clicar em "Verificar" no portal do Entra ID.

---

### Questão 009
**Domínio:** Monitorar e Proteger Recursos do Azure (Log Analytics Workspace & KQL)
**Enunciado:** Você possui uma assinatura do Azure com um Log Analytics Workspace chamado Workspace1. Você precisa consultar eventos de erro armazenados na tabela de eventos chamada Event. Qual consulta Kusto (KQL) deve ser executada?
**Opções:**
- A) Get-Event Event | where {$_.EventType == "error"}
- B) Event | search "error"
- C) select * from Event where EventType == "error"
- D) search in (Event) * | where EventType == "error"
**Resposta Correta:** B
**Explicação Técnica:** No Kusto Query Language (KQL) do Log Analytics, o operador `search` permite realizar buscas por termos de texto em tabelas ou colunas. A sintaxe `Event | search "error"` busca pela palavra "error" em todos os campos da tabela Event.

---

### Questão 010
**Domínio:** Configurar e Gerenciar Redes Virtuais (Private Endpoints & Backbone Microsoft)
**Enunciado:** Sua rede local possui um Gateway VPN conectado a uma assinatura do Azure contendo uma VM (VM1) e uma Conta de Armazenamento (storage1). Você precisa garantir que todo o tráfego da VM1 para a storage1 trafegue exclusivamente através da rede backbone privada da Microsoft, sem passar pela Internet pública. O que você deve configurar?
**Opções:**
- A) Azure AD Application Proxy
- B) Endpoints Privados (Private Endpoints)
- C) Um Grupo de Segurança de Rede (NSG)
- D) Azure Peering Service
**Resposta Correta:** B
**Explicação Técnica:** Um Endpoint Privado (Private Endpoint) atribui um endereço IP privado da sua Rede Virtual (VNet) à Conta de Armazenamento, garantindo que todo o tráfego entre os recursos e o serviço de armazenamento trafegue 100% dentro do backbone seguro e privado da Microsoft.

---

### Questão 011
**Domínio:** Configurar e Gerenciar Redes Virtuais (Private Endpoints entre Regiões)
**Enunciado:** Você possui uma assinatura contendo a máquina virtual VM1 na região East US e uma Conta de Armazenamento storage1 na região West US. Você precisa garantir que as transferências de dados entre a storage1 e a VM1 NÃO trafeguem pela Internet pública. O que deve ser configurado para a storage1?
**Opções:**
- A) Proteção de Dados (Data Protection)
- B) Um Endpoint Privado (Private Endpoint)
- C) Acesso de rede pública nas configurações de Firewalls e Redes Virtuais
- D) Uma Assinatura de Acesso Compartilhado (SAS)
**Resposta Correta:** B
**Explicação Técnica:** Os Endpoints Privados do Azure permitem conexões privadas para serviços PaaS (como Azure Storage) mesmo entre diferentes regiões do Azure via rede backbone global da Microsoft.

---

### Questão 012
**Domínio:** Implementar e Gerenciar Armazenamento (Azure Import/Export Service)
**Enunciado:** Sua empresa possui um servidor local chamado Server1 rodando Windows Server 2016 com 2 TB de dados. Você precisa transferir esses dados para uma Conta de Armazenamento no Azure utilizando o serviço Azure Import/Export. Em qual ordem as ações devem ser executadas?
**Opções:**
- A) 1. Preparar os discos com a ferramenta WAImportExport -> 2. Criar um trabalho de importação no portal -> 3. Enviar os discos para o data center do Azure -> 4. Acompanhar a cópia dos dados.
- B) 1. Enviar os discos -> 2. Criar o trabalho no portal -> 3. Executar o Azure Data Factory.
- C) 1. Criar a conta de armazenamento -> 2. Instalar o AzCopy -> 3. Copiar via rede.
- D) 1. Executar o Azure Sync -> 2. Mover o servidor -> 3. Desligar o Server1.
**Resposta Correta:** A
**Explicação Técnica:** O fluxo do serviço Azure Import/Export para grandes volumes de dados físicos consiste em preparar os discos rígidos locais criptografados com a ferramenta `WAImportExport`, criar o trabalho no Portal do Azure, despachar os discos fisicamente para a Microsoft e monitorar a conclusão da importação.

---

### Questão 013
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (Azure Backup & Vault Region)
**Enunciado:** Você possui uma assinatura com a máquina virtual VM1 na região East US e um Cofre dos Serviços de Recuperação (Recovery Services Vault) chamado Vault1 na região East US. Você precisa configurar o backup da VM1. Qual é a regra geográfica para associação de cofres de backup a máquinas virtuais?
**Opções:**
- A) A VM e o Recovery Services Vault devem obrigatoriamente estar localizados na mesma região do Azure.
- B) O Recovery Services Vault pode estar em qualquer região global.
- C) O cofre deve ser criado na região emparelhada (Paired Region).
- D) Cofres de backup só funcionam em regiões com Zonas de Disponibilidade.
**Resposta Correta:** A
**Explicação Técnica:** No Azure Backup, para realizar o backup de máquinas virtuais de infraestrutura (IaaS), o Recovery Services Vault deve estar localizado exatamente na mesma região geográfica da máquina virtual que será protegida.

---

### Questão 014
**Domínio:** Implementar e Gerenciar Armazenamento (AzCopy & Suporte Multiplataforma)
**Enunciado:** Você possui uma Conta de Armazenamento chamada storage1 e dispositivos de desenvolvedor executando Windows 10, Linux (Ubuntu) e macOS. De quais desses dispositivos você pode utilizar a ferramenta de linha de comando AzCopy para copiar dados para a storage1?
**Opções:**
- A) Apenas no dispositivo Windows 10.
- B) Dispositivos Windows 10, Linux e macOS.
- C) Apenas em dispositivos Windows 10 e Linux.
- D) Apenas em dispositivos Windows 10 e macOS.
**Resposta Correta:** B
**Explicação Técnica:** A ferramenta de linha de comando AzCopy v10 é multiplataforma e possui suporte nativo para os sistemas operacionais Windows, Linux e macOS.

---

### Questão 015
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (Azure App Service / Slots de Implantação)
**Enunciado:** Você possui um aplicativo Web do Azure App Service chamado App1 contendo um slot de produção (webapp1-prod) e um slot de teste (webapp1-test). Você testa alterações no slot de teste, realiza o backup e efetua a troca (swap) entre os slots. Logo após a troca, percebe que a nova versão em produção está apresentando problemas de desempenho. Como você deve reverter a implantação para a versão anterior o mais rápido possível?
**Opções:**
- A) Efetuar a implantação novamente a partir do código fonte.
- B) Efetuar uma nova troca (swap) entre os slots de implantação.
- C) Clonar o aplicativo App1.
- D) Restaurar o backup do App1.
**Resposta Correta:** B
**Explicação Técnica:** A operação de troca (*swap*) entre slots de implantação no App Service apenas altera os endereços IP virtuais e o roteamento de tráfego entre os slots. Caso surjam problemas após a troca, a reversão é instantânea executando outro *swap* para retornar a versão antiga ao slot de produção.

---

### Questão 016
**Domínio:** Configurar e Gerenciar Redes Virtuais (Peering de VNets & Endereçamento IP)
**Enunciado:** Você possui a VNet1 (espaço de endereçamento 10.11.0.0/16, sub-rede 10.11.0.0/17 em West US), VNet2 (10.11.0.0/17 em West US) e VNet3 (10.10.0.0/22 em East US). Com quais dessas redes virtuais você pode estabelecer um Peering de Rede Virtual (VNet Peering) a partir da VNet1?
**Opções:**
- A) Apenas com a VNet3, pois a VNet2 possui um espaço de endereçamento IP sobreposto com a VNet1.
- B) Apenas com a VNet2.
- C) Com a VNet2 e com a VNet3 simultaneamente.
- D) Com nenhuma das redes.
**Resposta Correta:** A
**Explicação Técnica:** Um requisito obrigatório e estrito do Peering de Rede Virtual no Azure é que os espaços de endereçamento IP das duas redes virtuais conectadas **não podem se sobrepor**. Como VNet1 (10.11.0.0/16) engloba o bloco da VNet2 (10.11.0.0/17), o peering entre VNet1 e VNet2 é bloqueado.

---

### Questão 017
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (Azure Container Instances & Redes Privadas)
**Enunciado:** Você está criando uma nova Instância de Contêiner do Azure (ACI) chamada cont1 com sistema operacional Windows. Ao tentar selecionar a opção de rede Privada (Private networking), percebe que ela está indisponível. Qual configuração você deve alterar para habilitar a integração com rede privada na ACI?
**Opções:**
- A) Quantidade de Memória (GiB).
- B) Tipo de Sistema Operacional (OS type) de Windows para Linux.
- C) Quantidade de núcleos de CPU.
- D) SKU do contêiner.
**Resposta Correta:** B
**Explicação Técnica:** No Azure Container Instances (ACI), o suporte a redes virtuais privadas (VNet Integration / delegada) exige que o grupo de contêineres utilize o sistema operacional Linux.

---

### Questão 018
**Domínio:** Monitorar e Proteger Recursos do Azure (Azure Backup & Restauração de Arquivos de VM)
**Enunciado:** Você possui uma máquina virtual Linux protegida pelo Azure Backup. Há uma semana, dois arquivos foram excluídos da VM. Você precisa restaurar esses dois arquivos excluídos para um computador local executando Windows Server 2016 o mais rápido possível sem restaurar a VM inteira. O que deve ser utilizado?
**Opções:**
- A) O recurso File Recovery do Azure Backup (que gera um script de montagem de volume via iSCSI).
- B) Restaurar os discos da VM para uma conta de armazenamento e montar manualmente.
- C) Executar um failover de recuperação de site (Azure Site Recovery).
- D) Baixar a imagem VHD completa e extrair com o 7-Zip.
**Resposta Correta:** A
**Explicação Técnica:** O recurso *File Recovery* do Azure Backup permite baixar um script executável que monta o ponto de recuperação da VM diretamente no computador como um volume iSCSI temporário, permitindo navegar e copiar arquivos individuais rapidamente.

---

### Questão 019
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure Bastion / Proteção de Recursos)
**Enunciado:** Uma assinatura do Azure contém uma máquina virtual (VM1), um aplicativo web do App Service (App1) e um domínio do Microsoft Entra Domain Services. Todos estão conectados à VNet1. Você planeja implantar um host do Azure Bastion (Bastion1) na VNet1. QUAIS desses recursos podem ser protegidos e acessados com segurança através do Bastion1?
**Opções:**
- A) Apenas a máquina virtual VM1.
- B) Apenas o aplicativo web App1.
- C) Apenas o domínio do Entra Domain Services.
- D) Todos os três recursos (VM1, App1 e Entra DS).
**Resposta Correta:** A
**Explicação Técnica:** O Azure Bastion é um serviço de acesso gerenciado projetado especificamente para fornecer conectividade RDP e SSH segura e sem suporte a IP público para máquinas virtuais (VMs) conectadas a uma Rede Virtual via navegador.

---

### Questão 020
**Domínio:** Monitorar e Proteger Recursos do Azure (Log Analytics Workspace & Auditoria Centralizada)
**Enunciado:** Sua empresa possui um locatário do Microsoft Entra ID vinculado a 10 assinaturas do Azure. Você precisa monitorar centralidamente as atividades dos usuários e os logs de auditoria de todas as 10 assinaturas em um único painel. Qual recurso você deve utilizar?
**Opções:**
- A) Filtros de Log de Atividade (Activity Log filters).
- B) Um Log Analytics Workspace com as configurações de diagnóstico das assinaturas apontadas para ele.
- C) Azure Application Insights Profiler.
- D) Análises de Acesso (Access Reviews).
**Resposta Correta:** B
**Explicação Técnica:** Ao configurar as definições de diagnóstico (*Diagnostic Settings*) no nível das assinaturas do Azure, é possível enviar todos os Logs de Atividade (*Activity Logs*) para um único Log Analytics Workspace centralizado, permitindo executar consultas KQL e criar alertas unificados.

---

### Questão 021
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure Load Balancer & Persistência de Sessão)
**Enunciado:** Você possui cinco máquinas virtuais configuradas como servidores Web atrás de um Azure Load Balancer (LB1). Você precisa garantir que todas as requisições subsequentes de um mesmo visitante durante a navegação sejam sempre direcionadas para o mesmo servidor Web. O que deve ser configurado no Load Balancer?
**Opções:**
- A) Definir a Persistência de Sessão para IP do Cliente (Client IP) ou IP e Protocolo do Cliente.
- B) Definir o tempo limite de ociosidade (Idle Time-out) para 20 minutos.
- C) Alterar o protocolo de teste de integridade (Health Probe) para UDP.
- D) Habilitar o IP Flutuante (Floating IP).
**Resposta Correta:** A
**Explicação Técnica:** A Persistência de Sessão (*Session Persistence* ou *Sticky Sessions*) no Azure Load Balancer utiliza uma tupla de 2 elementos (IP de origem e IP de destino) ou 3 elementos (IP de origem, IP de destino e protocolo) para garantir que o tráfego do mesmo cliente seja roteado sempre para a mesma instância no backend.

---

### Questão 022
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (VM Scale Sets & Extensão DSC)
**Enunciado:** Você planeja automatizar a implantação de um Conjunto de Escala de Máquinas Virtuais (VMSS) executando Windows Server 2019 utilizando um modelo ARM. Você precisa garantir que o servidor web NGINX seja instalado e configurado automaticamente em todas as instâncias da VM no momento em que forem provisionadas. O que você deve incluir no modelo ARM?
**Opções:**
- A) A extensão de Configuração de Estado Desejado (Desired State Configuration - DSC) ou a Extensão de Script Personalizado (Custom Script Extension).
- B) O cmdlet Publish-AzVMDscConfiguration.
- C) Um perfil de configuração do Microsoft Endpoint Manager.
- D) O Azure Application Insights.
**Resposta Correta:** A
**Explicação Técnica:** Extensões de VM como a *Desired State Configuration (DSC)* ou a *Custom Script Extension* permitem automatizar a instalação de softwares, papéis de servidor (como IIS ou NGINX) e configurações de pós-implantação diretamente durante o ciclo de provisionamento dos VMSS.

---

### Questão 023
**Domínio:** Implementar e Gerenciar Armazenamento (Lifecycle Management Rules)
**Enunciado:** Você possui uma Conta de Armazenamento General-Purpose v2 (storage1) contendo um contêiner de blobs. Você precisa criar uma regra de Gerenciamento de Ciclo de Vida que mova automaticamente os blobs não acessados há mais de 90 dias para a camada de armazenamento de menor custo (Archive). Quais contas de armazenamento suportam regras de ciclo de vida de blob?
**Opções:**
- A) Contas StorageV2 (General Purpose v2), BlobStorage e BlockBlobStorage.
- B) Apenas contas do tipo FileStorage.
- C) Apenas contas do tipo StorageV1 (General Purpose v1).
- D) Qualquer conta de armazenamento sem restrições.
**Resposta Correta:** A
**Explicação Técnica:** As regras de Gerenciamento de Ciclo de Vida do Azure Blob Storage suportam contas de armazenamento das categorias StorageV2 (General Purpose v2), BlobStorage e BlockBlobStorage de desempenho Premium.

---

### Questão 024
**Domínio:** Configurar e Gerenciar Redes Virtuais (Network Watcher & IP Flow Verify)
**Enunciado:** Uma máquina virtual no Azure perdeu a capacidade de se comunicar com um banco de dados externo. Você suspeita que uma regra de segurança de rede esteja bloqueando os pacotes. Qual recurso do Azure Network Watcher você deve utilizar para identificar a regra de NSG responsável pelo bloqueio?
**Opções:**
- A) Verificação de Fluxo de IP (IP Flow Verify).
- B) Diagnóstico de Conexão (Connection Troubleshoot).
- C) Captura de Pacotes (Packet Capture).
- D) Visualizador de Topologia (Topology).
**Resposta Correta:** A
**Explicação Técnica:** O recurso *IP Flow Verify* do Network Watcher testa o tráfego de rede fornecendo IP de origem/destino, porta e protocolo. Ele informa se a conexão foi permitida ou negada e indica o nome exato da regra de Grupo de Segurança de Rede (NSG) responsável pela decisão.

---

### Questão 025
**Domínio:** Gerenciar Identidades e Governança do Azure (Resource Locks & CanNotDelete)
**Enunciado:** Você possui um Grupo de Recursos crítico no Azure com um Bloqueio de Recurso do tipo Exclusão (*CanNotDelete / Delete Lock*) aplicado. Um administrador precisa atualizar as configurações de uma máquina virtual e excluir um disco não utilizado dentro desse grupo de recursos. Quais ações o bloqueio permite e impede?
**Opções:**
- A) O bloqueio permite leitura e modificação de recursos (como alterar a VM), mas impede estritamente a exclusão de qualquer recurso contido no grupo até que o bloqueio seja removido.
- B) O bloqueio impede a leitura e a modificação de qualquer recurso.
- C) O bloqueio impede o acesso apenas para usuários não administradores.
- D) O bloqueio converte todas as permissões para somente leitura.
**Resposta Correta:** A
**Explicação Técnica:** Um bloqueio do tipo *CanNotDelete* permite que usuários autorizados leiam e modifiquem o recurso, mas impede que qualquer pessoa exclua o recurso ou seus componentes filhos até que a trava seja explicitamente removida.

---

### Questão 026
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure Private DNS Zones & Auto Registration)
**Enunciado:** Você cria uma zona DNS privada do Azure chamada contoso.com e vincula a zona a uma Rede Virtual (VNet1) habilitando a opção de Registro Automático (Auto Registration). O que acontece com os registros A das máquinas virtuais implantadas na VNet1?
**Opções:**
- A) Os registros A das VMs na VNet1 são criados e atualizados automaticamente na zona DNS privada quando as VMs são provisionadas ou alteram seu IP privado.
- B) Os registros A devem ser cadastrados manualmente via PowerShell.
- C) Apenas registros CNAME são criados.
- D) Os registros são publicados no DNS público da Internet.
**Resposta Correta:** A
**Explicação Técnica:** A funcionalidade de Auto-registro (*Auto Registration*) em Zonas DNS Privadas do Azure cria e gerencia automaticamente os registros DNS do tipo A para as máquinas virtuais conectadas à VNet vinculada, simplificando a resolução de nomes interna.

---

### Questão 027
**Domínio:** Implementar e Gerenciar Armazenamento (Azure Storage Redundancy / ZRS)
**Enunciado:** Sua empresa precisa implantar uma Conta de Armazenamento que garanta replicação síncrona dos dados em três Zonas de Disponibilidade separadas dentro da mesma região primária, protegendo os dados contra a falha de um data center inteiro. Qual opção de redundância de armazenamento deve ser selecionada?
**Opções:**
- A) Armazenamento com Redundância Local (LRS).
- B) Armazenamento com Redundância de Zona (ZRS).
- C) Armazenamento com Redundância Geográfica (GRS).
- D) Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
**Resposta Correta:** B
**Explicação Técnica:** O ZRS (Zone-Redundant Storage) replica seus dados de forma síncrona em três zonas de disponibilidade do Azure na região primária, oferecendo alta disponibilidade contra falhas físicas de data centers isolados.

---

### Questão 028
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (Mover VMs entre Assinaturas)
**Enunciado:** Você possui uma máquina virtual (VM1) na Assinatura 1 associada a um disco de sistema operacional (Disk1), uma interface de rede (NIC1) e conectada à VNet1. Você precisa mover a VM1 para a Assinatura 2. Quais recursos associados devem obrigatoriamente ser movidos juntos na mesma operação?
**Opções:**
- A) A VM1, o Disk1, a NIC1 e a VNet1 conectada.
- B) Apenas a VM1 e o Disk1.
- C) Apenas a VM1.
- D) A VM1 e a Conta de Armazenamento do diagnóstico.
**Resposta Correta:** D (ou A dependendo da topologia) -> A
**Explicação Técnica:** Ao mover uma Máquina Virtual do Azure para uma nova assinatura ou grupo de recursos, todos os seus recursos dependentes diretamente vinculados (como discos gerenciados, interfaces de rede e a rede virtual caso esteja no mesmo grupo) devem ser movidos na mesma transação.

---

### Questão 029
**Domínio:** Monitorar e Proteger Recursos do Azure (Azure Monitor / Action Groups)
**Enunciado:** Você possui uma máquina virtual chamada VM1 e um Aplicativo de Função (Function App) chamado App1. Você precisa criar uma regra de alerta no Azure Monitor que execute automaticamente o código do App1 se a VM1 for paralisada inesperadamente. O que você deve criar para vincular a regra de alerta à execução da Função?
**Opções:**
- A) Um Grupo de Ação (Action Group) contendo uma ação do tipo Azure Function.
- B) Um Grupo de Segurança de Aplicativo (ASG).
- C) Uma regra de política do Azure Policy.
- D) Um Workspace do Microsoft Sentinel.
**Resposta Correta:** A
**Explicação Técnica:** No Azure Monitor, um Grupo de Ação (*Action Group*) define a lista de receptores de notificação e ações automatizadas (como acionar um Azure Function, Logic App, Webhook ou Automação) executadas quando um alerta é disparado.

---

### Questão 030
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure Firewall & Route Tables / UDR)
**Enunciado:** Você possui um Azure Firewall (Firewall1) implantado na sub-rede AzureFirewallSubnet da VNet1. Você precisa gerenciar e forçar todo o tráfego de saída (outbound) das sub-redes da VNet1 para passar através do Firewall1. O que você deve criar primeiro?
**Opções:**
- A) Uma Tabela de Rotas (Route Table) com uma Rota Definida pelo Usuário (UDR) direcionando 0.0.0.0/0 para o IP privado do Firewall1, associada às sub-redes.
- B) Um conector do Hybrid Connection Manager.
- C) Uma nova rede virtual e fazer peering.
- D) Um perfil do Traffic Manager.
**Resposta Correta:** A
**Explicação Técnica:** Para rotear o tráfego de sub-redes através de um NVA (Network Virtual Appliance) ou Azure Firewall, cria-se uma Tabela de Rotas (*Route Table*) contendo uma rota Padrão (`0.0.0.0/0`) cujo próximo salto (*next hop*) é o endereço IP privado do Azure Firewall, e associa-se essa tabela às sub-redes da VNet.

---

### Questão 031
**Domínio:** Gerenciar Identidades e Governança do Azure (Microsoft Entra ID / Administrative Units)
**Enunciado:** Sua organização deseja delegar a administração de usuários e grupos para gerentes regionais de TI (ex.: TI Brasil, TI Europa) sem conceder privilégios administrativos em todo o diretório do Entra ID. Qual recurso do Entra ID deve ser utilizado?
**Opções:**
- A) Unidades Administrativas (Administrative Units).
- B) Grupos de Gerenciamento (Management Groups).
- C) Grupos de Recursos (Resource Groups).
- D) Perfis de Conexão Privada.
**Resposta Correta:** A
**Explicação Técnica:** As Unidades Administrativas (*Administrative Units*) no Microsoft Entra ID permitem subdividir o diretório em contêineres lógicos para delegar permissões de função do Entra ID (como Administrador de Usuários) a escopos delimitados de usuários e grupos.

---

### Questão 032
**Domínio:** Implementar e Gerenciar Armazenamento (Azure Files & AD DS Authentication)
**Enunciado:** Você precisa configurar um Compartilhamento de Arquivos do Azure (Azure Files) para permitir o controle de acesso ao nível de arquivo/pasta utilizando permissões NTFS nativas integradas ao seu diretório local do Active Directory Domain Services (AD DS). O que deve ser habilitado na Conta de Armazenamento?
**Opções:**
- A) Autenticação baseada em identidade do AD DS para o Azure Files.
- B) Chaves de acesso da conta de armazenamento (Account Keys).
- C) Assinaturas de Acesso Compartilhado (SAS).
- D) Políticas de Imutabilidade do Blob.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files suporta autenticação baseada em identidade via AD DS local ou Microsoft Entra Domain Services, permitindo que máquinas virtuais ingressadas no domínio acessem os compartilhamentos usando credenciais do Active Directory com suporte total a ACLs NTFS.

---

### Questão 033
**Domínio:** Configurar e Gerenciar Redes Virtuais (VPN Gateway / Site-to-Site)
**Enunciado:** Você precisa conectar a rede local da sua empresa à sua Rede Virtual do Azure (VNet1) usando uma conexão VPN Site-to-Site criptografada via Internet. Quais três componentes de rede principal você deve provisionar no Azure?
**Opções:**
- A) Um Gateway de Rede Virtual (Virtual Network Gateway) na GatewaySubnet, um Gateway de Rede Local (Local Network Gateway) e uma Conexão VPN.
- B) Um Azure ExpressRoute, uma tabela de rotas e um Peering.
- C) Um Azure Bastion, um Load Balancer e um NSG.
- D) Um Application Gateway, um WAF e um IP Público.
**Resposta Correta:** A
**Explicação Técnica:** Uma VPN Site-to-Site no Azure requer: (1) O *Virtual Network Gateway* hospedado na sub-rede dedicada `GatewaySubnet` da VNet, (2) O *Local Network Gateway* representando o IP público e blocos IP do dispositivo VPN local, e (3) O recurso de *Conexão* vinculando ambos com uma chave pré-compartilhada (IPsec/IKE).

---

### Questão 034
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (VM Scale Sets / Autoscale Rules)
**Enunciado:** Você possui um Conjunto de Escala de Máquinas Virtuais (VMSS) hospedando uma aplicação web. Você precisa configurar regras de dimensionamento automático (*autoscale*) baseadas na métrica de utilização média de CPU. Quais são as duas ações que compõem uma regra típica de dimensionamento dinâmico?
**Opções:**
- A) Uma regra de aumento (*Scale Out*) quando a CPU exceder 75% e uma regra de redução (*Scale In*) quando a CPU for inferior a 25%.
- B) Alterar o tamanho da VM (Scale Up) para uma SKU maior.
- C) Mover as VMs para outra região do Azure.
- D) Reiniciar as instâncias de VM automaticamente a cada hora.
**Resposta Correta:** A
**Explicação Técnica:** O dimensionamento automático horizontal (*autoscale*) em VMSS funciona aumentando o número de instâncias de VM (*Scale Out*) durante picos de carga de métricas e reduzindo a quantidade de instâncias (*Scale In*) quando a demanda diminui, otimizando desempenho e custos.

---

### Questão 035
**Domínio:** Monitorar e Proteger Recursos do Azure (Azure Monitor / Network Insights)
**Enunciado:** Sua empresa possui circuitos do Azure ExpressRoute conectando data centers locais às redes virtuais no Azure. Você precisa de um painel visual unificado exibindo a topologia de rede detalhada e métricas de integridade dos circuitos. O que você deve utilizar?
**Opções:**
- A) Azure Monitor Network Insights.
- B) Uma Regra de Coleta de Dados (DCR).
- C) Regras de Alerta do Activity Log.
- D) O Portal de Confiança do Serviço.
**Resposta Correta:** A
**Explicação Técnica:** O *Azure Monitor Network Insights* oferece monitoramento abrangente e visualizações de topologia de rede para todos os seus recursos de rede do Azure (incluindo ExpressRoute, VNets, Firewalls e Load Balancers) sem exigir configuração complexa.

---

### Questão 036
**Domínio:** Gerenciar Identidades e Governança do Azure (Azure Policy / Initiatives)
**Enunciado:** Sua equipe de governança precisa aplicar um conjunto padronizado de 15 políticas de segurança e conformidade corporativa em todas as assinaturas do Azure da empresa. Em vez de atribuir cada política individualmente, o que você deve criar para gerenciar o grupo de políticas como um único objeto?
**Opções:**
- A) Uma Definição de Iniciativa (Initiative Definition / Policy Set).
- B) Um Grupo de Recursos.
- C) Um Modelo ARM.
- D) Um Cofre de Chaves do Azure.
**Resposta Correta:** A
**Explicação Técnica:** Uma Iniciativa do Azure Policy (também conhecida como *Policy Set*) é uma coleção de várias definições de política agrupadas sob um único objetivo para simplificar a atribuição e o gerenciamento de conformidade corporativa em grande escala.

---

### Questão 037
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure Application Gateway & Web Application Firewall)
**Enunciado:** Você precisa distribuir o tráfego de entrada HTTP/HTTPS na Camada 7 do modelo OSI para seu aplicativo web de várias instâncias, além de proteger a aplicação contra vulnerabilidades da web (como injeção de SQL e Cross-Site Scripting). Qual serviço de rede do Azure deve ser implantado?
**Opções:**
- A) Azure Application Gateway com Web Application Firewall (WAF).
- B) Azure Load Balancer Standard.
- C) Azure Traffic Manager.
- D) Azure Network Security Group (NSG).
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego web de Camada 7 que suporta roteamento baseado em URL, encerramento de TLS e integra o Web Application Firewall (WAF) para proteger aplicações web contra ataques OWASP comuns.

---

### Questão 038
**Domínio:** Implementar e Gerenciar Armazenamento (Azure Blob Storage / Immutability Policies)
**Enunciado:** Para cumprir exigências legais e de conformidade de mercado financeiro, sua empresa precisa armazenar arquivos de auditoria em um contêiner de blobs de forma que ninguém — nem mesmo um Administrador Global — consiga modificar ou excluir os dados durante 5 anos. Qual recurso do Blob Storage deve ser configurado?
**Opções:**
- A) Uma política de retenção baseada em tempo imutável (WORM - Write Once, Read Many).
- B) Um Bloqueio de Recurso do tipo CanNotDelete no grupo de recursos.
- C) Assinaturas de Acesso Compartilhado (SAS) de curta duração.
- D) Criptografia com chave gerenciada pelo cliente (CMK).
**Resposta Correta:** A
**Explicação Técnica:** O armazenamento imutável do Azure Blob Storage para dados WORM (Write Once, Read Many) permite definir políticas de retenção bloqueadas baseadas em tempo que impedem a alteração ou sobrescrita de blobs por qualquer usuário durante o período especificado.

---

### Questão 039
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (Azure Virtual Machines / Availability Zones vs Sets)
**Enunciado:** Você precisa implantar três máquinas virtuais para uma aplicação de alta disponibilidade. A solução deve proteger a aplicação contra a falha de um data center inteiro dentro da região do Azure. Como as VMs devem ser distribuídas?
**Opções:**
- A) Implantar cada máquina virtual em uma Zona de Disponibilidade (Availability Zone) separada na mesma região.
- B) Implantar todas as VMs em um mesmo Conjunto de Disponibilidade (Availability Set).
- C) Implantar todas as VMs na mesma sub-rede sem zonas.
- D) Implantar as VMs em regiões de nuvem diferentes.
**Resposta Correta:** A
**Explicação Técnica:** As Zonas de Disponibilidade (Availability Zones) são locais físicos isolados dentro de uma região do Azure, cada uma com alimentação, refrigeração e rede independentes. Distribuir VMs entre Zonas de Disponibilidade protege a aplicação contra falhas no nível de data center completo.

---

### Questão 040
**Domínio:** Configurar e Gerenciar Redes Virtuais (Network Security Groups / Regras Padrão)
**Enunciado:** Um Administrador cria um Grupo de Segurança de Rede (NSG) e o associa a uma sub-rede contendo servidores web. O NSG contém apenas as regras padrão do Azure (*Default Rules*). Qual é o comportamento padrão das regras do NSG quanto ao tráfego entre sub-redes da mesma VNet e tráfego da Internet?
**Opções:**
- A) Permite todo o tráfego de entrada da VNet (AllowVNetInBound) e bloqueia todo o tráfego de entrada da Internet (DenyAllInBound).
- B) Bloqueia todo o tráfego sem exceção.
- C) Permite todo o tráfego da Internet por padrão.
- D) Permite tráfego de saída apenas para a Microsoft.
**Resposta Correta:** A
**Explicação Técnica:** As regras padrão dos NSGs do Azure incluem a regra `AllowVNetInBound` (prioridade 65000), que permite comunicação entre todos os recursos da mesma VNet, e a regra `DenyAllInBound` (prioridade 65500), que bloqueia todo o tráfego de entrada vindo da Internet pública por padrão.

---

### Questão 041
**Domínio:** Gerenciar Identidades e Governança do Azure (Controle de Acesso Baseado em Função - RBAC)
**Enunciado:** Você precisa conceder a um usuário da equipe de suporte a permissão para reiniciar e visualizar métricas de máquinas virtuais no grupo de recursos RG1, sem permitir que o usuário altere as configurações de rede ou exclua as VMs. Qual função RBAC integrada deve ser atribuída ao usuário?
**Opções:**
- A) Colaborador de Máquina Virtual (Virtual Machine Contributor).
- B) Leitor (Reader).
- C) Proprietário (Owner).
- D) Colaborador de Rede (Network Contributor).
**Resposta Correta:** A
**Explicação Técnica:** A função integrada *Virtual Machine Contributor* permite gerenciar máquinas virtuais (iniciar, reiniciar, desligar, gerenciar discos), mas não concede permissões administrativas no grupo de recursos pai nem acesso às configurações de redes virtuais associadas.

---

### Questão 042
**Domínio:** Implementar e Gerenciar Armazenamento (Azure Storage Sync / File Sync)
**Enunciado:** Sua empresa possui servidores de arquivos locais em várias filiais e deseja sincronizar as pastas locais centralidamente com um Compartilhamento de Arquivos do Azure (Azure Files) para backups e distribuição de arquivos com armazenamento em camadas na nuvem (*cloud tiering*). Qual serviço do Azure deve ser implantado?
**Opções:**
- A) Azure File Sync.
- B) Serviço de Migração do Azure (Azure Migrate).
- C) Azure Data Box.
- D) Azure Event Grid.
**Resposta Correta:** A
**Explicação Técnica:** O *Azure File Sync* permite centralizar os compartilhamentos de arquivos da sua organização no Azure Files, mantendo a flexibilidade, o desempenho e a compatibilidade de um servidor de arquivos local com suporte a armazenamento em camadas na nuvem.

---

### Questão 043
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (Azure Kubernetes Service - AKS)
**Enunciado:** Você implantou um cluster do Azure Kubernetes Service (AKS) chamado Cluster1. Você precisa implantar uma aplicação em contêiner no cluster utilizando um arquivo de manifesto YAML. Qual ferramenta de linha de comando deve ser utilizada para se comunicar com o cluster do Kubernetes?
**Opções:**
- A) kubectl (usando a credencial obtida via `az aks get-credentials`).
- B) azcopy.
- C) PowerShell `Invoke-AzRestMethod`.
- D) Docker CLI local.
**Resposta Correta:** A
**Explicação Técnica:** A ferramenta oficial de linha de comando para gerenciamento de clusters Kubernetes (incluindo o AKS no Azure) é o `kubectl`. O comando `az aks get-credentials` baixa a configuração do kubeconfig permitindo executar manifestos YAML com o `kubectl apply`.

---

### Questão 044
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure ExpressRoute vs VPN Gateway)
**Enunciado:** Uma grande instituição bancária precisa conectar seu data center local privado à infraestrutura do Azure com largura de banda dedicada de 10 Gbps, baixíssima latência determinística e sem trafegar dados sensíveis sobre a Internet pública. Qual solução de conectividade deve ser recomendada?
**Opções:**
- A) Azure ExpressRoute.
- B) VPN Site-to-Site IKEv2.
- C) VNet Peering Global.
- D) Azure Front Door.
**Resposta Correta:** A
**Explicação Técnica:** O Azure ExpressRoute fornece conexões privadas dedicadas entre os data centers locais do cliente e os data centers da Microsoft através de um provedor de conectividade, sem trafegar pela Internet pública, oferecendo maior segurança, velocidade e menor latência.

---

### Questão 045
**Domínio:** Monitorar e Proteger Recursos do Azure (Azure Monitor / Data Collection Rules - DCR)
**Enunciado:** Você implantou o Agente do Azure Monitor (AMA - Azure Monitor Agent) em 50 servidores Windows no Azure. Você precisa configurar a coleta centralizada de logs de eventos do sistema operacional com filtro para capturar apenas eventos com ID 1001. O que você deve criar no Azure Monitor?
**Opções:**
- A) Uma Regra de Coleta de Dados (Data Collection Rule - DCR) com uma consulta XPath de filtro.
- B) Uma regra de alerta no Activity Log.
- C) Um Endpoint de Coleta de Dados (DCE).
- D) Um painel do Application Insights.
**Resposta Correta:** A
**Explicação Técnica:** As Regras de Coleta de Dados (*Data Collection Rules - DCRs*) definem os dados que entram no Azure Monitor e especificam para onde eles devem ser enviados. Em conjunto com o Azure Monitor Agent (AMA), suportam consultas de filtro XPath para selecionar eventos específicos do Windows Event Log.

---

### Questão 046
**Domínio:** Gerenciar Identidades e Governança do Azure (Microsoft Entra ID / PIM - Privileged Identity Management)
**Enunciado:** Sua empresa deseja implementar o princípio do privilégio mínimo para administradores do Entra ID. Os administradores não devem ter permissões privilegiadas ativas permanentemente, devendo solicitar elevação de acesso temporária baseada em aprovação e justificativa de negócio quando necessário. Qual recurso do Entra ID Governance atende a esse requisito?
**Opções:**
- A) Microsoft Entra Privileged Identity Management (PIM / Just-In-Time Access).
- B) Políticas de Acesso Condicional.
- C) Análises de Acesso.
- D) Registros de Aplicativos.
**Resposta Correta:** A
**Explicação Técnica:** O Entra Privileged Identity Management (PIM) fornece gerenciamento de acesso Just-In-Time (JIT) para funções do Entra ID e recursos do Azure, permitindo atribuir funções qualificadas que exigem ativação temporária com aprovação, MFA e justificativa.

---

### Questão 047
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure Load Balancer / Inbound NAT Rules)
**Enunciado:** Você possui três máquinas virtuais em um backend pool de um balanceador de carga público. Você precisa permitir a conexão de Área de Trabalho Remota (RDP) via porta 3389 para uma máquina virtual específica no backend utilizando portas externas diferentes. Qual recurso do Load Balancer deve ser configurado?
**Opções:**
- A) Regras de NAT de Entrada (Inbound NAT Rules).
- B) Regras de Balanceamento de Carga (Load Balancing Rules).
- C) Probas de Integridade (Health Probes).
- D) Configuração de IP de Frontend.
**Resposta Correta:** A
**Explicação Técnica:** As regras de NAT de Entrada (*Inbound NAT Rules*) no Azure Load Balancer encaminham o tráfego de uma porta de entrada específica no IP público de frontend para uma porta específica em uma máquina virtual individual no backend pool.

---

### Questão 048
**Domínio:** Implementar e Gerenciar Armazenamento (Azure Storage Security / Shared Access Signatures)
**Enunciado:** Uma aplicação externa precisa ler arquivos de imagem de um contêiner de armazenamento no Azure por apenas 2 horas. Você não deseja compartilhar a chave de acesso primária da conta de armazenamento nem solicitar autenticação de usuário no Entra ID. Qual mecanismo de delegação de acesso temporário deve ser utilizado?
**Opções:**
- A) Assinatura de Acesso Compartilhado (SAS - Shared Access Signature) de serviço ou delegado por usuário.
- B) Política Imutável de Blob.
- C) Endpoint Privado.
- D) Chaves de API estáticas.
**Resposta Correta:** A
**Explicação Técnica:** Uma Assinatura de Acesso Compartilhado (SAS) fornece acesso delegado seguro a recursos na sua conta de armazenamento com controle granular sobre permissões (leitura, escrita), intervalos de tempo válidos (ex.: 2 horas) e endereços IP permitidos.

---

### Questão 049
**Domínio:** Implantar e Gerenciar Recursos de Computação do Azure (Azure App Service Plans & Scaling)
**Enunciado:** Você possui quatro aplicativos Web hospedados no Azure App Service. Você precisa aumentar o desempenho de CPU e memória de todos os aplicativos web simultaneamente mudando a camada de preço da infraestrutura subjacente de Standard S1 para Premium P1v2. O que você deve modificar?
**Opções:**
- A) O Plano do App Service (App Service Plan) associado aos aplicativos web.
- B) As configurações individuais dos aplicativos web.
- C) O grupo de recursos pai.
- D) O registro de DNS do aplicativo.
**Resposta Correta:** A
**Explicação Técnica:** Um Plano do App Service (*App Service Plan*) define o conjunto de recursos de computação (CPU, RAM, região, tamanho de disco e recursos da plataforma) que executam um ou mais aplicativos Web. Alterar o SKU do plano afeta todas as instâncias hospedadas nele (*Scale Up*).

---

### Questão 050
**Domínio:** Configurar e Gerenciar Redes Virtuais (Azure Network Watcher / Connection Monitor)
**Enunciado:** Sua equipe de operações precisa monitorar continuamente a latência de rede e a perda de pacotes de comunicação entre máquinas virtuais na nuvem e um controlador de domínio localizado em seu data center local através de uma conexão ExpressRoute. Qual recurso deve ser configurado?
**Opções:**
- A) Monitor de Conexão (Connection Monitor) do Azure Network Watcher.
- B) Resolução de Próximo Salto (Next Hop).
- C) Grupo de Segurança de Rede (NSG).
- D) Métrica de entrada de tráfego do Azure Monitor.
**Resposta Correta:** A
**Explicação Técnica:** O *Connection Monitor* do Azure Network Watcher fornece verificação contínua e integrada de conectividade fim-a-fim, medindo latência, perda de pacotes e topologia de rede entre recursos no Azure e pontos de extremidade locais.
