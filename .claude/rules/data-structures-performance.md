# Rule: Escolha consciente de estruturas de dados e performance

## Escolha da estrutura

- NÃO use listas/arrays genericamente para qualquer problema.
- Escolha a estrutura com base na operação dominante (busca, inserção, deleção, iteração, etc.).
- Documente a complexidade esperada em Big-O quando a feature manipular grande volume de dados.
- Para dados sensíveis, minimize cópias em memória e evite estruturas globais mutáveis.
- Para APIs, use paginação, limites e filtros indexáveis para evitar DoS por payload ou consulta pesada.
- Para caches e maps, defina política de expiração (TTL), limite de tamanho e estratégia de invalidação.

## Riscos de DoS e Memória

- Defina limite máximo para listas, arrays, objetos, profundidade de árvore e recursão.
- Evite loops aninhados desnecessários (O(n²)).
- Evite buscas no banco dentro de loops; prefira consultas em lote.
- Proteja mapas em TypeScript contra poluição de protótipo (`__proto__`, `constructor`).
