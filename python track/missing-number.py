class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        set(nums)
        for i in range(0, n+1):
            if i in nums:
                continue
            else:
                return i
            
        