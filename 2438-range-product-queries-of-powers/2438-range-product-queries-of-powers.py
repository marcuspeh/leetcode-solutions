class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        powers = []
        curr = 1 << 32
        while curr and n:
            if curr <= n:
                powers.append(curr)
                n -= curr

            curr >>= 1
        
        products = [powers[-1]]
        for i in range(len(powers) - 2, -1, -1):
            products.append(products[-1] * powers[i])
        
        results = []
        for left, right in queries:
            if left == 0:
                results.append(products[right] % MOD)
                continue
            results.append((products[right] / products[left - 1]) % MOD)
        
        return results