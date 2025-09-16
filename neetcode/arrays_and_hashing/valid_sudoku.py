from collections import defaultdict
import json


class Solution:
    def isValidSudoku(board: list[list[str]]) -> bool:
        # valid_nums = [str(x) for x in range(1, 10)]
        rows: list[set] = [set()] * 9
        columns: list[set] = [set()] * 9
        boxes: list[set] = [set()] * 9
        box_mappings: dict[tuple[str], int] = {}

        # box_mappings = (
        #     {(i, j): 1 for i in range(0, 3) for j in range(0, 3)}
        #     | {(i, j): 2 for i in range(0, 3) for j in range(3, 6)}
        #     | {(i, j): 3 for i in range(0, 3) for j in range(6, 9)}
        #     | {(i, j): 4 for i in range(3, 6) for j in range(0, 3)}
        #     | {(i, j): 5 for i in range(3, 6) for j in range(3, 6)}
        #     | {(i, j): 6 for i in range(3, 6) for j in range(6, 9)}
        #     | {(i, j): 7 for i in range(6, 9) for j in range(0, 3)}
        #     | {(i, j): 8 for i in range(6, 9) for j in range(3, 6)}
        #     | {(i, j): 9 for i in range(6, 9) for j in range(6, 9)}
        # )

        # box_mappings = {
        #     (i, j): box_index + 1
        #     for i in range(box_index // 3 * 3, box_index // 3 * 3 + 3)
        #     for j in range(box_index % 3 * 3, box_index % 3 * 3 + 3)
        #     for box_index in range(9)
        # }

        for box_index in range(9):
            i_start = box_index // 3 * 3
            for i in range(i_start, i_start + 3):
                j_start = box_index % 3 * 3
                for j in range(j_start, j_start + 3):
                    assert (i, j) not in box_mappings
                    box_mappings[(i, j)] = box_index + 1

        print(json.dumps({str(k): v for k, v in box_mappings.items()}, indent=2))
        print(len(box_mappings))

        for i in range(9):
            for i in range(9):
                if board[i][j] == ".":
                    continue
                number = board[i][j]
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


Solution.isValidSudoku(board=[])
