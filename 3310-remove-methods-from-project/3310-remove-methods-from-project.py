class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        call = {}
        for a, b in invocations:
            if a not in call:
                call[a] = []
            call[a].append(b)
        
        invoke = {k}
        frontier = [k]
        while frontier:
            curr = frontier.pop()
            if curr not in call:
                continue

            for nextNode in call[curr]:
                if nextNode in invoke:
                    continue
                invoke.add(nextNode)
                frontier.append(nextNode)
        
        result = []
        for node in range(n):
            if node in invoke:
                continue

            if node not in call:
                result.append(node)
                continue

            for nextNode in call[node]:
                if nextNode in invoke:
                    return list(range(n))
            result.append(node)
        
        return result

