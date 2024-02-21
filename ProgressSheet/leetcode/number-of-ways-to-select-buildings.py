class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        zeroOne = [0]*(n+1)
        oneZero = [0]*(n+1)
        
        count_0 = count_1 = ans = 0
        for i in range(n):
            if s[i] == '0':
                oneZero[i+1] += count_1
                count_0 += 1
            elif s[i] == '1':
                zeroOne[i+1] += count_0
                count_1 += 1
            zeroOne[i+1] += zeroOne[i]
            oneZero[i+1] += oneZero[i]

        for i in range(n):
            if s[i] == '0':
                ans += zeroOne[i]
            else:
                ans += oneZero[i]

        return ans 




