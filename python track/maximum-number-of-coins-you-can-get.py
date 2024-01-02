class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #alice = []
        #myCoins = []
        #bob =[]
        n = len(piles)
        piles.sort(reverse = True)
        slices = []
        slices.extend(piles[:n - (n//3)])
        #print(slices)
        _sum = 0
        i = 1
        while i <= len(slices)-1:
            _sum += slices[i]
            i+= 2
        return _sum
        """if len(piles)== 0:
                break
            else:
                _max = max(piles)
                alice.append(_max)
                piles.pop(piles.index(_max))
                _max = max(piles)
                myCoins.append(_max)
                piles.pop(piles.index(_max))
                _max = max(piles)
                bob.append(_max)
                piles.pop(piles.index(_max))"""
            
            #print(piles[n//3:(2*n)//3])
            #_sum = sum(piles[n//3:(2*n)//3])
        return sum(myCoins)