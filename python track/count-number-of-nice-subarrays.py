class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        subArrayCount = count = 0
        l, odd = 0, 0
        for r in range(len(nums)):
            if nums[r] % 2!= 0:
                odd += 1
                count = 0
            while odd == k:
                count += 1
                if nums[l] % 2 != 0:
                    odd -= 1
                l += 1
            subArrayCount += count
        return subArrayCount

        # brute force
        # for i in range(len(nums)-k):
        #     j = i
        #     s = 0

        #     while j < len(nums):
                
        #         if nums[j] % 2 != 0 and k > 0:
        #             s += 1
        #         if s == k:
        #             count += 1
        #             break
        #         j += 1
        # return count