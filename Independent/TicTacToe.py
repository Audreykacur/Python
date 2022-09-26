# TicTacToe.py
"""Tic Tac Toe Game"""

# Requirements:

# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board


def Board():
    print(list1)
    print(list2)
    print(list3)


list1 = ['1', '2', 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print("\n\nTIC-TAC-TOE GAME\n")
Board()
print("Above is the tic-tac-toe board")
print("\nRules: Player 1: X\n       Player 2: O\n       Enter the # that you want to place your X or O\n")
winner = False


def Player1():
    Board()
    placement = input("Player 1: Enter the placement you would like: ")
    if (placement == 1):
        list1[0] == 'X'
    elif (placement == 2):
        list1[1] == 'X'
    elif (placement == 3):
        list1[2] == 'X'
    elif (placement == 4):
        list2[0] == 'X'
    elif (placement == 5):
        list2[1] == 'X'
    elif (placement == 6):
        list2[2] == 'X'
    elif (placement == 7):
        list3[0] == 'X'
    elif (placement == 8):
        list3[1] == 'X'
    elif (placement == 9):
        list3[2] == 'X'
    else:
        print("Invalid.")


def Player2():
    Board()


while (winner == False):
    Player1()
    Player2()
