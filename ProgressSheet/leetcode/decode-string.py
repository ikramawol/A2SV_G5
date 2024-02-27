class Solution:
    def decodeString(self, s: str) -> str:

        ans = []
        def helper(i):
            arr = []
            # multiplier
            mult = []
            while s[i] != "[":
                mult.append(s[i])
                i += 1
            mult = int("".join(mult))

            i += 1

            word = []
            while s[i] != ']':
                if s[i].isdigit():
                    x = helper(i)
                    word.append(x[0])
                    i = x[1]
                else:
                    word.append(s[i])
                    i += 1

            word = "".join(word)
            arr.append(word*mult)
            # arr.append(helper(i+1))

            return "".join(arr), i+1

        i = 0
        while i < len(s):
            if s[i].isdigit():
                x = helper(i)
                ans.append(x[0])
                i = x[1]
            else:
                ans.append(s[i])
                i += 1
        return ''.join(ans)
