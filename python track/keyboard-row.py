class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyBoard = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        
        result = []
        for word in words:
            lower_word = word.lower()
            
            if all(char in keyBoard[0] for char in lower_word) or all(char in keyBoard[1] for char in lower_word) or all(char in keyBoard[2] for char in lower_word):
                result.append(word)
        return result
            