# https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=simulation
from typing import List


class Solution:
    matrix: List[List[int]]
    w: int
    h: int
    def _recursive_search(self, result: List[int], row: int = 0, col: int = 0):
        w = self.w - 2 * col
        h = self.h - 2 * row
        if w <= 0 or h <= 0:
            return
        i, j = col, row
        for i in range(col, col+w):
            result.append(self.matrix[row][i])
        for j in range(row + 1, row+h):
            result.append(self.matrix[j][i])
        if h>1:
            for i in range(col+w-2, col - 1, -1):
                result.append(self.matrix[j][i])
        if w>1:
            for j in range(row+h-2, row, -1):
                result.append(self.matrix[j][i])
        self._recursive_search(result, row+1, col+1)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        self.matrix = matrix
        self.w = len(self.matrix[0])
        self.h = len(self.matrix)
        self._recursive_search(result)
        return result

if __name__ == '__main__':
    sol = Solution()
    assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert sol.spiralOrder([[1]]) == [1]
    assert sol.spiralOrder([[1,2]]) == [1,2]
    assert sol.spiralOrder([[1],[2]]) == [1,2]
    assert sol.spiralOrder([[1,2],[3,4],[5,6],[7,8]]) == [1,2,4,6,8,7,5,3]
    assert sol.spiralOrder([[1,2,3,4],[5,6,7,8]]) == [1,2,3,4,8,7,6,5]