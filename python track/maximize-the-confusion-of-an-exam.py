class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        l, r = 0, 0
        true, false = 0, 0
    
        res = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                true += 1
            else:
                false += 1
            while min(true, false) > k:
                if answerKey[l] == 'T':
                    true -= 1
                else:
                    false -= 1
                l+=1
            res = max(res, r - l +1)


        return res