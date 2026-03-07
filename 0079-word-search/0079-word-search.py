class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, ind, board, word):
            if ind == len(word):
                return True
            for r, c in [[1, 0], [0, -1], [0, 1], [-1, 0]]:
                nr = row + r
                nc = col + c
                if (
                    nr >= 0
                    and nr < n
                    and nc >= 0
                    and nc < m
                    and board[nr][nc] == word[ind]
                ):
                    board[nr][nc] = "."
                    if backtrack(nr, nc, ind + 1, board, word):
                        return True
                    board[nr][nc] = word[ind]
            return False

        n = len(board)
        m = len(board[0])
        for row in range(0, n):
            for col in range(0, m):
                if board[row][col] == word[0]:
                    board[row][col] = "."
                    if backtrack(row, col, 1, board, word):
                        return True
                    board[row][col] = word[0]
        return False
