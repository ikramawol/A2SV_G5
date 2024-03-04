class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(fst_num, path):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(fst_num, n+1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        ans = []
        backtrack(1, [])
        return ans