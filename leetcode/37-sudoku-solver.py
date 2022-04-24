from collections import defaultdict, deque
import time

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row,col,square,q = defaultdict(set), defaultdict(set), defaultdict(set), deque()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    q.append((i,j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i//3,j//3)].add(board[i][j])
        
        def dfs():
            if not q:
                return True
            
            curr = q.pop()
            r,c = curr[0], curr[1]
            
            for i in range(1, 10):
                i = str(i)
                if i not in row[r] and i not in col[c] and i not in square[(r//3,c//3)]:
                    print(i)
                    board[r][c] = i
                    row[r].add(i)
                    col[c].add(i)
                    square[(r//3,c//3)].add(i)
                    result = dfs()
                    print(result)
                    if result:
                        return True
                    else:
                        board[r][c] = "."
                        row[r].remove(i)
                        col[c].remove(i)
                        square[(r//3,c//3)].remove(i)
            q.append(curr)
            return False
    
        print(dfs())
        
newsol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == ".":
            board[r][c] = "."
newsol.solveSudoku(board)
print(board)