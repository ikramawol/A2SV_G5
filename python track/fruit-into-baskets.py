class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r = 0, 0
        max_num = 0
        fruits_count = defaultdict(int)

        for r in range(len(fruits)):
            fruits_count[fruits[r]] += 1
            while len(fruits_count) > 2:
                fruits_count[fruits[l]] -= 1
                if fruits_count[fruits[l]] == 0:
                    del fruits_count[fruits[l]]
                l += 1
            max_num = max(max_num, r - l + 1)
            # while fruits[l] != fruits[r]:
            #     if fruits[r+1] not in fruits[l:r+1]:
            #         max_num = max(max_num, r - l + 1)
            #         break
            #     l += 1
        return max_num