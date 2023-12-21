class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        no_one = nums.count(1)
        count = 0
        result = {}
        ans = []
        result[0]=no_one
        result[len(nums)] = nums.count(0)
        for i in range(1,len(nums)):
            if nums[i-1] == 0:
                count += 1
            else:
                no_one -=1
            score = count + no_one
            result[i] = score
        
        max_va = max(result.values())

        for key,value in result.items():
            if result[key]==max_va:
                ans.append(key)
        return ans
        
        