class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        res = []
        temp1=[]
        temp2=[]
        temp3=[]
        for num in nums:
            if num < pivot:
                temp1.append(num)
            elif num == pivot:
                temp2.append(num)
            else:
                temp3.append(num)
        res = temp1 + temp2 +temp3
        return res