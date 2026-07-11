class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {}
        for a, b in edges:
            if a not in edgeMap:
                edgeMap[a] = set()
            edgeMap[a].add(b)

            if b not in edgeMap:
                edgeMap[b] = set()
            edgeMap[b].add(a)
        
        seen = set()
        result = 0
        for i in range(n):
            if i in seen:
                continue

            stack = [i]
            seen.add(i)
            edgeCount = 0
            nodeCount = 0
            while stack:
                curr = stack.pop()
                nodeCount += 1

                if curr not in edgeMap:
                    continue

                edgeCount += len(edgeMap[curr])
                for nextNode in edgeMap[curr]:
                    if nextNode in seen:
                        continue

                    stack.append(nextNode)
                    seen.add(nextNode)

            if (nodeCount) * (nodeCount - 1) == edgeCount:
                result += 1


        return result