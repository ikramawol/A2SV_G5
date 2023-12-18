class Solution:
    def isHappy(self, n: int) -> bool:
        avail = set()
        while n not in avail:
            avail.add(n)
            sqSum =0
            while n > 0:
                sqSum += (n%10)**2
                n = floor(n/10)
            if sqSum == 1:
                return True
            n = sqSum
        return False