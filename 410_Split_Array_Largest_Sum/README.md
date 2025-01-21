# Split Array Largest Sum

Dado um array de inteiros `nums` e um inteiro `m`, o objetivo é dividir o array em **m subarrays não vazios** de forma que o **maior valor da soma de qualquer subarray** seja o **menor possível**. Em outras palavras, minimizamos o "peso máximo" entre os subarrays resultantes.

## Resumo da Tarefa
1. **Divisão em subarrays**: Você precisa dividir `nums` em exatamente `m` subarrays consecutivos.
2. **Minimizar a soma máxima**: O maior valor da soma de qualquer subarray resultante deve ser minimizado.
3. **Resultado**: Retorne esse menor valor possível.

## Regras e Restrições
- A ordem dos elementos em `nums` **não pode ser alterada**.
- Cada subarray deve ser **contíguo**.
- Todos os subarrays devem conter pelo menos um elemento.

---

### Exemplo 1
**Entrada**:
- `nums = [7, 2, 5, 10, 8]`
- `m = 2`

**Saída**:
- `18`

**Explicação**:
- Dividimos o array como `[7, 2, 5]` e `[10, 8]`.
- Soma máxima = `max(7+2+5, 10+8) = 18`.
- Qualquer outra divisão resultará em uma soma máxima maior que 18.

---

### Exemplo 2
**Entrada**:
- `nums = [1, 2, 3, 4, 5]`
- `m = 2`

**Saída**:
- `9`

**Explicação**:
- Dividimos o array como `[1, 2, 3]` e `[4, 5]`.
- Soma máxima = `max(1+2+3, 4+5) = 9`.

---

### Exemplo 3
**Entrada**:
- `nums = [1, 4, 4]`
- `m = 3`

**Saída**:
- `4`

**Explicação**:
- Dividimos o array como `[1]`, `[4]`, e `[4]`.
- Soma máxima = `max(1, 4, 4) = 4`.

---

## Abordagem de Solução
1. **Busca Binária**:
   - Determine o intervalo de possíveis valores para a soma máxima:
     - O limite inferior é o maior elemento em `nums` (nenhum subarray pode ter uma soma menor que isso).
     - O limite superior é a soma de todos os elementos de `nums` (um único subarray contendo todo o array).
   - Use **busca binária** para encontrar o menor valor de soma máxima possível.
   
2. **Verificação de Viabilidade**:
   - Para um valor candidato `mid` (durante a busca binária), verifique se é possível dividir `nums` em **m ou menos subarrays** com uma soma máxima menor ou igual a `mid`.
   - Isso pode ser feito iterando por `nums` e acumulando a soma atual até que exceda `mid`, momento em que iniciamos um novo subarray.

---

### Restrições
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^6`
- `1 <= m <= min(50, nums.length)`

---

## Links Relacionados
- [Página do problema no LeetCode](https://leetcode.com/problems/split-array-largest-sum/description/?envType=problem-list-v2&envId=greedy)