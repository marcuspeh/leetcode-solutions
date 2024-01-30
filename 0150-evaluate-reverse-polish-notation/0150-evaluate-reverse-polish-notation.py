class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "/": lambda x, y: int(x / y),
            "*": lambda x, y: x * y,
        }
        
        lastToken = tokens.pop()
        if lastToken not in operations:
            return int(lastToken)
        operation = operations[lastToken]
        right = self.evalRPN(tokens)
        left = self.evalRPN(tokens)
        return operation(left, right)