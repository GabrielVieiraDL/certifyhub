# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals - Lote 7 (Questões 301 a 350)

Esta base de conhecimento contém as questões 301 a 350 do exame **AZ-900: Microsoft Azure Fundamentals** formatadas para ingestão e automação no Antigravity.

---

### Questão 301
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual modelo de implantação de nuvem combina a infraestrutura física local de uma empresa com os serviços de uma nuvem pública, permitindo o compartilhamento seguro de dados e aplicações entre ambos os ambientes?
**Opções:**
- A) Nuvem Privada
- B) Nuvem Híbrida
- C) Nuvem Pública
- D) Nuvem Multilocatária Exclusiva
**Resposta Correta:** B
**Explicação Técnica:** A Nuvem Híbrida conecta a infraestrutura local (on-premises/nuvem privada) com a nuvem pública, permitindo a migração flexível de cargas de trabalho e integração de dados com segurança.

### Questão 302
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure oferece um ambiente totalmente gerenciado de banco de dados relacional baseado na mecânica open-source PostgreSQL, com suporte a alta disponibilidade e backups automáticos?
**Opções:**- A) Banco de Dados Azure para PostgreSQL (Azure Database for PostgreSQL)
- B) Azure Cosmos DB
- C) Banco de Dados SQL do Azure (Azure SQL Database)
- D) Azure Synapse Analytics
**Resposta Correta:** A
**Explicação Técnica:** O Azure Database for PostgreSQL é o serviço PaaS totalmente gerenciado da Microsoft para bancos de dados relacionais PostgreSQL, oferecendo patches automáticos, backups e escalabilidade de recursos.

### Questão 303
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja monitorar a integridade geral dos serviços globais do Azure e receber notificações proativas sobre interrupções de serviço planejadas e não planejadas que afetam sua assinatura. Qual recurso deve ser utilizado?
**Opções:**
- A) Azure Advisor
- B) Azure Service Health
- C) Azure Monitor
- D) Application Insights
**Resposta Correta:** B
**Explicação Técnica:** O Azure Service Health fornece um painel personalizado que informa a saúde dos serviços e regiões específicos do Azure que sua empresa utiliza, emitindo alertas sobre interrupções, manutenções planejadas e orientações técnicas.

### Questão 304
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de redundância do Azure Storage replica seus dados de maneira síncrona três vezes dentro de um único data center na região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS - Locally Redundant Storage)
- B) Armazenamento com Redundância de Zona (ZRS - Zone-Redundant Storage)
- C) Armazenamento com Redundância Geográfica (GRS - Geo-Redundant Storage)
- D) Armazenamento com Redundância Geográfica e de Zona (GZRS)
**Resposta Correta:** A
**Explicação Técnica:** O LRS (Locally Redundant Storage) copia os dados três vezes dentro de um único data center físico na região primária, oferecendo proteção contra falhas de hardware no nível de rack e disco.

### Questão 305
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure permite criar e gerenciar inventários detalhados de recursos, executando consultas analíticas orientadas por linguagem KQL sobre o estado atual de todos os recursos da assinatura?
**Opções:**
- A) Azure Resource Graph
- B) Azure Resource Manager (ARM)
- C) Azure Policy
- D) Log Analytics Workspace
**Resposta Correta:** A
**Explicação Técnica:** O Azure Resource Graph é um serviço projetado para estender o gerenciamento de recursos do Azure ARM, permitindo consultas eficientes e escaláveis entre assinaturas e grupos de gerenciamento.

### Questão 306
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual das seguintes afirmações descreve corretamente a diferença entre Escalabilidade Horizontal (Scaling Out) e Escalabilidade Vertical (Scaling Up)?
**Opções:**
- A) Scaling Out adiciona mais instâncias de servidores, enquanto Scaling Up adiciona mais recursos (CPU/RAM) a uma instância existente.
- B) Scaling Out aumenta a memória RAM de um único servidor, enquanto Scaling Up adiciona discos de armazenamento.
- C) Scaling Out aplica-se apenas a serviços SaaS, enquanto Scaling Up aplica-se a serviços IaaS.
- D) Scaling Out é automatizado, enquanto Scaling Up exige migração física de data center.
**Resposta Correta:** A
**Explicação Técnica:** Scaling Out (Escala Horizontal) significa adicionar mais instâncias de recursos (ex.: adicionar mais VMs a um conjunto), enquanto Scaling Up (Escala Vertical) significa aumentar a capacidade da VM atual (adicionando mais vCPU ou RAM).

### Questão 307
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa precisa garantir que o tráfego da Web de entrada seja distribuído uniformemente entre várias máquinas virtuais no Azure em nível de camada de aplicação (Camada 7 - HTTP/HTTPS). Qual serviço é o mais recomendado?
**Opções:**
- A) Azure Load Balancer
- B) Azure Application Gateway
- C) Azure Traffic Manager
- D) Azure ExpressRoute
**Resposta Correta:** B
**Explicação Técnica:** O Azure Application Gateway é um balanceador de carga de tráfego da Web (camada 7 de OSI) que permite gerenciar o tráfego de aplicações Web, oferecendo roteamento baseado em URL, terminação SSL e WAF.

### Questão 308
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso permite atribuir permissões específicas de controle de acesso aos usuários e grupos no Azure com base em suas funções de trabalho (como Leitor, Colaborador ou Proprietário)?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks)
- B) Controle de Acesso Baseado em Função (RBAC - Role-Based Access Control)
- C) Definições do Azure Policy
- D) Grupos de Gerenciamento
**Resposta Correta:** B
**Explicação Técnica:** O Azure RBAC (Role-Based Access Control) permite gerenciar quem tem acesso aos recursos do Azure, o que eles podem fazer com esses recursos e a quais áreas têm acesso.

### Questão 309
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite implantar e gerenciar clusters de contêineres Kubernetes totalmente automatizados de forma simples e escalável?
**Opções:**
- A) Instâncias de Contêiner do Azure (ACI)
- B) Serviço de Kubernetes do Azure (AKS - Azure Kubernetes Service)
- C) Serviço de Aplicativo do Azure (Azure App Service)
- D) Registro de Contêiner do Azure (ACR)
**Resposta Correta:** B
**Explicação Técnica:** O Azure Kubernetes Service (AKS) simplifica a implantação, o gerenciamento e a operação de clusters Kubernetes gerenciados na nuvem pública do Azure.

### Questão 310
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa precisa calcular a estimativa de custos operacionais mensais antes de criar e implantar novos recursos no Azure. Qual ferramenta deve ser utilizada?
**Opções:**
- A) Calculadora de Custo Total de Propriedade (TCO Calculator)
- B) Calculadora de Preços do Azure (Azure Pricing Calculator)
- C) Gerenciamento de Custos do Azure (Azure Cost Management)
- D) Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** A Calculadora de Preços do Azure (Azure Pricing Calculator) é usada para estimar os custos mensais esperados ao combinar e provisionar diferentes produtos e serviços no Azure antes da implantação.

### Questão 311
**Domínio:** Conceitos de Nuvem
**Enunciado:** No modelo de responsabilidade compartilhada para Plataforma como Serviço (PaaS), quem é o responsável pela manutenção e aplicação de patches de segurança no Sistema Operacional das máquinas subjacentes?
**Opções:**
- A) O Cliente
- B) A Microsoft
- C) O Provedor de Internet (ISP)
- D) Responsabilidade compartilhada em 50% entre Cliente e Microsoft
**Resposta Correta:** B
**Explicação Técnica:** Em ofertas PaaS (como o Azure App Service), a Microsoft é integralmente responsável por gerenciar o sistema operacional, hardware físico, rede, virtualização e patches do sistema.

### Questão 312
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é uma solução centralizada de armazenamento de chaves de criptografia, segredos de aplicações e certificados digitais com alto nível de proteção de hardware (HSM)?
**Opções:**
- A) Azure Key Vault
- B) Microsoft Entra ID
- C) Central de Segurança do Azure
- D) Azure Information Protection
**Resposta Correta:** A
**Explicação Técnica:** O Azure Key Vault ajuda a resolver os problemas de gerenciamento de segredos, chaves de criptografia e certificados digitais, armazenando-os de forma segura em módulos HSM validados.

### Questão 313
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual funcionalidade da governança do Azure permite aplicar marcas baseadas em pares de chave-valor (ex.: Ambiente: Produção, CentroDeCusto: 101) aos recursos para fins de organização e relatórios de faturamento detalhados?
**Opções:**
- A) Rótulos de Confidencialidade
- B) Tags do Azure (Azure Tags)
- C) Propriedades de Metadados do ARM
- D) Bloqueios de Recursos
**Resposta Correta:** B
**Explicação Técnica:** As Tags do Azure fornecem metadados em pares nome-valor para organizar os recursos em uma taxonomia lógica, simplificando a consolidação de relatórios de faturamento e auditoria.

### Questão 314
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure fornece um gateway de rede virtual gerenciado que permite conexões VPN criptografadas de ponto a site (Point-to-Site) ou site a site (Site-to-Site) pela Internet pública?
**Opções:**
- A) Azure ExpressRoute
- B) VPN Gateway do Azure
- C) Azure Application Gateway
- D) Azure Peering Service
**Resposta Correta:** B
**Explicação Técnica:** O VPN Gateway do Azure é um tipo específico de gateway de rede virtual usado para enviar tráfego criptografado entre uma rede virtual do Azure e uma localização local através da Internet pública.

### Questão 315
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a principal função dos Grupos de Gerenciamento do Azure (Management Groups)?
**Opções:**
- A) Agrupar usuários do Microsoft Entra ID por departamento.
- B) Fornecer um nível de escopo de governança acima das Assinaturas para gerenciar acesso, políticas e conformidade em escala.
- C) Agrupar máquinas virtuais em Zonas de Disponibilidade.
- D) Gerenciar redes virtuais de diferentes regiões.
**Resposta Correta:** B
**Explicação Técnica:** Os Grupos de Gerenciamento oferecem um nível de escopo acima das assinaturas do Azure. Eles permitem aplicar políticas de governança, permissões do RBAC e conformidade de forma hierárquica sobre múltiplas assinaturas.

### Questão 316
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa deseja transferir seus custos de infraestrutura de TI de um modelo de grande investimento de capital inicial (CapEx) para pagamentos operacionais contínuos à medida que utiliza os serviços. Qual é o nome deste benefício da nuvem?
**Opções:**
- A) Modelo de Despesas Operacionais (OpEx)
- B) Escalabilidade Financeira
- C) Custo Fixo de Propriedade
- D) Modelo de Amortização Direta
**Resposta Correta:** A
**Explicação Técnica:** O modelo OpEx (Operational Expenditure) substitui o investimento prévio em ativos fixos (CapEx) por despesas operacionais baseadas no consumo contínuo e sob demanda dos recursos de nuvem.

### Questão 317
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é projetado para coordenar e automatizar fluxos de trabalho e processos de negócios através de centenas de conectores pré-construídos para serviços SaaS e sistemas locais, sem necessidade de codificação pesada?
**Opções:**
- A) Azure Logic Apps
- B) Azure Functions
- C) Azure Event Grid
- D) Azure Service Bus
**Resposta Correta:** A
**Explicação Técnica:** O Azure Logic Apps é um serviço de nuvem que ajuda a agendar, automatizar e orquestrar tarefas, processos de negócios e fluxos de trabalho integrando aplicações e dados sem código (low-code/no-code).

### Questão 318
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual portal corporativo da Microsoft fornece relatórios de auditoria independente, certificações ISO/SOC, avaliações de conformidade de privacidade e documentos de validação regulatória dos serviços de nuvem?
**Opções:**
- A) Portal do Azure
- B) Portal de Confiança do Serviço (Service Trust Portal)
- C) Central de Segurança da Microsoft
- D) Azure DevTest Labs
**Resposta Correta:** B
**Explicação Técnica:** O Service Trust Portal (STP) é a publicação pública da Microsoft para relatórios de auditoria de conformidade, relatórios SOC, certificações ISO e materiais de orientação sobre privacidade e proteção de dados.

### Questão 319
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de banco de dados do Azure é totalmente gerenciado, possui arquitetura de nuvem nativa e suporta múltiplos modelos de dados (documentos, chave-valor, grafos, colunares) com latência de leitura e escrita de um dígito em milissegundos em escala global?
**Opções:**
- A) Azure Cosmos DB
- B) Banco de Dados SQL do Azure
- C) Instância Gerenciada de SQL do Azure
- D) Azure Database for MariaDB
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cosmos DB é um banco de dados NoSQL totalmente gerenciado e distribuído globalmente que oferece tempos de resposta de milissegundos de um dígito e garantia de disponibilidade de 99,999%.

### Questão 320
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa deseja impedir que uma máquina virtual crítica para os negócios seja excluída por engano por qualquer usuário, incluindo administradores do sistema. O que deve ser configurado na VM?
**Opções:**
- A) Política do Azure (Azure Policy) com negação
- B) Bloqueio de Recurso do tipo Exclusão (Delete Resource Lock)
- C) Regra no Grupo de Segurança de Rede (NSG)
- D) Rótulo no Microsoft Purview
**Resposta Correta:** B
**Explicação Técnica:** O Bloqueio de Recurso do tipo *CanNotDelete* (Delete) impede que qualquer usuário exclua o recurso até que o bloqueio seja explicitamente removido, prevalecendo mesmo sobre permissões de Proprietário no RBAC.

### Questão 321
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que significa o termo 'Alta Disponibilidade' (High Availability) no contexto de serviços do Azure?
**Opções:**
- A) Capacidade de rodar código sem servidores físicos.
- B) Garantia de que a aplicação permanecerá operacional e acessível por uma porcentagem muito alta do tempo com o mínimo de tempo de inatividade.
- C) Capacidade de ajustar automaticamente os preços em função da demanda.
- D) Garantia de que dados nunca serão duplicados em outra região.
**Resposta Correta:** B
**Explicação Técnica:** Alta Disponibilidade refere-se a sistemas projetados para garantir o tempo de funcionamento contínuo e a acessibilidade dos serviços, minimizando interrupções planejadas ou falhas de infraestrutura.

### Questão 322
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual ferramenta de desenvolvimento baseada em linha de comando é nativa do Azure e pode ser executada diretamente dentro do navegador de qualquer dispositivo sem instalar dependências locais?
**Opções:**
- A) Azure Cloud Shell
- B) Azure PowerShell local
- C) Azure CLI local
- D) Visual Studio Code Studio
**Resposta Correta:** A
**Explicação Técnica:** O Azure Cloud Shell é um shell interativo, acessível pelo navegador e autenticado para gerenciar recursos do Azure, oferecendo opções pré-configuradas com Bash ou PowerShell.

### Questão 323
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço de segurança SIEM (Gerenciamento de Eventos e Informações de Segurança) e SOAR nativo da nuvem da Microsoft fornece análise inteligente de ameaças e resposta automatizada em toda a empresa?
**Opções:**
- A) Microsoft Defender for Cloud
- B) Microsoft Sentinel
- C) Firewall do Azure
- D) Azure Key Vault
**Resposta Correta:** B
**Explicação Técnica:** O Microsoft Sentinel é uma solução nativa da nuvem de SIEM e SOAR que coleta dados em escala de todos os usuários, dispositivos, aplicações e infraestruturas locais e de nuvem.

### Questão 324
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O que caracteriza o serviço de computação sem servidor Azure Functions?
**Opções:**
- A) Exige a configuração permanente de máquinas virtuais dedicadas.
- B) Permite a execução de pequenos trechos de código acionados por eventos específicos, com faturamento baseado estritamente no tempo de execução e recursos consumidos.
- C) É um serviço exclusivo para armazenamento de arquivos de mídia.
- D) Substitui os Grupos de Segurança de Rede nas VNets.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Functions é uma plataforma Serverless (FaaS) orientada a eventos que permite rodar código sob demanda sem provisionar ou gerenciar infraestrutura de servidores subjacentes.

### Questão 325
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta da governança do Azure é recomendada para aplicar um conjunto consistente de modelos ARM, políticas (Azure Policy) e atribuições de acesso RBAC durante a criação de novos ambientes de assinatura?
**Opções:**
- A) Blueprints do Azure (Azure Blueprints)
- B) Azure Arc
- C) Azure Inspector
- D) Gerenciamento de Custos do Azure
**Resposta Correta:** A
**Explicação Técnica:** Os Azure Blueprints permitem que equipes de desenvolvimento implantem e configurem rapidamente novos ambientes em conformidade com padrões de governança pré-definidos (Modelos ARM, RBAC e Policies).

### Questão 326
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual é a principal vantagem da Nuvem Pública em relação à Nuvem Privada no que tange a investimentos de capital inicial?
**Opções:**
- A) A Nuvem Pública exige a compra inicial de racks e switches de rede.
- B) A Nuvem Pública elimina a necessidade de grandes custos de capital inicial (CapEx) para adquirir infraestrutura física.
- C) A Nuvem Pública não permite personalizar sistemas operacionais.
- D) A Nuvem Privada possui menores custos recorrentes de energia e refrigeração.
**Resposta Correta:** B
**Explicação Técnica:** Na Nuvem Pública, a infraestrutura física é de propriedade do provedor (Microsoft), eliminando a necessidade de investimento financeiro inicial (CapEx) em data centers pelo cliente.

### Questão 327
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure fornece roteamento inteligente de tráfego de usuários em nível global com base em desempenho, integridade do serviço e comutação por falha (failover) rápida?
**Opções:**
- A) Azure Traffic Manager
- B) Peering de Rede Virtual
- C) Pontos de Extremidade Privados do Azure
- D) Azure ExpressRoute
**Resposta Correta:** A
**Explicação Técnica:** O Azure Traffic Manager é um balanceador de carga de tráfego baseado em DNS que permite distribuir o tráfego de forma otimizada para aplicações em regiões globais do Azure.

### Questão 328
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Onde devem ser consultadas as garantias de porcentagem de tempo de atividade (uptime) oficial de um serviço específico do Azure, bem como os créditos de serviço aplicáveis caso essa meta não seja atingida?
**Opções:**
- A) No Contrato de Nível de Serviço (SLA - Service Level Agreement) do serviço.
- B) No documento de Termos de Serviço Online (OST).
- C) No Painel do Azure Advisor.
- D) No arquivo de configuração do Azure Policy.
**Resposta Correta:** A
**Explicação Técnica:** O SLA (Service Level Agreement) descreve os compromissos formais da Microsoft em relação ao tempo de atividade, desempenho e disponibilidade de cada serviço do Azure.

### Questão 329
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure armazena imagens de contêineres Docker e artefatos de OCI de forma privada para implantação rápida em serviços como AKS e ACI?
**Opções:**
- A) Registro de Contêiner do Azure (ACR - Azure Container Registry)
- B) Azure Blob Storage
- C) Azure Artifacts
- D) Azure App Service
**Resposta Correta:** A
**Explicação Técnica:** O Azure Container Registry (ACR) é um serviço de registro privado gerenciado baseado no Docker Registry 2.0 open-source para armazenar e gerenciar imagens de contêineres privadas.

### Questão 330
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual das alternativas descreve corretamente uma função da ferramenta Azure Advisor?
**Opções:**
- A) Fornecer recomendações proativas para otimização de custos, segurança, desempenho, confiabilidade e excelência operacional.
- B) Bloquear tentativas de login não autorizadas no Microsoft Entra ID.
- C) Compilar automaticamente código-fonte C# para implantação.
- D) Gerenciar certificados SSL no Application Gateway.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Advisor analisa a telemetria e as configurações dos seus recursos para sugerir soluções práticas divididas nos 5 pilares do Well-Architected Framework.

### Questão 331
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que é a Agilidade em nuvem?
**Opções:**
- A) Capacidade de migrar código sem alterar bancos de dados.
- B) Capacidade de provisionar e implantar recursos computacionais rapidamente em questão de minutos, permitindo inovação contínua.
- C) Velocidade física da fibra óptica entre data centers.
- D) Taxa de transferência máxima de um disco SSD.
**Resposta Correta:** B
**Explicação Técnica:** Agilidade é a flexibilidade e rapidez para criar, testar e implantar novas infraestruturas ou aplicações na nuvem com comandos simples ou automação, sem aguardar aquisições físicas.

### Questão 332
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual modalidade de armazenamento do Azure Blob Storage é ideal para dados que são raramente acessados, exigem retenção de longo prazo (anos) e aceitam tempo de latência de recuperação de várias horas?
**Opções:**
- A) Camada Quente (Hot tier)
- B) Camada Fria (Cool tier)
- C) Camada de Arquivamento (Archive tier)
- D) Camada Premium
**Resposta Correta:** C
**Explicação Técnica:** A Camada de Arquivamento (Archive tier) possui os menores custos de armazenamento por gigabyte, sendo indicada para dados históricos com tempo de recuperação de até 15 horas.

### Questão 333
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure permite gerenciar servidores físicos e máquinas virtuais hospedadas em data centers locais ou em outras nuvens (AWS/GCP) diretamente pelo plano de controle do Azure Resource Manager?
**Opções:**
- A) Azure Arc
- B) Azure ExpressRoute
- C) Azure Migrate
- D) Azure Policy Enforcer
**Resposta Correta:** A
**Explicação Técnica:** O Azure Arc simplifica a governança e o gerenciamento ao estender o plano de controle do Azure (ARM) para recursos fora do Azure (locais, multicloud e na borda).

### Questão 334
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure fornece proteção contra ataques distribuídos de negação de serviço (DDoS) na camada de rede para proteger recursos públicos implantados em redes virtuais?
**Opções:**
- A) Proteção Contra DDoS do Azure (Azure DDoS Protection)
- B) Grupos de Segurança de Rede (NSG)
- C) Azure Key Vault
- D) Microsoft Entra ID Protection
**Resposta Correta:** A
**Explicação Técnica:** O Azure DDoS Protection, combinado com as melhores práticas de design de aplicação, fornece recursos aprimorados de mitigação de DDoS para defender contra ataques de negação de serviço.

### Questão 335
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual escopo no Azure permite organizar assinaturas em uma hierarquia unificada para aplicar políticas de conformidade e controle de acesso de forma centralizada?
**Opções:**
- A) Grupos de Recursos
- B) Grupos de Gerenciamento (Management Groups)
- C) Regiões do Azure
- D) Zonas de Disponibilidade
**Resposta Correta:** B
**Explicação Técnica:** Os Grupos de Gerenciamento fornecem um escopo de governança acima das assinaturas, permitindo aplicar Azure Policy e RBAC em escala sobre várias assinaturas associadas.

### Questão 336
**Domínio:** Conceitos de Nuvem
**Enunciado:** O que é o Modelo de Nuvem Híbrida?
**Opções:**
- A) Uso exclusivo de servidores físicos privados dentro do próprio data center da empresa.
- B) Ambiente que combina infraestrutura local ou nuvem privada com os serviços de uma nuvem pública.
- C) Um ambiente de nuvem onde apenas dois usuários possuem acesso simultâneo.
- D) Uso de múltiplos provedores de internet para o mesmo data center.
**Resposta Correta:** B
**Explicação Técnica:** A Nuvem Híbrida combina ambientes locais (on-premises) e nuvens públicas (como o Azure), permitindo que dados e aplicações sejam compartilhados entre eles conforme a necessidade.

### Questão 337
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite integrar dados de várias fontes heterogêneas através de pipelines de ETL (Extração, Transformação e Carga) totalmente gerenciados em escala de Big Data?
**Opções:**
- A) Azure Data Factory
- B) Banco de Dados SQL do Azure
- C) Azure Stream Analytics
- D) Azure Event Hubs
**Resposta Correta:** A
**Explicação Técnica:** O Azure Data Factory é o serviço de integração de dados baseado na nuvem da Microsoft para criar fluxos de trabalho automatizados de movimentação e transformação de dados em escala (ETL/ELT).

### Questão 338
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** O que acontece quando uma empresa atinge o limite do orçamento definido no Azure Budgets dentro do serviço de Gerenciamento de Custos?
**Opções:**
- A) Todos os recursos da assinatura são excluídos imediatamente.
- B) As máquinas virtuais são desativadas automaticamente.
- C) Notificações e alertas configurados são emitidos para os administradores, sem interrupção automática dos serviços.
- D) A assinatura é convertida em uma conta gratuita.
**Resposta Correta:** C
**Explicação Técnica:** O Azure Budgets dispara alertas e notificações por e-mail ou webhooks quando os custos atingem ou excedem os limites pré-definidos, permitindo ação corretiva sem interromper recursos por padrão.

### Questão 339
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de rede do Azure atua como um firewall de rede com estado (stateful) totalmente gerenciado e com alta disponibilidade integrada para inspecionar e filtrar todo o tráfego de uma VNet?
**Opções:**
- A) Firewall do Azure (Azure Firewall)
- B) Grupos de Segurança de Rede (NSG)
- C) Azure Front Door
- D) Azure Application Gateway
**Resposta Correta:** A
**Explicação Técnica:** O Azure Firewall é um serviço de segurança de rede gerenciado e baseado na nuvem que protege os recursos de Rede Virtual do Azure com filtragem de tráfego de rede e aplicativo.

### Questão 340
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Azure Monitor permite coletar, analisar e visualizar métricas e logs detalhados de aplicações Web em tempo real para diagnosticar problemas de desempenho?
**Opções:**
- A) Application Insights
- B) Azure Service Health
- C) Azure Advisor
- D) Log Analytics Workspace Graph
**Resposta Correta:** A
**Explicação Técnica:** O Application Insights é um recurso do Azure Monitor focado em APM (Application Performance Management) para desenvolvedores e profissionais de TI monitorarem aplicações ao vivo.

### Questão 341
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual é o conceito de Tolerância a Falhas (Fault Tolerance) na nuvem?
**Opções:**
- A) Capacidade de um sistema continuar operando sem interrupção mesmo quando um ou mais de seus componentes falham.
- B) Redução do custo da mensalidade quando ocorrem falhas.
- C) Aumento automático da capacidade da memória RAM.
- D) Exclusão automática de registros corrompidos.
**Resposta Correta:** A
**Explicação Técnica:** Tolerância a Falhas garante que uma aplicação continue em execução sem queda de serviço através do uso de componentes redundantes e mecanismos automáticos de failover.

### Questão 342
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de Inteligência Artificial da Microsoft permite integrar modelos de linguagem de grande porte (LLMs), como GPT-4, com segurança corporativa e governança de dados no Azure?
**Opções:**
- A) Serviço do OpenAI do Azure (Azure OpenAI Service)
- B) Azure Bot Service
- C) Pesquisa de IA do Azure (Azure AI Search)
- D) Azure Machine Learning Studio
**Resposta Correta:** A
**Explicação Técnica:** O Azure OpenAI Service fornece acesso aos modelos de IA generativa avançados da OpenAI (incluindo GPT-4 e DALL-E) integrados aos recursos de segurança e rede privada do Azure.

### Questão 343
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta da linguagem declarativa Infrastructure as Code (IaC) foi desenvolvida pela Microsoft especificamente para substituir a sintaxe JSON complexa dos modelos ARM na implantação de recursos do Azure?
**Opções:**
- A) Bicep
- B) Terraform
- C) Ansible
- D) PowerShell DSC
**Resposta Correta:** A
**Explicação Técnica:** O Bicep é uma linguagem de domínio específico (DSL) declarativa que usa sintaxe limpa para implantar recursos do Azure, compilando diretamente em modelos ARM JSON.

### Questão 344
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o tempo de SLA de disponibilidade oferecido para uma única Máquina Virtual no Azure que utiliza discos Premium SSD ou Ultra Disk em todas as suas unidades?
**Opções:**
- A) 99,9%
- B) 99,99%
- C) 99,5%
- D) 99,0%
**Resposta Correta:** A
**Explicação Técnica:** A Microsoft garante um SLA de 99,9% de disponibilidade para uma única VM no Azure se todos os discos anexados forem Premium SSD ou Ultra Disk.

### Questão 345
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual das alternativas representa um exemplo de controle no nível de gerenciamento de identidades e acessos baseado no modelo Zero Trust?
**Opções:**
- A) Exigir Autenticação Multifator (MFA) e verificação explícita da identidade antes de conceder acesso.
- B) Permitir conexões de qualquer IP local sem senha.
- C) Armazenar senhas em arquivos de texto no desktop.
- D) Desativar atualizações de sistema operacional.
**Resposta Correta:** A
**Explicação Técnica:** O modelo Zero Trust baseia-se no princípio 'nunca confie, sempre verifique', exigindo autenticação forte (como MFA) e validação de contexto para cada solicitação de acesso.

### Questão 346
**Domínio:** Conceitos de Nuvem
**Enunciado:** No modelo de Software como Serviço (SaaS), qual das seguintes tarefas fica sob responsabilidade exclusiva do cliente?
**Opções:**
- A) Atualizações do sistema operacional.
- B) Manutenção física dos data centers.
- C) Gerenciamento de dados e controle de acesso dos usuários.
- D) Virtualização dos servidores.
**Resposta Correta:** C
**Explicação Técnica:** Mesmo em soluções SaaS (como o Microsoft 365), a responsabilidade pela governança dos dados, classificação de dados e gerenciamento de identidades/acessos pertence ao cliente.

### Questão 347
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de armazenamento do Azure é mais indicada para fornecer um compartilhamento de arquivos gerenciado na nuvem acessível através do protocolo SMB ou NFS padrão da indústria?
**Opções:**
- A) Arquivos do Azure (Azure Files)
- B) Azure Blob Storage
- C) Discos Gerenciados do Azure
- D) Azure Table Storage
**Resposta Correta:** A
**Explicação Técnica:** O Azure Files oferece compartilhamentos de arquivos totalmente gerenciados na nuvem acessíveis via protocolos padrão SMB (Server Message Block) e NFS (Network File System).

### Questão 348
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é o objetivo principal das iniciativas do Azure Policy?
**Opções:**
- A) Agrupar várias definições de políticas do Azure em um conjunto único para simplificar a atribuição e o monitoramento de conformidade.
- B) Criar Zonas de Disponibilidade adicionais em uma região.
- C) Executar scripts de backup automaticamente.
- D) Conectar VNets através de VPN.
**Resposta Correta:** A
**Explicação Técnica:** Uma iniciativa do Azure Policy (também chamada de política de iniciativa) é uma coleção de definições de política do Azure agrupadas para atingir um meta de governança específico.

### Questão 349
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure permite monitorar eventos de streaming em tempo real provenientes de milhões de dispositivos IoT (Internet das Coisas) com suporte a protocolo MQTT e AMQP?
**Opções:**
- A) Hub IoT do Azure (Azure IoT Hub)
- B) Azure Logic Apps
- C) Azure Functions
- D) Azure Notification Hubs
**Resposta Correta:** A
**Explicação Técnica:** O Azure IoT Hub é um serviço gerenciado que atua como uma central de mensagens bi-direcionais de comunicação entre aplicações de IoT e os dispositivos conectados.

### Questão 350
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta no Portal do Azure permite visualizar e exportar o histórico de todas as operações de gerenciamento (operações no nível do plano de controle) realizadas em uma assinatura nos últimos 90 dias?
**Opções:**
- A) Log de Atividades do Azure (Azure Activity Log)
- B) Log Analytics Workspace
- C) Azure Advisor
- D) Azure Service Health
**Resposta Correta:** A
**Explicação Técnica:** O Azure Activity Log fornece insights sobre eventos no nível de assinatura ocorridos no Azure ARM, como modificações ou exclusões de recursos nos últimos 90 dias.
