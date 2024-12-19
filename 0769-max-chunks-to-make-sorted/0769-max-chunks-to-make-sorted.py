class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        maxElement = 0
        for i in range(len(arr)):
            maxElement = max(arr[i], maxElement)
            if maxElement == i:
                result += 1
        return result