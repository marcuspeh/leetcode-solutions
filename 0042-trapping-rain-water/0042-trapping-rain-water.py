class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # (height, index)
        result = 0
        
        for index in range(len(height)):
            currHeight = height[index]
            
            while stack and stack[-1][0] < currHeight:
                prevHeight, prevIndex = stack.pop()
                if not stack:
                    break
                result += (min(currHeight, stack[-1][0]) - prevHeight) * (index - stack[-1][-1] - 1)
                
            stack.append((currHeight, index))
        
        return result