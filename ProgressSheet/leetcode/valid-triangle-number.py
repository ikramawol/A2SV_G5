class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        count = 0
        for i in range(n-1, 1, -1):
            l = 0
            r = i-1
            while l < r:
                if nums[r] + nums[l] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
                    
        return count