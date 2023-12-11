class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        _sum = 0
        for i in range(len(nums)-3, -1, -1):
            if nums[i+2] < nums[i+1] + nums[i]:
                return sum(nums[i:i+3])
        return 0