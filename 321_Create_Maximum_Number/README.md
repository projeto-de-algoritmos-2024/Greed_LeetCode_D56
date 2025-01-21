# Create Maximum Number

Dadas duas listas de inteiros não negativos, `nums1` e `nums2`, o objetivo é criar um novo array de **tamanho `k`** que seja lexicograficamente **o maior possível**. Você pode:
- Escolher alguns (ou todos) elementos de `nums1`, mantendo sua **ordem** original.
- Escolher alguns (ou todos) elementos de `nums2`, mantendo sua **ordem** original.
- Combinar esses elementos de forma que o resultado final (também em ordem) seja o **maior** array possível em termos lexicográficos.

**Resumo da Tarefa:**
1. Você precisa decidir **quantos elementos** pegar de `nums1` e `nums2` (totalizando `k` elementos).
2. Garantir que, ao concatenar as subsequências de cada lista, o resultado seja **lexicograficamente máximo**.
3. Respeitar a ordem em que os elementos aparecem originalmente em cada lista.

## Exemplo 1
- **Entrada:** `nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5`
- **Saída:** `[9, 8, 6, 5, 3]`

## Exemplo 2
- **Entrada:** `nums1 = [6, 7], nums2 = [6, 0, 4], k = 5`
- **Saída:** `[6, 7, 6, 0, 4]`

## Exemplo 3
- **Entrada:** `nums1 = [3, 9], nums2 = [8, 9], k = 3`
- **Saída:** `[9, 8, 9]`

## Restrições
- `1 <= nums1.length + nums2.length <= 50000`
- `0 <= nums1[i], nums2[i] <= 9`
- `1 <= k <= nums1.length + nums2.length`
- As entradas podem ser grandes, demandando algoritmos eficientes em tempo e espaço.

> **Observação:** Caso deseje o texto integral ou mais informações,  
> consulte a [página do problema no LeetCode](https://leetcode.com/problems/create-maximum-number/description/).  
