class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i, j = 0, 0
        _sum = 0
        while i <= len(mat)-1 and j <= len(mat)-1:
            _sum += mat[i][j]
            i+=1
            j+=1
        i = 0
        j = len(mat[0])-1
        while i <= len(mat)-1 and j <= len(mat)-1:
            _sum += mat[i][j]
            i+=1
            j-=1
        if len(mat[0]) % 2 != 0:
            return _sum - mat[len(mat)//2][len(mat)//2]
        else:
            return _sum
