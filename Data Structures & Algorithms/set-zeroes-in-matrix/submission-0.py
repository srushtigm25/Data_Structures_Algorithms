class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        zrows = set()
        zcols = set()


        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zrows.add(r)
                    zcols.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zrows or c in zcols:
                    matrix[r][c] = 0



#                     Time: O(rows × cols)

# You traverse the matrix twice. That is still O(m × n), not O(2mn).

# Space: O(rows + cols)

