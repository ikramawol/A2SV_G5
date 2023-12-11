class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicates = Counter(nums)
        if max(duplicates.values()) > 1:
            return True
        else:
            return False