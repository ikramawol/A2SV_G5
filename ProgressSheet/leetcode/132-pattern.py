class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        left = []
        min_r  = inf
        for num in nums:
            left.append(min_r)
            min_r = min(min_r, num)            

        for i in range(len(nums)-1, -1, -1):
            
            while stack and stack[-1] < nums[i]:
                right = stack.pop()

                if right > left[i]:
                    return True
            
            stack.append(nums[i])

        return False