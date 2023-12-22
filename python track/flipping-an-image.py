class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        temp = []
        for rev in image:
            rev.reverse()
            for i in range(len(rev)):
                if rev[i] == 0:
                    rev[i] = 1
                else:
                    rev[i] = 0
            temp.append(rev)
        ans.extend(temp)
        return ans