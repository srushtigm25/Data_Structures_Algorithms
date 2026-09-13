class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = defaultdict(set)
        # cols = defaultdict(set)
        # sqrs = defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         else:
        #             if (board[r][c] in rows[r]or
        #                 board[r][c] in cols[c] or
        #                 board[r][c] in sqrs[(r//3,c//3)]) :
        #                 return False
        #             rows[r].add(board[r][c])
        #             cols[c].add(board[r][c])
        #             sqrs[(r//3,c//3)].add(board[r][c])
        # return True
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                box = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True

      
     
                


