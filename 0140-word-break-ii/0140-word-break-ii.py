class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def helper(currString, currWords):
            nonlocal result
            if currString == "":
                result.append(" ".join(currWords))
            
            for word in wordDict:
                if currString[:len(word)] != word:
                    continue
                newCurrWords = currWords.copy()
                newCurrWords.append(word)
                helper(currString[len(word):], newCurrWords)
            
        helper(s, [])
        return result