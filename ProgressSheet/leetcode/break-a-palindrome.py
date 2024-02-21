class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        palindrome = list(palindrome)
        n = len(palindrome)

        if n == 1:
            return ""       

        for i in range(n):
            if i == n//2:
                continue
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return "".join(palindrome)
            
        palindrome[-1] = 'b'
        return "".join(palindrome)
