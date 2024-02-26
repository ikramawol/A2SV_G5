class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        sorted_diff = sorted(costs , key = lambda x : x[0] - x[1])

        print(sorted_diff) 

        diffA = diffB = 0
        for i in range(len(costs)//2):
            diffA += sorted_diff[i][0] 
        for j in range(len(costs)//2, len(costs)):
            diffB += sorted_diff[j][1]
        return diffA + diffB