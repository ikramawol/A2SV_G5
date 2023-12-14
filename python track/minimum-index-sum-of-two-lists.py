class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = {}
        idx_sum = 0
        
        for i, strs in enumerate(list1):
            common[strs] = i
        
        result = []
        min_idx_sum = float('inf')
        
        for j, strs2 in enumerate(list2):
            if strs2 in common:
                index_sum  = common[strs2] + j
                
                if index_sum < min_idx_sum:
                    min_idx_sum = index_sum
                    result = [strs2]
                elif index_sum == min_idx_sum:
                    result.append(strs2)
                    
        return result