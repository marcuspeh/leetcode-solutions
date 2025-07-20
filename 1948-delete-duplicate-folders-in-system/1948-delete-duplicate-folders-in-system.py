class Node:
    def __init__(self, folder, isRoot=False):
        self.folder = folder
        self.isRoot = isRoot
        self.parent = None
        self.children = {}
        self.hash = ""
    
    def add(self, folder, isRoot=False):
        if folder not in self.children:
            self.children[folder] = Node(folder)
            self.children[folder].parent = self
        if isRoot:
            self.children[folder].isRoot = isRoot
        return self.children[folder]

    def hashNodes(self, hashCount):
        if len(self.children) == 0:
            return str(hash(self.folder))
        
        ordered = sorted(list(self.children.keys()))
        for item in ordered:
            self.hash += self.children[item].hashNodes(hashCount)
            self.hash = str(hash(self.hash))
        
        if self.hash not in hashCount:
            hashCount[self.hash] = 0
        hashCount[self.hash] += 1

        return str(hash(self.folder + self.hash))
    
    def removeDuplicate(self, hashCount):
        if self.hash not in hashCount:
            return
        
        if hashCount[self.hash] > 1:
            if self.folder in self.parent.children:
                del self.parent.children[self.folder]
            return

        for child in list(self.children.values()):
            child.removeDuplicate(hashCount)

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node("/")
        for path in paths:
            curr = root
            for i in range(len(path)):
                folder = path[i]
                curr = curr.add(folder, i == len(path) - 1)

        hashCount = {}
        root.hashNodes(hashCount)
        root.removeDuplicate(hashCount)
    
        result = []
        stack = [(root, tuple())]

        while stack:
            curr, prevPath = stack.pop()
            currPath = prevPath
            if curr.folder != "/":
                currPath = currPath + (curr.folder,)
            if curr.isRoot:
                result.append(currPath)
            
            for child in curr.children.values():
                stack.append((child, currPath))
        
        return result
