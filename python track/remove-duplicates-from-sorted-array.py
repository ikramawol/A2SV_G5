class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ptr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[ptr]:
                ptr += 1
                nums[ptr] = nums[i]
            elif len(nums) == 0:
                return 0
                break
        return ptr + 1  