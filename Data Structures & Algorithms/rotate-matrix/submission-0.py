class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 90° clockwise = transpose + reverse each row
#         The important part is the transpose. We swap:

# matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


        n = len(matrix)
            # Step 1: Transpose
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()