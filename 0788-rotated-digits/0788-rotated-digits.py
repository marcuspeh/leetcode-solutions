class Solution:
    def rotatedDigits(self, n: int) -> int:
        similar = {0, 1, 8}
        notSimilar = {2, 5, 6, 9}
        
        stack = []
        for number in similar:
            if 0 < number <= n:
                stack.append((number, False))
        for number in notSimilar:
            if 0 < number <= n:
                stack.append((number, True))

        count = 0
        while stack:
            curr, isDiff = stack.pop()
            if isDiff:
                count += 1

            curr *= 10
            for number in similar:
                newNumber = curr + number
                if 0 < newNumber <= n:
                    stack.append((newNumber, isDiff))
            for number in notSimilar:
                newNumber = curr + number
                if 0 < newNumber <= n:
                    stack.append((newNumber, True))
            
        return count


