# Base de Conhecimento do Exame AZ-104: Microsoft Azure Administrator - Lote 8 (Questões 351 a 400)

Esta base de conhecimento contém as questões 351 a 400 do exame **AZ-104: Microsoft Azure Administrator** traduzidas e formatadas em pt-BR com nomenclatura técnica oficial da Microsoft para automação e ingestão no Antigravity.

---

### Questão 351
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #351) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 352
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #352) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 353
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #353) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 354
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #354) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 355
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #355) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 356
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #356) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 357
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #357) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 358
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #358) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 359
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #359) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 360
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #360) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 361
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #361) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 362
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #362) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 363
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #363) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 364
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #364) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 365
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #365) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 366
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #366) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 367
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #367) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 368
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #368) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 369
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #369) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 370
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #370) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 371
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #371) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 372
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #372) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 373
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #373) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 374
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #374) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 375
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #375) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 376
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #376) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 377
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #377) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 378
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #378) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 379
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #379) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 380
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #380) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 381
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #381) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 382
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #382) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 383
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #383) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 384
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #384) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 385
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #385) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 386
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #386) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 387
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #387) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 388
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #388) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 389
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #389) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 390
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #390) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 391
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #391) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 392
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #392) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 393
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #393) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 394
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #394) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 395
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #395) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

### Questão 396
**Domínio:** Configurar e Gerenciar Redes Virtuais
**Enunciado:** (Questão AZ-104 #396) Você possui uma Rede Virtual (VNet1) no Azure com três sub-redes (Subnet1, Subnet2 e Subnet3). Você precisa garantir que todo o tráfego de saída da Subnet1 destinado à Internet seja inspecionado e filtrado por uma Solução Virtual de Rede (NVA) implantada na Subnet2. O que você deve criar e associar à Subnet1?
**Opções:**
- A) Uma Tabela de Roteamento (Route Table) com uma Rota Definida pelo Usuário (UDR) apontando o prefixo 0.0.0.0/0 para o IP privado da NVA como Próximo Salto (Next Hop).
- B) Um Grupo de Segurança de Rede (NSG) com uma regra de saída bloqueando todas as portas.
- C) Uma rota BGP dinâmica configurada no Azure Route Server.
- D) Um Peering de Rede Virtual configurado com a opção de trânsito de gateway ativada.
**Resposta Correta:** A
**Explicação Técnica:** Para forçar todo o tráfego de saída para a Internet (0.0.0.0/0) a passar por uma NVA (Network Virtual Appliance), deve-se criar uma Tabela de Roteamento contendo uma Rota Definida pelo Usuário (UDR) atribuindo o IP privado da NVA como Next Hop (Virtual Appliance).

### Questão 397
**Domínio:** Gerenciar Identidades e Governança do Azure
**Enunciado:** (Questão AZ-104 #397) Sua empresa precisa impor uma regra corporativa exigindo que todos os recursos implantados no Grupo de Recursos 'RG-Production' contenham uma tag chamada 'Environment' com o valor 'PROD'. Caso uma tentativa de implantação ocorra sem essa tag, a criação deve ser impedida. Qual componente do Azure deve ser utilizado?
**Opções:**
- A) Bloqueios de Recursos (Resource Locks) com nível ReadOnly.
- B) Definição de Azure Policy com o efeito Deny.
- C) Função RBAC de Colaborador de Tag (Tag Contributor).
- D) Iniciativa do Azure Policy com o efeito Audit.
**Resposta Correta:** B
**Explicação Técnica:** O Azure Policy com o efeito Deny impede a criação ou atualização de recursos que não estejam em conformidade com as regras estabelecidas pela política, como a ausência de uma tag obrigatória.

### Questão 398
**Domínio:** Implementar e Gerenciar Armazenamento
**Enunciado:** (Questão AZ-104 #398) Você precisa configurar uma Conta de Armazenamento do Azure para manter logs auditáveis da empresa por 7 anos. A política de conformidade exige que os dados gravados não possam ser alterados ou excluídos por ninguém, inclusive administradores do sistema, durante o período de retenção. Qual recurso deve ser habilitado?
**Opções:**
- A) Criptografia Baseada em Chaves Gerenciadas pelo Cliente (CMK).
- B) Armazenamento Imutável de Blobs com Política baseada em tempo no modo de Conformidade (Compliance Mode).
- C) Replicação com Armazenamento com Redundância Geográfica com Acesso de Leitura (RA-GRS).
- D) Regras de Gerenciamento do Ciclo de Vida (Lifecycle Management) para mover dados para a camada Archive.
**Resposta Correta:** B
**Explicação Técnica:** A Política de Retenção Imutável no modo de Conformidade (Compliance Mode) garante WORM (Write Once, Read Many), impedindo que blobs sejam sobrescritos ou excluídos por qualquer usuário ou administrador durante o período estipulado.

### Questão 399
**Domínio:** Implantar e Gerenciar Recursos de Computação
**Enunciado:** (Questão AZ-104 #399) Sua equipe gerencia um Conjunto de Escala de Máquinas Virtuais (VMSS) no Azure. Durante picos de tráfego, o uso médio de CPU ultrapassa 85% por 10 minutos. Você precisa configurar o escalamento automático para adicionar 2 instâncias automaticamente quando esse limite for atingido e remover 1 instância quando a CPU cair abaixo de 30%. Qual recurso do Azure executa esse ajuste?
**Opções:**
- A) Azure Load Balancer com sondas de integridade.
- B) Regras de Autoscale (Dimensionamento Automático) baseadas em métricas no Azure Monitor.
- C) Extensão de Script Personalizado (Custom Script Extension).
- D) Azure Automation Runbooks com agendamento.
**Resposta Correta:** B
**Explicação Técnica:** As regras de Autoscale configuradas no VMSS usam métricas agregadas do Azure Monitor (como % de CPU) para aumentar (scale-out) ou diminuir (scale-in) automaticamente a contagem de instâncias.

### Questão 400
**Domínio:** Monitorar e Proteger Recursos do Azure
**Enunciado:** (Questão AZ-104 #400) Você precisa centralizar a coleta de logs de eventos do sistema operacional e métricas de desempenho de 50 Máquinas Virtuais Windows e Linux no Azure. Os dados devem ser analisados através de consultas KQL. Qual combinação de componentes é necessária?
**Opções:**
- A) Log Analytics Workspace, Azure Monitor Agent (AMA) e Regras de Coleta de Dados (DCR).
- B) Conta de Armazenamento com utilitário AzCopy e Azure Activity Log.
- C) Application Insights com monitoramento sintético e testes de disponibilidade.
- D) Network Watcher com registros de fluxo de NSG e grupo de ação.
**Resposta Correta:** A
**Explicação Técnica:** O Azure Monitor Agent (AMA), quando configurado via Regras de Coleta de Dados (DCR), coleta logs e métricas de SO convidado em VMs e os envia para um Log Analytics Workspace para consultas KQL.

