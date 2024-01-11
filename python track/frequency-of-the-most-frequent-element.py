class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
    
        l ,s = 0, 0
        ans = 0
        nums.sort()
        for r in range(len(nums)):
            s += nums[r]
            while l < r and (r - l + 1)*nums[r] - s > k:
                s = s - nums[l]
                l += 1
            ans = max(ans, r-l+1)
            
        return ans