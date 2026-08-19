class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        bitmaps = {}
        for row, seat in reservedSeats:
            if seat == 1 or seat == 10:
                continue
            if row not in bitmaps:
                bitmaps[row] = 0
            
            bitmap = 0x1 << (9 - seat)
            bitmaps[row] |= bitmap
        
        middle = 0x3C
        left = 0xF0
        right = 0x0F
        result = (n - len(bitmaps))  * 2
        for row, bitmap in bitmaps.items():
            leftFree = (bitmap & left) == 0
            rightFree = (bitmap & right) == 0
            middleFree = (bitmap & middle) == 0
            print(row, leftFree, rightFree, middleFree)

            if leftFree or rightFree or middleFree:
                result += 1
            
        return result
            

            
