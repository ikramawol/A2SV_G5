class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        ans = prefix = 0
        counter = defaultdict(int)
        counter[0] = 1

        for num in nums:
            prefix += num
            if prefix % k in counter:
                ans += counter[prefix % k]
        
            counter[prefix % k] += 1
        print(counter)
        return ans
        """
        Brute Force
        prefix = count = 0
        for i in range(len(nums)):
            prefix = 0
            for j in range(i, len(nums)):
                prefix += nums[j]
                if prefix % k == 0:
                    count += 1
        return count"""