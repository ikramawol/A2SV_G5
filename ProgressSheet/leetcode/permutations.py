class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()

        def backtrack(path):
            
            if len(path) == len(nums):
                ans.append(path[:])
                
            for i in range(len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    backtrack(path)
                    path.pop()
                    visited.remove(nums[i])


        ans = []
        backtrack([])
        return ans