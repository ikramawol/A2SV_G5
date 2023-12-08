class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        temp = []
        for n in range(len(num)-2):
            if num[n] == num[n+1] and num[n+1] == num[n+2]:
                    temp.append(num[n:n+3])
            else:
                continue
        if temp:
            elements = str(max(temp))
        else:
            elements = ""
        return elements