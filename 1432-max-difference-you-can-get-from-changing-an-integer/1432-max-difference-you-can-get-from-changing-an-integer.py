class Solution:
    def maxDiff(self, num: int) -> int:
        a = str(num)
        for i in range(len(a)):
            if a[i] == "9":
                continue

            a = a.replace(a[i], "9")
            break

        b = str(num)
        for i in range(len(b)):
            toReplace = "0"
            if b[i] == b[0]:
                toReplace = "1"
            if b[i] == toReplace:
                continue

            b = b.replace(b[i], toReplace)
            break

        return int(a) - int(b)