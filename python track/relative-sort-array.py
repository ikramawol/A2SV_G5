class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = Counter(arr1)
        ans = []
        temp = []
        for i in range(len(arr2)):
            ans.extend([arr2[i]]*dic[arr2[i]])
        for i in arr1:
            if i not in arr2:
                temp.append(i)
            temp.sort()
        ans += temp
        return ans
            
        print(ans)