class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        iteration = (n // 2)+1
        for i in range(0, iteration):
            if n % 2 == 0:
                count += (n/2)
                n = (n/2)
            else:
                count += (n//2)
                n = (n//2) + 1
        return count