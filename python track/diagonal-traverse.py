class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        dic = defaultdict(list)
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonal = i+j
                dic[diagonal] += [mat[i][j]]
        for key, val in dic.items():
            if key % 2 ==0:
                ans.extend(val[::-1])
            else:
                ans.extend(val)
        return ans