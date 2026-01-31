class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        idx = bisect.bisect_right(letters, target)
        
        # Use modulo so that if idx == len(letters), it wraps to 0
        return letters[idx % len(letters)]