class Solution:
    def balancedString(self, s: str) -> int:
        # The approch is count the occurance of the four
        # chars and try to make every occurance of the chars 
        # less than the target then taking the min of r-l+1
        n = len(s)
        counter = Counter(s)
        l , res = 0, float('inf')
        target = n//4

        for r in range(n):
            counter[s[r]] -= 1
            
            while l < n and counter['Q'] <= target and counter['W'] <= target and counter['E'] <= target and counter['R'] <= target:
                res = min(res, r - l + 1)
                counter[s[l]] += 1
                l += 1
        return res