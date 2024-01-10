class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(p)
        dic = Counter(p)
        res = []
        idx = n - 1
        sub = Counter(s[:idx])

        while idx < len(s):
            sub[s[idx]] += 1
            if sub == dic:
                res.append(idx-n+1)
            sub[s[idx-n+1]] -= 1
            if sub[s[idx-n+1]] == 0:
                del sub[s[idx-n+1]]
            idx += 1
        return res    
            