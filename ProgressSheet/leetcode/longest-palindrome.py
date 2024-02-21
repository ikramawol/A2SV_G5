class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)

        oddCount = 0
        res = sum(count.values())
        for i in count:
            if count[i] % 2 != 0:
                oddCount += 1
        if oddCount > 1:
            res -= oddCount - 1
            
        return res
