class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        duplicate = defaultdict(int)

        l, ans = 0, float('inf')

        for r in range(len(cards)):
            duplicate[cards[r]] += 1

            if duplicate[cards[r]] == 2:
                while cards[r] != cards[l]:
                    duplicate[cards[l]] -= 1
                    l += 1
                ans = min(ans, r - l + 1)
                duplicate[cards[l]] -= 1
                l += 1

        return ans if ans != float('inf') else -1



        # duplicat = Counter(cards.copy())
        
        # for key, val in dict(duplicat).items():
        #     if val == 1:
        #         del duplicat[key]
        # print(duplicat)
        # if not duplicat:
        #     return -1
        # _max = l = 0
        # r = 1
        # while r < len(cards):
        #     count = 0
        #     if duplicat[cards[l]] > 1:
        #         while cards[r] == cards[l]:
        #             count = r - l + 1

        #             l += 1
        #     _max = min(_max, count)
        #     r += 1
           
        # return _max
        
