class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        arr = [-1]*n
        stack = []
        # dic = defaultdict(int)
        for i in range(n):
            while stack and nums[i] > stack[-1][0]:
                popped = stack.pop()
                arr[popped[1]] = nums[i]
            
            stack.append((nums[i], i))

        for i in range(n):
            while stack and nums[i] > stack[-1][0]:
                popped = stack.pop()
                arr[popped[1]] = nums[i]
            
        return arr