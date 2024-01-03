class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        count = 0
        nums.sort()
        #print(nums)
        """l, r = 0, len(nums)-1
        while l < len(nums):
            r = 
            if nums[l] + nums[r] < target:
                count += 1
                r-=1"""
            
        
        for l in range(len(nums)):
            r = l+1
            while r < len(nums):
                if nums[l] + nums[r] < target:
                    count += 1   
                r += 1
            #r += 1
        return count