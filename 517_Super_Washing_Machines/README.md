# **Super Washing Machines**

### **Descrição do Problema**
Dado um array `machines` onde cada elemento representa o número de roupas em uma máquina de lavar, o objetivo é redistribuir as roupas entre todas as máquinas para que todas contenham o mesmo número de roupas. Cada máquina pode:
1. Enviar uma peça de roupa para a máquina à sua esquerda.
2. Enviar uma peça de roupa para a máquina à sua direita.

O problema é determinar o **número mínimo de movimentos necessários** para atingir o equilíbrio, onde todas as máquinas têm o mesmo número de roupas.

---

### **Regras e Restrições**
1. Se o total de roupas dividido pelo número de máquinas não for um número inteiro, o equilíbrio não será possível.
2. Cada movimento representa a transferência de uma peça de roupa de uma máquina para outra adjacente.

#### **Entradas**:
- `machines`: Lista de inteiros representando o número de roupas em cada máquina.
  - \( 1 \leq \text{machines.length} \leq 10^4 \)
  - \( 0 \leq \text{machines[i]} \leq 10^4 \)

#### **Saídas**:
- Um número inteiro representando o número mínimo de movimentos necessários para alcançar o equilíbrio, ou -1 se o equilíbrio não for possível.

---

### **Exemplo 1**
**Entrada**:
```python
machines = [1, 0, 5]
```

**Saída**:
```python
3
```

**Explicação**:
- Passo 1: A máquina 3 envia 1 peça para a máquina 2 → `[1, 1, 4]`.
- Passo 2: A máquina 3 envia 1 peça para a máquina 2 → `[1, 2, 3]`.
- Passo 3: A máquina 2 envia 1 peça para a máquina 1 → `[2, 2, 2]`.

---

### **Exemplo 2**
**Entrada**:
```python
machines = [0, 3, 0]
```

**Saída**:
```python
2
```

**Explicação**:
- Passo 1: A máquina 2 envia 1 peça para a máquina 1 → `[1, 2, 0]`.
- Passo 2: A máquina 2 envia 1 peça para a máquina 3 → `[1, 1, 1]`.

---

### **Exemplo 3**
**Entrada**:
```python
machines = [0, 2, 0]
```

**Saída**:
```python
-1
```

**Explicação**:
- O total de roupas é 2 e o número de máquinas é 3. Como \( 2 \div 3 \) não é um número inteiro, o equilíbrio é impossível.

---

### **Links Relacionados**
- [Página do problema no LeetCode](https://leetcode.com/problems/super-washing-machines/?envType=problem-list-v2&envId=greedy)