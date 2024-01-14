class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k
        res = []
        leng = len(blocks) - k + 1
        for l in range(leng):
            i = l
            count = 0
            while i < l+k:
                if blocks[i] =='W':
                    count += 1
                i += 1
            res.append(count)
            # print(l, leng)
            # if blocks[l] == 'W':
            #     count += 1
        return min(res)
            