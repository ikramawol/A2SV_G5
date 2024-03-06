class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if target not in nums:
            return [-1, -1]

        return [bisect_left(nums, target), bisect_right(nums, target)-1]

        # while left <= right:
        #     mid = (left + right)//2
        #     if nums[mid] < target:
        #         right = mid - 1
        #     elif nums[mid] > target:
        #         left = mid + 1
        #     elif nums[mid] == target:
            
        #         return [-1 ,-1]

        #     return [-1, -1]