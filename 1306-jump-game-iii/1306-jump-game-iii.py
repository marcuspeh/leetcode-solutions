class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        stack = [start]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            
            right = curr + arr[curr]
            if right < len(arr) and right not in visited:
                if arr[right] == 0:
                    return True

                stack.append(right)

            left = curr - arr[curr]
            if left >= 0 and left not in visited:
                if arr[left] == 0:
                    return True
                
                stack.append(left)
        
        return False
