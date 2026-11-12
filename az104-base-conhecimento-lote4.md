# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 4 (Questões 151 a 200)

Esta base de conhecimento contém as questões 151 a 200 do exame **AZ-104: Microsoft Azure Administrator** formatadas para ingestão e automação no Antigravity.

---

### Questão 151
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Sua empresa possui 10 subscrições do Azure associadas ao mesmo locatário do Microsoft Entra ID. Você precisa aplicar uma política que impeça a criação de IP público em todas as subscrições. Qual o nível de escopo mais eficiente para aplicar o Azure Policy?
**Opções:**
- A) Em cada Grupo de Recursos individualmente
- B) Em um Grupo de Gerenciamento (Management Group) contendo todas as subscrições
- C) Na conta de usuário do Administrador Global
- D) Em cada Máquina Virtual existente
**Resposta Correta:** B
**Explicação Técnica:** Aplicar o Azure Policy no nível de um Grupo de Gerenciamento (Management Group) permite governar centralidamente todas as subscrições contidas nele por herança, evitando a necessidade de aplicar a política repetidamente em cada subscrição ou grupo de recursos.

### Questão 152
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você configura um balanceador de carga interno (Internal Load Balancer) no Azure para distribuir tráfego entre duas VMs em uma VNet. O teste de conexão na porta 80 falha. Ao verificar a investigação de integridade (Health Probe), ela reporta status não saudável (Unhealthy). Qual a causa mais provável?
**Opções:**
- A) O Peering de Rede Virtual não está configurado
- B) Uma regra de Grupo de Segurança de Rede (NSG) na sub-rede das VMs está bloqueando a porta da investigação de integridade
- C) O SKU do Load Balancer é Basic e não suporta investigação HTTP
- D) A interface de rede das VMs possui IP público atribuído
**Resposta Correta:** B
**Explicação Técnica:** As investigações de integridade do Azure Load Balancer originam-se do endereço IP AzureInfrastructure (168.63.129.16). Se um NSG bloquear o tráfego de entrada dessa origem ou na porta configurada da investigação, o Load Balancer marcará as instâncias como Unhealthy e não enviará tráfego.

### Questão 153
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa garantir que os arquivos armazenados em um compartilhamento de arquivos do Azure (Azure Files) fiquem protegidos contra exclusões acidentais por até 14 dias após a exclusão. Qual recurso deve ser ativado na Conta de Armazenamento?
**Opções:**
- A) Bloqueio de Exclusão (Delete Lock)
- B) Exclusão Reversível para Compartilhamentos de Arquivos (Soft Delete for Azure Files)
- C) Armazenamento Imutável (WORM)
- D) Gerenciamento do Ciclo de Vida (Lifecycle Management)
**Resposta Correta:** B
**Explicação Técnica:** A Exclusão Reversível (Soft Delete) para o Azure Files permite recuperar compartilhamentos de arquivos excluídos acidentalmente dentro de um período de retenção configurável (entre 1 e 365 dias, sendo 14 dias um valor comum).

### Questão 154
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma aplicação web hospedada em um Conjunto de Escalonamento de Máquinas Virtuais (VMSS) precisa dimensionar horizontalmente quando o uso médio de CPU ultrapassar 75% por 10 minutos. Qual recurso deve ser configurado?
**Opções:**
- A) Escalonamento Automático Baseado em Regras de Métrica (Autoscale Rules)
- B) Conjuntos de Disponibilidade (Availability Sets)
- C) Azure Advisor Recommendations
- D) Atualização Manual da SKU da VM
**Resposta Correta:** A
**Explicação Técnica:** O escalonamento automático (Autoscale) no VMSS permite definir regras baseadas em métricas de desempenho (como uso de CPU, memória ou fila) para aumentar (scale-out) ou diminuir (scale-in) automaticamente o número de instâncias de VMs.

### Questão 155
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa criar uma consulta KQL no Log Analytics Workspace para listar os 10 computadores que geraram o maior número de eventos de erro nos últimos 7 dias. Qual operador KQL é usado para agrupar e contar os registros por computador?
**Opções:**
- A) join
- B) summarize count() by Computer
- C) project Computer, EventID
- D) filter Computer by Error
**Resposta Correta:** B
**Explicação Técnica:** O operador `summarize` no KQL (Kusto Query Language) agrega dados agregando funções (como `count()`) agrupadas por dimensões especificadas (como `by Computer`). O complemento `top 10 by count_` pode ser usado para retornar os 10 maiores.

### Questão 156
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um administrador precisa conceder a um usuário permissão para reiniciar Máquinas Virtuais em um Grupo de Recursos específico, sem permitir que o usuário altere as configurações de rede ou exclua as VMs. Qual função RBAC integrada é a mais adequada?
**Opções:**
- A) Proprietário (Owner)
- B) Colaborador (Contributor)
- C) Colaborador de Máquina Virtual (Virtual Machine Contributor)
- D) Leitor (Reader)
**Resposta Correta:** C
**Explicação Técnica:** A função integrada Colaborador de Máquina Virtual (Virtual Machine Contributor) permite gerenciar máquinas virtuais (incluindo iniciar, reiniciar e desligar), mas não concede acesso às redes virtuais associadas ou permissões de gerenciamento de acesso (RBAC).

### Questão 157
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa permitir que servidores locais acessem recursos em uma VNet do Azure usando uma conexão criptografada através da Internet pública. Qual serviço do Azure atende a esse requisito mantendo a solução econômica?
**Opções:**
- A) Azure ExpressRoute Direct
- B) Gateway de VPN Site a Site (S2S VPN Gateway)
- C) Peering de Rede Virtual Global
- D) Azure Private Link
**Resposta Correta:** B
**Explicação Técnica:** Uma conexão de Gateway de VPN Site a Site (Site-to-Site VPN) cria um túnel IPsec/IKE criptografado sobre a Internet pública conectando a rede local à VNet do Azure de forma segura e com custo muito menor do que o ExpressRoute.

### Questão 158
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua organização deve armazenar arquivos de auditoria financeira no Azure Blob Storage por 7 anos. A política da empresa estabelece que nenhum arquivo pode ser modificado ou excluído por ninguém durante esse período, nem mesmo por Administradores Globais. O que deve ser configurado?
**Opções:**
- A) Bloqueio de Recurso do tipo ReadOnly
- B) Política de Retenção Imutável com Bloqueio de Conformidade (Locked Compliance Policy)
- C) Controle de Acesso Baseado em Função (RBAC)
- D) Exclusão Reversível de Blob (Blob Soft Delete)
**Resposta Correta:** B
**Explicação Técnica:** Uma política de retenção imutável baseada em tempo no estado bloqueado (Locked Compliance Policy) no Azure Blob Storage garante a conformidade WORM (Write Once, Read Many). Uma vez bloqueada, a política não pode ser removida ou alterada, nem mesmo por administradores.

### Questão 159
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um contêiner Docker no Azure de forma rápida, sem a necessidade de provisionar e gerenciar máquinas virtuais subjacentes ou configurar um cluster Kubernetes. Qual serviço deve utilizar?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Serviço de Kubernetes do Azure (AKS)
- C) Conjunto de Escalonamento de Máquinas Virtuais (VMSS)
- D) Serviços de Domínio do Microsoft Entra
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Instances (ACI) é a solução mais rápida e simples para executar contêineres no Azure sob demanda de forma serverless, sem necessidade de gerenciar VMs ou orquestradores complexos.

### Questão 160
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar o backup diário de 20 máquinas virtuais do Azure executando o Windows Server. Qual recurso do Azure é responsável por armazenar os pontos de recuperação de backup e gerenciar as políticas de retenção?
**Opções:**
- A) Log Analytics Workspace
- B) Cofre dos Serviços de Recuperação (Recovery Services Vault)
- C) Conta de Armazenamento de Blobs de Blocos
- D) Azure Key Vault
**Resposta Correta:** B
**Explicação Técnica:** O Cofre dos Serviços de Recuperação (Recovery Services Vault) é uma entidade de armazenamento no Azure que guarda dados de backup, pontos de restauração e gerencia as políticas de backup automatizado para VMs do Azure, discos e servidores locais.

### Questão 161
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Uma empresa precisa delegar temporariamente o papel de Administrador de Segurança a um usuário do Microsoft Entra ID por 4 horas para realizar uma auditoria. Qual recurso do Microsoft Entra ID Governance deve ser utilizado?
**Opções:**
- A) Grupos de Acesso Dinâmico
- B) Privileged Identity Management (PIM)
- C) Unidades Administrativas (AU)
- D) Autenticação Multifator (MFA)
**Resposta Correta:** B
**Explicação Técnica:** O Microsoft Entra Privileged Identity Management (PIM) permite gerenciar, controlar e monitorar o acesso a recursos críticos, oferecendo a ativação de funções 'Just-In-Time' (JIT) por tempo determinado com exigência de aprovação e justificativa.

### Questão 162
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você possui duas Redes Virtuais (VNet1 e VNet2) na mesma região. As máquinas virtuais na VNet1 precisam se comunicar com as VMs na VNet2 usando endereços IP privados com a menor latência possível. O que você deve configurar?
**Opções:**
- A) Peering de Rede Virtual (VNet Peering)
- B) Conexão VPN Site a Site (S2S)
- C) Conexão VPN Ponto a Site (P2S)
- D) Azure Traffic Manager
**Resposta Correta:** A
**Explicação Técnica:** O Peering de Rede Virtual (VNet Peering) conecta redes virtuais diretamente através da rede backbone privada de alta velocidade da Microsoft, garantindo baixíssima latência e tráfego criptografado no nível da rede física.

### Questão 163
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa migrar 80 TB de dados locais para o Azure Blob Storage. A largura de banda da conexão de Internet da empresa é de apenas 10 Mbps, tornando o upload pela rede inviável. Qual solução é a mais recomendada pela Microsoft?
**Opções:**
- A) Upload via AzCopy em lote
- B) Azure Data Box
- C) Azure Import/Export via discos rígidos SATA próprios enviados pelo correio
- D) Sincronização de Arquivos do Azure (Azure File Sync)
**Resposta Correta:** B
**Explicação Técnica:** O Azure Data Box é um dispositivo de armazenamento físico seguro fornecido pela Microsoft (com capacidade de 80 TB) para transferir grandes volumes de dados offline para o Azure de forma rápida e segura via transporte terrestre.

### Questão 164
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Ao tentar implantar uma nova Máquina Virtual da série D no Azure, a implantação falha informando que o limite de vCPUs da subscrição para aquela região foi atingido. Como resolver esse problema?
**Opções:**
- A) Alterar a política do Azure (Azure Policy)
- B) Criar uma nova solicitação de suporte no Portal do Azure para aumento de cota (Quota Increase)
- C) Reiniciar o agente da máquina virtual
- D) Mudar a zona de disponibilidade
**Resposta Correta:** B
**Explicação Técnica:** Os limites de cota de vCPU por família de VMs no Azure são impostos por região e por subscrição. Para aumentar o limite, o administrador deve enviar uma solicitação de aumento de cota (Quota Increase Request) gratuita no portal do Azure.

### Questão 165
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você deseja enviar um alerta por e-mail e SMS para a equipe de infraestrutura sempre que uma Máquina Virtual crítica for desligada de forma inesperada. Qual recurso do Azure Monitor coordena as ações executadas quando um alerta é disparado?
**Opções:**
- A) Regras de Coleta de Dados (DCR)
- B) Grupos de Ação (Action Groups)
- C) Métricas do Azure Advisor
- D) Log Analytics Workspaces
**Resposta Correta:** B
**Explicação Técnica:** Um Grupo de Ação (Action Group) no Azure Monitor define a lista de notificações (como e-mail, SMS, notificação no aplicativo Azure) e ações automatizadas (como acionar um Webhook ou Azure Function) executadas quando um alerta é disparado.

### Questão 166
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Um desenvolvedor precisa acessar um banco de dados SQL do Azure a partir de uma Máquina Virtual sem armazenar credenciais ou senhas no código da aplicação ou em arquivos de configuração. O que você deve configurar?
**Opções:**
- A) Chave de Acesso da Conta de Armazenamento
- B) Identidade Gerenciada Atribuída ao Recurso (Managed Identity)
- C) Token SAS de Serviço
- D) Usuário Convidado do Microsoft Entra B2B
**Resposta Correta:** B
**Explicação Técnica:** As Identidades Gerenciadas para Recursos do Azure (Managed Identities) fornecem uma identidade gerenciada automaticamente no Microsoft Entra ID para que a aplicação na VM se autentique em serviços que suportam autenticação Entra (como Azure SQL) sem gravar senhas no código.

### Questão 167
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa garantir que todo o tráfego de saída da Internet vindo de VMs em uma sub-rede passe obrigatoriamente por uma solução de Firewall virtual (NVA) antes de ir para a Internet. Qual recurso de rede deve ser configurado?
**Opções:**
- A) Regra do Grupo de Segurança de Rede (NSG)
- B) Tabela de Rotas Personalizada (User-Defined Route - UDR) com rota para 0.0.0.0/0
- C) Peering de Rede Virtual
- D) Azure DNS Private Zone
**Resposta Correta:** B
**Explicação Técnica:** Uma Tabela de Rotas (UDR) permite sobrescrever a rota padrão do Azure adicionando uma rota personalizada para a faixa de destino `0.0.0.0/0` com o próximo salto (*Next hop type*) definido como *Virtual Appliance* apontando para o endereço IP do Firewall.

### Questão 168
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual ferramenta de linha de comando da Microsoft é otimizada para cópia e sincronização de dados de alta performance de e para Contas de Armazenamento do Azure usando endereçamento paralelo?
**Opções:**
- A) Azure CLI (az storage)
- B) PowerShell (Get-AzStorageAccount)
- C) AzCopy v10
- D) Robocopy
**Resposta Correta:** C
**Explicação Técnica:** O AzCopy v10 é a ferramenta de linha de comando oficial desenvolvida pela Microsoft projetada para transferência de alta performance de dados para dentro e para fora de Blobs e Compartilhamentos de Arquivos do Azure.

### Questão 169
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você possui uma aplicação web no Azure App Service. Você precisa implantar uma nova versão da aplicação em ambiente de testes antes de direcionar o tráfego dos usuários finais, garantindo tempo de inatividade zero. Qual recurso do App Service deve utilizar?
**Opções:**
- A) Slots de Implantação (Deployment Slots)
- B) Registros de Contêiner do Azure
- C) Grupos de Disponibilidade
- D) Regras de Dimensionamento Automático
**Resposta Correta:** A
**Explicação Técnica:** Os Slots de Implantação (Deployment Slots) são ambientes dinâmicos hospedados com seus próprios nomes de host. Eles permitem testar uma nova versão da aplicação e realizar a troca (swap) instantânea com o slot de produção sem nenhum downtime.

### Questão 170
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa coletar logs de auditoria e eventos de desempenho de 50 VMs Linux no Azure e centralizá-los para análise de dados com consultas KQL. Qual agente deve ser instalado nas VMs?
**Opções:**
- A) Agente do Azure Monitor (AMA - Azure Monitor Agent)
- B) Agente do Network Watcher
- C) Agente do Dependency Agent apenas
- D) Agente da Extensão VMAccess
**Resposta Correta:** A
**Explicação Técnica:** O Agente do Azure Monitor (AMA) consolida a coleta de telemetria, eventos do sistema operacional e métricas de desempenho de VMs Windows e Linux, enviando os dados para um Log Analytics Workspace por meio de Regras de Coleta de Dados (DCR).

### Questão 171
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Como um administrador pode impedir que qualquer usuário (incluindo o próprio proprietário da subscrição) exclua acidentalmente uma Conta de Armazenamento crítica no Azure?
**Opções:**
- A) Aplicar uma política do Azure Policy de negação
- B) Aplicar um Bloqueio de Recurso do tipo Bloquear Exclusão (CanNotDelete / Delete Lock)
- C) Remover as permissões de leitura do usuário
- D) Desativar o Microsoft Entra ID
**Resposta Correta:** B
**Explicação Técnica:** Um Bloqueio de Recurso (Resource Lock) do tipo `CanNotDelete` impede que o recurso seja excluído por qualquer usuário, independentemente de seus privilégios RBAC, até que a trava de bloqueio seja explicitamente removida.

### Questão 172
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Uma aplicação web precisa rotear as requisições HTTP/HTTPS com base no caminho da URL (ex.: `/images` para um pool de servidores e `/api` para outro pool). Qual serviço de balanceamento de carga do Azure é o mais adequado?
**Opções:**
- A) Azure Load Balancer (Basic)
- B) Azure Traffic Manager
- C) Gateway de Aplicativo do Azure (Azure Application Gateway)
- D) Azure ExpressRoute
**Resposta Correta:** C
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego web de Camada 7 (HTTP/HTTPS) que suporta roteamento baseado em caminho de URL (Path-based routing), terminação TLS/SSL e Firewall de Aplicação Web (WAF).

### Questão 173
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa configurar a sincronização contínua de arquivos entre um servidor de arquivos Windows local e um compartilhamento de arquivos do Azure (Azure Files). Qual serviço deve ser implantado?
**Opções:**
- A) Azure File Sync
- B) AzCopy em modo daemon
- C) Azure Data Factory
- D) Azure Backup Server
**Resposta Correta:** A
**Explicação Técnica:** O Azure File Sync centraliza os compartilhamentos de arquivos da organização no Azure Files, mantendo a flexibilidade, o desempenho e a compatibilidade de um servidor de arquivos Windows local com o recurso de Cloud Tiering.

### Questão 174
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa implantar um grupo de Máquinas Virtuais no Azure garantindo que elas estejam fisicamente isoladas em data centers distintos dentro da mesma região, com fontes de energia e rede independentes. O que você deve usar?
**Opções:**
- A) Conjuntos de Disponibilidade (Availability Sets)
- B) Zonas de Disponibilidade (Availability Zones)
- C) Domínios de Atualização (Update Domains)
- D) Grupos de Recursos Diferentes
**Resposta Correta:** B
**Explicação Técnica:** As Zonas de Disponibilidade (Availability Zones) são locais físicos exclusivos e separados dentro de uma mesma região do Azure. Cada zona é composta por um ou mais data centers equipados com energia, refrigeração e rede independentes.

### Questão 175
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Sua empresa deseja configurar o backup automático de arquivos em máquinas virtuais. Em caso de desastre, a empresa exige que os dados de backup permaneçam acessíveis mesmo se uma região inteira do Azure ficar indisponível. Qual opção de redundância de armazenamento deve ser escolhida no Recovery Services Vault?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento SSD Premium
**Resposta Correta:** C
**Explicação Técnica:** O Armazenamento com Redundância Geográfica (GRS) replica os dados três vezes na região primária e depois copia assincronamente os dados para uma região secundária par (centenas de quilômetros de distância), garantindo proteção contra desastres regionais.

### Questão 176
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa gerenciar permissões no Azure de forma eficiente para 50 funcionários do departamento de Finanças. Qual é a melhor prática recomendada pela Microsoft?
**Opções:**
- A) Atribuir funções RBAC individualmente a cada um dos 50 usuários
- B) Criar um grupo no Microsoft Entra ID, adicionar os 50 usuários ao grupo e atribuir a função RBAC necessária ao grupo
- C) Compartilhar a senha do Administrador Global entre a equipe
- D) Criar uma subscrição separada para cada funcionário
**Resposta Correta:** B
**Explicação Técnica:** A prática recomendada de governança no Azure é atribuir funções RBAC a grupos de segurança do Microsoft Entra ID em vez de usuários individuais. Isso simplifica o gerenciamento de acesso e auditoria à medida que os funcionários entram ou saem da equipe.

### Questão 177
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa permitir o tráfego da porta 443 para um grupo de VMs e bloquear o tráfego de todas as outras portas de entrada. Onde essas regras devem ser aplicadas com o menor esforço administrativo?
**Opções:**
- A) Tabela de Rotas (UDR)
- B) Grupo de Segurança de Rede (NSG) associado à sub-rede
- C) Azure ExpressRoute Direct
- D) Arquivo hosts das VMs
**Resposta Correta:** B
**Explicação Técnica:** Um Grupo de Segurança de Rede (NSG) contém regras de segurança que permitem ou negam tráfego de rede de entrada ou saída em sub-redes ou interfaces de rede (NICs) virtuais.

### Questão 178
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual tipo de replicação do Azure Storage mantém três cópias síncronas de seus dados distribuídas entre três Zonas de Disponibilidade separadas em uma única região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS)
**Resposta Correta:** B
**Explicação Técnica:** O Armazenamento com Redundância de Zona (ZRS) replica os dados de forma síncrona em três zonas de disponibilidade do Azure na região primária, oferecendo excelente resiliência contra falhas de data centers individuais.

### Questão 179
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa estender um disco de dados anexado a uma Máquina Virtual Linux no Azure. O que deve ser feito antes de expandir o tamanho do disco gerenciado no portal do Azure?
**Opções:**
- A) Excluir a Máquina Virtual
- B) Desalocar (Desligar) a Máquina Virtual se o recurso de expansão online não for suportado pelo tamanho da VM
- C) Formatar a partição do sistema operacional
- D) Alterar a subscrição do Azure
**Resposta Correta:** B
**Explicação Técnica:** Embora alguns tamanhos e configurações permitam expansão de disco online, a regra padrão clássica para alterar o tamanho de um disco gerenciado anexado exige que a VM esteja no estado Desalocada (Deallocated).

### Questão 180
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual ferramenta do Azure permite visualizar interativamente a topologia da rede, rastrear a rota de pacotes (Hop-by-hop) e verificar o status das conexões entre uma VM e um destino remoto?
**Opções:**
- A) Azure Monitor Log Analytics
- B) Network Watcher (com o recurso Connection Troubleshoot / IP Flow Verify)
- C) Azure Security Center
- D) Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** O Azure Network Watcher fornece uma suíte de ferramentas de diagnóstico de rede, incluindo solução de problemas de conexão (Connection Troubleshoot), verificação de fluxo IP (IP Flow Verify) e visualização de topologia.

### Questão 181
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você deseja garantir que todas as novas contas de armazenamento criadas na subscrição tenham a opção 'Permitir acesso público a blobs' desativada. Qual recurso do Azure deve ser utilizado?
**Opções:**
- A) Azure Policy
- B) Bloqueios de Recursos (Resource Locks)
- C) Grupos de Recursos
- D) Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy permite definir e impor regras de conformidade e configuração de segurança automaticamente durante ou após a implantação de recursos do Azure.

### Questão 182
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa expor um serviço interno executado em uma VM diretamente para outra VNet sem expor o serviço à Internet pública e sem precisar criar Peering completo entre todas as sub-redes. Qual recurso do Azure deve utilizar?
**Opções:**
- A) Azure Private Link / Endpoint Privado
- B) Gateway de VPN Ponto a Site
- C) IP Público Estático
- D) Peering de Rede Virtual Global
**Resposta Correta:** A
**Explicação Técnica:** O Azure Private Link permite acessar serviços PaaS do Azure ou serviços próprios hospedados por clientes/parceiros através de um Endpoint Privado (Private Endpoint) na sua VNet, mantendo o tráfego totalmente na rede privada da Microsoft.

### Questão 183
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Uma aplicação gera dados de log que são acessados com frequência nos primeiros 30 dias, mas raramente acessados depois. No entanto, os logs devem ser mantidos por 1 ano. Qual regra de Gerenciamento de Ciclo de Vida (Lifecycle Management) deve ser configurada?
**Opções:**
- A) Mover Blobs para a camada Fria (Cool) ou de Arquivo (Archive) após 30 dias da última modificação
- B) Excluir os Blobs imediatamente após 30 dias
- C) Converter os Blobs em arquivos ZIP
- D) Alterar a redundância da Conta de Armazenamento para LRS
**Resposta Correta:** A
**Explicação Técnica:** O Gerenciamento do Ciclo de Vida do Azure Blob Storage automatiza a transição de blobs entre as camadas de acesso Hot, Cool, Cold e Archive com base em regras de tempo decorrido desde a criação ou última modificação.

### Questão 184
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Sua empresa precisa implantar um banco de dados de alta performance em uma VM Azure. Para garantir o menor tempo de latência de E/S de disco e alta taxa de IOPS, qual tipo de armazenamento de disco gerenciado deve ser selecionado?
**Opções:**
- A) HDD Padrão (Standard HDD)
- B) SSD Padrão (Standard SSD)
- C) SSD Premium v2 ou Ultra Disk
- D) Compartilhamento de Arquivos Azure Files
**Resposta Correta:** C
**Explicação Técnica:** Os discos gerenciados SSD Premium v2 e Ultra Disk do Azure fornecem o mais alto desempenho de armazenamento em disco, com latência inferior a um milissegundo e taxas de IOPS e throughput altamente configuráveis para cargas críticas.

### Questão 185
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Qual é a linguagem de consulta utilizada no Log Analytics Workspace para realizar pesquisas de dados, filtros, agregações e gráficos a partir dos logs coletados?
**Opções:**
- A) Transact-SQL (T-SQL)
- B) Kusto Query Language (KQL)
- C) PowerShell
- D) Python
**Resposta Correta:** B
**Explicação Técnica:** O Azure Log Analytics e o Azure Data Explorer utilizam a Kusto Query Language (KQL), uma linguagem de consulta avançada e otimizada para pesquisa e análise de grandes volumes de dados estruturados e semiestruturados.

### Questão 186
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual tipo de identidade do Microsoft Entra ID é usado para permitir a comunicação segura entre microsserviços automatizados sem intervenção humana e sem senhas em código?
**Opções:**
- A) Usuário Convidado (Guest User)
- B) Principal de Serviço (Service Principal) ou Identidade Gerenciada (Managed Identity)
- C) Grupo de Segurança
- D) Contato de Correio
**Resposta Correta:** B
**Explicação Técnica:** Principais de Serviço (Service Principals) e Identidades Gerenciadas (Managed Identities) são identidades de aplicativo no Microsoft Entra ID criadas para uso por recursos, automações e serviços sem exigir contas de usuários humanos.

### Questão 187
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa conectar com segurança 100 laptops de funcionários remotos trabalhando de casa diretamente a uma VNet do Azure. Qual tipo de solução VPN deve ser configurada no Azure VPN Gateway?
**Opções:**
- A) Conexão VPN Site a Site (S2S)
- B) Conexão VPN Ponto a Site (P2S)
- C) Azure ExpressRoute Direct
- D) VNet Peering
**Resposta Correta:** B
**Explicação Técnica:** Uma conexão de Gateway de VPN Ponto a Site (Point-to-Site VPN) permite criar uma conexão individual e segura entre computadores clientes remotos (trabalhadores em casa ou em trânsito) e uma VNet no Azure.

### Questão 188
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Qual é a principal diferença entre o protocolo SMB e o protocolo NFS suportados pelos Compartilhamentos de Arquivos do Azure (Azure Files)?
**Opções:**
- A) O SMB é voltado para sistemas Windows, enquanto o NFS é otimizado para ambientes Linux
- B) O SMB só funciona com conexões ExpressRoute
- C) O NFS é exclusivo para armazenamento de objetos de imagem
- D) Não há diferença prática
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files suporta dois protocolos principais: o SMB (Server Message Block), nativo para clientes Windows e integração com AD DS, e o NFS (Network File System), amplamente utilizado por cargas de trabalho e clientes baseados em Linux.

### Questão 189
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa criar um modelo declarativo que defina a infraestrutura de 10 VMs, 1 VNet e 2 Contas de Armazenamento para implantação automatizada e repetível no Azure. Qual tecnologia nativa de infraestrutura como código (IaC) da Microsoft é recomendada?
**Opções:**
- A) Scripts em Shell Bash
- B) Modelos do Azure Resource Manager (ARM Templates) ou arquivos Bicep
- C) Código C# copilado
- D) Arquivos Dockerfile
**Resposta Correta:** B
**Explicação Técnica:** O Azure Bicep (e os modelos JSON ARM) é a linguagem declarativa nativa de Infraestrutura como Código (IaC) da Microsoft para implantar recursos no Azure de maneira consistente, idempotente e reproduzível.

### Questão 190
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa configurar a retenção de dados de diagnóstico do Azure por 365 dias para fins de conformidade regulatória com o menor custo possível. Para onde os logs devem ser exportados a partir das Configurações de Diagnóstico?
**Opções:**
- A) Para uma Conta de Armazenamento do Azure (Azure Storage Account)
- B) Para o histórico do navegador do administrador
- C) Para a memória cache RAM de uma VM
- D) Para o painel de status do Azure
**Resposta Correta:** A
**Explicação Técnica:** Exportar logs de diagnóstico para uma Conta de Armazenamento (Azure Storage Account) é a opção de retenção de longo prazo mais econômica no Azure para atender a requisitos legais e regulatórios de auditoria.

### Questão 191
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Qual recurso do Microsoft Entra ID permite exigir que os usuários forneçam uma segunda forma de verificação (como um aplicativo autenticador ou SMS) somente ao realizar login de locais não confiáveis ou dispositivos desconhecidos?
**Opções:**
- A) Acesso Condicional (Conditional Access)
- B) Unidades Administrativas
- C) Bloqueio de Recursos
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** As políticas de Acesso Condicional (Conditional Access) no Microsoft Entra ID utilizam sinais (como localização do usuário, estado do dispositivo e nível de risco) para impor controles de acesso automáticos, incluindo a exigência de Autenticação Multifator (MFA).

### Questão 192
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Sua empresa implantou uma VNet do Azure com a faixa de endereços `10.0.0.0/16`. Qual o número máximo de endereços IP disponíveis para recursos em uma sub-rede configurada com o bloco CIDR `10.0.1.0/24`?
**Opções:**
- A) 256
- B) 251
- C) 254
- D) 248
**Resposta Correta:** B
**Explicação Técnica:** Uma sub-rede `/24` possui 256 endereços IP totais (`2^8`). No entanto, o Azure reserva 5 endereços IP em cada sub-rede (o primeiro IP de rede, 3 IPs de gerenciamento/DNS/gateway e o IP de broadcast), restando 251 endereços IP disponíveis para recursos.

### Questão 193
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Você precisa disponibilizar uma URL temporária com limite de tempo para que um cliente faça upload de um arquivo diretamente para um container no Blob Storage sem fornecer suas chaves primárias da Conta de Armazenamento. O que você deve gerar?
**Opções:**
- A) Assinatura de Acesso Compartilhado de Serviço (Service Shared Access Signature - SAS)
- B) Um novo certificado SSL
- C) Uma chave pública RSA
- D) Um token de acesso do Microsoft Entra ID sem permissão
**Resposta Correta:** A
**Explicação Técnica:** Uma Assinatura de Acesso Compartilhado (SAS) fornece acesso delegado seguro aos recursos da sua conta de armazenamento com controle granular sobre permissões (leitura, escrita), tempo de expiração e faixas de IP permitidas.

### Questão 194
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Você precisa redeplacar uma Máquina Virtual do Azure para um novo host físico para solucionar um problema de travamento no hardware subjacente. Qual comando/opção no portal do Azure deve ser utilizado?
**Opções:**
- A) Reiniciar (Restart)
- B) Redimplantar (Redeploy)
- C) Capturar (Capture)
- D) Desconectar NIC
**Resposta Correta:** B
**Explicação Técnica:** A opção Redimplantar (Redeploy) move a máquina virtual para um novo nó/host físico dentro do data center do Azure e a liga novamente, mantendo a configuração do disco e dos endereços IP atribuídos.

### Questão 195
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Sua equipe quer ser notificada sempre que a Microsoft publicar um aviso relativo a interrupções planejadas de manutenção que afetem os serviços do Azure na sua região de produção. Qual serviço deve ser configurado?
**Opções:**
- A) Saúde do Serviço do Azure (Azure Service Health)
- B) Azure Advisor
- C) Log Analytics Workspace
- D) Azure Monitor Metrics
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Health fornece painéis e alertas personalizados sobre a integridade dos serviços do Azure, informando sobre interrupções de serviço, manutenções planejadas e orientações relativas às suas subscrições específicas.

### Questão 196
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** Você precisa atribuir a uma equipe de auditores a permissão de apenas visualizar as configurações do Azure sem poder alterar nada. Qual função RBAC integrada deve ser concedida?
**Opções:**
- A) Leitor (Reader)
- B) Colaborador (Contributor)
- C) Proprietário (Owner)
- D) Usuário de Acesso Geral
**Resposta Correta:** A
**Explicação Técnica:** A função integrada Leitor (Reader) permite que o usuário visualize todos os recursos e configurações em um determinado escopo do Azure, mas impede a realização de qualquer alteração ou exclusão.

### Questão 197
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** Você precisa resolver nomes de domínio DNS privados para VMs dentro de suas Redes Virtuais sem provisionar servidores DNS personalizados em VMs. Qual serviço nativo do Azure atende a isso?
**Opções:**
- A) Zonas Privadas do DNS do Azure (Azure DNS Private Zones)
- B) Registro de Nomes NetBIOS
- C) Azure ExpressRoute
- D) Azure Traffic Manager
**Resposta Correta:** A
**Explicação Técnica:** As Zonas Privadas do DNS do Azure (Azure DNS Private Zones) fornecem uma solução de gerenciamento e resolução de nomes confiável e segura para sua rede virtual, eliminando a necessidade de implantar soluções DNS personalizadas.

### Questão 198
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** Sua empresa exige que todas as Contas de Armazenamento criadas no Azure utilizem criptografia com chaves que a própria empresa gerencia e rotaciona no Azure Key Vault. Qual o nome dessa funcionalidade de criptografia?
**Opções:**
- A) Criptografia do Serviço de Armazenamento com Chaves Gerenciadas pelo Cliente (Customer-Managed Keys - CMK)
- B) Criptografia BitLocker Local
- C) Chaves Gerenciadas pela Microsoft (MMK)
- D) Hash MD5 de Conteúdo
**Resposta Correta:** A
**Explicação Técnica:** O uso de Chaves Gerenciadas pelo Cliente (Customer-Managed Keys - CMK) permite que as organizações utilizem suas próprias chaves de criptografia armazenadas no Azure Key Vault para criptografar os dados em repouso do Azure Storage.

### Questão 199
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** Uma máquina virtual Windows no Azure não responde via RDP. Você precisa verificar os logs de inicialização do sistema operacional e visualizar uma captura de tela da tela de login para diagnosticar o erro. Qual recurso você deve ativar na VM?
**Opções:**
- A) Diagnóstico de Inicialização (Boot Diagnostics)
- B) Extensão Custom Script
- C) Azure Serial Console apenas
- D) Regras de Coleta de Dados (DCR)
**Resposta Correta:** A
**Explicação Técnica:** O recurso Diagnóstico de Inicialização (Boot Diagnostics) captura saídas do log de texto e telas de captura (screenshots) do console de inicialização da máquina virtual para auxiliar na depuração de falhas de boot.

### Questão 200
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** Você precisa enviar dados de telemetria e métricas personalizadas de uma aplicação hospedada no Azure App Service para análise detalhada no Azure Monitor. Qual recurso do Azure Monitor deve ser integrado à aplicação?
**Opções:**
- A) Application Insights
- B) Azure Sentinel
- C) Network Watcher
- D) Log Analytics Agent clássico
**Resposta Correta:** A
**Explicação Técnica:** O Application Insights é um recurso do Azure Monitor que fornece Gerenciamento de Desempenho de Aplicativos (APM) para desenvolvedores, coletando telemetria de chamadas HTTP, exceções, tempos de resposta e métricas personalizadas.
