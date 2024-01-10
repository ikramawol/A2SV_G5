class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l,r = 0,0

        while r < len(nums):

            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l+=1
            r += 1

        return r - l
            
        """no_zeros = nums.count(0)

        leng = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                leng.append(count)
                count = 0
        leng.append(count)
        print(leng)
        if no_zeros >= k:
            return max(leng) + k
        else:
            return count"""
                
