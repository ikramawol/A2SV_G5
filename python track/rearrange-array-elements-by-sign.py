class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums, key = lambda x : x < 0)
        n = len(nums)
        nums[1::2], nums[::2] = nums[n//2:], nums[:n//2]
        
        return nums