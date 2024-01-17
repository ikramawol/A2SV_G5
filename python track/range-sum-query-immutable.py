class NumArray:

    def __init__(self, nums: List[int]):
        self.ans = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.ans[i+1] = self.ans[i] + nums[i]
        print(self.ans)
    def sumRange(self, left: int, right: int) -> int:

        return self.ans[right+1] - self.ans[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)