class Wrapper:
    def __init__(self, word):
        self.word = word
        self.currSet = ""
        self.index = 0
    
    def takeNextSet(self):
        if self.index < len(self.currSet):
            return
        
        if not self.word:
            return
        
        self.currSet = self.word.pop(0)
        self.index = 0
    
    def getNext(self):
        self.takeNextSet()
        if not self.hasNext():
            return ""
        
        result = self.currSet[self.index]
        self.index += 1
        return result
    
    def hasNext(self):
        self.takeNextSet()
        return self.index < len(self.currSet)
    
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1Wrapper = Wrapper(word1)
        word2Wrapper = Wrapper(word2)
        
        while word1Wrapper.hasNext() and word2Wrapper.hasNext():
            currChar1 = word1Wrapper.getNext()
            currChar2 = word2Wrapper.getNext()
            
            print(currChar1, currChar2)
            if currChar1 != currChar2:
                return False
        
        return not (word1Wrapper.hasNext() or word2Wrapper.hasNext())