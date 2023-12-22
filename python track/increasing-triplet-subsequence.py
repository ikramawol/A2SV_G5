class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x, y = nums[0], float('inf')
        for i in range(len(nums)-1):
           
            if nums[i+1] <= x:
                x = nums[i+1]
            elif nums[i+1] <= y :
                y = nums[i+1]
            elif nums[i+1] > x and nums[i+1] > y:
                return True
        return False