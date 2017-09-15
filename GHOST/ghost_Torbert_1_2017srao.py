from __future__ import print_function
import time

def main():
    allWords = open("ghost.txt").read().split("\n")
    #allWords = ["random", "royal", "rower", "rowing", "runner", "running"]
    myDict = {}
    start_time = time.time()
    for tempWord in allWords:
        myDict = add(tempWord, myDict)
    s = (time.time() - start_time)
    print("  --- %s seconds ---" % s)
    currString = ""
    numOfPlayers = int(input("Number of Players: "))
    players = [""] * numOfPlayers
    turn = 0
    while True:
        print("Player " + str(turn + 1) + " Turn")
        letter = input("Current String: " + currString + "\nNext: ")
        if letter == "end":
            quit()
        if letter == "!":
            print(challenge(currString, myDict))
            currString = ""
            if turn == 0:
                players[numOfPlayers - 1] = ("GHOST")[0:len(players[numOfPlayers - 1]) + 1]
            else:
                players[turn - 1] = ("GHOST")[0:len(players[turn - 1]) + 1]
            print(players)
        if letter == "help":
            print(sorted(possibilities(currString, myDict)))
            continue
        if letter == "clear":
            currString = ""
        if letter == "?":
            start_time = time.time()
            poss = possibilities(currString, myDict)
            temp = turn + 1
            if temp == numOfPlayers:
                temp = 0
            toPrint = []
            for a in poss:
                if not recurse(currString + a, temp, myDict, numOfPlayers):
                    toPrint.append(a)
            print(toPrint)
            s = (time.time() - start_time)
            print("  --- %s seconds ---" % s)
            continue
        else:
            if not letter == "!":
                currString = currString + letter
            #print(possibilities(currString, myDict))
        turn = turn + 1
        if turn == numOfPlayers:
            turn = 0


def recurse(currString, turn, myDict, numOfPlayers):
    if challenge(currString, myDict):#current string is a loss at turn
        return True
    poss = possibilities(currString, myDict)
    currVals = {}
    temp = turn + 1
    if temp == numOfPlayers:
        temp = 0
    for a in poss:
        val = recurse(currString + a, temp, myDict, numOfPlayers)
        if val:
            currVals[a] = False
        else:
            currVals[a] = True
    for a in currVals:
        if currVals[a]:
            return True
    return False
    
    
         
        
    

def add(word, myDict):
    if len(word) == 0:
        return myDict
    if not word[0] in myDict:
        myDict[word[0]] = {}
    curr = myDict[word[0]]
    for i in range(1, len(word)):
        if not word[i] in curr:
            curr[word[i]] = {}
        curr = curr[word[i]]
    curr[" "] = None
    return myDict

def possibilities(currString, myDict):
    if len(currString) == 0:
        return list(myDict.keys())
    if not currString[0] in myDict:
        return []
    curr = myDict[currString[0]]
    for i in range(1, len(currString)):
        if not currString[i] in curr:
            return []
        else:
            curr = curr[currString[i]]
    return list(curr.keys())

def challenge(currString, myDict):
    if len(currString) == 0:
        return list(myDict.keys())
    if not currString[0] in myDict:
        return True
    curr = myDict[currString[0]]
    for i in range(1, len(currString)):
        if not currString[i] in curr:
            return True
        else:
            curr = curr[currString[i]]
    if " " in curr:
        return True
    return False

main()
