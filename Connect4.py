import numpy as np 

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT, COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

def won(board, piece):
	# Check all horizontal locations for win 
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] and board[r][c+2] and board[r][c+3]:
				return True

	# Check all vertical locations for win 
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] and board[r+2][c] and board[r+3][c]:
				return True

board = create_board()
game_over = False
turn = 0

while not game_over:
	print_board(board)
	# Ask for Player 1 input 
	if turn == 0:
		col = int(input("Make your choice Player 1 (0-6): "))
		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 1)

			if won(board, 1):
				print("Player 1 won")
				game_over = True
	# Ask for Player 2 input
	else:
		col = int(input("Make your choice Player 2 (0-6): "))
		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, 2)

		if won(board, 1):
			print("Player 2 won")
			game_over = True

	turn += 1
	turn = turn % 2
	