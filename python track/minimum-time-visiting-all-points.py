class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        tot_time = 0

        for i in range(len(points)-1):
            x1,y1 = points[i]
            x2,y2 = points[i+1]

            tot_time += max(abs(x2-x1), abs(y2-y1))
        return tot_time