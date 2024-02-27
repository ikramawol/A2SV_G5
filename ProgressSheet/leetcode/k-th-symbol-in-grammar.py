class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # def gramm(n):

        #     if n == 1:
        #         return "0"
        
        #     rs = ""
        #     prev = gramm(n-1)
        #     for i in range(len(prev)):
        #         if prev[i] == "0":
        #             rs += "01" 
        #         elif prev[i] == "1":
        #             rs += "10"
        
        #     return rs
        # val = gramm(n)
        # return int(val[k-1]) 
        if k == 1:
            return 0
        if  k % 2 != 0:
            return self.kthGrammar(n, ceil(k/2))
        if k % 2 == 0:
            val = self.kthGrammar(n, ceil(k/2))
            if val == 0:
                return 1
            else:
                return 0

