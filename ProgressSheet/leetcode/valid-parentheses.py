class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        if s == "":
            return True

        validBrackets = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []
        for par in s:
            if par in validBrackets:
                    stack.append(par)
            else:
                if len(stack) == 0 or validBrackets[stack.pop()] != par:
                    return False
                
        if len(stack) > 0:
            return False
        return True


            
        
