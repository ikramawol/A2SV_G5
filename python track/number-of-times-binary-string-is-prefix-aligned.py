class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max = count = 0
        for i in range(len(flips)):
            if max < flips[i]:
                max = flips[i]
            if max == i + 1:
                count += 1
        return count
        """arr = [0]*len(flips)
        count = 0
        for i in range(0, len(flips)):
            arr[flips[i]-1] = 1
            #_sort = arr.copy()
            #_sort.sort(reverse = True)
            arr1 = list(map(str, arr))
            arr1 = "".join(arr1)
            if '01' not in arr1:
                count += 1
        return count"""