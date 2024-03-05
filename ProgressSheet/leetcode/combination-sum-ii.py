class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ans = []
        last, _sum = 0, 0
        def combSum(fn,path):
            nonlocal _sum, last
            if target == _sum:
                ans.append(path[:])
            
            if target < _sum:
                return

            for i in range(fn, len(candidates)):
                if candidates[i] != last:
                    _sum += candidates[i]
                    path.append(candidates[i])
                    combSum(i+1, path)
                    last = path.pop()
                    _sum -= last
        
        combSum(0, [])
        return ans
                
