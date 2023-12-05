class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        val = 0
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for j in dic.values():
            val += j * (j-1) // 2
            
        return val