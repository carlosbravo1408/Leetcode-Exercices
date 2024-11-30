# https://leetcode.com/problems/valid-sudoku/
from typing import List, Tuple


class Solution:
    def _valid_row(self, board: List[List[str]], row: int) -> bool:
        values = set()
        for r in board[row]:
            if r == '.':
                continue
            if r not in values:
                values.add(r)
            else:
                return False
        return True

    def _valid_column(self, board: List[List[str]], column: int) -> bool:
        values = set()
        for c in board:
            if c[column] == '.':
                continue
            if c[column] not in values:
                values.add(c[column])
            else:
                return False
        return True

    def _valid_subgrid(self, board: List[List[str]], subgrid: Tuple[int, int]) -> bool:
        m = 3
        values = set()
        for i in range(subgrid[0]*m, subgrid[0]*m+3):
            for j in range(subgrid[1]*m, subgrid[1]*m+3):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in values:
                    values.add(board[i][j])
                else:
                    return False
        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        columns = [self._valid_row(board, c) for c in range(9)]
        rows = [self._valid_column(board, c) for c in range(9)]
        subgrids = [self._valid_subgrid(board, (i,j)) for i in range(3) for j in range(3)]
        return all(columns + rows + subgrids)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        data = set()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == '.':
                    continue
                if (i, element) in data or (element, j) in data or (i//3, j//3, element) in data:
                    return False
                data.add((i//3, j//3, element))
                data.add((i, element))
                data.add((element, j))
        return True

if __name__ == "__main__":
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert solution.isValidSudoku(board)