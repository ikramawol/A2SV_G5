class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(costs)
        count = 0
        _sum = 0
        for i in range(0, 1):
            for j in range(i, len(costs)):
                if costs[j] < coins:
                    _sum += costs[j]
                    print(_sum)
                    count+=1
                    if _sum > coins:
                        count -= 1
                        break
            else:
                continue
        return count
