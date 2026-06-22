class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {}
        characters = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        for char in text:
            if char not in characters:
                continue
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
        
        result = float("inf")
        for char, num in characters.items():
            if char not in counter:
                return 0
            
            result = min(result, counter[char] // num)
        
        return result
