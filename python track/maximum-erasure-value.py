class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        _sum, _max = 0, 0

        seen = set()
        while r < len(nums):
            
            if nums[r] not in seen:
                _sum += nums[r]
                seen.add(nums[r])
                
            else:
                while nums[l] != nums[r]:
                    seen.remove(nums[l])
                    _sum -= nums[l]
                    l += 1

                l += 1

            r += 1
            _max = max(_max, _sum)
            
        return _max