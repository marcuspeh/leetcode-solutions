class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            curr = 0
            for char in word:
                curr += weights[ord(char) - ord('a')]
            
            curr %= 26
            result.append(chr(ord('z') - curr))
        
        return "".join(result)