class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        r = len(nums)-1
        l = r - 1
        count = 0
        
        while l >= 0 and r >= 1:
            #print(nums[r], nums[l])
            if nums[r] > nums[l]:
                count += len(nums)-1 - l
            l -= 1
            r -= 1
        return count

                

