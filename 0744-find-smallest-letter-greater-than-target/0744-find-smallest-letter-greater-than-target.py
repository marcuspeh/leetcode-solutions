class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) 
        while start < end:
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
                continue

            end = mid 
        
        if start == len(letters):
            return letters[0]
        
        return letters[start]