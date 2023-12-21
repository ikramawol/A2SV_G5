class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        zipped = list(zip(*strs))
        print(zipped)
        count = 0
        for i in range(len(zipped)):
            for j in range(len(zipped[i])-1):
                if ord(zipped[i][j]) > ord(zipped[i][j+1]):
                    count += 1
                    break
        return count