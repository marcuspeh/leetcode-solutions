class Node:
    def __init__(self, val, isEnd = False):
        self.val = val
        self.isEnd = isEnd
        self.child = {}
        
    def addWord(self, word, index = 0):
        node = self
        for letter in word:
            if letter in node.child:
                node = node.child[letter]
                continue
          
            newNode = Node(letter)
            node.child[letter] = newNode
            node = newNode
        node.isEnd = True
                
class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        self.root.addWord(word)

    def search(self, word: str) -> bool:
        frontier = [self.root]
        for letter in word:
            newFrontier = []
        
            for node in frontier:
                if letter == ".":
                    newFrontier.extend(node.child.values())
                    continue
                    
                if letter not in node.child:
                    continue
                
                newFrontier.append(node.child[letter])
            
            frontier = newFrontier
            
        for letter in frontier:
            if letter.isEnd:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)