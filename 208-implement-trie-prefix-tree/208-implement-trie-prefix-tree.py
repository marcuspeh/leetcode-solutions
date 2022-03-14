class Trie:

    def __init__(self, letter="_"):
        self.letter = letter
        self.nextNodes = {}
        self.isLetter = False

    def insert(self, word: str, index=0) -> None:
        if index == len(word):
            self.isLetter = True
            return
        
        character = word[index]
        
        if character in self.nextNodes:
            self.nextNodes[character].insert(word, index + 1)
        else:
            newNode = Trie(character)
            self.nextNodes[character] = newNode
            newNode.insert(word, index + 1)
            
    def searchPrefix(self, word):
        curr = self
        
        for w in word:
            if w in curr.nextNodes:
                curr = curr.nextNodes[w]
            else:
                return None
        
        return curr        
    
    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node != None and node.isLetter
        

    def startsWith(self, prefix: str) -> bool:   
        node = self.searchPrefix(prefix)
        return node != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)