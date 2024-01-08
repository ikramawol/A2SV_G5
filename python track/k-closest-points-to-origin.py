class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda points: points[0]**2 + points[1]**2)
        print(points)
        res = []
        l, r = 0, min(k, len(points))-1
        while l <= r:
            res.append(points[l])
            l += 1
        return res