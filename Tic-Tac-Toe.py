#Tic-tac-toe
#Computer vs human
#global constants
X = "X"
O = "O"
EMPTY = " "
DRAW = "Draw"
NUM_SQUARES = 9
WAYS_TO_WIN = ( (0, 1, 2),
 				(3, 4, 5),
 				(6, 7, 8),
 				(0, 3, 6),
 				(1, 4, 7),
 				(2, 5, 8),
 				(0, 4, 8),
 				(2, 4, 6)) 
def instruct():
	"""Instruction"""
	print(
		"""
		Welcome to the game "Computer vs Human"!
		On the basis of the game "Tic-tac-toe" you have to fight against artificial intelligence.
		To make a move, enter a number from 1 to 9. The numbers correspond to the board fields:
		
		1 | 2 | 3
		---------
		4 | 5 | 6
		---------
		7 | 8 | 9

		Good luck!\n
		"""
		)
def ask_yes_no(question):
	"""Asks a question with a "Yes" or a "No"."""
	answer = None
	while answer not in ("y", "n"):
		answer = input(question).lower()
	return answer
def ask_number(question, low, high):
	"""Requests the number from the range"""
	answer = None
	while answer not in range(low, high+1):
		answer = int(input(question))
	return answer
def choice():
	"""Determines who goes first"""
	step_first = ask_yes_no("Would you like to reserve the first move? (y/n): ")
	if step_first == "y":
		print("\nOkay, you go first.")
		human = X
		computer = O
	else:
		print("\nOkey, computer goes first")
		computer = X
		human = O
	return computer, human
def new_board():
	"""Creates a "clean" board"""
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return(board)
def display_board(board):
	"""Displays the game board on the screen"""
	print("\n\t", board[0], "|", board[1], "|",board[2])
	print("\t ---------")
	print("\n\t", board[3], "|", board[4], "|",board[5])
	print("\t ---------")
	print("\n\t", board[6], "|", board[7], "|",board[8])
def legal_moves(board):
	"""Creates a list of available moves"""
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves
def winner(board):
	"""Determines the winner of the game"""
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board:
			return DRAW
	return None
def human_move(board, human):
	"""Takes a man’s turn"""
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Your move, pick one of the fields (1 - 9):" , 1, NUM_SQUARES) - 1
		if move not in legal:
			print("Don’t fool around, this field’s already taken.")
	return move
def computer_move(board, computer, human):
	"""Making a move for a computer opponent"""
	#create a copy of the board so that the function does not change some values in the list
	board = board[:]
	#fields from worst to better
	BEST_MOVES = (4, 0, 6, 2, 8, 1, 3, 5, 7)
	print("\nComputer selects a field with number -",end=" ")
	for move in legal_moves(board):
		board[move] = computer
	#if the following move can defeat the computer, select it
		if winner(board) == computer:
			print(move+1)
			return move
	#by checking and undoing the changes
		board[move] = EMPTY
	for move in legal_moves(board):
		board[move] = human
	#if the next move can win a person, choose him
		if winner(board) == human:
			print(move+1)
			return move
		board[move] = EMPTY
	for move in BEST_MOVES:
		if move in legal_moves(board):
			print(move+1)
			return move
def next_turn(turn):
	"""Moves over."""
	if turn == X:
		return O
	else:
		return X
def con_winner(the_winner, computer, human):
	"""Congratulations to the winner of the game."""
	if the_winner != DRAW:
		print("Three", the_winner, "in a row!\n")
	else:
		print("Draw!\n")
	if the_winner == computer:
		print("Computer won !!!")
	elif the_winner == human:
		print("You won !!!")
def main():
	instruct()
	computer, human = choice()
	turn = X 
	board = new_board()
	display_board(board)
	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		display_board(board)
		turn = next_turn(turn)
	the_winner = winner(board)
	con_winner(the_winner, computer, human)
	
main()
input()