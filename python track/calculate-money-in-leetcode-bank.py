class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        _sum = 0
        temp = 0
        #tracke the number of iteration 
        for num in range((n+7)/7):
            end = min(7, n-(num*7))
            temp = num+end+1
            #_sum = (temp * (temp+1))/ 2 - (num*(num+1))/2 
            for i in range(num+1, num+end+1):
                _sum += i
        return _sum
        
        