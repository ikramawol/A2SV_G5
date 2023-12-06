class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans  = 0
        for left in range(len(nums)):
            if nums[left] != 0:
                count +=1 
            else:
                ans = max(ans , count)
                count = 0
        ans = max(ans, count)
        return ans