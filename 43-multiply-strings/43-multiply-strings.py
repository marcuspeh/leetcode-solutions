class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        convert = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        
        result = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1) - 1, -1, -1):
            int1 = convert[num1[i]]
            
            for j in range(len(num2) - 1, -1, -1):
                int2 = convert[num2[j]]
                index = i + j + 1
                
                newNum = int1 * int2 + result[index]
                result[index] = newNum % 10
                result[index - 1] += newNum // 10
                
        if result[0] == 0:
            result.pop(0)
            
        return "".join(map(lambda x: str(x), result))