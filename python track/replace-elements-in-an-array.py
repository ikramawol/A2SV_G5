class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        #nums_copy = [0]*len(nums)
        comb = {}

        for i in range(len(nums)):
            comb[nums[i]] = i
        for val, rep in operations:
            nums[comb[val]] = rep
            comb[rep] = comb[val]
        return nums
        