class Solution:
    def solveNQueens(self, n):
        def queen(n):
            nonlocal p
            board = [[0 for j in range(n)] for i in range(n)]
            row = 0
            col = [0 for i in range(n)]
            ans = []
            while 0 <= row < n:
                # print(row, col, board)
                if col[row] >= n:
                    col[row] = 0
                    row -= 1
                    board[row][col[row]] = 0
                    for i in range(row+1, n):
                        if board[i][col[row]] == row+1:
                            board[i][col[row]] = 0
                        if i-row+col[row] < n and board[i][i-row+col[row]] == row+1:
                            board[i][i-row+col[row]] = 0
                        if col[row]-i+row >= 0 and board[i][col[row]-i+row] == row+1:
                            board[i][col[row]-i+row] = 0
                    col[row] += 1
                    continue

                if board[row][col[row]] == 0:
                    board[row][col[row]] = 'Q'
                    if row == n-1:
                        ans = board[:]
                        for i in range(n):
                            s = ''
                            for j in range(n):
                                if ans[i][j] != 'Q':
                                    s += '.'
                                else:
                                    s += 'Q'
                            ans[i] = s
                        # print(ans)
                        p.append(ans)
                        board[row][col[row]] = 0
                        col[row] = 0
                        row -= 1
                        board[row][col[row]] = 0
                        for i in range(row+1, n):
                            if board[i][col[row]] == row+1:
                                board[i][col[row]] = 0
                            if i-row+col[row] < n and board[i][i-row+col[row]] == row+1:
                                board[i][i-row+col[row]] = 0
                            if col[row]-i+row >= 0 and board[i][col[row]-i+row] == row+1:
                                board[i][col[row]-i+row] = 0
                        col[row] += 1
                    else:
                        for i in range(row+1, n):
                            if board[i][col[row]] == 0:
                                board[i][col[row]] = row+1
                            if i-row+col[row] < n and board[i][i-row+col[row]] == 0:
                                board[i][i-row+col[row]] = row+1
                            if col[row]-i+row >= 0 and board[i][col[row]-i+row] == 0:
                                board[i][col[row]-i+row] = row+1
                        row += 1
                else:
                    col[row] += 1
        p = []
        queen(n)
        return p
