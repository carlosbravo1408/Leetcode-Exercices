# https://leetcode.com/problems/sudoku-solver/
# https://www.geeksforgeeks.org/sudoku-backtracking-7/
import copy
import time
from typing import List

digits = set(chr(i) for i in range(49, 58))


class Solution:

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

    def is_valid_insertion(self, board: List[List[str]], row, col, key) -> bool:
        for i in range(9):
            if board[row][i] == key or board[i][col] == key:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == key:
                return False
        return True

    def _backtrack(self, board: List[List[str]]):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in digits:
                        if self.is_valid_insertion(board, row, col, num):
                            board[row][col] = num
                            if self._backtrack(board):
                                return True
                            board[row][col] = '.'
                    return False
        return True

    def _bit_mask(self, board: List[List[str]], row, col) -> int:
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0

        if board[row][col] != '.':
            return self._bit_mask(board, row, col + 1)

        for num in digits:
            if self.is_valid_insertion(board, row, col, num):
                board[row][col] = num
                if self._bit_mask(board, row, col + 1):
                    return True
            board[row][col] = '.'
        return False

    def _cross_hatching_with_backtrack(self, board: List[List[str]]):
        position_input_elements = {}
        remaining_number_of_elements = {}
        graph = {}

        def build_position_and_remaining():
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        if board[i][j] not in position_input_elements:
                            position_input_elements[board[i][j]] = []
                        position_input_elements[board[i][j]].append((i, j))
                        if board[i][j] not in remaining_number_of_elements:
                            remaining_number_of_elements[board[i][j]] = 9
                        remaining_number_of_elements[board[i][j]] -= 1

            for num in digits:
                if num not in position_input_elements:
                    position_input_elements[num] = []
                if num not in remaining_number_of_elements:
                    remaining_number_of_elements[num] = 9

        def build_graph():
            for k, v in position_input_elements.items():
                if k not in graph:
                    graph[k] = {}
                row = set(range(0,9))
                col = set(range(0,9))
                for cord in v:
                    row.remove(cord[0])
                    col.remove(cord[1])

                if len(row) == 0 or len(col) == 0:
                    continue

                for r in row:
                    for c in col:
                        if board[r][c] == '.':
                            if r not in graph[k]:
                                graph[k][r] = []
                            graph[k][r].append(c)

        def fill_matrix(k, keys, r, rows):
            for c in graph[keys[k]][rows[r]]:
                if board[rows[r]][c] != ".":
                    continue
                if self.is_valid_insertion(board, rows[r], c, keys[k]):
                    board[rows[r]][c] = keys[k]
                    if r < len(rows) - 1:
                        if fill_matrix(k, keys, r + 1, rows):
                            return True
                        else:
                            board[rows[r]][c] = '.'
                            continue
                    else:
                        if k < len(keys) - 1:
                            if fill_matrix(k + 1, keys, 0,
                                           list(graph[keys[k + 1]].keys())):
                                return True
                            else:
                                board[rows[r]][c] ='.'
                                continue
                        return True
                board[rows[r]][c] = '.'
            return False

        build_position_and_remaining()
        remaining_number_of_elements = {
            k: v for k, v in sorted(remaining_number_of_elements.items(),
                                    key=lambda item: item[1])
        }
        build_graph()
        key_s = list(remaining_number_of_elements.keys())
        fill_matrix(0, key_s, 0, list(graph[key_s[0]].keys()))

    def solveSudoku(self, board: List[List[str]]) -> None:
        b1 = copy.deepcopy(board)
        t = time.time()
        self._backtrack(b1)
        print(time.time() - t)
        b2 = copy.deepcopy(board)
        t = time.time()
        self._bit_mask(b2, 0, 0)
        print(time.time() - t)
        b3 = copy.deepcopy(board)
        t = time.time()
        self._cross_hatching_with_backtrack(b3)
        print(time.time() - t)


if __name__ == '__main__':
    s = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    s.solveSudoku(board)
    board = [
        [".",".",".",".",".",".",".",".","."],
        [".","9",".",".","1",".",".","3","."],
        [".",".","6",".","2",".","7",".","."],
        [".",".",".","3",".","4",".",".","."],
        ["2","1",".",".",".",".",".","9","8"],
        [".",".",".",".",".",".",".",".","."],
        [".",".","2","5",".","6","4",".","."],
        [".","8",".",".",".",".",".","1","."],
        [".",".",".",".",".",".",".",".","."]
    ]
    s.solveSudoku(board)
    board = [
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]
    ]
    s.solveSudoku(board)