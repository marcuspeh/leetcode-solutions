class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        visited = []
        result = [0 for _ in temperatures]
        
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while visited and visited[-1][0] < temp:
                _, idx = visited.pop()
                result[idx] = i - idx
            visited.append((temp, i))
        
        return result
        