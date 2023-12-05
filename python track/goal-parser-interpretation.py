class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        # dic = {G : "G", () : "o", (al) : "al"}
        strs = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                strs.append('G')
                i += 1
            else:
                if command[i+1] == ')':
                    strs.append("o")
                    i += 2
                else:
                    strs.append("al")
                    i += 4
           
            
        return "".join(strs)
    
        