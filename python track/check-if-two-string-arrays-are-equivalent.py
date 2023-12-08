class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        new_word1 = ''
        new_word2 = ''
        for i in word1:
            new_word1 += i

        for j in word2:
            new_word2 += j
            
        if new_word1 == new_word2:
            return True
        else:
            return False