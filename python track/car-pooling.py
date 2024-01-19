class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = [0]*(max(trips, key= lambda x:x[2])[2] + 1)
        n = len(ans)
        print(n)
        for trip in trips:
            numPassengers, start, dest = trip
            ans[start - 1] += numPassengers
            ans[dest - 1] -= numPassengers
            
        for i in range(n):
            ans[i] += ans[i-1]
            if ans[i] > capacity:
                return False     
        return True
        
        