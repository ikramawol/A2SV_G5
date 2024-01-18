class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftPro = rightPro = 1 
        exclPro = [1]*len(nums)

        for i in range(len(nums)):
            exclPro[i] *= leftPro
            leftPro *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            exclPro[i] *= rightPro
            rightPro *= nums[i]

        return exclPro