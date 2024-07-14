class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        curr = {}
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                stack.append(curr)
                curr = {}
                i += 1
                continue
            
            if formula[i] == ")":
                i += 1
                multiplier, i = self.getMultiplier(formula, i)
                for key in curr.keys():
                    curr[key] *= multiplier
                
                if stack:
                    prev = stack.pop()
                    for key, value in prev.items():
                        if key not in curr:
                            curr[key] = 0
                        curr[key] += value
                continue
                
            symbol, i = self.getSymbol(formula, i)
            multiplier, i = self.getMultiplier(formula, i)
            if symbol not in curr:
                curr[symbol] = 0
            curr[symbol] += multiplier
        
        while stack:
            prev = stack.pop()
            for key, value in prev.items():
                if key not in curr:
                    curr[key] = 0
                curr[key] += value
        
        result = list(sorted([(x, y) for x, y in curr.items()]))
        result = list(map(lambda x: f"{x[0]}" if x[1] == 1 else f"{x[0]}{x[1]}", result))
        return "".join(result)
            
    def getSymbol(self, s, index):
        symbol = s[index]
        index += 1
        while index < len(s) and s[index].islower():
            symbol += s[index]
            index += 1
        return symbol, index
                
    def getMultiplier(self, s, index):
        number = 0
        while index < len(s) and s[index].isnumeric():
            number = number * 10 + int(s[index])
            index += 1
        
        if number == 0:
            number = 1
        return number, index
            
                    
            