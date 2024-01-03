class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l, r = 0, 0
        g.sort()
        s.sort()
        print(g, s)
        count = 0
        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                count += 1
                r += 1
                l += 1
            else:
                r += 1
             
        return count