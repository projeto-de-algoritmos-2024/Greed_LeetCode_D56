class Solution:
    def maxNumber(self, nums1, nums2, k):
        best = [0] * k
        m, n = len(nums1), len(nums2)

        for i in range(k+1):
            if i <= m and (k - i) <= n:
                # Subsequência de tamanho i em nums1
                subseq1 = self.maxSubsequence(nums1, i)
                # Subsequência de tamanho k-i em nums2
                subseq2 = self.maxSubsequence(nums2, k - i)
                
                merged = self.merge(subseq1, subseq2)
                if merged > best:
                    best = merged
        return best

    def maxSubsequence(self, nums, length):
        stack = []
        to_remove = len(nums) - length

        for num in nums:
            # Remover elementos que são menores que o atual
            while stack and to_remove > 0 and stack[-1] < num:
                stack.pop()
                to_remove -= 1
            stack.append(num)

        # Remove se sobrou to_remove
        while to_remove > 0:
            stack.pop()
            to_remove -= 1

        return stack[:length]

    def merge(self, seq1, seq2):
        # usando greedy (compare seq1[i:] e seq2[j:])
        res = []
        i, j = 0, 0
        while i < len(seq1) and j < len(seq2):
            if seq1[i:] > seq2[j:]:
                res.append(seq1[i])
                i += 1
            else:
                res.append(seq2[j])
                j += 1
        res.extend(seq1[i:])
        res.extend(seq2[j:])
        return res