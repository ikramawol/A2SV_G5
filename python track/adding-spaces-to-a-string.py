class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        substr = []
        start = 0
        
        for end in spaces:
            substr.append(s[start:end])
            start = end
        substr.append(s[start:])
        return " ".join(map(str, substr))
        """
        lists = list(s)
        new_s = ''
        
        for pointer in reversed(spaces):
            lists.insert(pointer, ' ')
        new_s += "".join(lists)
        return new_s
        """