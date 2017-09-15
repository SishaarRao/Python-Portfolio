from math import *
import random
import time

def main():
    board = [' ']*900
    #make checkerboard
    for i in range(0, 900):
        if int(i/int(len(board)**0.5))%2 == 0:
            if i%2 == 0:
                board[i] = 'X'
            else:
                board[i] = '.'
        else:
            if i%2 == 0:
                board[i] = '.'
            else:
                board[i] = 'X'
    #display(board)

    #remove corners
    board[0], board[int(len(board)**0.5)-1], board[len(board)-1], board[len(board)-int(len(board)**0.5)] = ' ',' ',' ',' '
    #display(board)
    
    #remove 20 at random
    for i in range(0,20):
        index = 0
        while board[index] == ' ':
            index = random.randint(0,len(board)-1)
        board[index] = ' '
    #display(board)
        
    #add 5 at random
    for i in range(0,5):
        index = random.randint(0,len(board)-1)
        while not board[index] == ' ':
            index = random.randint(0,len(board)-1)
        if random.random() < 0.5:
            board[index] = 'X'
        else:
            board[index] = '.'
    display(board)

    macro(board)
    display(board)


def macro(board):
    H = 0
    check = True
    while check == True:
        check = False
        for i in range(0, len(board)):
            if not board[i] == ' ':
                nbrs = genNbrs(board, i)
                emptyCount = 0
                #count empty
                for j in nbrs:
                    if j == ' ':
                        emptyCount = emptyCount+1
                #determine H
                if emptyCount <= 2:
                    H = 3
                elif emptyCount <= 5:
                    H = 2
                else:
                    H = 1
                #count same
                sameType = 0
                for j in nbrs:
                    if j == board[i]:
                        sameType = sameType+1
                #check if happy, if not, swap
                if sameType < H:
                    check = True
                    swap(board, i, random.randint(0,len(board)-1))


def swap(board, a, b):
    temp = board[a]
    board[a] = board[b]
    board[b] = temp

def genNbrs(board, pos):
    nbrs = []
    count = int(len(board)**0.5)
    #north
    if not int(pos/count) == 0:
       nbrs.append(board[pos-count])
    #south
    if not int(pos/count) == count-1:
        nbrs.append(board[pos+count])
    #east
    if not int(pos%count) == count-1:
        nbrs.append(board[pos+1])
    #west
    if not int(pos%count) == 0:
        nbrs.append(board[pos-1])
    #northwest
    if not int(pos/count) == 0 and not int(pos%count) == 0:
        nbrs.append(board[pos-count-1])
    #northeast
    if not int(pos/count) == 0 and not int(pos%count) == count-1:
        nbrs.append(board[pos-count+1])
    #southwest
    if not int(pos%count) == 0 and not int(pos/count) == count-1:
        nbrs.append(board[pos+count-1])
    #southeast
    if not int(pos/count) == count-1 and not int(pos%count) == count-1:
        nbrs.append(board[pos+count+1])
    return nbrs

def display(board):
    print("-----------------------")
    for i in range(0, int(len(board)**0.5)):
        toPrint = "| "
        for j in range(0, int(len(board)**0.5)):
            toPrint = toPrint + str(board[i*int(len(board)**0.5) + j]) + " | "
        print(toPrint)
    print("-----------------------")





main()
