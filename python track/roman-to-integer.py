class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_value = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        tot = 0
        num = len(s)
        
        for i in range(num-1):
            if roman_value[s[i]] < roman_value[s[i+1]]:
                tot -= roman_value[s[i]]
            else:
                tot += roman_value[s[i]]
        tot += roman_value[s[num-1]]
        return tot