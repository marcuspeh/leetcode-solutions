class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len(expression) == 0:
            return []
        if len(expression) == 1:
            return [int(expression)]
        if len(expression) == 2 and expression.isdigit():
            return [int(expression)]
        
        result = []
        for i in range(len(expression)):
            if expression[i].isdigit():
                continue
            
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i + 1:])
            
            if expression[i] == "+":
                operation = lambda x, y: x + y
            elif expression[i] == "-":
                operation = lambda x, y: x - y
            else:
                operation = lambda x, y: x * y
            
            for leftN in left:
                for rightN in right:
                    result.append(operation(leftN, rightN))
        
        return result