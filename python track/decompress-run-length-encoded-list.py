class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        i = 0
        while i <= len(nums)-1:
            sliced = []
            sliced.append(nums[i:i+2])
            for freq, val in sliced:
                for j in range(0, freq):
                    res.append(val)
            i+=2
        return res