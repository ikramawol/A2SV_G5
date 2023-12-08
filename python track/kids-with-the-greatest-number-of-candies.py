class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        lists = []
        larger = max(candies)
        for i in candies:
            if i + extraCandies >= larger:
                lists.append(True)
            else:
                lists.append(False)
        return lists
