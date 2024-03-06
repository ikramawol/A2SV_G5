class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        path = []
        def constructor(open, cloth):
            nonlocal path, ans
            
            if len(path) == 2*n:
                ans.append("".join(path[:]))
                return

            if open < n:
                path.append("(")
                constructor(open + 1, cloth)
                path.pop()
            
            if cloth < open:
                path.append(")")
                constructor(open, cloth + 1)
                path.pop()
                

        constructor(0, 0)       
        return ans