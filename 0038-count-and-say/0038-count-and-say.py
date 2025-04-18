class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            res = self.process(res)

        return res

    def process(self, prev):
        result = []
        i = 0
        while i < len(prev):
            curr = prev[i]
            count = 1
            i += 1

            while i < len(prev) and prev[i] == curr:
                count += 1
                i += 1

            result.append(str(count))
            result.append(curr)
        return "".join(result)