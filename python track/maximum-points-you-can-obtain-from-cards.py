class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        leng = len(cardPoints)

        window_size = leng - k
        window = sum(cardPoints[:window_size])
        
        min_point = window
        for i in range(window_size, leng):
            
            window -= cardPoints[i - window_size] 
            window += cardPoints[i]
    
            min_point = min(min_point, window)
            
        return total - min_point