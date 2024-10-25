class Trie:
    def __init__(self, val):
        self.val = val
        self.nextNodes = {}
        self.isEnd = False
    
    def add(self, paths, idx=0):
        path = paths[idx]        
        if path not in self.nextNodes:
            self.nextNodes[path] = Trie(path)
            
        if idx == len(paths) - 1:
            self.nextNodes[path].isEnd = True
            return
        
        return self.nextNodes[path].add(paths, idx + 1)
        
    def getPath(self):
        if self.isEnd:
            return [[self.val]]
    
        result = []
        for nextNode in self.nextNodes.values():
            for path in nextNode.getPath():
                path.append(self.val)
                result.append(path)
                
        return result

        
class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        root = Trie("")
        for folder in folders:
            paths = folder.split("/")
            root.add(paths, 1)
        
        result = root.getPath()
        for i in range(len(result)):
            result[i] = "/".join(result[i][::-1])
        return result
        
        