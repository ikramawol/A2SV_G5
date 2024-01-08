class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num > 0:
            s = list(map(int,str(num)))
            s.sort()
            print(s)
            if s[0] == 0:
                zero = s.count(0)
                s[0], s[zero] = s[zero], s[0]

            return int("".join(map(str, s)))
        else:
            s = abs(num)
            s = list(map(int,str(s)))
            s.sort(reverse = True)

            return -int("".join(map(str, s)))