# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    matrix: List[List[int]]
    cols: int
    rows: int
    def matrix_to_index(self, row, col) -> int:
        return row * self.cols + col

    def index_to_matrix(self, index: int) -> List[int]:
        row = index // self.cols
        col = index % self.cols
        return [row, col]

    def binary_search_mod(
            self,
            target: int,
            start:int=0,
            end:int=None
    ) -> bool:
        if self.cols*self.rows == 0:
            return False
        if self.cols*self.rows == 1:
            return True if self.matrix[0][0] == target else False
        if end is None:
            end = self.cols*self.rows - 1
        if start < 0 or end >= self.cols*self.rows:
            return False
        if end - start == 0:
            r, c = self.index_to_matrix(start)
            return True if self.matrix[r][c] == target else False
        pivot = start + (end - start) // 2
        while True:
            r, c = self.index_to_matrix(pivot)
            if target == self.matrix[r][c]:
                return True
            if target < self.matrix[r][c]:
                return self.binary_search_mod(target, start, pivot)
            else:
                return self.binary_search_mod(target, pivot+1, end)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.matrix = matrix
        self.cols = len(matrix[0])
        self.rows = len(matrix)
        return self.binary_search_mod(target)

if __name__ == "__main__":
    sol = Solution()
    assert sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
    assert not sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)