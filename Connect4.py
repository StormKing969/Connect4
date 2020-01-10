import numpy as np 

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT, COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[5][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
	# Ask for Player 1 input 
	if turn == 0:
		col = int(input("Make your choice Player 1 (0-6): "))
		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 1)
	# Ask for Player 2 input
	else:
		col = int(input("Make your choice Player 2 (0-6): "))
		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 2)

	turn += 1
	turn = turn % 2
	print_board(board)