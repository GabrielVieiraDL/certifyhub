# CertifyHub — CLAUDE.md

## Idioma de trabalho
- Responder e documentar preferencialmente em português do Brasil.

## Antes de qualquer tarefa
1. Leia `/docs/specs/main.md`.
2. Leia `/docs/specs/architecture.md`.
3. Siga o workflow obrigatório: Research -> Plan -> Implement -> Verify -> Review -> Report.
4. Respeite todas as regras em `.claude/rules/`.

## Agentes Universais Configurados
- `architect`: Modelagem, contratos e decisões de arquitetura.
- `researcher`: Pesquisa de código e documentação (read-only).
- `backend`: Endpoints, regras de negócio, persistência e APIs.
- `frontend`: Interfaces, componentes, responsividade e interatividade.
- `database`: Esquemas de banco, migrações e índices.
- `security-reviewer`: Auditoria de OWASP, IDOR e segredos.
- `code-reviewer`: Qualidade de código, Clean Code e SOLID.
- `test-engineer`: Cobertura e suites de testes.
- `devops`: Build, Docker e CI/CD.
- `documentation-writer`: Docs e OpenAPI.

## Regras invioláveis
- Nunca expor ou versionar segredos e arquivos `.env`.
- Nunca expor o gabarito das questões no frontend antes da conclusão do exame.
- Nunca concatenar consultas SQL ou ignorar validação de DTOs.
- Obrigatório gerar o Task Report em `docs/tasks/` após cada entrega.
