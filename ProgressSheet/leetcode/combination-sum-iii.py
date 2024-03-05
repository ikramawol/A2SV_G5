class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        _sum = 0
        ans = []
        last = 0

        def combinationSum(fn ,path):
            nonlocal last, ans, _sum
            
            if len(path) == k and _sum == n:
                ans.append(path[:])
            
            if _sum > n:
                return

            for i in range(fn, 10):
                if i != last:
                    _sum += i
                    path.append(i)
                    combinationSum(i + 1, path)
                    last = path.pop()
                    _sum -= last

        combinationSum(1, [])
        return ans



        