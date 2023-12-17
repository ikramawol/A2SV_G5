class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        repeted = Counter(arr)
        n = len(arr)
        most_used = 0

        for key, val in repeted.items():
            if val > n//4:
                most_used = key
                
        return most_used