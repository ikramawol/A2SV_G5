class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        even_sum = sum(num for num in nums if num % 2 == 0)
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            ans.append(even_sum)
        return ans