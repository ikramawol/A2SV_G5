class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_occ = defaultdict(int)
        ans = []
        n = len(s)
        for i in range(n):
            last_occ[s[i]] = i
        curr = 0
        while curr < n:
            end = last_occ[s[curr]]
            j = curr + 1
            while j < end:
                end = max(end, last_occ[s[j]])
                j += 1
            ans.append(end - curr + 1)
            curr =  end + 1
        return ans 