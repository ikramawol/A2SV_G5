class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = Counter(s)
        print(letters)
        count = 0
        for val in letters.values():
            if val > 1:
                count += val-1

        _sum = sum(letters.values())

        return _sum - count
