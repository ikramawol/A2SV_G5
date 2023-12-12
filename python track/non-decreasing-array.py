class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        violation = 0
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                violation += 1
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        return violation <= 1
            