class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        width = len(box[0])
        height = len(box)
        
        result = [["." for _ in range(height)] for _ in range(width)]
        for i in range(height):
            newHeight = width - 1
            newWidth = height - i - 1
            for j in range(width - 1, -1, -1):
                curr = box[i][j]
                
                if curr == ".": 
                    continue
                
                if curr == "*":
                    newHeight = j
                
                result[newHeight][newWidth] = curr
                newHeight -= 1
        
        return result
                