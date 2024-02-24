class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = unreachable = 0

        i = 0
        while unreachable < n:
            if i < len(nums) and nums[i] <= unreachable + 1:
                unreachable += nums[i]
                i += 1
            else:
                unreachable += unreachable + 1
                patch += 1
        return patch