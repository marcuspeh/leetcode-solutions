class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowedDict = {}
        for allow in allowed:
            below = allow[:2]
            top = allow[2]
            if below not in allowedDict:
                allowedDict[below] = set()
            allowedDict[below].add(top)
        
        return self.dfs(bottom, allowedDict)
        
    def dfs(self, layer, allowed):
        if len(layer) == 1:
            return True
        
        combi = [""]
        for i in range(len(layer) - 1):
            nextPair = layer[i] + layer[i + 1]
            if nextPair not in allowed:
                return False
            
            newCombi = []
            for temp in combi:
                for char in allowed[nextPair]:
                    newCombi.append(temp + char)
            combi = newCombi
        
        for nextLayer in combi:
            if not nextLayer:
                continue
            if self.dfs(nextLayer, allowed):
                return True
        
        return False