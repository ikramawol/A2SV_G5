class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        strs = []
        _min = min(len(word1), len(word2))
        x = abs(len(word1) - len(word2))
        for i in range(_min):
            pointer1 = word1[i]
            pointer2 = word2[i]
            strs.append(pointer1)
            strs.append(pointer2)    
        if x > 0:
            if len(word1) > len(word2):
                strs.append(word1[_min:])
            else:
                strs.append(word2[_min:])
        return ''.join(map(str, strs))