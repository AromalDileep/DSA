class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        
        if target >= letters[-1]:
            return letters[0]

        return letters[bisect.bisect_right(letters, target)]
            
