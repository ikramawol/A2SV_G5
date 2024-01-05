class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                if people[r] <= limit:
                    count += 1
                r -= 1
            #print(people[r])
        return count
        """while l <= r:
            if people[l] + people[r] > limit:
                
                    count += 1
                r -= 1
            elif people[l] + people[r] > limit and people[r] < limit:
                
                r -= 1
            elif people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
        return count"""
            

