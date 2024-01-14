class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        count = float('inf') 
        _sum = 0

        for r in range(len(nums)):
            _sum += nums[r]
            while _sum >= target:
                count = min(r - l + 1, count)
                _sum -= nums[l]
                l += 1
        return 0 if count == float('inf') else count