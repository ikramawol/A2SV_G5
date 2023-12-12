class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        container = {i for a,b in ranges for i in range(a, b + 1)}
        
        left_right = {i for i in range(left,right + 1)}
        return left_right <= container
        