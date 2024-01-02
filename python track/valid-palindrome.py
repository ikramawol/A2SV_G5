class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(l for l in s if l.isalnum()).lower()
        left, right = 0, len(s)-1

        while left in range(len(s)-1):
            if s[left] != s[right]:
                return False
                break
            left += 1
            right -= 1
        return True