class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        if index < n // 2:
            index = n - index - 1
        n_left = index
        n_right = n - 1 - index
        tri_left = (n_left * (n_left + 1)) // 2
        tri_right = (n_right * (n_right + 1)) // 2
        
        if maxSum <= (tri_right * 2 + n_right + 1):
            return int(math.sqrt(maxSum)) + 1
        
        if maxSum <= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1):
            b = 3 + 2 * n_right
            return int((-b + math.sqrt(b * b - 8 * (tri_right + 1 - n_right * n_right - maxSum))) / 2) + 1 + 1
        
        maxSum -= (tri_left + tri_right + (n_left - n_right) * n_right + n_left + 1)
        return n_left + 1 + 1 + (maxSum // n)