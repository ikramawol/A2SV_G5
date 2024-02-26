class Solution:
    def __init__(self):
        self.avail = {}
    def countGoodNumbers(self, n: int) -> int:

        # self.avail = {}
        
        if n == 1:
            return 5
        if n == 2:
            return 20

        if n not in self.avail:
            x = n//2
            if n % 2 != 0:
                self.avail[n] = (self.countGoodNumbers(x) * self.countGoodNumbers(x + 1))%((10**9) + 7)
            else:
                self.avail[n] = (self.countGoodNumbers((n-1))*4)%(10**9 + 7)
            return self.avail[n]%(10**9 + 7)
        else:
            return self.avail[n]%(10**9 + 7)