from __future__ import print_function
from NeighborContainer2 import *
from math import pi , acos , sin , cos
from heapq import *
import time

def main():
    global myData, word1, word2, myCoords, count
    #names = open("romFullNames.txt").read().split()
    coords = open("romNodes.txt").read().split()
    edges = open("romEdges.txt").read().split()
    
    myCoords = {}
    myEdges = {}
    myData = {}
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
            myData[letter][nbr] = (calcd(myCoords[nbr][0], myCoords[nbr][1], myCoords[letter][0], myCoords[letter][1]))

    while True:
        word1 = input("Word 1: ")
        if word1 == "end":
            quit()
        word2 = input("Word 2: ")
        if word2 == "end":
            quit()
        start_time = time.time()
        count = 0
        trace = aStarSearch()
        
        #print("Words visited: ", wordsVisited)
        #print("Max Length of Queue: ", maxLenOfQ)
        totalDistance = 0
        before = word1
        if not trace == None:
            trace.reverse()
            for a in trace:
                totalDistance = totalDistance + calcd(myCoords[a][0], myCoords[a][1], myCoords[before][0], myCoords[before][1])
                before = a
                print(a)
        print("--- %s seconds ---" % (time.time() - start_time))
        print(len(trace))
        print("Count: ", count)
        print("Distance: ", totalDistance)
        print("Straight Distance: ", calcd(myCoords[word1][0], myCoords[word1][1], myCoords[word2][0], myCoords[word2][1]),"\n\n")

def aStarSearch():
    global myData, word1, word2, myCoords, heap
    heap = []
    heappush(heap, [calcd(myCoords[word1][0], myCoords[word1][1], myCoords[word2][0], myCoords[word2][1]), [word1]])
    return check()

def check():
    global myData, word1, word2, myCoords, heap, count
    used = {}
    used[word1] = None
    while True:
        if len(heap) == 0:
            print("no path available")
            return
        pos = heap[0]
        if pos[1][0] == word2:
            return pos[1]
        neighbors = myData[pos[1][0]].keys()
        for a in neighbors:
            hNPosToEnd = calcd(myCoords[pos[1][0]][0], myCoords[pos[1][0]][1], myCoords[word2][0], myCoords[word2][1])
            hNAToEnd = calcd(myCoords[a][0], myCoords[a][1], myCoords[word2][0], myCoords[word2][1])
            gNPosToA = calcd(myCoords[pos[1][0]][0], myCoords[pos[1][0]][1], myCoords[a][0], myCoords[a][1])
            if not a in used or (not used[a] == None and used[a] > pos[0] - hNPosToEnd + gNPosToA):
                used[a] = pos[0] - hNPosToEnd + gNPosToA
                heappush(heap, [pos[0] - hNPosToEnd + hNAToEnd + gNPosToA, [a] + pos[1]])
        heap.remove(pos)
        count = count + 1
    

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
   x = sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1)
   if x > 1:
       x = 1
   return acos( x ) * R
        
    
main()   
