class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        scoreMap = {}
        for i in range(len(score)):
            scoreMap[chr(ord('a') + i)] = score[i]
        
        wordMap = {}
        for word in words:
            score = 0
            for character in word:
                score += scoreMap[character]
            wordMap[word] = score
        
        letterCount = {}
        for letter in letters:
            if letter not in letterCount:
                letterCount[letter] = 0
            letterCount[letter] += 1
        
        def helper(words, letterCount):
            if not words:
                return 0
            
            newWords = words[:-1]
            skipLast = helper(newWords, letterCount)
            
            newLetterCount = letterCount.copy()
            for letter in words[-1]:
                if letter not in newLetterCount or newLetterCount[letter] == 0:
                    return skipLast
                newLetterCount[letter] -= 1
            takeLast = helper(newWords, newLetterCount) + wordMap[words[-1]]
            return max(skipLast, takeLast)
            
            
        return helper(words, letterCount)