class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bitX = bin(x)[2:]
        bitN = bin(n - 1)[2:]

        result = []
        i = len(bitX) - 1
        j = len(bitN) - 1
        while i >= 0 and j >= 0:
            if bitX[i] == "1":
                result.append("1")
            else:
                result.append(bitN[j])
                j -= 1
            i -= 1

        while i >= 0:
            result.append(bitX[i])
            i -= 1

        while j >= 0:
            result.append(bitN[j])
            j -= 1
        
        return int("".join(result[::-1]), 2)

            