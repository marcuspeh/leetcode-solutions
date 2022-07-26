class Solution:
    def calculate(self, s: str) -> int:
        parsed = []
        curr = ''
        op = '+'
        
        for i in s:
            if i in ['+', '-', '/', '*']:
                if op == '+':
                    parsed.append(int(curr))
                elif op == '-':
                    parsed.append(-int(curr))
                elif op == "/":
                    prev = parsed.pop()
                    parsed.append(int(prev / int(curr)))
                elif op == '*':
                    prev = parsed.pop()
                    parsed.append(prev * int(curr))
                curr = ''
                op = i
            elif i.isnumeric():
                curr += i
        print(parsed)  
        if op == '+':
            parsed.append(int(curr))
        elif op == '-':
            parsed.append(-int(curr))
        elif op == "/":
            prev = parsed.pop()
            parsed.append(int(prev / int(curr)))
        elif op == '*':
            prev = parsed.pop()
            parsed.append(prev * int(curr))
        
        return sum(parsed)
        
        