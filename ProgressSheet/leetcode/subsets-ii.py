class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    
        ans = []
        subset = []
        _sub = set()
        def sub(st):
            nonlocal subset, ans
            val = tuple(sorted(subset[:]))
            if val not in _sub:
                _sub.add(val)
                ans.append(subset[:])

            for i in range(st, len(nums)):
                subset.append(nums[i])
                sub(i+1)
                subset.pop()
                
        sub(0)
        return ans