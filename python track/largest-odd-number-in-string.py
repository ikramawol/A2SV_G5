class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        lists = list(map(int, num))
        
        if any(x % 2 != 0 for x in lists):
            while lists[-1] % 2 == 0:
                lists.pop()
                
            return "".join(map(str, lists))
        else:
            return ""
