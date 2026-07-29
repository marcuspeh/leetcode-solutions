class Solution:
    def comb(self, n, m, k):
        res = 1
        m = min(m, n - m)

        for i in range(1, m + 1):
            res = res * (n - i + 1) // i
            if res > k:
                return res

        return res

    def perm(self, bucket, rem, k):
        ways = 1
        for i in range(26):
            if bucket[i] == 0:
                continue

            ways *= self.comb(rem, bucket[i], k)
            if ways > k:
                return ways
            rem -= bucket[i]

        return ways

    def smallestPalindrome(self, s: str, k: int) -> str:
        bucket = [0] * 26
        for char in s:
            bucket[ord(char) - ord('a')] += 1
        
        middle = None
        count = 0
        for i in range(26):
            if bucket[i] % 2:
                middle = chr(ord('a') + i)
            bucket[i] //= 2
            count += bucket[i]

        if self.perm(bucket, count, k) < k:
            return ""
        
        result = []
        while count:
            count -= 1
            for i in range(26):
                if bucket[i] == 0:
                    continue

                bucket[i] -= 1
                combi = self.perm(bucket, count, k)
                if combi >= k:
                    result.append(chr(ord('a') + i))
                    break
                bucket[i] += 1
                
                k -= combi
        
        firstHalf = "".join(result)
        secondHalf = "".join(result[::-1])
        if middle:
            return firstHalf + middle + secondHalf
        return firstHalf + secondHalf