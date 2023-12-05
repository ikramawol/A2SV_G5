class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        _min = min(salary)
        _max = max(salary)
        
        salary.remove(_min)
        salary.remove(_max)
        
        ave = 0
        _sum = 0
        for i in range(len(salary)):
            _sum += float(salary[i])
        ave = _sum / len(salary)
        return ave