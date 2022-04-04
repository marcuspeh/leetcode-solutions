class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        def helper(image, sr, sc, orgColor):
            if sr < 0 or sr >= len(image):
                return
            if sc < 0 or sc >= len(image[0]):
                return
            
            if image[sr][sc] != orgColor:
                return
            
            image[sr][sc] = newColor
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for r, c in directions:
                helper(image, sr + r, sc + c, orgColor)
                
        helper(image, sr, sc, image[sr][sc])
        
        return image
            