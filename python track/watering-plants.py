class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        n = len(plants)
        total = 0
        cur_pos = capacity
        
        for i in range(n):
            total += 1
            if plants[i] > cur_pos:
                total += i + i
                cur_pos = capacity - plants[i]
            else:
                cur_pos =  cur_pos - plants[i]
        return total