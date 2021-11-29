#!/usr/bin/env python3
from math import inf as infinity
import random
import time

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#This function prints the Game Board numbering (1-9)
def boardPosNum():
	print("\nGame Board Numbering")
	print("  1  2  3\n ---------\n  4  5  6\n ---------\n  7  8  9\n")


#This function prints the current status of the board
def printBoard(board):
	print("\nGame Board")
	print('', board[0], board[1], board[2],"\n", board[3], board[4], board[5], "\n", board[6], board[7], board[8], "\n")


#This function tells whether any player has won the game or not
def winner(board):
	if (board[0]=='X' or board[0]=='O') and board[0]==board[1] and board[1]==board[2]:
		return board[0]
	elif (board[0]=='X' or board[0]=='O') and board[0]==board[3] and board[3]==board[6]:
		return board[0]
	elif (board[2]=='X' or board[2]=='O') and board[2]==board[5] and board[5]==board[8]:
		return board[2]
	elif (board[6]=='X' or board[6]=='O') and board[6]==board[7] and board[7]==board[8]:
		return board[6]
	elif (board[0]=='X' or board[0]=='O') and board[0]==board[4] and board[4]==board[8]:
		return board[0]
	elif (board[2]=='X' or board[2]=='O') and board[2]==board[4] and board[4]==board[6]:
		return board[2]
	elif (board[1]=='X' or board[1]=='O') and board[1]==board[4] and board[4]==board[7]:
		return board[1]
	elif (board[3]=='X' or board[3]=='O') and board[3]==board[4] and board[4]==board[5]:
		return board[3]
	else:
		return 'N'


#This function calculates the score of the current board
def eval(board, comp, user):
	if winner(board)==comp:
		score = +1
	elif winner(board)==user:
		score = -1
	else:
		score = 0

	return score


#This function tells the empty places in the current board
def empty_place(board):
	cells = []

	for i, obj in enumerate(board):
		if obj == '-':
			cells.append(i)

	return cells


#This function is the MiniMax Algorithm which helps the computer to make the best move
def minimax(board, depth, player, comp, user):
	if player == 1:
		bestMove = [-1, -infinity]
	else:
		bestMove = [-1, +infinity]

	if depth == 0 or winner(board)!='N':
		score = eval(board, comp, user)
		return [-1, score]

	for cell in empty_place(board):
		if player == 1:
			board[cell] = comp
		else:
			board[cell] = user
        		
		score = minimax(board, depth - 1, -player, comp, user)
		board[cell] = '-'
		score[0] = cell+1

		if player == 1:
			if score[1] > bestMove[1]:
				bestMove = score  # max value
		else:
			if score[1] < bestMove[1]:
				bestMove = score  # min value

	return bestMove


#This function makes moves for the computer in HARD level
def Comp_turn(board, comp, user):
	d = len(empty_place(board))
	if d==0 or winner(board)!='N':
		return
		
	print("Player", comp, "turn")
	if d==9:
		c_place = random.choice(num)
	else:
		pos = minimax(board, d, 1, comp, user)
		c_place = pos[0]
		
	board[c_place -1]= comp
	time.sleep(1)


#This function makes moves for the computer in EASY level
def EasyMode(board, comp):
	c_place = random.choice(num)
	while board[c_place-1]!='-':
		c_place = random.choice(num)

	print("Player", comp, "turn")
	board[c_place-1]= comp
	time.sleep(1)


#Driver Code
p = input("Choose your letter: X/O  ")
while p!='X' and p!='O':
	print("\nInvalid choice")
	p = input("Choose your letter: X/O  ")
	
c = 'O'
if p=='O':
	c = 'X'

t = random.choice([0, 1])

while True:
	m = input("\nChoose difficulty level (Enter 0 for EASY and 1 for HARD): ")
	while m!='0' and m!='1':
		print("\nInvalid choice")
		m = input("Choose difficulty level (Enter 0 for EASY and 1 for HARD): ")

	board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
	boardPosNum()

	m = int(m)
	if t%2==0:
		while ('-' in board) and winner(board)=='N':
			print("Player", p, "turn")
			print("Enter 0 to view Game Board Numbering\n")
			pos = input("Enter a number to choose place (1-9): ")
			
			while not pos.isnumeric():
				print("Invalid move")
				pos = input("Enter a number to choose place (1-9): ")
			
			pos = int(pos)	
			while pos<1 or pos>9 or board[pos-1]!='-':
				if pos!=0:
					print("Invalid move")
				else:
					boardPosNum()
				pos = int(input("Enter a number to choose place (1-9): "))

			board[pos-1]= p
			printBoard(board)
			
			if ('-' in board)==False or winner(board)==p:
				break
			
			if m==0:
				EasyMode(board, c)
			else:
				Comp_turn(board, c, p)
			printBoard(board)
	else:
		while ('-' in board) and winner(board)=='N':
			if m==0:
				EasyMode(board, c)
			else:
				Comp_turn(board, c, p)
			printBoard(board)
			
			if ('-' in board)==False or winner(board)==c:
				break
			
			print("Player", p, "turn")
			print("Enter 0 to view Game Board Numbering\n")
			pos = input("Enter a number to choose place (1-9): ")
			
			while not pos.isnumeric():
				print("Invalid move")
				pos = input("Enter a number to choose place (1-9): ")
			
			pos = int(pos)
			while pos<1 or pos>9 or board[pos-1]!='-':
				if pos!=0:
					print("Invalid move")
				else:
					boardPosNum()
				pos = int(input("Enter a number to choose place (1-9): "))

			board[pos-1]= p
			printBoard(board)

	if winner(board)==p:	
		print("You WON!!!")
	elif winner(board)==c:
		print("You LOSE:(")
	else:
		print("It's a TIE!")

	play = input("\nDo you want to play again? (y/n)  ")
	while play!='y' and play!='Y' and play!='n' and play!='N':
		print("\nInvalid choice")
		play = input("Do you want to play again? (y/n)  ")
	
	if play=='n' or play=='N':
		break
	
	t=t+1
