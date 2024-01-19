class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        ans = [0]*(n+1)
        for booking in bookings:
            first, last, seats = booking
            ans[first - 1] += seats
            ans[last] -= seats
        
        for i in range(1, n):
            ans[i] += ans[i-1]

        ans.pop()

        return ans

        """
        brute force
        ans = [0]*n
        for i in range(len(bookings)):
            first = bookings[i][0] - 1
            last = bookings[i][1]
            for j in range(first, last):
                ans[j] += bookings[i][-1]
        return ans"""