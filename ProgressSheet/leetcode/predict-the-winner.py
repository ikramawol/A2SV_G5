class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(left, right, Turn):
            if Turn:
                if left == right:
                    return nums[left]
                
                lf = predict(left + 1, right, not(Turn)) + nums[left]
                rt = predict(left, right - 1, not(Turn)) + nums[right]

                return max(lf, rt)
            else:
                if left == right:
                    return nums[right]
                lf = predict(left + 1, right, not(Turn)) - nums[left]
                rt = predict(left, right - 1, not(Turn)) - nums[right]

                return min(lf, rt)

        return predict(0, len(nums) - 1, True) >= 0
        
