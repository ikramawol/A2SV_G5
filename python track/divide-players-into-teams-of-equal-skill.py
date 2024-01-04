class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1

        ans = 0
        while l < r:
            pair_sum = skill[l] + skill[r]
            if pair_sum == skill[-1] + skill[0]:
                ans += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        return ans
       

