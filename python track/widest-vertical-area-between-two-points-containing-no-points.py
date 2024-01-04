class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        _max = 0
        res = set()
        for i in range(len(points)-1):
            _max = points[i+1][0] - points[i][0]
            res.add(_max)
        return max(res)