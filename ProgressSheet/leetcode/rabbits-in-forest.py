class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        # print(count)
        
        res = 0
        for i in count:
            if count[i] % (i+1) == 0:
                res += count[i]
            else:
                res += count[i] + (i+1 - (count[i]%(i+1)))
        return res