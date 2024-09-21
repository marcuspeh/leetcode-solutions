class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def helper():
            nonlocal result
            if not result:
                return
            
            prev = result[-1]
            for i in range(10):
                curr = prev * 10 + i
                if curr > n:
                    break
                result.append(curr)
                helper()
        for i in range(1, 10):
            if i > n:
                break
            result.append(i)
            helper()
        return result