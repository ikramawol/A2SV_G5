class Solution:
    def maxScore(self, s: str) -> int:
        pref = [0]*len(s)
        tot = count = maxPref = max_ans = 0 

        for i in range(len(s)):
            tot += int(s[i])
            pref[i] = tot

        maxPref = pref[-1]
        for i in range(len(pref)-1):
            if s[i]== '0':
                count += 1
            else:
                maxPref -= 1

            max_ans = max(max_ans, count + maxPref)
            
        return max_ans