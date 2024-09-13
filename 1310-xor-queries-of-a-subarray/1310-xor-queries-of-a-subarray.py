class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        for num in arr:
            if not prefix:
                prefix.append(num)
                continue
            prefix.append(prefix[-1] ^ num)
        
        result = []
        for start, end in queries:
            if start == 0:
                result.append(prefix[end])
                continue
            result.append(prefix[end] ^ prefix[start - 1])
        return result