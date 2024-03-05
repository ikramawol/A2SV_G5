class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        path = []
        ans = []
        n = len(digits)

        if digits == "":
            return []
            
        def combine(fn):
            nonlocal path, ans
            if len(path) == n:
                ans.append("".join(path[:]))
                return

            val = dic[digits[fn]]
            for i in val:
                path.append(i)
                combine(fn+1)
                path.pop()

        combine(0)
        return ans