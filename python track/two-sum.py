class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = {}
        
        for i, n in enumerate(nums):
            val = target - n
            if val not in pairs:
                pairs[n] = i
            else:
                return [i, pairs[val]]
                