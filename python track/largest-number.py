class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(num1, num2):
            num1 = str(num1)
            num2 = str(num2)
            return int(num2+num1) > int(num1+num2)
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        nums = list(map(str, nums))
        return str(int("".join(nums)))
