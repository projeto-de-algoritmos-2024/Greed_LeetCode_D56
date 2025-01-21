class Solution(object):
    def splitArray(self, nums, k):
        def can_split(max_sum): # Verifica se é possível dividir o array em k ou menos subarrays com soma máxima <= max_sum. 
            current_sum = 0
            subarrays = 1  # Iniciando a variável com um subarray
            for num in nums:
                # Se adicionar este número exceder max_sum, precisamos criar um novo subarray
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:  # Não é possível dividir em k subarrays
                        return False
                else:
                    current_sum += num
            return True

        # Busca binária nos limites
        left = max(nums)  # Nenhum subarray pode ter soma menor que o maior elemento
        right = sum(nums)  # Nenhum subarray pode ter soma maior que a soma total

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid  # Soma máxima menor
            else:
                left = mid + 1  # Soma máxima maior

        return left  # O menor valor de soma máxima possível
