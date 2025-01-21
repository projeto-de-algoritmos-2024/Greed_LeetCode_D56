class Solution(object):
    def splitArray(self, nums, k):
        def can_split(max_sum):
            current_sum = 0
            subarrays = 0
            for num in nums:
                if current_sum + num >= max_sum:
                    subarrays += 1
                    current_sum = 0
                else:
                    current_sum += num
            return subarrays <= k

        left = sum(nums)
        right = max(nums) * k

        while left < right:
            mid = (left + right + 1) // 2
            if can_split(mid):
                right = mid - 1
            else:
                left = mid

        return right