class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        size = len(arr)
        count = 0
        prefix = 0

        count_map = defaultdict(int)
        count_map[0] = 1
        total_map = defaultdict(int)

        for i in range(size):
            prefix ^= arr[i]

            count += count_map[prefix] * i - total_map[prefix]

            total_map[prefix] += i + 1
            count_map[prefix] += 1

        return count