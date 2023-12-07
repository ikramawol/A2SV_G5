class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        n = len(distance)
        cw_dir = 0
        ccw_dir = 0

        i = start
        while i != destination:
            cw_dir += distance[i]
            i = (i + 1) % n
            
        i = start
        while i != destination:
            i = (i - 1 + n) % n
            ccw_dir += distance[i]

        return min(cw_dir, ccw_dir)