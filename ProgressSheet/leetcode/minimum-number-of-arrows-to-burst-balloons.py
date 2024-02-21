class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        
        ans = 1
        n = len(points)
        
        j = 0
        for i in range(n):
            
            if points[j][1] < points[i][0]:
                ans += 1
                j = i
        return ans