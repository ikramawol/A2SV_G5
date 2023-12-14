class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l = len(nums)
        res = [0]*len(nums)
        for i in range(l//2):
            res[i*2] = nums[i]
            res[i*2+ 1] = nums[l//2 + i]
        return res