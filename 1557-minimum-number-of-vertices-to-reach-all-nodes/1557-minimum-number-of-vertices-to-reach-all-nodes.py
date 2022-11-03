class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Acyclic -> nodes with no incoming edge can lead to all states
        noIncoming = set(range(n))
        
        for fro, to in edges:
            if to in noIncoming:
                noIncoming.remove(to)
                            
        return list(noIncoming)