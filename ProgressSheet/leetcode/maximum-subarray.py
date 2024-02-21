class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArrSum = nums[0]
        ans = nums[0]

        n = len(nums)
        for i in range(1, n):
            subArrSum = max(subArrSum + nums[i], nums[i])
            ans = max(ans, subArrSum)
            
        return ans