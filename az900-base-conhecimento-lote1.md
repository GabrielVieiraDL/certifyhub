# Base de Conhecimento do Exame AZ-900 — Lote 1 (Questões 001 a 050)

Esta base de conhecimento em Markdown foi estruturada no formato determinístico de parsing para agentes de IA no **Antigravity**, abrangendo as questões de 001 a 050 do exame **AZ-900: Microsoft Azure Fundamentals**, totalmente traduzidas para **Português do Brasil (pt-BR)** com a nomenclatura técnica oficial da Microsoft.

---

## Esquema de Parsing (Agent Schema)
Cada questão segue estritamente a sintaxe:
```markdown
### Questão [ID]
**Domínio:** [Conceitos de Nuvem | Arquitetura e Serviços | Gerenciamento e Governança]
**Enunciado:** [Texto traduzido em pt-BR]
**Opções:**
- A) [Alternativa A]
- B) [Alternativa B]
- C) [Alternativa C]
- D) [Alternativa D]
**Resposta Correta:** [Letra(s) da resposta oficial]
**Explicação Técnica:** [Justificativa didática fundamentada no Microsoft Learn]
```

---

## Questões do Lote 1 (001 a 050)

### Questão 001
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** A assinatura do Azure da sua empresa possui atualmente o plano de suporte Basic. Quais dos seguintes são planos de suporte que permitirão a abertura de novas solicitações de suporte no Portal do Azure?
**Opções:**
- A) Apenas Premier e Professional Direct
- B) Apenas Premier, Professional Direct e Standard
- C) Apenas Premier, Professional Direct, Standard e Developer
- D) Premier, Professional Direct, Standard, Developer e Basic
**Resposta Correta:** D
**Explicação Técnica:** Todos os planos de suporte do Azure (inclusive o Basic) permitem a abertura de chamados no Portal do Azure. No plano Basic, o suporte é voltado para gerenciamento de conta, cobrança e solicitações de aumento de cota de assinatura.

### Questão 002
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** A assinatura do Azure da sua empresa possui o plano de suporte Basic. A empresa gostaria de solicitar à Microsoft uma avaliação técnica do design de um ambiente Azure (*architectural review*). Você recomenda assinar o plano de suporte Developer para atender a essa necessidade mantendo os custos no mínimo. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** A avaliação arquitetural de ambientes no Azure exige pelo menos o plano de suporte **Professional Direct** ou **Premier / Unified**. O plano Developer cobre apenas suporte técnico para testes e ambientes não de produção.

### Questão 003
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Sua empresa possui o plano de suporte Basic e deseja solicitar à Microsoft uma avaliação técnica do design de um ambiente Azure (*architectural review*), mantendo os custos no mínimo. Você recomenda a assinatura do plano de suporte Professional Direct. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** O plano **Professional Direct** é o nível mínimo de suporte que inclui assistência arquitetural básica, orientação de implantação e revisões de design fornecidas por engenheiros proativos do Azure.

### Questão 004
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa planeja migrar máquinas virtuais locais hospedadas em Hyper-V para uma assinatura do Azure Pague o que Usar (Pay-As-You-Go). Você precisa garantir que a solução utilize o modelo de despesas correto. Você recomenda o uso do modelo de despesas de capital (CapEx). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** O modelo CapEx (Despesas de Capital) aplica-se a custos iniciais de hardware e infraestrutura física local. A migração para serviços sob demanda na nuvem utiliza o modelo OpEx (Despesas Operacionais).

### Questão 005
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa planeja migrar máquinas virtuais locais para uma assinatura Pague o que Usar do Azure. Qual benefício financeiro da nuvem é obtido ao substituir custos fixos de infraestrutura física por despesas operacionais flexíveis?
**Opções:**
- A) Modelo de Despesas Operacionais (OpEx)
- B) Modelo de Despesas de Capital (CapEx)
- C) Custo Fixo Permanente
- D) Modelo de Armazenamento Dedicado
**Resposta Correta:** A
**Explicação Técnica:** A computação em nuvem opera predominantemente sob o modelo OpEx, permitindo às empresas pagar apenas pelos recursos consumidos ao longo do tempo, sem a necessidade de investimentos massivos prévios em data centers físicos.

### Questão 006
**Domínio:** Conceitos de Nuvem
**Enunciado:** Você precisa implantar máquinas virtuais do Azure para a sua empresa utilizando o modelo de implantação de nuvem adequado. Você recomenda o uso de Infraestrutura como Serviço (IaaS). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** As Máquinas Virtuais do Azure (VMs) são o exemplo clássico do modelo IaaS (Infraestrutura como Serviço), no qual a Microsoft gerencia o hardware e hipervisor, enquanto o cliente gerencia o SO e as aplicações.

### Questão 007
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Seus desenvolvedores criaram 10 aplicações web que serão hospedadas no Azure. Cada aplicação requer domínio personalizado, 10 GB de armazenamento, instâncias de computação dedicadas e balanceamento de carga entre instâncias ao menor custo. Qual plano de Serviço de Aplicativo (App Service Plan) deve ser utilizado?
**Opções:**
- A) Gratuito (Free)
- B) Compartilhado (Shared)
- C) Básico (Basic)
- D) Padrão (Standard)
**Resposta Correta:** D
**Explicação Técnica:** O nível **Standard** (Padrão) do Azure App Service é o menor nível que oferece instâncias de computação dedicadas, domínios personalizados, armazenamento suficiente e recursos nativos de balanceamento de carga e dimensionamento automático (auto-scaling).

### Questão 008
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa deseja segmentar a administração de recursos do Azure entre diversas divisões organizacionais, reduzindo o esforço administrativo ao mínimo. Você recomenda criar diretórios do Microsoft Entra ID (Azure AD) separados para cada divisão. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** Criar múltiplos diretórios do Microsoft Entra ID aumenta drasticamente o esforço de gerenciamento de identidades. A abordagem recomendada é utilizar uma única locação (tenant) com **Assinaturas** ou **Grupos de Recursos** separados por divisão.

### Questão 009
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa pretende migrar máquinas virtuais locais para o Azure sob a assinatura Pague o que Usar. Você recomenda a utilização do modelo de despesas elásticas. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** Embora a nuvem seja elástica, a nomenclatura técnica oficial para a classificação de custos no ecossistema de finanças da nuvem é o **Modelo de Despesas Operacionais (OpEx)**, e não "modelo de despesas elásticas".

### Questão 010
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa pretende migrar máquinas virtuais locais para o Azure sob a assinatura Pague o que Usar. Você recomenda a utilização do modelo de despesas escaláveis. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** A terminologia contábil oficial reconhecida nos exames da Microsoft para a transição de pagamentos de infraestrutura na nuvem é **OpEx (Operational Expenditure)**.

### Questão 011
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa pretende migrar máquinas virtuais locais para o Azure sob a assinatura Pague o que Usar. Você recomenda a utilização do modelo de despesas operacionais (OpEx). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** A assinatura Pague o que Usar do Azure categoriza todos os custos de computação e armazenamento como **OpEx (Despesas Operacionais)**, eliminando custos prévios de infraestrutura física.

### Questão 012
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa precisa implantar uma solução de Inteligência Artificial no Azure que permita construir, testar e implantar análises preditivas. Você recomenda o uso do Azure Machine Learning Studio. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** O **Azure Machine Learning Studio** é o serviço voltado para cientistas de dados e desenvolvedores construírem, treinarem e implantarem modelos preditivos e de IA na nuvem.

### Questão 013
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** A infraestrutura da sua empresa possui várias unidades de negócios que exigem a criação automática e padronizada dos mesmos conjuntos de recursos no Azure. Você recomenda incluir o serviço Gerenciamento de API do Azure (Azure API Management) na estratégia. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** O Azure API Management é uma plataforma para publicar e gerenciar APIs. Para automatizar e padronizar a criação de recursos no Azure, deve-se utilizar modelos do **Azure Resource Manager (ARM Templates)** ou **Azure Bicep**.

### Questão 014
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa deseja implementar uma estratégia para provisionar recursos idênticos do Azure automaticamente para várias unidades de negócios. Você recomenda o uso de modelos do Azure Resource Manager (ARM Templates). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** Os **Modelos ARM (Azure Resource Manager Templates)** fornecem infraestrutura como código (IaC), permitindo implantar e replicar ambientes e recursos do Azure de forma consistente e automatizada.

### Questão 015
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Você precisa implantar uma aplicação crítica de linha de negócios (LOB) em uma máquina virtual no Azure garantindo um SLA de disponibilidade de 99,99%. A estratégia deve utilizar o menor número possível de VMs e Zonas de Disponibilidade. Você recomenda incluir uma máquina virtual e duas zonas de disponibilidade. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** Para obter o SLA de 99,99% de disponibilidade no Azure, é necessário implantar pelo menos **duas ou mais máquinas virtuais** distribuídas entre duas ou mais **Zonas de Disponibilidade (Availability Zones)**. Uma única VM não atinge 99,99%.

### Questão 016
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Os desenvolvedores da sua empresa precisam implantar e remover semanalmente uma grande quantidade de máquinas virtuais personalizadas de teste (Windows e Linux) minimizando o esforço administrativo. Você recomenda o uso do Azure DevTest Labs. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** O **Azure DevTest Labs** permite provisionar rapidamente ambientes de teste e desenvolvimento com imagens pré-configuradas e desprovimento automático para controle de custos e redução de tarefas administrativas.

### Questão 017
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Durante a automação da implantação de servidores no Azure, sua empresa deseja garantir que credenciais administrativas sejam criptografadas durante o processo. Você recomenda o uso do Azure Information Protection. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** O Azure Information Protection é voltado para proteção e classificação de documentos e e-mails. Para armazenar e gerenciar chaves e credenciais criptografadas de forma segura durante implantações, deve-se utilizar o **Azure Key Vault**.

### Questão 018
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Sua empresa deseja garantir que usuários que se conectam ao Microsoft Entra ID (Azure AD) a partir de endereços IP não identificados sejam forçados automaticamente a alterar suas senhas. Você recomenda o uso do Azure AD Privileged Identity Management (PIM). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** O recurso que detecta riscos de entrada (como conexões de IPs desconhecidos) e aplica políticas de alteração de senha automática é o **Microsoft Entra ID Protection (Identity Protection)**. O PIM é focado na gestão de privilégios temporários (Just-In-Time).

### Questão 019
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Você está planejando uma estratégia para implantar servidores web e servidores de banco de dados no Azure. A estratégia deve permitir controlar e restringir os tipos de tráfego de rede permitidos entre os servidores web e de banco de dados. Você recomenda incluir Grupos de Segurança de Rede (NSGs). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** Os **Grupos de Segurança de Rede (NSGs - Network Security Groups)** funcionam como firewalls de camada de rede/transporte, permitindo filtrar e controlar o tráfego de entrada e saída entre subredes e recursos no Azure.

### Questão 020
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Você precisa controlar o tráfego de rede entre servidores web e de banco de dados no Azure. Você recomenda o uso de um Gateway de Rede Local (Local Network Gateway). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** O Local Network Gateway representa o dispositivo VPN local e seu endereço IP público em conexões VPN site a site. Ele não é utilizado para filtrar tráfego interno entre subredes no Azure.

### Questão 021
**Domínio:** Conceitos de Nuvem
**Enunciado:** Ao implementar uma solução de Software como Serviço (SaaS), qual das seguintes responsabilidades permanece sob o controle e configuração do cliente?
**Opções:**
- A) Configuração do software e dados da aplicação
- B) Definição de regras de escalabilidade de infraestrutura
- C) Instalação de patches do sistema operacional
- D) Configuração de alta disponibilidade física do data center
**Resposta Correta:** A
**Explicação Técnica:** No modelo SaaS, a Microsoft gerencia toda a infraestrutura física, virtualização, sistema operacional e runtime da aplicação. O cliente é responsável apenas por configurar o uso do software e gerenciar os dados de entrada e acesso dos usuários.

### Questão 022
**Domínio:** Conceitos de Nuvem
**Enunciado:** Ao planejar a migração de um site público para o Azure, qual fator financeiro a empresa deve considerar no modelo de preços?
**Opções:**
- A) Implantar uma rede privada virtual (VPN) obrigatória
- B) Pagar custos de uso mensal sob o modelo Pague o que Usar
- C) Pagar tarifas para transferir todos os dados de entrada para o Azure
- D) Reduzir o número de conexões simultâneas do site
**Resposta Correta:** B
**Explicação Técnica:** O Azure opera no modelo Pague o que Usar (Pay-As-You-Go), onde os serviços de hospedagem e tráfego de saída são faturados mensalmente com base no consumo real. A transferência de dados de entrada (*inbound data transfer*) para o Azure é gratuita.

### Questão 023
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O plano de migração da sua empresa estabelece que apenas soluções de Plataforma como Serviço (PaaS) devem ser utilizadas no Azure. Você recomenda implantar o Azure App Service e Bancos de Dados SQL do Azure (Azure SQL Databases). Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** Tanto o **Azure App Service** (hospedagem de aplicações web) quanto o **Azure SQL Database** (banco de dados relacional gerenciado) são serviços totalmente classificados como Plataforma como Serviço (PaaS).

### Questão 024
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O plano de migração da sua empresa estabelece que apenas soluções de Plataforma como Serviço (PaaS) devem ser utilizadas no Azure. Você recomenda a criação de Máquinas Virtuais do Azure com o Microsoft SQL Server instalado. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** Máquinas Virtuais (VMs) pertencem à categoria Infraestrutura como Serviço (IaaS). Mesmo instalando o SQL Server nelas, a responsabilidade pelo gerenciamento do SO e patches continua sendo do cliente.

### Questão 025
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual modelo de serviço de nuvem é representado por Máquinas Virtuais do Azure e pelo Banco de Dados SQL do Azure, respectivamente?
**Opções:**
- A) Máquinas Virtuais: IaaS | Banco de Dados SQL: PaaS
- B) Máquinas Virtuais: PaaS | Banco de Dados SQL: SaaS
- C) Máquinas Virtuais: IaaS | Banco de Dados SQL: IaaS
- D) Máquinas Virtuais: SaaS | Banco de Dados SQL: PaaS
**Resposta Correta:** A
**Explicação Técnica:** As Máquinas Virtuais oferecem controle total de infraestrutura (IaaS), enquanto o Azure SQL Database abstrai o sistema operacional e infraestrutura subjacente, oferecendo um mecanismo de banco de dados totalmente gerido (PaaS).

### Questão 026
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual funcionalidade de continuidade de negócios do Azure oferece proteção contra falhas em nível de site copiando e replicando cargas de trabalho de máquinas virtuais de um local primário para um secundário?
**Opções:**
- A) Tolerância a falhas local
- B) Azure Site Recovery (Disaster Recovery)
- C) Elasticidade automática
- D) Conjuntos de Escalonamento de VMs
**Resposta Correta:** B
**Explicação Técnica:** O **Azure Site Recovery** é a solução de recuperação de desastres (Disaster Recovery) como serviço da Microsoft que replica cargas de trabalho de VMs físicas ou virtuais para um local secundário, garantindo a continuidade dos negócios durante paralisações operacionais.

### Questão 027
**Domínio:** Conceitos de Nuvem
**Enunciado:** Em qual modelo de nuvem todos os recursos de hardware pertencem a um provedor terceirizado e são compartilhados entre múltiplos locatários (multitenant)?
**Opções:**
- A) Nuvem Privada
- B) Nuvem Híbrida
- C) Nuvem Pública
- D) Nuvem Comunitária Dedicada
**Resposta Correta:** C
**Explicação Técnica:** Na **Nuvem Pública** (como o Microsoft Azure), a infraestrutura física pertence e é mantida pelo provedor, sendo compartilhada eficientemente por múltiplos clientes através do isolamento lógico de locatários.

### Questão 028
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual afirmativa sobre as soluções de Plataforma como Serviço (PaaS) é verdadeira?
**Opções:**
- A) O PaaS fornece controle total sobre o sistema operacional hospedado
- B) O PaaS exige a instalação manual de atualizações do sistema operacional pelo cliente
- C) O PaaS permite dimensionar automaticamente o número de instâncias com base na demanda
- D) O PaaS não inclui armazenamento de dados gerenciado
**Resposta Correta:** C
**Explicação Técnica:** As plataformas PaaS automatizam o gerenciamento de sistemas operacionais e infraestrutura, permitindo que as aplicações escalem horizontalmente (aumentando ou diminuindo instâncias automaticamente) conforme a demanda de tráfego.

### Questão 029
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa possui uma rede local com vários servidores físicos. Ao migrar os servidores para Máquinas Virtuais do Azure, quais responsabilidades administrativas serão eliminadas? (Escolha duas opções)
**Opções:**
- A) Substituição de hardware de servidor com falha
- B) Backup dos dados da aplicação
- C) Gerenciamento da segurança física do data center
- D) Atualização do sistema operacional das VMs
- E) Gerenciamento de permissões de documentos compartilhados
**Resposta Correta:** A, C
**Explicação Técnica:** No modelo IaaS das VMs do Azure, a Microsoft assume a manutenção física do hardware (substituição de peças defeituosas) e a segurança física dos data centers. O cliente mantém a responsabilidade pelo SO, dados e aplicação.

### Questão 030
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O Banco de Dados SQL do Azure e o Azure Cosmos DB são exemplos de qual modelo de serviço de nuvem?
**Opções:**
- A) Infraestrutura como Serviço (IaaS)
- B) Plataforma como Serviço (PaaS)
- C) Software como Serviço (SaaS)
- D) Desktops Virtuais
**Resposta Correta:** B
**Explicação Técnica:** Tanto o Azure SQL Database quanto o Azure Cosmos DB são bancos de dados totalmente gerenciados sem servidor/servidores aparentes para manutenção de SO, enquadrando-se como Plataforma como Serviço (PaaS).

### Questão 031
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Azure permite aplicar travas para impedir a exclusão ou modificação acidental de recursos por administradores?
**Opções:**
- A) Azure Blueprints
- B) Bloqueio de Recursos (Resource Lock)
- C) Azure Policy
- D) Endpoints de Serviço
**Resposta Correta:** B
**Explicação Técnica:** Os **Bloqueios de Recursos (Resource Locks)** do tipo *CanNotDelete* ou *ReadOnly* impedem a exclusão ou alteração de recursos essenciais do Azure, mesmo por usuários com perfil de Administrador Global.

### Questão 032
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que um cliente fornece em um modelo de Software como Serviço (SaaS)?
**Opções:**
- A) Dados e configurações da aplicação
- B) Infraestrutura de armazenamento de dados
- C) Recursos de computação e servidores
- D) Licenciamento do sistema operacional
**Resposta Correta:** A
**Explicação Técnica:** Em soluções SaaS (como o Microsoft 365), o provedor cuida de toda a pilha de software e infraestrutura. O cliente apenas fornece os dados da aplicação e os parâmetros de configuração e usuários.

### Questão 033
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual benefício da computação em nuvem permite que os recursos computacionais sejam provisionados dinamicamente para atender às mudanças nas demandas de tráfego?
**Opções:**
- A) Agilidade
- B) Distribuição Geográfica
- C) Escalabilidade
- D) Tolerância a Falhas
**Resposta Correta:** C
**Explicação Técnica:** **Escalabilidade** é a capacidade de adicionar ou remover recursos computacionais (memória, CPU ou instâncias) de forma dinâmica para acompanhar o aumento ou a diminuição da carga de trabalho.

### Questão 034
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa possui uma aplicação contábil legada (App1) baseada em banco de dados antigo. Ao migrar a App1 para a nuvem sem alterar seu código ou arquitetura (*Lift-and-Shift*), qual modelo de serviço deve ser utilizado?
**Opções:**
- A) Plataforma como Serviço (PaaS)
- B) Infraestrutura como Serviço (IaaS)
- C) Software como Serviço (SaaS)
- D) Função como Serviço (FaaS)
**Resposta Correta:** B
**Explicação Técnica:** A estratégia de migração *Lift-and-Shift* (re-hospedagem de sistemas legados em máquinas virtuais na nuvem sem reescrita de código) é atendida pelo modelo IaaS (Infraestrutura como Serviço).

### Questão 035
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure de armazenamento suporta a sincronização bidirecional de arquivos entre servidores locais da empresa e a nuvem?
**Opções:**
- A) Azure Blob Storage
- B) Azure Files (Azure File Sync)
- C) Azure Queue Storage
- D) Azure Table Storage
**Resposta Correta:** B
**Explicação Técnica:** O **Azure File Sync** é o agente que centraliza os compartilhamentos de arquivos da sua empresa no Azure Files, mantendo o desempenho e a compatibilidade de um servidor de arquivos local com sincronização na nuvem.

### Questão 036
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual termo representa a capacidade de aumentar a capacidade de computação de uma máquina virtual adicionando mais memória RAM ou CPUs à mesma instância?
**Opções:**
- A) Agilidade
- B) Escalabilidade Vertical (Scale Up)
- C) Escalabilidade Horizontal (Scale Out)
- D) Elasticidade
**Resposta Correta:** B
**Explicação Técnica:** A **Escalabilidade Vertical (Scale Up)** consiste no aumento da capacidade de um recurso individual (adicionando mais vCPU ou memória a uma VM existente). A escalabilidade horizontal adiciona mais instâncias de VMs.

### Questão 037
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Você planeja implantar várias máquinas virtuais no Azure. O que deve ser feito para garantir que os serviços nas VMs continuem disponíveis mesmo se um data center físico inteiro falhar?
**Opções:**
- A) Implantar as máquinas virtuais em um Conjunto de Disponibilidade (Availability Set)
- B) Implantar as máquinas virtuais em Zonas de Disponibilidade (Availability Zones) distintas
- C) Implantar as máquinas virtuais em Grupos de Recursos diferentes
- D) Aumentar o tamanho do disco de armazenamento das VMs
**Resposta Correta:** B
**Explicação Técnica:** As **Zonas de Disponibilidade** são data centers fisicamente separados dentro da mesma região do Azure. Distribuir VMs entre zonas garante resiliência contra a falha completa de um data center.

### Questão 038
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Sua empresa possui vários departamentos e cada um terá um administrador para gerenciar seus próprios recursos no Azure. Quais são duas técnicas válidas para segmentar o gerenciamento do Azure para os departamentos? (Escolha duas opções)
**Opções:**
- A) Múltiplas Assinaturas do Azure
- B) Múltiplos diretórios do Microsoft Entra ID
- C) Múltiplas regiões geográficas
- D) Múltiplos Grupos de Recursos
**Resposta Correta:** A, D
**Explicação Técnica:** **Assinaturas** e **Grupos de Recursos** funcionam como limites de gerenciamento, faturamento e controle de acesso (RBAC), permitindo delegar a administração de recursos por departamento de forma isolada.

### Questão 039
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure envia notificações proativas sobre interrupções de serviço, atividades de manutenção planejadas e avisos de saúde relevantes para a sua assinatura?
**Opções:**
- A) Azure Monitor
- B) Azure Service Health
- C) Azure Advisor
- D) Central de Confiabilidade (Trust Center)
**Resposta Correta:** B
**Explicação Técnica:** O **Azure Service Health** fornece uma visão personalizada do status de integridade dos serviços e regiões do Azure que a sua empresa efetivamente utiliza, notificando sobre falhas e manutenções programadas.

### Questão 040
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é a falha mais severa contra a qual uma Zona de Disponibilidade (Availability Zone) do Azure protege os seus serviços?
**Opções:**
- A) Falha em um servidor físico individual
- B) Falha em uma região inteira do Azure
- C) Falha em um disco de armazenamento local
- D) Falha em um data center físico do Azure
**Resposta Correta:** D
**Explicação Técnica:** Cada Zona de Disponibilidade possui infraestrutura de energia, refrigeração e rede independente. Portanto, a proteção máxima é contra o nocaute/falha de um **data center completo**.

### Questão 041
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O que acontece quando você cria uma nova assinatura do Azure em relação às máquinas virtuais existentes de outra assinatura?
**Opções:**
- A) As máquinas virtuais não podem ser movidas para a nova assinatura
- B) As máquinas virtuais podem ser movidas para a nova assinatura através do Portal do Azure
- C) As máquinas virtuais só podem ser movidas se estiverem no mesmo grupo de recursos
- D) As máquinas virtuais só podem ser movidas se executarem o Windows Server
**Resposta Correta:** B
**Explicação Técnica:** O Azure permite mover recursos (como Máquinas Virtuais e suas redes e discos associados) entre diferentes assinaturas do Azure sem necessidade de recriação.

### Questão 042
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual solução de Internet das Coisas (IoT) da Microsoft inclui microcontroladores certificados, um sistema operacional baseado em Linux e um serviço de segurança de nuvem dedicado?
**Opções:**
- A) Azure Arc
- B) Azure IoT Central
- C) Azure IoT Hub
- D) Azure Sphere
**Resposta Correta:** D
**Explicação Técnica:** O **Azure Sphere** é a solução completa de segurança de IoT composta por hardware (microcontroladores de chip único), SO Linux customizado e serviço de segurança contínua em nuvem.

### Questão 043
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual ferramenta do Azure permite adquirir soluções de software de terceiros, imagens de máquinas virtuais e serviços certificados desenvolvidos por parceiros da Microsoft?
**Opções:**
- A) Subscrições do Azure
- B) Central de Segurança do Azure
- C) Azure Marketplace
- D) Microsoft Store
**Resposta Correta:** C
**Explicação Técnica:** O **Azure Marketplace** é o catálogo oficial onde parceiros e fornecedores oferecem milhares de softwares, imagens de VMs, APIs e soluções integradas prontas para implantação na sua assinatura do Azure.

### Questão 044
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual tipo de serviço de nuvem é representado pelas Instâncias de Contêiner do Azure (Azure Container Instances - ACI)?
**Opções:**
- A) Serviço de Computação (Compute Service)
- B) Serviço de Identidade (Identity Service)
- C) Serviço de Rede (Networking Service)
- D) Serviço de Armazenamento (Storage Service)
**Resposta Correta:** A
**Explicação Técnica:** As **Instâncias de Contêiner do Azure (ACI)** pertencem à categoria de **Serviços de Computação (Compute Services)** serverless, permitindo executar contêineres Docker sem gerenciar servidores subjacentes.

### Questão 045
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual funcionalidade do Azure Monitor fornece gerenciamento de desempenho de aplicações (APM) e monitoramento de telemetria em tempo real para aplicações web ativas?
**Opções:**
- A) Azure Advisor
- B) Application Insights
- C) Azure Service Health
- D) Azure Arc
**Resposta Correta:** B
**Explicação Técnica:** O **Application Insights** é uma extensão do Azure Monitor focada em APM (Application Performance Management), coletando logs, exceções e métricas de desempenho de aplicações web em tempo real.

### Questão 046
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Como as opções de redundância de Contas de Armazenamento do Azure são ordenadas da MENOR redundância para a MAIOR redundância?
**Opções:**
- A) LRS (Armazenamento com Redundância Local) -> ZRS (Redundância de Zona) -> GRS (Redundância Geográfica)
- B) GRS -> ZRS -> LRS
- C) ZRS -> LRS -> GRS
- D) LRS -> GRS -> ZRS
**Resposta Correta:** A
**Explicação Técnica:** O **LRS** replica os dados 3 vezes em um único data center local (menor redundância). O **ZRS** replica os dados em 3 zonas de disponibilidade na mesma região. O **GRS** replica os dados em uma região secundária distante (maior redundância).

### Questão 047
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Um administrador do Azure planeja executar um script em PowerShell para criar recursos no Azure a partir de um computador Linux com o Azure CLI instalado. Essa solução atinge o objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** Um script de PowerShell (`.ps1`) exige o runtime do **PowerShell Core** ou o módulo **Azure PowerShell (`Az`)** instalado para rodar seus cmdlets. Ter apenas o Azure CLI no Linux não permite executar scripts nativos de PowerShell.

### Questão 048
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ícone no cabeçalho do Portal do Azure deve ser selecionado para abrir a experiência de linha de comando interativa no navegador (*Azure Cloud Shell*)?
**Opções:**
- A) Ícone de Notificações (Sino)
- B) Ícone do Cloud Shell (`>_`)
- C) Ícone de Configurações (Engrenagem)
- D) Ícone de Ajuda e Suporte (`?`)
**Resposta Correta:** B
**Explicação Técnica:** O ícone representado por um terminal de comando **`>_`** na barra superior do Portal do Azure inicializa a sessão do **Azure Cloud Shell** (Bash ou PowerShell).

### Questão 049
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure permite enviar alertas automáticos por e-mail quando a utilização de recursos ou os custos de uma assinatura atingem um limite financeiro especificado?
**Opções:**
- A) Recomendações do Azure Advisor
- B) Alertas de Orçamento (Budget Alerts) no Gerenciamento de Custos
- C) Azure Policy
- D) Controle de Acesso (IAM)
**Resposta Correta:** B
**Explicação Técnica:** Os **Alertas de Orçamento (Budget Alerts)** no Azure Cost Management notificam os administradores quando o gasto acumulado ou estimado excede o valor teto configurado no orçamento da assinatura.

### Questão 050
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Onde o Azure Monitor armazena os dados de eventos, logs de diagnóstico e métricas coletados dos recursos do Azure para execução de consultas KQL (Kusto Query Language)?
**Opções:**
- A) Em uma Conta de Armazenamento do Azure Blob
- B) Em uma Fila do Azure Storage
- C) Em um Banco de Dados SQL do Azure
- D) Em um Workspace do Log Analytics (Log Analytics Workspace)
**Resposta Correta:** D
**Explicação Técnica:** O **Log Analytics Workspace** é o repositório central do Azure Monitor onde os logs de eventos e telemetrias são indexados e armazenados, permitindo análises e consultas avançadas via KQL.
