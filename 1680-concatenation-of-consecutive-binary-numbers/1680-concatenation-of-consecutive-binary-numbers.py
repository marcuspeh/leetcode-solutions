class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        1,
        10, 11
        100, 101, 110, 111,
        1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111 
        """
        result = 1
        count = 1
        level = 1
        frontier = [1]
        while count < n:
            newFrontier = []
            level += 1
            for curr in frontier:
                for toAdd in [0, 1]:
                    newCurr = (curr << 1) | toAdd
                    newFrontier.append(newCurr)
                    if count >= n:
                        break

                    result = result << level
                    result = result | newCurr
                    result %= 10 ** 9 + 7
                    count += 1

            if count == n:
                break                
            frontier = newFrontier
        
        return result
            