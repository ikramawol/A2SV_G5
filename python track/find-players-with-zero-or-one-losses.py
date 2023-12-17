class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losser = {}
        winners = {}
        lossers = set()
        winner = set()

        for win, loss in matches:
            losser[loss] = losser.get(loss, 0)+1
            lossers.add(loss)
            winner.add(win)
        intersection = (winner & lossers)
        winner = winner - intersection
        print(winner)
        """for win, _ in matches:
            if win not in losser.keys():
                winner.add(win)
            #winners[win] = winners.get(win, 0)+1"""


        lossers = [key for key, val in losser.items() if val == 1]
        """for key, val in winners.items():
            if key not in losser.keys():
                winner.append(key)"""
        print(lossers)
        print(losser)
        return [sorted(winner), sorted(lossers)]