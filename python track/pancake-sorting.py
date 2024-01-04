class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        k = len(arr)
        def flip(arr,idx,k):
            arr = arr[:idx+1][::-1] + arr[idx+1:]
            arr = arr[:k][::-1]
            return arr

        while k > 1:
            idx = arr.index(k)
            res.append(idx + 1)
            arr = flip(arr, idx, k)
            res.append(k)
            k-=1
        return res
        