class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}
        vowelCnt = 0
        consonantCnt = 0
        for char in word:
            if char in vowel:
                vowelCnt += 1
                continue
            if char.isalpha():
                consonantCnt += 1
                continue
            if char.isdigit():
                continue
            return False

        return consonantCnt > 0 and vowelCnt > 0 