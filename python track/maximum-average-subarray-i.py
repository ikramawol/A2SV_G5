class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """r = 0
        _sum,_max = 0, float("-inf")
        """
        
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for l in range(k, len(nums)):
            window_sum = window_sum - nums[l - k] + nums[l]
            max_sum = max(window_sum, max_sum)
            """
            _sum = sum(nums[l:l+k])
            _max = max(_max, _sum)
            """
        return float(max_sum / k)
