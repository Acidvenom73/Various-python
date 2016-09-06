from random import randint
import os
clear = lambda: os.system('cls')

board = []

for x in range(5):
	board.append(["O"] * 5)

def print_board(board):
	for row in board:
		print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range (1, 6):
	guess_row = int(raw_input("Guess Row:"))
	print guess_row
	guess_row = guess_row - 1
	print guess_row
	guess_col = int(raw_input("Guess Col:"))
	print guess_col
	guess_col = guess_col - 1
	print guess_col
	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations! You sunk my battleship!"
		break
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			clear()
			print "Oops, that's not even in the ocean."
		elif(board[guess_row][guess_col] == "X"):
			clear()
			print "You guessed that one already."
		elif turn == 5:
			clear()
			print "Game Over! Would you like to try again?"
			break
		else:
			clear()
			print "You missed my battleship!"
			board[guess_row][guess_col] = "X"
	print "Turn", turn
	print_board(board)
	
	
### Bug-fixes and similar: 
# "Game Over" doesn't work : DONE
# Print nicely, clear inbetween turns : DONE
# Doesn't count a turn if you choose wrong number or already taken one
# Range is from 1 to 5, not 0 to 4 : DONE
# Properly print turns : DONE
# Properly end after "Game Over" is printed : DONE
# Input starts from 0 instead of 1

### Extra features:

#Make multiple battleships:
#you'll need to be careful because you need to make sure that you don't place battleships on top of each other on the game board.
#You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

#Make battleships of different sizes:
#this is trickier than it sounds.
#All the parts of the battleship need to be vertically or horizontally touching and you'll need to make sure you don't accidentally place part of a ship off the side of the board.

#Make your game a two-player game.
#Use functions to allow your game to have more features like rematches, statistics and more!
#