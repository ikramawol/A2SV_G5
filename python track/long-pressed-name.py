class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        l, r = 0, 0

        flag = False
        while l < len(name) and r < len(typed):
            """if name[0] != typed[0]:
                flag = False
                break"""
            if name[l] == typed[r]:
                print(name[l], typed[r])
                flag = True
                l += 1
                r += 1
        
            elif l > 0 and name[l - 1] == typed[r]:
                r += 1
            else:
                flag = False
                break
        while r < len(typed) and name[-1] == typed[r]:
            r += 1

        return flag and l == len(name) and r == len(typed)