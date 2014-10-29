from sudoku import ValidationException, Solution
import csv
import string

file = open("board1.csv","rb")
inp = []
for line in file.xreadlines():
	# print line
	# inp.append(string.split(line,','))
	line = [i.strip() for i in line.split(',')]
	inp.append(line)

board = [[0]*9 for rows in range(9)]
for i in range(9):
    for j in range(9):
        board[i][j]=ord(inp[i][j])-ord('0')

sl = Solution()
sl.solveSudoku(board)
for rows in board:
	print rows 