# Base de Conhecimento do Exame AZ-900: Microsoft Azure Fundamentals (Lote 2 - Questões 051 a 100)

Esta base de conhecimento foi estruturada especificamente para ser consumida por agentes de IA, frameworks de *vibe coding* e sistemas de automação (como o Antigravity). Ela organiza as questões representativas do exame **AZ-900: Microsoft Azure Fundamentals** extraídas do banco de dados oficial em blocos padronizados em Português do Brasil (pt-BR), aplicando estritamente a nomenclatura oficial da Microsoft Brasil.

---

## 1. Especificação de Esquema de Parsing para Agentes (Agent Schema Definition)

Para processamento automatizado e extração estruturada por agentes de IA ou ferramentas de parsing no Antigravity, cada entrada de questão segue uma sintaxe Markdown determinística:

```markdown
### Questão [ID]
**Domínio:** [Conceitos de Nuvem | Arquitetura e Serviços | Gerenciamento e Governança]
**Enunciado:** [Texto do problema traduzido para pt-BR]
**Opções:**
- A) [Alternativa A]
- B) [Alternativa B]
- C) [Alternativa C]
- D) [Alternativa D]
**Resposta Correta:** [Letra / Opção Correta]
**Explicação Técnica:** [Justificativa didática fundamentada no Microsoft Learn]
```

---

## 2. Domínio 1: Conceitos de Nuvem (Cloud Concepts)

### Questão 051
**Domínio:** Conceitos de Nuvem
**Enunciado:** Em qual tipo de modelo de nuvem todos os recursos de hardware pertencem a um terceiro e são compartilhados entre múltiplos locatários (tenants)?
**Opções:**
- A) Nuvem Privada (Private Cloud)
- B) Nuvem Híbrida (Hybrid Cloud)
- C) Nuvem Pública (Public Cloud)
- D) Nuvem Dedicada Local
**Resposta Correta:** C
**Explicação Técnica:** Na nuvem pública (como o Microsoft Azure), a infraestrutura física de hardware pertence inteiramente ao provedor de nuvem e é compartilhada de forma segura entre múltiplos clientes (ambiente multilocatário).

### Questão 052
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Selecione o serviço que completa corretamente a frase: "O ________ é um serviço de virtualização de área de trabalho e aplicativos na nuvem que permite o uso de uma versão do Windows hospedada na nuvem a partir de qualquer local."
**Opções:**
- A) Conjunto de Disponibilidade (Availability Set)
- B) Máquinas Virtuais Spot do Azure (Azure Spot VMs)
- C) Área de Trabalho Virtual do Azure (Azure Virtual Desktop)
- D) Conjuntos de Escala de Máquinas Virtuais (VM Scale Sets)
**Resposta Correta:** C
**Explicação Técnica:** O Azure Virtual Desktop é a solução gerenciada de virtualização de desktop e aplicativos na nuvem da Microsoft, permitindo entregar a experiência do Windows 11 ou Windows 10 multissessão com gerenciamento centralizado.

### Questão 053
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa possui 1.000 máquinas virtuais hospedadas em servidores Hyper-V em um data center local. A empresa planeja migrar todas as máquinas virtuais para uma assinatura Azure do tipo Pague o que Usar (Pay-As-You-Go). Qual modelo de despesas deve ser identificado para a solução Azure planejada?
**Opções:**
- A) Despesas Operacionais (OpEx)
- B) Modelo Elástico
- C) Despesas de Capital (CapEx)
- D) Modelo Escalável
**Resposta Correta:** A
**Explicação Técnica:** A migração de um data center local para a nuvem pública sob demanda transforma os custos de CapEx (investimento em infraestrutura física e servidores) em OpEx (despesas operacionais recorrentes baseadas no consumo real).

### Questão 054
**Domínio:** Conceitos de Nuvem
**Enunciado:** Uma empresa planeja mover várias aplicações para o Azure. A empresa precisa identificar a solução de nuvem que requer o menor esforço de gerenciamento contínuo da infraestrutura subjacente por parte da equipe interna de TI. Qual modelo deve ser recomendado?
**Opções:**
- A) Infraestrutura como Serviço (IaaS)
- B) Plataforma como Serviço (PaaS)
- C) Software como Serviço (SaaS)
- D) Nuvem Privada
**Resposta Correta:** C
**Explicação Técnica:** O modelo Software como Serviço (SaaS) minimiza a responsabilidade do cliente, pois a Microsoft gerencia toda a infraestrutura, rede, virtualização, sistema operacional e o próprio software da aplicação.

### Questão 055
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual das seguintes opções descreve corretamente a oferta oferecida em um modelo de Plataforma como Serviço (PaaS) do Azure?
**Opções:**
- A) Apenas o hardware físico e a rede do data center
- B) Um ambiente completo de desenvolvimento e implantação na nuvem onde o provedor gerencia o SO e o runtime
- C) Um software de aplicação final pronto para uso sem necessidade de código
- D) Acesso de controle total ao hipervisor e ao sistema operacional
**Resposta Correta:** B
**Explicação Técnica:** No PaaS, o provedor de nuvem gerencia os servidores físicos, rede, armazenamento, sistemas operacionais e middleware, permitindo que os desenvolvedores foquem exclusivamente na criação, implantação e gerenciamento do código das aplicações.

### Questão 056
**Domínio:** Conceitos de Nuvem
**Enunciado:** Avalie as afirmações a seguir sobre soluções de Plataforma como Serviço (PaaS):
1. Uma solução PaaS fornece controle total dos sistemas operacionais que hospedam as aplicações.
2. Uma solução PaaS fornece memória adicional aos aplicativos alterando as camadas de preço (pricing tiers).
3. Uma solução PaaS pode escalar automaticamente o número de instâncias.
Quais afirmações são verdadeiras (Sim) e falsas (Não)?
**Opções:**
- A) 1: Não | 2: Sim | 3: Sim
- B) 1: Não | 2: Não | 3: Sim
- C) 1: Sim | 2: Sim | 3: Não
- D) 1: Sim | 2: Não | 3: Sim
**Resposta Correta:** A
**Explicação Técnica:** No PaaS, o cliente não possui acesso nem controle direto do SO subjacente (1: Não). É possível ajustar recursos como memória alterando os planos de serviço/tiers (2: Sim) e configurar regras de auto-scaling de instâncias (3: Sim).

### Questão 057
**Domínio:** Conceitos de Nuvem
**Enunciado:** Sua empresa possui uma rede local com vários servidores físicos. A empresa planeja migrar esses servidores para Máquinas Virtuais do Azure (IaaS). Quais DUAS responsabilidades administrativas serão eliminadas para a empresa após a migração planejada? (Escolha duas opções)
**Opções:**
- A) Substituir hardware de servidor com falha
- B) Fazer backup dos dados de aplicativos
- C) Gerenciar a segurança física dos servidores
- D) Atualizar sistemas operacionais dos servidores
- E) Gerenciar permissões em documentos compartilhados
**Resposta Correta:** A, C
**Explicação Técnica:** Ao migrar para o Azure IaaS, a Microsoft assume a manutenção e substituição de hardware com falha e a segurança física dos data centers. O cliente continua responsável pelo backup de dados, atualização de SO e controle de permissões.

### Questão 058
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual é a definição exata de um modelo de Nuvem Híbrida (Hybrid Cloud)?
**Opções:**
- A) Um ambiente que combina infraestrutura local (ou nuvem privada) com nuvem pública, permitindo o compartilhamento de dados e aplicações entre elas
- B) Um data center local gerenciado por dois provedores de nuvem diferentes
- C) Uma nuvem mantida exclusivamente por órgãos governamentais
- D) Um modelo que roda 100% dos serviços em Software como Serviço (SaaS)
**Resposta Correta:** A
**Explicação Técnica:** A nuvem híbrida conecta a infraestrutura local (on-premises) ou nuvem privada com os recursos de uma nuvem pública (como o Azure), oferecendo flexibilidade e permitindo otimizar a conformidade e os investimentos existentes.

### Questão 059
**Domínio:** Conceitos de Nuvem
**Enunciado:** Qual benefício da computação em nuvem garante que os recursos computacionais possam ser alocados e desalocados dinamicamente em resposta às variações de demanda de tráfego?
**Opções:**
- A) Agilidade
- B) Elasticidade (Elasticity)
- C) Alta Disponibilidade
- D) Previsibilidade
**Resposta Correta:** B
**Explicação Técnica:** Elasticidade é a capacidade do sistema de aumentar ou diminuir automaticamente a quantidade de recursos provisionados de acordo com o pico ou a queda de demanda em tempo real.

### Questão 060
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O serviço Azure Site Recovery fornece qual das seguintes funcionalidades para máquinas virtuais?
**Opções:**
- A) Tolerância a falhas (Fault tolerance)
- B) Recuperação de desastres (Disaster recovery)
- C) Elasticidade (Elasticity)
- D) Alta disponibilidade (High availability)
**Resposta Correta:** B
**Explicação Técnica:** O Azure Site Recovery é o serviço de Recuperação de Desastres (Disaster Recovery - DR) da Microsoft, que mantém a continuidade dos negócios ao replicar cargas de trabalho de máquinas virtuais para um local secundário durante paralisações ou desastres.

---

## 3. Domínio 2: Arquitetura e Serviços do Azure (Azure Architecture & Core Services)

### Questão 061
**Domínio:** Conceitos de Nuvem
**Enunciado:** Em qual modelo de nuvem uma organização possui controle total sobre todos os recursos físicos e segurança, mas também é responsável por 100% dos custos de capital (CapEx)?
**Opções:**
- A) Nuvem Pública
- B) Nuvem Privada (Private Cloud)
- C) Software como Serviço (SaaS)
- D) Plataforma como Serviço (PaaS)
**Resposta Correta:** B
**Explicação Técnica:** Na nuvem privada (local ou dedicada), a organização é dona da infraestrutura física, arcando com todas as despesas de capital (CapEx) para aquisição e substituição de hardware.

### Questão 062
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual estrutura do Azure é usada para organizar e aplicar políticas de governança e controle de acesso (RBAC) centralizado em nível hierárquico acima de múltiplas assinaturas?
**Opções:**
- A) Grupos de Gerenciamento (Management Groups)
- B) Grupos de Recursos (Resource Groups)
- C) Zonas de Disponibilidade (Availability Zones)
- D) Unidades Administrativas do Entra ID
**Resposta Correta:** A
**Explicação Técnica:** Os Grupos de Gerenciamento fornecem um nível de escopo acima das Assinaturas. As políticas e permissões aplicadas a um grupo de gerenciamento são herdadas automaticamente por todas as assinaturas contidas nele.

### Questão 063
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Ao criar novos recursos no Azure (como VMs, VNets ou bancos de dados), qual elemento de organização lógica é OBRIGATÓRIO para armazená-los e gerenciar seu ciclo de vida conjunto?
**Opções:**
- A) Conta de Armazenamento
- B) Grupo de Recursos (Resource Group)
- C) Grupo de Gerenciamento
- D) Conjunto de Disponibilidade
**Resposta Correta:** B
**Explicação Técnica:** Todo recurso implantado no Azure deve pertencer a exatamente um Grupo de Recursos (Resource Group), que funciona como um contêiner lógico para gerenciamento de implantação, permissões e ciclo de vida.

### Questão 064
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa planeja migrar suas aplicações para o Azure adotando estritamente uma estratégia baseada em Plataforma como Serviço (PaaS). A equipe propõe implantar um Azure App Service e Bancos de Dados SQL do Azure (Azure SQL Database). Essa solução atende ao objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** A
**Explicação Técnica:** Tanto o Azure App Service quanto o Azure SQL Database são ofertas nativas de PaaS da Microsoft, nas quais a infraestrutura subjacente é totalmente gerenciada pelo Azure.

### Questão 065
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa planeja migrar dados e recursos para o Azure adotando apenas soluções de PaaS. A solução proposta inclui a criação de Máquinas Virtuais do Azure, Banco de Dados SQL do Azure e Contas de Armazenamento. Essa solução atende ao objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** A inclusão de Máquinas Virtuais do Azure viola a premissa de usar exclusivamente PaaS, pois as VMs pertencem ao modelo de Infraestrutura como Serviço (IaaS).

### Questão 066
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o nível garantido de SLA (Service Level Agreement) de disponibilidade oferecido pela Microsoft para Máquinas Virtuais do Azure quando duas ou mais instâncias são implantadas em duas ou mais Zonas de Disponibilidade na mesma região?
**Opções:**
- A) 99,9%
- B) 99,95%
- C) 99,99%
- D) 100%
**Resposta Correta:** C
**Explicação Técnica:** A implantação de instâncias de VMs distribuídas entre Zonas de Disponibilidade (Availability Zones) oferece o maior SLA de uptime para VMs no Azure, garantido em 99,99%.

### Questão 067
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o SLA de disponibilidade garantido para duas ou mais instâncias de Máquinas Virtuais do Azure implantadas dentro do mesmo Conjunto de Disponibilidade (Availability Set)?
**Opções:**
- A) 99,9%
- B) 99,95%
- C) 99,99%
- D) 99,5%
**Resposta Correta:** B
**Explicação Técnica:** Para instâncias de VMs configuradas no mesmo Conjunto de Disponibilidade (protegendo contra falhas de rack/hardware e manutenção planejada no mesmo data center), o SLA oferecido é de 99,95%.

### Questão 068
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa atinge o limite de cota padrão de instâncias para um serviço do Azure em sua assinatura. O que deve ser feito para solicitar um aumento desse limite de cota?
**Opções:**
- A) Criar uma nova conta de diretório no Entra ID
- B) Abrir uma solicitação de suporte de cota/limite no portal do Azure (Ajuda + Suporte)
- C) Migrar obrigatoriamente para o plano de suporte Premier
- D) Excluir o Grupo de Gerenciamento
**Resposta Correta:** B
**Explicação Técnica:** Aumentos de limites e cotas de assinatura podem ser solicitados gratuitamente abrindo um chamado de suporte do tipo "Service and subscription limits (quotas)" no Portal do Azure.

### Questão 069
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de armazenamento do Azure fornece compartilhamentos de arquivos totalmente gerenciados na nuvem acessíveis via protocolos padrão da indústria como SMB e NFS?
**Opções:**
- A) Azure Blob Storage
- B) Azure Files
- C) Azure Disk Storage
- D) Azure Queue Storage
**Resposta Correta:** B
**Explicação Técnica:** O Azure Files permite criar compartilhamentos de arquivos na nuvem acessíveis simultaneamente por sistemas locais ou VMs na nuvem via SMB ou NFS.

### Questão 070
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual opção de redundância de armazenamento do Azure mantém três cópias dos seus dados dentro de um único data center físico na região primária?
**Opções:**
- A) Armazenamento com Redundância Local (LRS)
- B) Armazenamento com Redundância de Zona (ZRS)
- C) Armazenamento com Redundância Geográfica (GRS)
- D) Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS)
**Resposta Correta:** A
**Explicação Técnica:** O LRS (Locally-Redundant Storage) replica os dados três vezes síncronamente dentro de uma única instalação física/data center na região primária.

### Questão 071
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Avalie as afirmativas sobre modelos de serviço dos seguintes bancos de dados:
1. O Microsoft SQL Server 2019 instalado em uma máquina virtual do Azure é um exemplo de PaaS.
2. O Banco de Dados SQL do Azure (Azure SQL Database) é um exemplo de PaaS.
3. O Azure Cosmos DB é um exemplo de Software como Serviço (SaaS).
Quais afirmações estão corretas (Sim/Não)?
**Opções:**
- A) 1: Não | 2: Sim | 3: Não
- B) 1: Sim | 2: Sim | 3: Não
- C) 1: Não | 2: Sim | 3: Sim
- D) 1: Sim | 2: Não | 3: Não
**Resposta Correta:** A
**Explicação Técnica:** SQL Server em VM é IaaS (1: Não). Azure SQL Database é banco gerenciado PaaS (2: Sim). Azure Cosmos DB é um serviço de banco de dados NoSQL gerenciado (PaaS), não SaaS (3: Não).

### Questão 072
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Selecione o recurso que completa corretamente a frase: "Você pode atribuir um ________ a qualquer recurso do Azure para evitar a exclusão acidental ou modificações não autorizadas."
**Opções:**
- A) Azure Blueprint
- B) Bloqueio de Recurso (Resource Lock)
- C) Azure Policy
- D) Ponto de Extremidade de Serviço (Service Endpoint)
**Resposta Correta:** B
**Explicação Técnica:** Os Bloqueios de Recursos (Resource Locks) permitem aplicar restrições dos tipos *CanNotDelete* (exclusão) ou *ReadOnly* (somente leitura) a recursos, grupos de recursos ou assinaturas.

### Questão 073
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é o objetivo principal do serviço Azure ExpressRoute?
**Opções:**
- A) Conectar redes locais ao Azure via VPN pela Internet pública
- B) Criar uma conexão privada e dedicada de alta velocidade entre redes locais e o Azure sem passar pela Internet pública
- C) Aumentar a velocidade de download de arquivos no Blob Storage
- D) Conectar duas redes virtuais dentro da mesma região do Azure
**Resposta Correta:** B
**Explicação Técnica:** O ExpressRoute estende as redes locais para a nuvem da Microsoft através de uma conexão privada facilitada por um provedor de conectividade, oferecendo maior confiabilidade, velocidade e menor latência sem usar a Internet pública.

### Questão 074
**Domínio:** Conceitos de Nuvem
**Enunciado:** No modelo de Software como Serviço (SaaS), qual das seguintes responsabilidades permanece com o cliente?
**Opções:**
- A) Dados da aplicação e gerenciamento de contas de usuários
- B) Armazenamento físico de dados
- C) Infraestrutura de rede e servidores
- D) Desenvolvimento e manutenção do código da aplicação
**Resposta Correta:** A
**Explicação Técnica:** No SaaS, a Microsoft gerencia toda a pilha de infraestrutura e software; o cliente é responsável por fornecer seus próprios dados e gerenciar o acesso de seus usuários.

### Questão 075
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure permite que administradores e arquitetos definam um conjunto repetível de recursos e configurações (incluindo ARM templates, políticas e papéis RBAC) para garantir conformidade em novas assinaturas?
**Opções:**
- A) Azure Blueprints
- B) Azure Advisor
- C) Grupos de Recursos
- D) Azure Monitor
**Resposta Correta:** A
**Explicação Técnica:** O Azure Blueprints orquestra a implantação de vários artefatos de modelo (políticas, atribuições de função, modelos ARM) de forma padronizada em nível de governança corporativa.

---

## 4. Domínio 3: Gerenciamento e Governança no Azure (Azure Management & Governance)

### Questão 076
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure fornece gerenciamento unificado de postura de segurança da informação e proteção avançada contra ameaças para recursos no Azure, em outras nuvens e no ambiente local?
**Opções:**
- A) Microsoft Defender para Nuvem (Microsoft Defender for Cloud)
- B) Azure Firewall
- C) Grupos de Segurança de Rede (NSG)
- D) Azure Key Vault
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Defender for Cloud analisa continuamente a postura de segurança dos recursos híbridos e multinuvem, fornecendo a pontuação de segurança (Secure Score) e alertas de proteção contra ameaças.

### Questão 077
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta online gratuita é usada para estimar os custos mensais de contratação de novos serviços do Azure antes de implantá-los?
**Opções:**
- A) Calculadora de Preços do Azure (Azure Pricing Calculator)
- B) Calculadora de TCO (Total Cost of Ownership)
- C) Gerenciamento de Custos do Azure (Azure Cost Management)
- D) Azure Advisor
**Resposta Correta:** A
**Explicação Técnica:** A Calculadora de Preços do Azure permite configurar e estimar os custos operacionais de recursos do Azure com base em métricas planejadas de uso.

### Questão 078
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta é recomendada para comparar os custos financeiros diretos e indiretos de manter uma infraestrutura física local versus a migração para a plataforma Azure ao longo de anos?
**Opções:**
- A) Calculadora de Preços do Azure
- B) Calculadora de Custo Total de Propriedade (TCO Calculator)
- C) Azure Monitor
- D) Azure Advisor
**Resposta Correta:** B
**Explicação Técnica:** A Calculadora de TCO analisa a economia financeira potencial ao comparar os custos de capital e operacionais de um data center local (energia, resfriamento, licenças, hardware) com o consumo no Azure.

### Questão 079
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Selecione o recurso que completa corretamente a frase: "Você pode usar ________ no Azure para enviar alertas por e-mail quando o custo do período de faturamento de uma assinatura exceder um limite especificado."
**Opções:**
- A) Recomendações do Azure Advisor
- B) Controle de Acesso (IAM)
- C) Alertas de Orçamento (Budget Alerts)
- D) Alertas de Conformidade
**Resposta Correta:** C
**Explicação Técnica:** Os Alertas de Orçamento no Azure Cost Management notificam os administradores por e-mail quando o custo acumulado ou previsto ultrapassa os patamares percentuais definidos no orçamento da assinatura.

### Questão 080
**Domínio:** Conceitos de Nuvem
**Enunciado:** Associe os benefícios da computação em nuvem às suas respectivas descrições:
- Benefício 1: Os recursos podem ser provisionados dinamicamente para atender às mudanças de demanda.
- Benefício 2: Aplicações e dados podem ser implantados em múltiplas regiões ao redor do mundo.
- Benefício 3: Aplicações podem ser desenvolvidas, testadas e lançadas rapidamente.
Qual é a associação correta?
**Opções:**
- A) 1: Escalabilidade | 2: Distribuição Geográfica | 3: Agilidade
- B) 1: Agilidade | 2: Escalabilidade | 3: Distribuição Geográfica
- C) 1: Distribuição Geográfica | 2: Agilidade | 3: Escalabilidade
- D) 1: Escalabilidade | 2: Agilidade | 3: Distribuição Geográfica
**Resposta Correta:** A
**Explicação Técnica:** Escalabilidade refere-se à capacidade de ajustar recursos; Distribuição Geográfica à alocação global de workloads; Agilidade à velocidade de colocação de soluções em produção.

### Questão 081
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Selecione o serviço que completa a frase: "Você configura a recuperação de desastres (Disaster Recovery) para máquinas virtuais do Azure usando o ________."
**Opções:**
- A) Azure Backup
- B) Azure Site Recovery
- C) Azure Migrate
- D) Azure Monitor
**Resposta Correta:** B
**Explicação Técnica:** O Azure Site Recovery permite configurar a replicação contínua e o plano de recuperação de falhas (failover) entre regiões do Azure para proteger contra falhas regionais.

### Questão 082
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual das seguintes afirmações descreve corretamente a diferença entre Azure Backup e Azure Site Recovery?
**Opções:**
- A) O Azure Backup é usado para failover em tempo real e o Site Recovery para salvar arquivos
- B) O Azure Backup foca no salvamento, retenção e restauração de dados e arquivos históricos, enquanto o Site Recovery foca na replicação contínua e recuperação rápida de desastres para continuidade de negócios
- C) O Azure Backup exige obrigatoriamente um plano de suporte Premier
- D) Não há diferença entre ambos os serviços
**Resposta Correta:** B
**Explicação Técnica:** O Azure Backup é uma solução de backup tradicional baseada em snapshots/pontos de restauração de dados; o Site Recovery é voltado para alta disponibilidade e failover rápido em desastres.

### Questão 083
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure é projetado para armazenar com segurança e controlar o acesso a segredos, chaves de criptografia e certificados digitais?
**Opções:**
- A) Azure Key Vault
- B) Microsoft Entra ID
- C) Análise de Logs do Azure (Log Analytics)
- D) Azure Dedicated Host
**Resposta Correta:** A
**Explicação Técnica:** O Azure Key Vault центраliza o armazenamento de segredos da aplicação (chaves API, senhas, certificados SSL) com controle rígido via RBAC e políticas de acesso.

### Questão 084
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual recurso de rede permite interconectar duas Redes Virtuais (VNets) do Azure na mesma região ou em regiões diferentes, fazendo com que o tráfego entre elas trafegue exclusivamente pela rede backbone privada da Microsoft?
**Opções:**
- A) Peering de Rede Virtual (VNet Peering)
- B) Conexão Gateway VPN Site-to-Site
- C) ExpressRoute
- D) Azure Front Door
**Resposta Correta:** A
**Explicação Técnica:** O VNet Peering conecta redes virtuais diretamente com baixíssima latência e alta largura de banda através da infraestrutura de rede privada da Microsoft.

### Questão 085
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço de segurança de rede do Azure é um firewall com estado (stateful) totalmente gerenciado na nuvem que fornece proteção e inspeção de tráfego de rede para recursos dentro de VNets?
**Opções:**
- A) Azure Firewall
- B) Grupo de Segurança de Rede (NSG)
- C) Microsoft Defender para Nuvem
- D) Proteção contra DDoS do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Firewall é um serviço nativo de segurança de rede que oferece inspeção stateful de tráfego de rede (camadas 3 a 7) com alta disponibilidade e escalabilidade ilimitada.

### Questão 086
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** O que é um Grupo de Segurança de Rede (Network Security Group - NSG) no Azure?
**Opções:**
- A) Um recurso usado para conter regras de segurança que permitem ou negam o tráfego de rede de entrada e saída para interfaces de rede, VMs ou sub-redes
- B) Um serviço para armazenar senhas e chaves criptográficas
- C) Uma solução de aceleração de entrega de conteúdo web
- D) Um banco de dados de regras de governança de custos
**Resposta Correta:** A
**Explicação Técnica:** O NSG atua como um firewall de camada de rede básico (camadas 3 e 4) que filtra o tráfego com base em IP de origem/destino, portas e protocolos.

### Questão 087
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual é a diferença primária entre um Grupo de Segurança de Rede (NSG) e o Azure Firewall?
**Opções:**
- A) O NSG filtra tráfego básico por regras IP/porta a nível de NIC/sub-rede, enquanto o Azure Firewall é um serviço de firewall corporativo gerenciado com regras FQDN, inteligência contra ameaças e roteamento centralizado
- B) O NSG só funciona em conexões de saída e o Azure Firewall em conexões de entrada
- C) O Azure Firewall é gratuito e o NSG é pago
- D) O NSG não suporta protocolos TCP e UDP
**Resposta Correta:** A
**Explicação Técnica:** Os NSGs são filtros de tráfego orientados a portas/IPs aplicados localmente a sub-redes ou NICs; o Azure Firewall é um serviço gerenciado central para toda a VNet com recursos avançados de filtragem e inspeção L3-L7.

### Questão 088
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Qual serviço do Azure é responsável por monitorar o tráfego de IP público e mitigar automaticamente ataques volumétricos de Negação de Serviço Distribuída (DDoS)?
**Opções:**
- A) Proteção contra DDoS do Azure (Azure DDoS Protection)
- B) Azure Web Application Firewall (WAF)
- C) Microsoft Sentinel
- D) Azure Policy
**Resposta Correta:** A
**Explicação Técnica:** O Azure DDoS Protection fornece recursos aprimorados de mitigação de DDoS para proteger recursos do Azure conectados a IPs públicos contra ataques volumétricos e de camada de rede.

### Questão 089
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual solução nativa de nuvem do Azure atua como SIEM (Security Information and Event Management) e SOAR (Security Orchestration, Automation, and Response) para coletar e analisar dados de segurança em tempo real?
**Opções:**
- A) Microsoft Sentinel (antigo Azure Sentinel)
- B) Azure Monitor
- C) Microsoft Defender para Nuvem
- D) Azure Key Vault
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Sentinel oferece análise de segurança inteligente e inteligência contra ameaças em toda a empresa, fornecendo uma solução única para detecção de alertas, visibilidade de ameaças e resposta automatizada.

### Questão 090
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função do Controle de Acesso Baseado em Função (RBAC - Role-Based Access Control) do Azure?
**Opções:**
- A) Garantir o gerenciamento refinado de autorização, concedendo apenas as permissões necessárias para usuários realizarem suas tarefas em escopos específicos
- B) Autenticar a identidade de um usuário usando biometria
- C) Criptografar arquivos armazenados em contas de armazenamento
- D) Limitar a quantidade de dinheiro gasta na assinatura
**Resposta Correta:** A
**Explicação Técnica:** O Azure RBAC permite atribuir permissões específicas (como Leitor, Colaborador ou Proprietário) a usuários, grupos ou entidades de serviço em escopos específicos (Grupo de Gerenciamento, Assinatura, Grupo de Recursos ou Recurso).

### Questão 091
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a diferença fundamental entre os conceitos de Autenticação e Autorização no ecossistema de identidade da Microsoft?
**Opções:**
- A) Autenticação valida A IDENTIDADE do usuário (quem é você); Autorização concede AS PERMISSÕES para realizar ações (o que você pode fazer)
- B) Autenticação é usada apenas em máquinas virtuais e Autorização em bancos de dados
- C) Autorização sempre ocorre antes da Autenticação
- D) Ambos os termos são sinônimos e possuem a mesma função
**Resposta Correta:** A
**Explicação Técnica:** Autenticação (AuthN) é o processo de verificar quem é a pessoa ou serviço apresentando credenciais (ex.: senha/MFA). Autorização (AuthZ) determina quais recursos e ações a pessoa autenticada tem direito de acessar.

### Questão 092
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso de segurança do Microsoft Entra ID exige a apresentação de dois ou mais fatores de prova para autenticar a identidade de um usuário?
**Opções:**
- A) Autenticação Multifator do Microsoft Entra (MFA)
- B) Logon Único (SSO)
- C) Controle de Acesso Baseado em Função (RBAC)
- D) Definição de Iniciativa do Azure Policy
**Resposta Correta:** A
**Explicação Técnica:** O Microsoft Entra MFA adiciona uma camada adicional de segurança exigindo fatores como senhas combinadas com notificações no aplicativo Authenticator, códigos SMS ou biometria.

### Questão 093
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual recurso do Microsoft Entra ID permite que um usuário insira suas credenciais corporativas uma única vez para acessar múltiplos aplicativos e recursos autorizados na nuvem e locais?
**Opções:**
- A) Logon Único (Single Sign-On - SSO)
- B) Autenticação Multifator (MFA)
- C) Acesso Condicional
- D) Privileged Identity Management (PIM)
**Resposta Correta:** A
**Explicação Técnica:** O Single Sign-On (SSO) melhora a experiência do usuário e a segurança permitindo autenticar-se apenas uma vez e obter acesso a todos os aplicativos corporativos confiados.

### Questão 094
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual funcionalidade do Microsoft Entra ID analisa sinais de contexto (como localização do usuário, dispositivo, estado do risco de entrada e aplicativo acessado) para tomar decisões automatizadas de acesso (permitir, bloquear ou exigir MFA)?
**Opções:**
- A) Acesso Condicional (Conditional Access)
- B) Azure Policy
- C) Bloqueios de Recursos
- D) Grupos de Segurança de Rede
**Resposta Correta:** A
**Explicação Técnica:** O Acesso Condicional é o mecanismo de política do modelo Zero Trust da Microsoft que avalia sinais e aplica controles de acesso automatizados no momento do login.

### Questão 095
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Uma empresa exige que todos os recursos criados em suas assinaturas contenham uma Tag chamada "CentroDeCusto". Qual recurso do Azure deve ser configurado para auditar ou bloquear a criação de recursos sem essa tag?
**Opções:**
- A) Azure Policy
- B) Bloqueio de Recurso (Resource Lock)
- C) Azure Advisor
- D) Microsoft Entra ID
**Resposta Correta:** A
**Explicação Técnica:** O Azure Policy aplica regras sobre recursos para garantir conformidade organizacional, como auditar ou proibir o provisionamento de recursos sem tags obrigatórias.

### Questão 096
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual tecnologia declarativa nativa do Azure baseada em arquivos JSON é usada para definir e implantar infraestrutura como código (IaC) de maneira automatizada e consistente?
**Opções:**
- A) Modelos do Azure Resource Manager (ARM Templates)
- B) Azure Policy
- C) Azure Blueprints
- D) Scripts de inicialização em lote do Windows
**Resposta Correta:** A
**Explicação Técnica:** Os ARM Templates usam sintaxe JSON declarativa para definir os recursos a serem implantados no Azure, garantindo implantação idêntica e repetível.

### Questão 097
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual ferramenta do Azure fornece alertas personalizados em tempo real sobre a saúde dos serviços da infraestrutura global da Microsoft que afetam especificamente as suas assinaturas e recursos?
**Opções:**
- A) Azure Service Health
- B) Azure Monitor
- C) Azure Advisor
- D) Application Insights
**Resposta Correta:** A
**Explicação Técnica:** O Azure Service Health informa sobre interrupções de serviço do Azure, eventos de manutenção planejada e outros avisos de saúde específicos para os recursos que você utiliza.

### Questão 098
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual serviço do Azure coleta, analisa e age sobre dados de telemetria, logs e métricas de desempenho de aplicações e recursos de infraestrutura hospedados no Azure ou no ambiente local?
**Opções:**
- A) Azure Monitor
- B) Azure Advisor
- C) Portal do Azure
- D) Gerenciamento de Custos do Azure
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor maximiza a disponibilidade e o desempenho de suas aplicações coletando, analisando e agindo sobre a telemetria do ambiente.

### Questão 099
**Domínio:** Arquitetura e Serviços do Azure
**Enunciado:** Sua empresa planeja implantar várias máquinas virtuais no Azure. Você precisa garantir que as aplicações continuem acessíveis se um único data center físico falhar. A solução proposta recomenda implantar as VMs em um Conjunto de Escala (VM Scale Set) sem Zonas de Disponibilidade ativas. Essa solução atende ao objetivo?
**Opções:**
- A) Sim
- B) Não
**Resposta Correta:** B
**Explicação Técnica:** Um Scale Set básico sem configuração de Zonas de Disponibilidade distribui VMs dentro do mesmo data center (entre domínios de falha). Para tolerar a falha de um data center inteiro, as VMs devem ser distribuídas entre Zonas de Disponibilidade (Availability Zones).

### Questão 100
**Domínio:** Gerenciamento e Governança no Azure
**Enunciado:** Qual é a função principal do serviço Azure Advisor?
**Opções:**
- A) Analisar seus recursos do Azure e fornecer recomendações personalizadas baseadas em boas práticas nos pilares de Custo, Segurança, Confiabilidade, Desempenho e Excelência Operacional
- B) Executar backups automáticos de máquinas virtuais
- C) Atuar como gateway de borda para conexões de rede
- D) Autenticar usuários corporativos
**Resposta Correta:** A
**Explicação Técnica:** O Azure Advisor analisa continuamente as métricas de telemetria e configuração dos seus recursos do Azure e fornece recomendações personalizadas para otimizar custos, reforçar a segurança e aumentar a confiabilidade.
