# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals - Lote 6 (Questões 251 a 300)

Esta base de conhecimento contém as questões 251 a 300 do exame **AZ-900: Microsoft Azure Fundamentals** formatadas para ingestão e automação no Antigravity.

---

### Questão 251
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa precisa migrar sua aplicação legada para o Azure. A aplicação exige acesso direto ao sistema operacional subjacente para instalar drivers personalizados e softwares de terceiros antigos. Qual modelo de serviço de nuvem atende a esse requisito?
**Opções:**
- A) Software como Serviço (SaaS)
- B) Plataforma como Serviço (PaaS)
- C) Infraestrutura como Serviço (IaaS)
- D) Função como Serviço (FaaS)
**Resposta Correta:** C
**Explicação Técnica:** O modelo Infraestrutura como Serviço (IaaS) fornece controle total sobre os sistemas operacionais das máquinas virtuais, permitindo a instalação de drivers customizados, modificações no kernel e softwares legados incompatíveis com PaaS ou SaaS.

### Questão 252
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é projetado para processamento e análise de grandes volumes de dados (Big Data) utilizando clusters gerenciados do Apache Spark, Hadoop e HBase?
**Opções:**
- A) Azure HDInsight
- B) Azure Synapse Analytics
- C) Azure Event Grid
- D) Azure Data Factory
**Resposta Correta:** A
**Explicação Técnica:** O Azure HDInsight é um serviço gerenciado de análise de dados de código aberto que simplifica a execução de frameworks popularizados como Apache Spark, Hadoop, Hive e HBase em escala de Big Data.

### Questão 253
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja centralizar e visualizar os logs de auditoria, eventos de segurança e alertas gerados por múltiplos serviços do Azure em uma única ferramenta de visualização interativa com suporte a relatórios personalizados. Qual serviço deve ser utilizado?
**Opções:**
- A) Pastas de Trabalho do Azure Monitor (Azure Monitor Workbooks)
- B) Azure Advisor
- C) Bloqueios de Recursos (Resource Locks)
- D) Grupos de Ação do Azure (Azure Action Groups)
**Resposta Correta:** A
**Explicação Técnica:** As Pastas de Trabalho do Azure Monitor (Workbooks) fornecem uma tela flexível para análise de dados e a criação de relatórios visuais avançados e interativos no Portal do Azure combinando métricas e logs.

### Questão 254
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite que desenvolvedores publiquem, protejam, transformem e monitorem APIs expostas a consumidores internos ou externos?
**Opções:**
- A) Gerenciamento de API do Azure (Azure API Management)
- B) Azure Application Gateway
- C) Azure Front Door
- D) Azure Service Bus
**Resposta Correta:** A
**Explicação Técnica:** O Gerenciamento de API do Azure (API Management) funciona como uma porta de entrada (API Gateway) para abstrair e proteger APIs de backend, controlando acesso via chaves e tokens, aplicandos rate limiting e fornecendo documentação para desenvolvedores.

### Questão 255
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Sua empresa deseja restringir quais regiões do Azure os administradores de TI podem selecionar no momento do provisionamento de novos recursos. Qual ferramenta de governança atende a essa exigência?
**Opções:**
- A) Azure Policy
- B) Controle de Acesso Baseado em Função (RBAC)
- C) Bloqueio de Recursos (Resource Lock)
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy permite definir e aplicar regras de conformidade organizacional, como a política nativa "Regiões Permitidas" (*Allowed Locations*), impedindo a criação de recursos fora das regiões geográficas aprovadas.

### Questão 256
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é a função principal do serviço Azure Event Grid?
**Opções:**
- A) Roteamento de eventos serverless altamente escalável e baseado no modelo pub/sub
- B) Armazenamento persistente de mensagens de fila para processamento em lote
- C) Balanceamento de carga de tráfego web na camada 7
- D) Execução contínua de contêineres Docker sem estado
**Resposta Correta:** A
**Explicação Técnica:** O Azure Event Grid é um barramento de roteamento de eventos sem servidor (serverless) que utiliza o modelo de publicação/assinatura (pub/sub) para conectar emissores de eventos a receptores com baixa latência e alta disponibilidade.

### Questão 257
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure permite simular os custos operacionais futuros e comparar os custos de manter a infraestrutura no data center local com os custos de migração para o Azure?
**Opções:**
- A) Calculadora de TCO (Custo Total de Propriedade) do Azure
- B) Calculadora de Preços do Azure
- C) Gerenciamento de Custos do Azure (Azure Cost Management)
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** A Calculadora do Custo Total de Propriedade (TCO) permite estimar a economia de custos direta ao comparar todos os custos do ambiente local (servidores, energia, resfriamento, licenças e mão de obra) com o custo equivalente no Azure.

### Questão 258
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma arquitetura de nuvem que aproveita recursos de computação serverless e microsserviços atende principalmente a qual benefício da nuvem?
**Opções:**
- A) Agilidade e Eficiência Operacional
- B) Soberania de Dados Nacional
- C) Latência Zero Garantida
- D) Custo Fixo Previsível
**Resposta Correta:** A
**Explicação Técnica:** Arquiteturas serverless e baseadas em microsserviços aceleram o ciclo de desenvolvimento e implantação de softwares (agilidade), permitindo que as equipes foquem no valor de negócio enquanto a nuvem cuida da infraestrutura e escala automática.

### Questão 259
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual tipo de armazenamento de redundância do Azure replica os dados dentro da mesma região primária através de três data centers separados (Zonas de Disponibilidade)?
**Opções:**
- A) Armazenamento com Redundância de Zona (ZRS)
- B) Armazenamento com Redundância Local (LRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS)
**Resposta Correta:** A
**Explicação Técnica:** O Armazenamento com Redundância de Zona (ZRS - *Zone-Redundant Storage*) replica dados de forma síncrona em três Zonas de Disponibilidade independentes dentro da mesma região Azure.

### Questão 260
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Um administrador precisa atribuir a um auditor a permissão de visualizar os recursos de uma assinatura do Azure sem permitir a criação ou modificação de qualquer recurso. Qual função do RBAC do Azure deve ser atribuída?
**Opções:**
- A) Leitor (Reader)
- B) Colaborador (Contributor)
- C) Proprietário (Owner)
- D) Usuário de Acesso Central
**Resposta Correta:** A
**Explicação Técnica:** A função nativa *Leitor (Reader)* permite visualizar todos os recursos de um escopo, mas não concede permissões para criar, alterar ou excluir nada.

### Questão 261
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure fornece um registro centralizado para gerenciar e armazenar imagens privadas de contêineres Docker e artefatos relacionados?
**Opções:**
- A) Registro de Contêiner do Azure (Azure Container Registry - ACR)
- B) Instâncias de Contêiner do Azure (ACI)
- C) Serviço de Kubernetes do Azure (AKS)
- D) Aplicativos de Contêiner do Azure (ACA)
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Registry (ACR) é um serviço de registro privado baseado no Docker Registry 2.0 que permite armazenar e gerenciar imagens de contêineres e artefatos de implantação.

### Questão 262
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual opção do Azure permite agrupar várias Assinaturas em uma hierarquia organizacional para aplicar políticas de conformidade e controle de acesso unificados?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups)
- B) Grupos de Recursos (Resource Groups)
- C) Locatários do Microsoft Entra ID (Tenants)
- D) Unidades Administrativas
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento (*Management Groups*) fornecem um nível de escopo acima das Assinaturas. Eles permitem organizar assinaturas em uma hierarquia para aplicar Azure Policy e RBAC em escala sobre todas as assinaturas vinculadas.

### Questão 263
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual ferramenta de linha de comando multiplataforma baseada no Shell de comandos pode ser instalada no Windows, Linux e macOS para administrar recursos do Azure via scripts?
**Opções:**
- A) Azure CLI (Interface de Linha de Comando do Azure)
- B) Registro de Mensagens do Azure
- C) Azure Portal App
- D) Azure Quickstart Templates
**Resposta Correta:** A
**Explicação Técnica:** A Azure CLI é a interface de linha de comando nativa, multiplataforma e open-source para conectar ao Azure e executar comandos ou automações no Windows, macOS e Linux.

### Questão 264
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual é uma característica fundamental do modelo de nuvem privada?
**Opções:**
- A) A infraestrutura é dedicada exclusivamente a uma única organização
- B) Os custos são sempre compartilhados entre várias empresas
- C) Não exige equipe de TI para manutenção de hardware
- D) O acesso é totalmente aberto ao público via Internet
**Resposta Correta:** A
**Explicação Técnica:** Na nuvem privada (*Private Cloud*), os recursos computacionais são utilizados exclusivamente por uma única organização, seja em um data center próprio no local ou hospedados por terceiros.

### Questão 265
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que acontece quando duas políticas do Azure (Azure Policy) entram em conflito em um determinado grupo de recursos (ex.: uma política permite a criação de um tipo de recurso e outra nega explicitamente)?
**Opções:**
- A) A negação explícita (Deny) sempre prevalece sobre a permissão
- B) A permissão (Allow) sempre prevalece
- C) O grupo de recursos é bloqueado para todos os usuários
- D) O Azure envia um e-mail de alerta e aguarda aprovação manual
**Resposta Correta:** A
**Explicação Técnica:** No Azure Policy, os efeitos de negação (*Deny*) possuem prioridade sobre a liberação ou permissão para garantir a conformidade e a segurança do ambiente.

### Questão 266
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece um banco de dados relacional totalmente gerenciado baseado no mecanismo do PostgreSQL com alta disponibilidade nativa e backups automáticos?
**Opções:**
- A) Banco de Dados do Azure para PostgreSQL (Azure Database for PostgreSQL)
- B) Banco de Dados SQL do Azure (Azure SQL Database)
- C) Azure Cosmos DB
- D) Instância Gerenciada do SQL do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Database for PostgreSQL é um serviço de banco de dados relacional PaaS totalmente gerenciado baseado no mecanismo open-source PostgreSQL.

### Questão 267
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja garantir que certas VMs críticas não possam ter suas configurações alteradas nem serem excluídas acidentalmente, mesmo por administradores com papel de Proprietário. Qual tipo de trava deve ser aplicada?
**Opções:**
- A) Bloqueio de Somente Leitura (ReadOnly Lock)
- B) Bloqueio de Exclusão (Delete Lock)
- C) Política de Negação do Azure Policy
- D) Tag de Segurança
**Resposta Correta:** A
**Explicação Técnica:** O bloqueio de *Somente Leitura (ReadOnly)* impede que usuários leiam apenas atualizações ou modificações no recurso (o recurso pode ser lido, mas não alterado ou excluído). O bloqueio *CanNotDelete* impede apenas a exclusão.

### Questão 268
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure monitora o desempenho de aplicações web e fornece insights em tempo real sobre exceções, tempos de resposta de requisições e taxas de falha?
**Opções:**
- A) Application Insights (recurso do Azure Monitor)
- B) Azure Service Health
- C) Azure Advisor
- D) Log Analytics Workspace
**Resposta Correta:** A
**Explicação Técnica:** O Application Insights é um recurso do Azure Monitor que oferece Gerenciamento de Desempenho de Aplicações (APM) para desenvolvedores e equipes de DevOps monitorarem aplicações ativas em tempo real.

### Questão 269
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que caracteriza o conceito de "Tolerância a Falhas" (Fault Tolerance) na nuvem?
**Opções:**
- A) A capacidade de um sistema continuar operando sem interrupção perceptível mesmo em caso de falha de um componente de hardware
- B) O aumento da memória RAM do servidor quando o uso atinge 90%
- C) O direito de cancelar o contrato de nuvem sem multas a qualquer momento
- D) A duplicação automática da fatura mensal para fins de auditoria
**Resposta Correta:** A
**Explicação Técnica:** Tolerância a Falhas é a capacidade de uma arquitetura manter o serviço totalmente funcional e sem paralisação caso um componente (servidor, disco, fonte de alimentação) falhe, utilizando redundância transparente.

### Questão 270
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual camada de armazenamento do Azure Blob Storage é mais recomendada para armazenar backups de longo prazo que raramente são acessados e podem tolerar várias horas de latência de recuperação?
**Opções:**
- A) Camada de Arquivamento (Archive)
- B) Camada Fria (Cool)
- C) Camada Quente (Hot)
- D) Camada Premium
**Resposta Correta:** A
**Explicação Técnica:** A camada Archive é otimizada para dados que são raramente acessados e possuem requisitos de retenção flexíveis (meses/anos). Oferece o menor custo de armazenamento por gigabyte, porém com maior tempo e custo de recuperação.

### Questão 271
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é o objetivo principal do Portal de Confiança do Serviço (Service Trust Portal) da Microsoft?
**Opções:**
- A) Fornecer relatórios de auditoria independente, certificações ISO/SOC e documentação de conformidade regulatória dos serviços de nuvem da Microsoft
- B) Permitir a compra de licenças do Windows Server com desconto
- C) Monitorar a disponibilidade em tempo real dos data centers do Azure
- D) Abrir chamados de suporte técnico diretamente com a engenharia da Microsoft
**Resposta Correta:** A
**Explicação Técnica:** O Service Trust Portal é o site oficial da Microsoft que fornece acesso a relatórios de auditoria de terceiros, guias de proteção de dados, certificações de conformidade (ISO, SOC, HIPAA, GDPR) e recursos de conformidade corporativa.

### Questão 272
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Uma empresa precisa implantar uma solução para processar pagamentos com cartão de crédito via API com baixíssima latência e alcance global. Qual serviço de banco de dados NoSQL é o mais indicado no Azure?
**Opções:**
- A) Azure Cosmos DB
- B) Banco de Dados SQL do Azure
- C) Azure Database for MariaDB
- D) Azure Table Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cosmos DB é um banco de dados NoSQL totalmente gerenciado e distribuído globalmente, projetado para oferecer latência de leitura e escrita de um único dígito de milissegundo no 99º percentil com SLAs de 99,999%.

### Questão 273
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure permite associar metadados em formato de pares de chave-valor (Key-Value) aos recursos para categorizá-los e consolidar relatórios de faturamento?
**Opções:**
- A) Tags (Etiquetas) do Azure
- B) Azure Policy
- C) Bloqueios de Recursos (Resource Locks)
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** As Tags são pares de chave-valor atribuídos a recursos, grupos de recursos e assinaturas para organizá-los em uma taxonomia lógica para gerenciamento, auditoria e consolidação de custos.

### Questão 274
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual recurso de rede do Azure funciona como um balanceador de carga de tráfego web de camada 7 que inclui funcionalidades de Firewall de Aplicativo Web (WAF) e encerramento SSL/TLS?
**Opções:**
- A) Azure Application Gateway
- B) Azure Load Balancer
- C) Azure ExpressRoute
- D) Azure Traffic Manager
**Resposta Correta:** A
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego web (Camada 7) que permite gerenciar o tráfego de aplicações web, oferecendo recursos como roteamento baseado em URL, encerramento SSL e proteção WAF.

### Questão 275
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual plano de suporte do Azure inclui acesso 24 horas por dia, 7 dias por semana a engenheiros de suporte por e-mail e telefone para problemas de severidade A (críticos) com tempo de resposta inicial inferior a 1 hora?
**Opções:**
- A) Standard
- B) Developer
- C) Basic
- D) Community Support
**Resposta Correta:** A
**Explicação Técnica:** O plano de suporte *Standard* oferece suporte técnico 24x7 por e-mail e telefone com tempo de resposta inicial de < 1 hora para incidentes de impacto crítico (Severidade A).

### Questão 276
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual das seguintes afirmações sobre o modelo de responsabilidade compartilhada no Azure é verdadeira para uma máquina virtual (IaaS)?
**Opções:**
- A) A Microsoft é responsável pela segurança física do data center e o cliente é responsável pelo patching do sistema operacional da VM
- B) O cliente é responsável por manter os roteadores físicos do data center
- C) A Microsoft gerencia o controle de contas de usuários dentro da aplicação da VM
- D) O cliente é totalmente isento de configurar firewalls no sistema operacional
**Resposta Correta:** A
**Explicação Técnica:** No modelo IaaS, a Microsoft gerencia a infraestrutura física (data centers, energia, servidores e hipervisores), enquanto o cliente assume a responsabilidade do sistema operacional (patches, atualizações), configurações de rede virtual e segurança das aplicações.

### Questão 277
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é usado para criar, implantar e testar modelos de aprendizado de máquina (Machine Learning) utilizando ferramentas sem código (no-code), notebooks Jupyter e pipelines automatizados de MLOps?
**Opções:**
- A) Azure Machine Learning
- B) Azure AI Search
- C) Azure Bot Service
- D) Azure Cognitive Search
**Resposta Correta:** A
**Explicação Técnica:** O Azure Machine Learning é um serviço de nuvem de ponta a ponta para cientistas de dados e desenvolvedores criarem, treinarem e implantarem modelos de ML.

### Questão 278
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Um administrador precisa agendar a exclusão automática de recursos de teste todas as noites para evitar cobranças indesejadas. Qual recurso pode ser utilizado para criar essa automação sem servidor?
**Opções:**
- A) Automação do Azure (Azure Automation) com Runbooks ou Azure Functions
- B) Azure Advisor
- C) Bloqueios de Recursos (Resource Locks)
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Automation (usando Runbooks PowerShell/Python) ou o Azure Functions permitem programar rotinas e tarefas automatizadas de gerenciamento de recursos no Azure.

### Questão 279
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual recurso de armazenamento do Azure permite expor compartilhamentos de arquivos acessíveis via protocolo SMB (Server Message Block) ou NFS para acesso simultâneo de máquinas virtuais na nuvem ou locais?
**Opções:**
- A) Azure Files
- B) Azure Blob Storage
- C) Azure Table Storage
- D) Azure Disk Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files oferece compartilhamentos de arquivos totalmente gerenciados na nuvem acessíveis por meio dos protocolos padrão SMB e NFS.

### Questão 280
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Onde no Portal do Azure um usuário pode visualizar notificações proativas sobre interrupções de serviço planejadas e eventos que afetam a saúde dos serviços específicos que ele utiliza?
**Opções:**
- A) Azure Service Health
- B) Status do Azure (Azure Status - público)
- C) Azure Advisor
- D) Microsoft Defender for Cloud
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Health fornece um painel personalizado focado no status e saúde dos serviços e regiões específicos que a sua assinatura realmente utiliza, incluindo relatórios de incidentes e manutenções programadas.

### Questão 281
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é a função de um Grupo de Segurança de Rede (Network Security Group - NSG) no Azure?
**Opções:**
- A) Filtrar o tráfego de rede para e de recursos do Azure em uma Rede Virtual (VNet) usando regras de entrada e saída
- B) Criptografar automaticamente todas as comunicações de e-mail corporativo
- C) Gerenciar chaves de criptografia e certificados SSL
- D) Fornecer conexões privadas dedicadas sem passar pela Internet
**Resposta Correta:** A
**Explicação Técnica:** Um NSG contém regras de segurança que permitem ou negam o tráfego de rede de entrada (inbound) e saída (outbound) para interfaces de rede (NIC), VMs ou sub-redes em uma VNet.

### Questão 282
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta de gerenciamento do Azure permite escrever código declarativo em arquivos `.bicep` para provisionar e atualizar a infraestrutura de maneira reproduzível?
**Opções:**
- A) Bicep (linguagem para modelos do Azure Resource Manager)
- B) Azure CLI Scripts bash
- C) Azure Portal GUI
- D) Azure Mobile App
**Resposta Correta:** A
**Explicação Técnica:** O Bicep é uma linguagem de sintaxe declarativa específica para implantação de recursos do Azure como código (IaC), servindo como uma abstração mais simples e limpa sobre os modelos ARM (JSON).

### Questão 283
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que é o conceito de "Alcance Global" (Global Reach) fornecido pela Microsoft Azure?
**Opções:**
- A) A capacidade de implantar aplicações e dados em data centers espalhados por diversos continentes e regiões do mundo para aproximação com os usuários finais
- B) O direito de utilizar qualquer software da Microsoft em qualquer computador pessoal
- C) A garantia de que todos os funcionários da empresa terão acesso ilimitado à Internet
- D) A conversão automática de relatórios de faturamento para todas as moedas globais
**Resposta Correta:** A
**Explicação Técnica:** Alcance Global refere-se à presença mundial da infraestrutura da Microsoft com mais de 60 regiões ativas conectadas por uma rede backbone privada global, permitindo atender usuários em qualquer lugar do planeta com baixa latência.

### Questão 284
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é a principal vantagem de utilizar o Azure ExpressRoute Direct em comparação com uma conexão VPN baseada na Internet?
**Opções:**
- A) Largura de banda massiva de até 100 Gbps com conexões físicas diretas aos roteadores de borda da Microsoft sem tráfego na Internet pública
- B) Custo gratuito para transferência de dados de saída
- C) Dispensa o uso de placas de rede virtuais em VMs
- D) Não exige contratos com provedores de serviço
**Resposta Correta:** A
**Explicação Técnica:** O ExpressRoute Direct oferece portas dedicadas de 10 Gbps ou 100 Gbps conectadas diretamente aos roteadores globais da Microsoft, proporcionando a maior velocidade, menor latência e segurança isolada da Internet.

### Questão 285
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa quer auditar todas as ações de gerenciamento realizadas nos recursos do Azure nos últimos 90 dias (como quem excluiu uma máquina virtual e quando). Qual registro deve ser consultado?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Azure Log Analytics Workspace
- C) Microsoft Defender for Cloud Alerts
- D) Azure Service Health Incidents
**Resposta Correta:** A
**Explicação Técnica:** O Azure Activity Log registra eventos do plano de controle (gerenciamento), fornecendo visibilidade sobre todas as operações (criação, atualização, exclusão) executadas nos recursos da assinatura.

### Questão 286
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de banco de dados no Azure é uma solução de armazenamento de chave-valor baseada em memória extremamente rápida, frequentemente usada para caching e sessão de aplicações?
**Opções:**
- A) Azure Cache for Redis
- B) Azure Table Storage
- C) Azure Cosmos DB
- D) Banco de Dados SQL do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cache for Redis fornece um armazenamento de dados em memória totalmente gerenciado com base no software open-source Redis, usado para melhorar o desempenho e a escalabilidade de aplicações de alta taxa de Leitura/Escrita.

### Questão 287
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual funcionalidade da Conta de Armazenamento do Azure permite bloquear a alteração ou exclusão de dados de arquivos blob por um período retenção definido para atender a requisitos de conformidade legal (WORM - Write Once, Read Many)?
**Opções:**
- A) Armazenamento Imutável para o Azure Blob Storage (Immutable Blob Storage)
- B) Bloqueio de Recursos (Resource Lock) do Azure
- C) Criptografia de Serviços de Armazenamento (SSE)
- D) Azure Policy
**Resposta Correta:** A
**Explicação Técnica:** O Immutable Storage for Azure Blob Storage permite armazenar dados de objetos no formato WORM (Write Once, Read Many), garantindo que os dados não possam ser apagados ou modificados até o término do prazo de retenção.

### Questão 288
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual componente da infraestrutura física do Azure garante resiliência contra falhas no nível de instalações dentro de uma mesma região geográfica por meio de edifícios separados com energia e redes independentes?
**Opções:**
- A) Zonas de Disponibilidade (Availability Zones)
- B) Conjuntos de Disponibilidade (Availability Sets)
- C) Pares de Regiões (Region Pairs)
- D) Geografias do Azure
**Resposta Correta:** A
**Explicação Técnica:** Zonas de Disponibilidade são data centers fisicamente separados dentro de uma região Azure, equipados com infraestrutura própria e independente de energia, refrigeração e conectividade.

### Questão 289
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função do Microsoft Purview no ecossistema do Azure?
**Opções:**
- A) Governança, catalogação e auditoria unificada de dados em ambientes locais, multicloud e SaaS
- B) Gerenciamento de licenças do Windows e Office
- C) Balanceamento de carga de tráfego de rede local
- D) Provisionamento automático de servidores físicos
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Purview é uma solução abrangente de governança de dados que ajuda a gerenciar, mapear, catalogar e proteger seus dados corporativos em todas as fontes (locais, multicloud e SaaS).

### Questão 290
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de implantação do Banco de Dados SQL do Azure oferece quase 100% de compatibilidade com o mecanismo do SQL Server local (on-premises), facilitando a migração "lift-and-shift" de bancos de dados legados?
**Opções:**
- A) Instância Gerenciada do SQL do Azure (Azure SQL Managed Instance)
- B) Banco de Dados Único do Azure SQL
- C) Pool Elástico do SQL do Azure
- D) Azure Cosmos DB
**Resposta Correta:** A
**Explicação Técnica:** O Azure SQL Managed Instance é um serviço PaaS que combina a ampla compatibilidade do mecanismo de banco de dados do SQL Server com os benefícios operacionais de uma nuvem gerenciada.

### Questão 291
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Como a Microsoft garante a privacidade e os direitos de titularidade sobre os dados do cliente armazenados no Azure?
**Opções:**
- A) O cliente é o proprietário exclusivo dos seus dados, e a Microsoft não os utiliza para fins de marketing ou publicidade
- B) Os dados pertencem à Microsoft enquanto a assinatura estiver ativa
- C) A Microsoft pode vender dados agregados para parceiros sem consentimento
- D) Os dados são obrigatoriamente abertos para auditoria governamental sem notificar o cliente
**Resposta Correta:** A
**Explicação Técnica:** Nos compromissos de privacidade da Microsoft, o cliente detém a propriedade total dos seus dados. A Microsoft processa dados apenas para fornecer os serviços contratados e não os utiliza para publicidade.

### Questão 292
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite conectar dispositivos de Internet das Coisas (IoT) de forma bidirecional e segura para telemetria em escala de milhões de dispositivos?
**Opções:**
- A) Hub IoT do Azure (Azure IoT Hub)
- B) Azure Event Grid
- C) Azure Notification Hubs
- D) Azure Service Bus
**Resposta Correta:** A
**Explicação Técnica:** O Azure IoT Hub é um serviço PaaS gerenciado que atua como um ponto central de comunicação bidirecional entre a aplicação de IoT e os dispositivos conectados.

### Questão 293
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual plano de suporte do Azure é ideal para organizações que exigem um Gerente de Conta Técnico de Sucesso (TAM - Technical Account Manager) dedicado e tempo de resposta de 15 minutos para problemas críticos?
**Opções:**
- A) Premier / Unified Support
- B) Professional Direct
- C) Standard
- D) Developer
**Resposta Correta:** A
**Explicação Técnica:** O suporte Premier (ou Microsoft Unified Support) é o nível mais avançado de suporte corporativo da Microsoft, incluindo atendimento técnico prioritário com SLA de 15 minutos para Severidade A e acompanhamento por Gerentes de Conta dedicados.

### Questão 294
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual ferramenta web integrada no Portal do Azure permite executar scripts PowerShell ou Bash diretamente no navegador sem a necessidade de instalar ferramentas locais no computador?
**Opções:**
- A) Azure Cloud Shell
- B) Azure Virtual Desktop
- C) Azure CLI local
- D) Visual Studio Code Online
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cloud Shell é um terminal interativo e acessível pelo navegador para gerenciar recursos do Azure, oferecendo suporte nativo para Bash ou PowerShell pré-configurados.

### Questão 295
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja impedir que qualquer recurso criado em um grupo de recursos específico exceda o orçamento estipulado para o departamento. Qual ação automatizada pode ser configurada usando o Azure Cost Management?
**Opções:**
- A) Disparar Alertas de Orçamento e acionar automações via Grupos de Ação (Action Groups) para notificar administradores ou desativar recursos
- B) Cancelar automaticamente a fatura do cartão de crédito
- C) Bloquear o login de todos os usuários do Microsoft Entra ID
- D) Mover os recursos automaticamente para a nuvem privada
**Resposta Correta:** A
**Explicação Técnica:** Os Alertas de Orçamento do Azure Cost Management acionam notificações por e-mail e podem se integrar a Grupos de Ação (Action Groups) para disparar runbooks/webhooks automatizados quando os limites de gastos configurados são atingidos.

### Questão 296
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual tipo de serviço do Azure é mais indicado para executar contêineres Docker sem a necessidade de gerenciar nós de cluster ou aprender orquestração complexa como o Kubernetes?
**Opções:**
- A) Instâncias de Contêiner do Azure (Azure Container Instances - ACI)
- B) Serviço de Kubernetes do Azure (AKS)
- C) Azure Virtual Machines
- D) Azure Batch
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Instances (ACI) é a forma mais rápida e simples de executar um contêiner no Azure, sem necessidade de provisionar máquinas virtuais ou adotar um orquestrador complexo.

### Questão 297
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual funcionalidade de segurança do Microsoft Entra ID exige que o usuário apresente duas ou mais formas de verificação (ex.: senha + código SMS ou aplicativo autenticador) antes de conceder o acesso?
**Opções:**
- A) Autenticação Multifator do Microsoft Entra (MFA)
- B) Proteção de Identidade (Identity Protection)
- C) Login Único (SSO)
- D) Controle de Acesso Baseado em Função (RBAC)
**Resposta Correta:** A
**Explicação Técnica:** A Autenticação Multifator (MFA) reforça a segurança do login exigindo múltiplos fatores de verificação independentes (algo que você sabe + algo que você possui/é).

### Questão 298
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o objetivo do serviço Azure ExpressRoute Peering do tipo Microsoft Peering?
**Opções:**
- A) Permitir acesso privado e direto a serviços SaaS e PaaS da Microsoft, como Microsoft 365 e Azure Storage, sem passar pela Internet pública
- B) Conectar duas redes virtuais dentro da mesma região Azure
- C) Criptografar tráfego HTTP para sites públicos
- D) Fornecer endereços de IP estáticos para computadores locais
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Peering do ExpressRoute fornece conectividade privada aos serviços de nuvem da Microsoft (incluindo Microsoft 365, serviços PaaS do Azure e Dynamics 365) ignorando a Internet pública.

### Questão 299
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa precisa migrar 100 TB de dados locais para o Azure Blob Storage, porém a conexão de Internet local é muito lenta e levaria meses para concluir o upload. Qual solução física da Microsoft resolve este problema?
**Opções:**
- A) Família Azure Data Box (dispositivo físico de transporte de dados)
- B) Azure ExpressRoute Direct 100 Gbps
- C) Azure Storage Explorer via Internet
- D) Azure Migrate Appliance
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Box é um dispositivo físico fornecido pela Microsoft para transferir terabytes ou petabytes de dados de forma segura e offline para o Azure quando a largura de banda de rede é limitada.

### Questão 300
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual benefício da nuvem permite que uma empresa atenda a picos repentinos de acessos durante uma campanha promocional (como a Black Friday) adicionando mais servidores de forma automática e, em seguida, reduzindo os servidores quando o tráfego volta ao normal?
**Opções:**
- A) Elasticidade (Elasticity)
- B) Tolerância a Falhas (Fault Tolerance)
- C) Recuperação de Desastres (Disaster Recovery)
- D) Alta Disponibilidade (High Availability)
**Resposta Correta:** A
**Explicação Técnica:** A Elasticidade é o recurso fundamental da nuvem que permite dimensionar automaticamente os recursos para cima ou para baixo conforme a flutuação da demanda, garantindo alto desempenho nos picos e otimização financeira nos vales.
