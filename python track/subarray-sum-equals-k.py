class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = prefix = 0
        counter = defaultdict(int)
        counter[0] = 1

        for num in nums:
            prefix += num
            if prefix - k in counter:
                ans += counter[prefix - k]

            if prefix not in counter:
                counter[prefix] = 1

            else:
                counter[prefix] += 1

        return ans