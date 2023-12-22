class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        _max = max(arr)
        idx=arr.index(_max)

        if len(arr)<3 :
            return False
        if len(arr)-1 == idx or idx == 0:
            return False
        for i in range(idx):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(idx,len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
        return True