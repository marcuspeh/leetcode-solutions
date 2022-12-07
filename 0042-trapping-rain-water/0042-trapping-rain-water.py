class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        
        for i in range(len(height)):
            h = height[i]
            
            while stack and stack[-1][0] < h:
                temp = stack.pop()
                if not stack:
                    break
                result += (i - stack[-1][1] - 1) * (min(h, stack[-1][0]) - temp[0])
                
            stack.append((h, i))
        return result
                
        