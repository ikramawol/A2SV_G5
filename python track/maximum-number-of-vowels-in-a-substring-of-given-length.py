class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, _max, count  = 0, 0, 0
        n = len(s)
        vowel = {'a', 'e', 'i', 'o', 'u'}
        
        for r in range(n):
            if s[r] in vowel:
                count += 1
            if r-l+1 > k:
                if s[l] in vowel:
                    count -= 1
                l += 1
            _max = max(_max, count)
        return _max

    
        """
        vowel_counter1 = 0
        for l in range(n-k+1):
            r = l + k - 1
            vowel_counter = Counter(char for char in s[l:r+1] if char in vowel)
            vowel_counter1 = max(sum(vowel_counter.values()), vowel_counter1)
        return vowel_counter1"""

