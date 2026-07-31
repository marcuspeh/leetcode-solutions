class Solution:
    def minimumPushes(self, word: str) -> int:
        count = len(word)
        result = 0
        batch = 1

        while count > 0:
            currBatchSize = min(8, count)
            result += batch * currBatchSize
            count -= currBatchSize
            batch += 1

        return result
