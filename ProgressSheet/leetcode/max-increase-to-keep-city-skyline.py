class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
       
        zipped = list(zip(*grid))
        for i in range(len(grid)):
            for j in range(len(grid[i])): 
                ans += min(max(grid[i]), max(zipped[j])) -  grid[i][j] 
        return ans