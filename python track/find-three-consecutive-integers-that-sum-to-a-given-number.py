class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        n = int(num / 3) - 1
        if num == (n+n+1+n+2): 
            ans.append(n)
            ans.append(n+1)
            ans.append(n+2)
            return ans
        else:
            return ans