class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        
        for word in words:
            if word not in count:
                count[word] = 0
            count[word] += 1
            
        keys = sorted(count.keys())
        
        result = sorted(keys, key=lambda x: count[x], reverse=True)
        
        return result[:k]