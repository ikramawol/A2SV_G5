class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        while t > 0:
            num += t
            x = num + t
            t += 1
            return x
