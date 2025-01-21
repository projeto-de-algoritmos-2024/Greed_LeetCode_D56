# Course Schedule III

Você tem uma lista de cursos, onde cada curso é descrito por um par `[t, d]`:
- `t` representa o número de dias necessários para concluir o curso.
- `d` representa o último dia até o qual o curso deve estar concluído.

É possível cursar somente um curso por vez. O objetivo é **encontrar a quantidade máxima de cursos** que podem ser completados seguindo o critério de conclusão antes do prazo `d`.

## Exemplo 1

- **Entrada:** `courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]`
- **Saída:** `3`

Explicação:
- É possível completar no máximo 3 cursos dentro de seus respectivos prazos.
- Uma possível ordem de cursos concluídos pode ser:
  1. `[100, 200]` (leva 100 dias, finalizando no dia 100)
  2. `[1000, 1250]` (leva 1000 dias, mas pode ser ajustado na sequência, finalizando no dia 1100, por exemplo)
  3. `[200, 1300]` (leva 200 dias, finalizando no dia 1300)
- O quarto curso `[2000, 3200]` não seria possível encaixar a tempo.

## Observações Importantes
- É necessário encontrar um modo de ordenar a realização dos cursos de forma a maximizar o total concluído.
- Geralmente, uma estratégia envolve priorizar cursos de menor duração e descartar cursos menos vantajosos caso ultrapasse o prazo.

## Restrições
- `1 <= courses.length <= 10^4`
- `1 <= t_i, d_i <= 10^9`
- A soma de `t_i` ao longo dos cursos pode ser muito grande, exigindo uma solução mais eficiente do que tentativas de agendamento ingênuas.

> **Nota**: Para ver o enunciado completo ou buscar soluções detalhadas, consulte  
> [a página do problema no LeetCode](https://leetcode.com/problems/course-schedule-iii/description/).  
