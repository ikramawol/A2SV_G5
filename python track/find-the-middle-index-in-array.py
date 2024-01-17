class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
    
        leftSum = 0
        for i in range(len(nums)): 
            if leftSum == total - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        else:
            return -1