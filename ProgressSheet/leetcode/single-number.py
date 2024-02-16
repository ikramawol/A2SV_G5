class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dic = Counter(nums)
        for key, val in dic.items():
            if val == 1:
                return key
            
              