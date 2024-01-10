class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r = 0, 0
        max_length = 0
        unique_char = set()
        while r < len(s):
            if s[r] not in unique_char:
                unique_char.add(s[r])
                r += 1
                max_length = max(max_length, r - l)

            else:
                unique_char.remove(s[l])
                l += 1

        return max_length
     