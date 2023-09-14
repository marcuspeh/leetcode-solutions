class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        cache = {}
        for start, end in sorted(tickets, reverse=True):
            if start not in cache:
                cache[start] = []
            cache[start].append(end)
        
        result = []
        frontier = ['JFK']
        
        while frontier:
            while frontier[-1] in cache and cache[frontier[-1]]:
                frontier += cache[frontier[-1]].pop(),
            result.append(frontier.pop())
        return result[::-1]
    