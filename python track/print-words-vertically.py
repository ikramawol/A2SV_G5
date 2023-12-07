class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        words = s.split()
        word = ""
        _max = max(len(word) for word in words)
        for i in range(0, _max):
           # _max = max(len(new_arr[i]))
            column = []
            for word in words:
                if i < len(word):
                    column.append(word[i])
                else:
                    column.append(" ")
            res.append("".join(column).rstrip())
        return res
                