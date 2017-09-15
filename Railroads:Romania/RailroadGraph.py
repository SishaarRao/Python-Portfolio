from __future__ import print_function
from NeighborContainer2 import *
from math import pi , acos , sin , cos
from heapq import *
import time

def main():
    global myData, word1, word2, myCoords
    names = open("rrNodeCity.txt").read().split("\n")
    coords = open("rrNodes.txt").read().split()
    edges = open("rrEdges.txt").read().split()
    
    myCoords = {}
    myEdges = {}
    myData = {}
    myNames = {}

    i = 0
    while i < len(names) - 1:
        myNames[names[i][0:7]] = names[i][8:]
        i = i + 1
    print(myNames)
        
    i = 0
    while i < len(coords):
        myCoords[coords[i]] = [float(coords[i+1]), float(coords[i+2])]
        i = i + 3
    i = 0
    while i < len(edges):
        if not edges[i] in myEdges:
            myEdges[edges[i]] = []
        myEdges[edges[i]].append(edges[i+1])
        if not edges[i + 1] in myEdges:
            myEdges[edges[i+1]] = []
        myEdges[edges[i+1]].append(edges[i])
        i = i+2
    for letter in myEdges:
        myData[letter] = {}
        for nbr in myEdges[letter]:
            myData[letter][nbr] = (calcd(myCoords[nbr][1], myCoords[nbr][0], myCoords[letter][1], myCoords[letter][0]))

    while True:
        word1 = input("Word 1: ")
        if word1 == "end":
            quit()
        word2 = input("Word 2: ")
        if word2 == "end":
            quit()
        word1 = list(myNames.keys())[list(myNames.values()).index(word1)]
        word2 = list(myNames.keys())[list(myNames.values()).index(word2)]
        print(word1, word2)
        start_time = time.time()
        trace = aStarSearch()
        print("--- %s seconds ---" % (time.time() - start_time))
        #print("Words visited: ", wordsVisited)
        #print("Max Length of Queue: ", maxLenOfQ)
        if not trace == None:
            print(len(trace))
            trace.reverse()
            totalDistance = 0
            before = word1
            for a in trace:
                totalDistance = totalDistance + calcd(myCoords[a][1], myCoords[a][0], myCoords[before][1], myCoords[before][0])
                before = a
                if a in myNames:
                    print(myNames[a])
                else:
                    print(a)
            print("Distance: ", totalDistance)
            print("Straight Distance: ", calcd(myCoords[word1][1], myCoords[word1][0], myCoords[word2][1], myCoords[word2][0]),"\n\n")

def aStarSearch():
    global myData, word1, word2, myCoords, heap
    heap = []
    heappush(heap, [calcd(myCoords[word1][1], myCoords[word1][0], myCoords[word2][1], myCoords[word2][0]), [word1]])
    return check()

def check():
    global myData, word1, word2, myCoords, heap
    used = {}
    used[word1] = None
    while True:
        if len(heap) == 0:
            print("no path available")
            return
        pos = heap[0]
        neighbors = myData[pos[1][0]].keys()
        for a in neighbors:
            if a == word2:
                pos[1].insert(0, a)
                return pos[1]
            else:
                if not a in used:
                    used[a] = None
                    #heappush(heap, [calcd(myCoords[a][1], myCoords[a][0], myCoords[word1][1], myCoords[word1][0]) + calcd(myCoords[a][1], myCoords[a][0], myCoords[word2][1], myCoords[word2][0]), [a] + pos[1]])
                    #print(pos[0] - calcd(myCoords[pos[1][0]][1], myCoords[pos[1][0]][0], myCoords[word2][1], myCoords[word2][0]))
                    heappush(heap, [pos[0] + calcd(myCoords[a][1], myCoords[a][0], myCoords[word2][1], myCoords[word2][0]), [a] + pos[1]])

        heap.remove(pos)
    
    

def calcd(y1,x1, y2,x2):
   #
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 3958.76 # miles
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
        
    
main()   
