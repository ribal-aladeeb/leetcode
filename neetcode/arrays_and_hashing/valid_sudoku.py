from collections import defaultdict
import json


class Solution:
    def isValidSudoku(board: list[list[str]]) -> bool:
        # valid_nums = [str(x) for x in range(1, 10)]
        rows: list[set] = [set() for _ in range(9)]
        columns: list[set] = [set() for _ in range(9)]
        boxes: list[set] = [set() for _ in range(9)]
        box_mappings: dict[tuple[str], int] = {}

        for box_index in range(9):
            i_start = box_index // 3 * 3
            for i in range(i_start, i_start + 3):
                j_start = box_index % 3 * 3
                for j in range(j_start, j_start + 3):
                    box_mappings[(i, j)] = box_index

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                number = int(board[i][j])
                box_of_interest = boxes[box_mappings[(i, j)]]
                if (
                    number in rows[i]
                    or number in columns[j]
                    or number in box_of_interest
                ):
                    return False
                rows[i].add(number)
                columns[j].add(number)
                box_of_interest.add(number)
        return True


x = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(Solution.isValidSudoku(board=x))
