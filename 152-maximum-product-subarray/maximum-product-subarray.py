class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProduct = nums[0]
        maxProduct = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = minProduct * nums[i]
            v3 = maxProduct * nums[i]
            maxending = max(v1, max(v2, v3))
            minending = min(v1, min(v2, v3))
            maxProduct = maxending
            minProduct = minending
            
            result = max(result, max(maxending, minending))
        return result

