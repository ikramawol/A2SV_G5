class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = close = 0

        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            elif s[i] == ')':
                if open != 0:
                    open -= 1
                else:
                    ans += 1
        return ans + open