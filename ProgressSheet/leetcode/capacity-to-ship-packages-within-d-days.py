class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)

        def validator(capacity):
            _sum, dCount = 0, 0

            for i in range(len(weights)):
                _sum += weights[i]
                if _sum > capacity:
                    dCount += 1
                    _sum = weights[i]
                elif _sum == capacity:
                    dCount += 1
                    _sum = 0
            if _sum > 0:
                dCount += 1

            return dCount
            
        while left <= right:
            mid = (left + right)//2
            d = validator(mid)
            if d > days:
                left = mid + 1
            else:
                right = mid - 1
            
        return left
        