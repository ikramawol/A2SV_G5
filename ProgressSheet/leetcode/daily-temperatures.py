class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0]*n

        monoStack = []
        
        for i in range(n-1, -1, -1):
            while monoStack and temp[i] >= monoStack[-1][0]:
                monoStack.pop()
            if monoStack:
                ans[i] = monoStack[-1][1] - i
            monoStack.append((temp[i], i))
        return ans
            
