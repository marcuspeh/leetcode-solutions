class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = []
        
        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            while stack and stack[-1][0] < temp:
                prevTemp, prevI = stack.pop()
                result[prevI] = i - prevI 
                
            stack.append((temp, i))
            
            
        return result