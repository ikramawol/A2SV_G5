class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_un = float("inf")
        ch = [0]*k

        def backtrack(i):
            nonlocal min_un
            if i == len(cookies):
                un = max(ch)
                min_un = min(min_un, un)
                return
            
            for j in  range(k):
                ch[j] += cookies[i]
                if ch[j] < min_un:
                    backtrack(i+1)
                ch[j] -= cookies[i]
        backtrack(0)
        return min_un   