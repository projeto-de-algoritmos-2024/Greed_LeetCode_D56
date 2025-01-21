class Solution(object):
    def splitArray(self, nums, k):
        def can_split(max_sum):

            current_sum = 0
            subarrays = 1
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True
