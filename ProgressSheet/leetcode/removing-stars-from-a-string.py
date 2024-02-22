class Solution:
    def removeStars(self, s: str) -> str:

        s = list(s)
        print(s)
        stack = []

        for i in range(len(s)):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
                
        return "".join(stack)