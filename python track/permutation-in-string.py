import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        """permutation = defaultdict(int)

        s1 = list(map(str, s1))
        s2 = list(map(str, s2))
     
        
        perms = [''.join(i) for i in itertools.permutations(s1)]

        for i in range(len(perms)):
            permutation[perms[i]] += 0

        r, l = 1, 0
        for l in range(0, len(s2)):
            sub = "".join(s2[l:len(s1)+l])
            if sub in permutation:
                return True
                break
            r += 1
            l += 1
        return False"""
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False

        counter_s1 = Counter(s1)
        #print(counter_s1)
        counter_window = Counter()
        #print(counter_window)

        for i in range(len_s2):
            counter_window[s2[i]] += 1

            if i >= len_s1:
                if counter_window[s2[i - len_s1]] == 1:
                    del counter_window[s2[i - len_s1]]
                else:
                    counter_window[s2[i - len_s1]] -= 1

            if counter_window == counter_s1:
                return True
            print(counter_window)
        return False

        