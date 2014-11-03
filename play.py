from sudoku import ValidationException, Solution
import csv
import string
filename = raw_input('Enter the filename of your unsolved sudoku puzzle: ') or 'board1.csv'
raw_name = filename.split('.')[0];
file = open(filename,"rb")
inp = []
for line in file.xreadlines():
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

resultFile = open(raw_name + "_solved.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(board)