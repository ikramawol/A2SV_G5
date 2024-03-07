class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums)-1

        if nums[left] < nums[right]:
            return nums[left]
        
        while left + 1 < right:
            mid = (left + right)//2
            # curr = min(curr, mid)
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            
            
        return nums[right]
        