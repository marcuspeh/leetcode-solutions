class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        for i in range(len(mat)):
            row = mat[i]
            for j in range(len(row)):
                if row[j] != row[(j + k) % len(row)]:
                    return False

        return True
