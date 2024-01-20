class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suff = [0]*n, [0]*n

        ans = []
        left = right = tot1 = tot2 = 0
       
        for i in range(n):
            tot1 += nums[i]
            pref[i] = tot1
            tot2 += nums[(n-i-1)]
            suff[n-i-1] = tot2

        for i in range(n):
            left = (nums[i] * i) - pref[i]
            right = suff[i] - (nums[i] * (n-i-1))
            
            ans.append(right + left)

        return ans