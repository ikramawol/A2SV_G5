class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        
        n = len(nums)
        res = []
        for i in nums:
            dic[i] = dic.get(i, 0)+1
            if dic[i] > n//3 and i not in res:
                res.append(i)
        return res