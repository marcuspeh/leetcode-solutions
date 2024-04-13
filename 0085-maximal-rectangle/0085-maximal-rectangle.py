class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        preorder = [0 for _ in range(len(matrix[0]) + 1)]
        
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '0':
                    preorder[i] = 0
                    continue
                preorder[i] += 1
            
            result = max(result, self.calculateMaxInPreorder(preorder))
            
        return result

        
    def calculateMaxInPreorder(self, preorder):
        stack = [-1]
        result = 0
        
        for i in range(len(preorder)):
            currHeight = preorder[i]
            while stack and preorder[stack[-1]] > currHeight:
                prevIdx = stack.pop()
                prevHeight = preorder[prevIdx]
                result = max(result, (i - stack[-1] - 1) * prevHeight)
            stack.append(i)
        return result