class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def getAverage(x, y):
            total = 0
            count = 0
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    newX = x + i
                    newY = y + j
                    
                    if newX < 0 or newX >= len(img):
                        continue
                    if newY < 0  or newY >= len(img[0]):
                        continue
                    
                    total += img[newX][newY]
                    count += 1
            return total // count
        
        result = []
        for i in range(len(img)):
            currRow = []
            for j in range(len(img[i])):
                currAvg = getAverage(i, j)
                currRow.append(currAvg)
            result.append(currRow)
        
        return result