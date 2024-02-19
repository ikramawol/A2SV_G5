class Solution:
    def minimumSteps(self, s: str) -> int:

        count = 0
        l = 0

        for r in range(len(s)):
            if s[r] == '0':
                count += r - l 
                l += 1
        return count 