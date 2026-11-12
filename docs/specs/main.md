# CertifyHub — Simulados para Certificações Oficiais de TI

## Visão
Plataforma moderna, interativa e de alta fidelidade para estudantes e profissionais de Tecnologia realizarem simulados preparatórios para exames de certificações oficiais (ex: AWS, Azure, GCP, CompTIA, Cisco, Kubernetes, Linux Foundation, etc.).

## Problema
Candidatos a exames de certificações sofrem com materiais desatualizados, interfaces confusas, falta de justificativa detalhada para respostas e ausência de métricas de desempenho por domínio de conhecimento do exame oficial.

## Usuários Principais
- **Estudante / Profissional de TI:** Realiza simulados por certificação, por tópico ou exame completo cronometrado; acompanha estatísticas de acertos por domínio.
- **Instrutor / Criador de Conteúdo:** Cadastra bancos de questões oficiais, justifica alternativas e organiza simulados.
- **Administrador:** Gerencia certificações, categorias, planos de assinatura/acesso e métricas da plataforma.

## Métricas de Sucesso
- Simulação realista (modo exame com tempo, pontuação de corte e revisão).
- Explicações detalhadas para todas as opções (corretas e incorretas) com links para documentação oficial.
- Desempenho rápido (p95 < 200ms nas trocas de questões e consultas).
- Resiliência offline/interrupção (salvamento automático de progresso do simulado).

## Escopo Inicial (MVP)
1. Autenticação e Perfis de Usuário.
2. Catálogo de Certificações e Exames (ex: AWS Cloud Practitioner / Solutions Architect, Azure Fundamentals AZ-900, CompTIA Security+).
3. Motor de Simulado:
   - Modo Prática (feedback imediato e explicação).
   - Modo Exame (cronômetro oficial, sem dicas, nota final e percentual por domínio).
4. Painel de Desempenho e Histórico de Tentativas.
5. Painel Administrativo para Gestão de Questões e Exames.
