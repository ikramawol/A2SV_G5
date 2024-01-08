class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0 
        for l in range(len(nums)):
            if nums[l] != val:
                nums[count] = nums[l]
                count += 1
        return count