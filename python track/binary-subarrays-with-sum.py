class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = prefix = 0
        counter = defaultdict(int)
        counter[0] = 1

        for num in nums:
            prefix += num
            if prefix - goal in counter:
                ans += counter[prefix - goal]

            counter[prefix] += 1
        return ans
        # n = len(nums)
        # ans = [0]*(n + 1)
        # tot = 0
        # for i in range(1, n+1):
        #     tot += nums[i-1]
        #     ans[i] += tot
        # print(ans)
        # return 0