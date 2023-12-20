class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = 0
        for digit in digits:
            x *= 10
            x += digit
        x += 1
        ans = list()
        while (x != 0):
            p = x%10
            ans.append(p)
            x //= 10
        return reversed(ans)