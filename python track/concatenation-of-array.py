class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lists = []
        n = len(nums) 
        i = 0
        while i <= 1:
            j = 0
            while j < n:
                lists.append(nums[j])
                j+=1
            i+=1
        return lists