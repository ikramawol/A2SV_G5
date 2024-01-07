class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for l in range(len(nums)):
            r = len(nums)-1
            while l < r:
                if nums[l] > nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                    r-=1
                else:
                    r-= 1

        """
        l = 1
        for r in range(len(nums)-1):

            if nums[r] == nums[l]:
                
                nums[r+1], nums[l] = nums[l], nums[r+1]
                l += 1
        """
        """
        for i in range(1, len(nums)):
            j = i
            while j > 0 and  nums[j] < nums[j-1]:
                nums[j], nums[j-1] =nums[j-1],nums[j]
                j-=1"""
