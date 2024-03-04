class Solution:
    def splitString(self, s: str) -> bool:
        
        ans = []

        def backtrack(start):

            if start == len(s):
                return len(ans) >= 2
            
            for i in range(start, len(s)):
                num = int(s[start:i+1])

                if ans and ans[-1] - num != 1:
                    continue

                ans.append(num)
                if backtrack(i+1):
                    return True
                ans.pop()
            return False
        
        return backtrack(0)