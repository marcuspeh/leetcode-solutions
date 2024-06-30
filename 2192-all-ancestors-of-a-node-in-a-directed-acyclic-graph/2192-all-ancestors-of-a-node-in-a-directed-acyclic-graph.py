class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edgeMap = {}
        noStart = {i for i in range(n)}
        for i, j in edges:
            if j not in edgeMap:
                edgeMap[j] = []
            
            if i in noStart:
                noStart.remove(i)
            
            edgeMap[j].append(i)
            
        result = [set() for i in range(n)]
        for i in noStart:
            self.dfs(edgeMap, i, result)
            
        sortedResult = []
        for ancestor in result:
            sortedResult.append(list(sorted(list(ancestor))))
        
        return sortedResult
    
    def dfs(self, edgeMap, curr, result):
        if result[curr]:
            return result[curr].union({curr})
    
        currResult = set()
        if curr in edgeMap:
            for nextNode in edgeMap[curr]:
                currResult.update(self.dfs(edgeMap, nextNode, result))
        
        result[curr] = currResult
        return currResult.union({curr})
        
        