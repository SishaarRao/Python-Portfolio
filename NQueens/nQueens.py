from math import *
import random
import time
def main():
    board = []
    count = 10
    totalTime = 0
    for n in range(0, 1):
        board = []
        for i in range(0, count):
            board.append(i)
        display(board)
        start_time = time.time()
        nQueen(board)
        display(board)
        s = (time.time() - start_time)
        totalTime = totalTime + s
        print(n,":  --- %s seconds ---" % s)
    print("Total Time: ", str(totalTime))
    print("Average: ", str(totalTime/100))
    #start_time = time.time()
    #s = (time.time() - start_time)
    #print("  --- %s seconds ---" % s)
    fileName = "tsp38.txt"
    data = open(fileName, "r").read().split()
    i = 1
    tspList = []
    countList = []
    while i < len(data):
        tspList.append((float(data[i]), float(data[i+1])))
        i = i+2
    for i in range(0,len(tspList)):
        countList.append(i)
    print("\n\n",sumDistance(tspList))
    start_time = time.time()
    tsp(tspList,countList)
    s = (time.time() - start_time)
    print(sumDistance(tspList))
    print(n,":  --- %s seconds ---" % s)
    print(countList)


def detectCollisions(board):
    count = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if not i == j:
                if abs(i - j) == abs(board[i] - board[j]):
                    count = count + 1
    return count/2

def nQueen(board):
    collisions = detectCollisions(board)
    if collisions == 0:
        return board
    myMin = collisions
    myTuple = [(-1,-1)]
    for i in range(0, len(board)):
        for j in range(i+1, len(board)):
            tempboard = board[:]
            collisions = detectCollisions(swap(tempboard, i, j))
            if myMin > collisions:
                myMin = collisions
                myTuple = [(i,j)]
            elif myMin == collisions:
                myTuple.append((i,j))
    choice = random.randint(0, len(myTuple)-1)
    board = swap(board, myTuple[choice][0], myTuple[choice][1])
    return nQueen(board)

def sumDistance(tspList):
    totalDistance = 0
    for i in range(1, len(tspList)):
        toAdd = ((tspList[i][0] - tspList[i-1][0])**2 + (tspList[i][1] - tspList[i-1][1])**2)**0.5
        totalDistance = totalDistance + toAdd
    return totalDistance

def tsp(tspList,countList):
    totalDistance = sumDistance(tspList)
    #if collisions == 0:
        #return board
    myMin = totalDistance
    myTuple = [(-1,-1)]
    for i in range(0, len(tspList)):
        for j in range(i+1, len(tspList)):
            tempList = tspList[:]
            totalDistance = sumDistance(swap(tempList, i, j))
            if myMin > totalDistance:
                myMin = totalDistance
                myTuple = [(i,j)]
            elif myMin == totalDistance:
                myTuple.append((i,j))
    if myTuple == [(-1,-1)]:
        return tspList
    choice = random.randint(0, len(myTuple)-1)
    tspList = swap(tspList, myTuple[choice][0], myTuple[choice][1])
    countList = swap(countList, myTuple[choice][0], myTuple[choice][1])
    return tsp(tspList,countList)

def swap(board, a, b):
    temp = board[b]
    board[b] = board[a]
    board[a] = temp
    return board

def display(board):
    print("-----------------")
    for r in range(len(board)):
        toPrint = ""
        for c in range(len(board)):
            if board[c] == len(board)-1 - r:
                toPrint = toPrint + ("| X ")
            else:
                toPrint = toPrint + ("|   ")
        print(toPrint + "|")
        print("-----------------")
                



main()
