class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def comb(fn, path, target):

            if target == 0:
                ans.append(path[:])
            
            if target < 0:
                return

            for i in range(fn, len(candidates)):
                path.append(candidates[i])
                comb(i, path, target - candidates[i])
                path.pop()

        ans = []
        comb(0, [], target)
        return ans