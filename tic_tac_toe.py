import random
'''
Title : Tic-Tac-Toe Game
wriiten by : Md Rahmat Hussain
'''
#display board function
def display_board(board):
	print('\n'*30)

	print("  \t\t\t   |   |  ")
	print("\t\t\t",board[7]+" | "+board[8]+" |"+board[9])
	print("  \t\t\t   |   |  ")
	print("\t\t\t-------------")
	print("  \t\t\t   |   |  ")
	print("\t\t\t",board[4]+" | "+board[5]+" |"+board[6])
	print("  \t\t\t   |   |  ")
	print("\t\t\t-------------")
	print("  \t\t\t   |   |  ")
	print("\t\t\t",board[1]+" | "+board[2]+" |"+board[3])
	print("  \t\t\t   |   |  ")

#player_input function
def player_input():
	marker =''

	#keep asking player1 to choose x or o until correct input

	while marker !='X' and marker !='O':
		marker =input('\t\tenter your choice X or O : ').upper()
	player1 =marker

	#assign player2 , the opposite marker
	if player1 =='X':
		player2 ='O'
	else:
		player2 ='X'

	return (player1, player2)

#place_marker function
def place_marker(board, marker, pos):
	if pos in range(1, 10):
		board[pos] =marker

#win checker function

def win_check(board, mark):

	if board[7]==board[9]==board[8]==mark:
		return True
	elif board[4]==board[5]==board[6]==mark:
		return True
	elif board[1]==board[2]==board[3]==mark:
		return True
	elif board[7]==board[4]==board[1]==mark:
		return True
	elif board[8]==board[5]==board[2]==mark:
		return True
	elif board[9]==board[6]==board[3]==mark:
		return True
	elif board[7]==board[5]==board[3]==mark:
		return True
	elif board[9]==board[5]==board[1]==mark:
		return True
	else:
		return False


#which player play first knowing function
def choose_first():
	s =random.randint(1,2)
	if s==1:
		return "player1"
	else:
		return "player2"



#free space checking function
def space_check(board, pos):
	return board[pos] == ' '

#board is full or not checking function
def full_board_check(board):

	for i in range(1, 10):
		if space_check(board, i):
			return False
	return True

#player choice move function
def player_choice(board):

	pos=0

	while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board, pos):
		pos =int(input("\t\tEnter your position (1-9) : "))
	return pos

#function to check if they want to replay the game
def replay():
	choice =input("\t\tWant to play Again ? enter yes or no :  ")
	return choice=='yes'

# Main Code

print("Welcome to Tic Tac Toe Game")

while True:
	#set up

	board =[' ']*10
	display_board(board)
	turn =choose_first();
	print("\t\t",turn+" will move first")
	player1_mark, player2_mark =player_input()
	game_on =input("\t\tAre you ready to play? y or n? :   ")

	if game_on=='y':
		game_on=True
	else:
		game_on =False

	while game_on:
		if turn=="player1":
			display_board(board)
			position =player_choice(board)
			place_marker(board, player1_mark, position)

			if win_check(board,player1_mark):
				display_board(board)
				print("\t\tplayer 1 has Won!!!")
				game_on =False
			else:
				if full_board_check(board):
					display_board(board)
					print("\t\tgame Tie!!!")
					game_on =False
				else:
					turn ="player2"
		else:
			display_board(board)
			position =player_choice(board)
			place_marker(board, player2_mark, position)

			if win_check(board,player2_mark):
				display_board(board)
				print("\t\tplayer 2 has Won!!!")
				game_on =False
			else:
				if full_board_check(board):
					display_board(board)
					print("\t\tgame Tie!!!")
					game_on =False
				else:
					turn ="player1"

	if not replay():
		break
