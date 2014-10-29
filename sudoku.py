import pdb 
class ValidationException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class Solution:
    rl = [[0]*10 for i in range(9)]
    cl = [[0]*10 for i in range(9)]
    bl = [[0]*10 for i in range(9)]
    board = []
    def __init(self,board):
        self.board = board
        
    def solveSudoku(self, board):
        for i in range(9):
            for j in range(9): 
                if board[i][j] != 0 :
                   self.fill(i,j,board[i][j])
        self.dfs(board, 0)

    def isValid(self,x,y,v):
        if self.rl[x][v]==0 and self.cl[y][v]==0 and self.bl[x/3*3+y/3][v]==0:
            return True
        else: return False

    def dfs(self, board, ind):
        if ind>80: return True
        i = ind / 9
        j = ind - 9*i
        if board[i][j]!=0: return self.dfs(board, ind+1)
        else:
            for k in range(1,10):
                    if self.isValid(i,j,k):
                        board[i][j]=k
                        # pdb.set_trace()
                        self.fill(i,j,k)
                        if self.dfs(board, ind+1): return True
                        self.clear(i,j,k)
                    board[i][j]= 0
                    # pdb.set_trace()
            return False
        return True

    def fill(self, x,y,v):
        self.rl[x][v]=1
        self.cl[y][v]=1
        self.bl[x/3*3+y/3][v]=1
        
    def clear(self,x,y,v):
        self.rl[x][v]=0
        self.cl[y][v]=0
        self.bl[x/3*3+y/3][v]=0
        
        
                            


