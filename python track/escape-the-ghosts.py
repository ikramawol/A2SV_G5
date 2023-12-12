class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        dest = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            distance = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            
            if distance <= dest:
                return False
            
        return True