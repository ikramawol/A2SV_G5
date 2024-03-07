class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = max(nums)

        def helper(mid):
            _sum = 0
            for i in range(len(nums)):
                _sum += ceil(nums[i]/mid)
            return _sum
        
        while left + 1 < right:
            mid = (left + right)//2
            if helper(mid) <= threshold:
                right = mid 
            else:
                left = mid
        return right