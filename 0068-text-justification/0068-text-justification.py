class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr = []
        charCount = 0
        
        for word in words:
            if len(word) + charCount + len(curr) > maxWidth:
                self.formatString(result, curr, maxWidth, charCount)
                curr = []
                charCount = 0
            charCount += len(word)
            curr.append(word)
            
        result.append(" ".join(curr))
        result[-1] += " " * (maxWidth - len(result[-1]))
        return result
            
    def formatString(self, result, curr, maxWidth, charCount):
        spacesCount = maxWidth - charCount
        spaces = len(curr) - 1
        string = ""
        
        for i in range(len(curr)):
            word = curr[i]
            string += word
            if spaces:
                currSpaceCount = math.ceil(spacesCount / spaces)
                string += " " * currSpaceCount
                spaces -= 1
                spacesCount -= currSpaceCount
                
        string += " " * (maxWidth - len(string))
                
        result.append(string)
        
        