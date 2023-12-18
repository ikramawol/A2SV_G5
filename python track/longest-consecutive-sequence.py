class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(sorted(set(nums)))
        count = 1
        max_len = 1

        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                count += 1
            else:
                count = 1
            max_len = max(count, max_len)
        return max_len