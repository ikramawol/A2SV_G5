class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key = lambda a : len(a))
        result = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return result
            result = result + strs[0][i]
        return result
        