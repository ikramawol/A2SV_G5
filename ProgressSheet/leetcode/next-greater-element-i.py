class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        dic = defaultdict(int)
        stack = []
        ans = []
        for num in nums2:
            while stack and stack[-1] <= num:
                popped = stack.pop()
                dic[popped] = num

            stack.append(num)
        for num in stack:
            dic[num] = -1
        for num in nums1:
            ans.append(dic[num])
        
        return ans
                
            
