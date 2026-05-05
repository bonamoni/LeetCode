class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def canWeplace(row, col, mat):
            r, c = row, col
            
            # top-left diagonal
            while r >= 0 and c >= 0:
                if mat[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            
            # same column
            r = row
            while r >= 0:
                if mat[r][col] == "Q":
                    return False
                r -= 1
            
            # top-right diagonal
            r, c = row, col
            while r >= 0 and c < n:
                if mat[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            
            return True
        
        def backtrack(row, mat):
            if row == n:
                return 1   # found one valid solution
            
            count = 0
            for col in range(n):
                if canWeplace(row, col, mat):
                    mat[row][col] = "Q"
                    count += backtrack(row + 1, mat)
                    mat[row][col] = "."
            
            return count
        
        # create board
        mat = [["."] * n for _ in range(n)]
        
        return backtrack(0, mat)
        
        