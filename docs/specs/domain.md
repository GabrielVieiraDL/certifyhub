# CertifyHub — domain.md

## Linguagem Ubíqua

- **Certificação (Certification):** Título oficial outorgado por um provedor (ex: Microsoft Certified: Azure Fundamentals).
- **Exame (Exam):** O teste em si (código: AZ-900, AZ-104, AZ-204, etc.), composto por regras como tempo limite, nota de corte (geralmente 700/1000) e número de questões.
- **Domínio / Objetivo (Skill Domain):** Tópico oficial avaliado no exame (ex: "Descrever a arquitetura e serviços do Azure", com peso de 35-40%).
- **Questão (Question):** Item de avaliação, podendo ser de Múltipla Escolha Simples (Single Choice), Múltipla Escolha Múltipla (Multiple Choice) ou Associação de Casos.
- **Alternativa (Option):** Opção de resposta com texto e justificativa detalhada (por que está certa ou errada).
- **Tentativa de Simulado (ExamSession / Attempt):** Sessão ativa ou finalizada de um aluno respondendo a um simulado.
- **Modo do Simulado (ExamMode):**
  - `Practice`: Feedback imediato a cada resposta com explicação e referências Microsoft Learn.
  - `Exam`: Simulação fiel do exame oficial (tempo regressivo, sem consulta de gabarito durante o teste, cálculo de nota final e pontuação por domínio).

## Entidades e Invariantes

### ExamSession
- **Invariantes:**
  - Não é possível responder questões após o `ExpiresAt` expirado no modo `Exam`.
  - A pontuação final é calculada estritamente no backend.
  - Gabaritos de respostas nunca são revelados para sessões com status `InProgress`.
