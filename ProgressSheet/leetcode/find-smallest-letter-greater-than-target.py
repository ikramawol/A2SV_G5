class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left = -1
        right = len(letters) -1

        # if target =='z' and 'z' not in letters:
        #     return letters[0]
        # if target not in letters:
        #     return letters[bisect_left(letters, target)]
        # elif target in letters:
        #     return letters[bisect_right(letters, target)-1]
        # else:
        #     return letters[0]

        # if target not in letters or letters[-1] < target:
        #     return letters[0]
    
        while left + 1 < right:
            mid = (left + right)//2
            
            if letters[mid] > target:
                right = mid
            else:
                left = mid
 
        if letters[right] <= target:
            return letters[0]
        else:
            return letters[right]
            