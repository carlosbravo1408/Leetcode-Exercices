# https://leetcode.com/problems/spiral-matrix-ii/?envType=problem-list-v2&envId=simulation
from typing import List


class Solution:
    matrix: List[List[int]]
    w:int
    h: int
    def _recursive_search(self, k: int = 1, row: int = 0, col: int = 0):
        w = self.w - 2 * col
        h = self.h - 2 * row
        if w <= 0 or h <= 0:
            return
        i, j = col, row
        for i in range(col, col + w):
            self.matrix[row][i] = k
            k += 1
        for j in range(row + 1, row + h):
            self.matrix[j][i] = k
            k += 1
        if h > 1:
            for i in range(col + w - 2, col - 1, -1):
                self.matrix[j][i] = k
                k += 1
        if w > 1:
            for j in range(row + h - 2, row, -1):
                self.matrix[j][i] = k
                k += 1
        self._recursive_search(k, row + 1, col + 1)

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.matrix = [[0] * n for _ in range(n)]
        self.w = self.h = n
        self._recursive_search()
        return self.matrix

if __name__ == "__main__":
    sol = Solution()
    assert sol.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]]
    assert sol.generateMatrix(2) == [[1, 2], [4, 3]]
    assert sol.generateMatrix(1) == [[1]]
    assert sol.generateMatrix(4) == [[1,2,3,4],[12,13,14,5],[11,16,15,6],
                                     [10,9,8,7]]
