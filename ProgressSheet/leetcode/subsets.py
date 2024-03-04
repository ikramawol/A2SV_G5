class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        
        def sub(st):
            nonlocal subset, ans
            
            ans.append(subset[:])

            for i in range(st, len(nums)):
                subset.append(nums[i])
                sub(i+1)
                subset.pop()
        sub(0)
        print(ans)
        return ans