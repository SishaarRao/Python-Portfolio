import os
from math import *
filename = "circle"
def main():
   myText = open(filename + ".ppm").read().split()
   header, width, height = myText[0], myText[1], myText[2]
   for i in range(0, 4):
      myText.pop(0)
   greyScale(myText, header, width, height)
   print("GreyScale complete")
   
   myText = open(filename + "Grey.ppm").read().split()
   header, width, height = myText[0], myText[1], myText[2]
   for i in range(0, 4):
      myText.pop(0)
   blur(myText, header, width, height)
   myText = open(filename + "Blur.ppm").read().split()
   header, width, height = myText[0], myText[1], myText[2]
   for i in range(0, 4):
      myText.pop(0)
   reblur(myText, header, width, height)
   print("burring complete")   
   
   myText = open(filename + "ReBlur.ppm").read().split()
   header, width, height = myText[0], myText[1], myText[2]
   for i in range(0, 4):
      myText.pop(0)
   outline2(myText, header, width, height)
   print("outline complete")   

   myText = open(filename + "Outline2.ppm").read().split()
   header, width, height = myText[0], myText[1], myText[2]
   for i in range(0, 4):
      myText.pop(0)
   thin(myText, header, width, height)
   print("thinning complete")

   myText = open(filename + "Thin.ppm").read().split()
   header, width, height = myText[0], myText[1], myText[2]
   for i in range(0, 4):
      myText.pop(0)
   voting(myText, header, width, height)
   print("voting complete")

   
def greyScale(myText, header, width, height):
   printFile = open(filename + "Grey.ppm", "w+")
   printFile.write(header + "\n" + width + "\n" + height + "\n255\n")
   i = 0
   #print(len(myText))
   while i < len(myText):
      r = 0.3 * int(myText[i])
      g = 0.59 * int(myText[i + 1])
      b = 0.11 * int(myText[i + 2]) 
      avg = int(r + g + b)
      printFile.write(str(avg) + " " + str(avg) + " " + str(avg) + "\n")
      i = i + 3
   printFile.close()
   
def isEdge(width, height, index):
   r = int(index / width)
   c = index % width
   if r <= 0 or r >= height-1 or c <= 0 or c >= width-1:
      return True
   return False
   
def blur(myText, header, width, height):
   printFile = open(filename + "Blur.ppm", "w+")
   printFile.write(header + "\n" + width + "\n" + height + "\n255\n")
   r, c = 0, 0
   myFinalText = []
   width, height = int(width), int(height)
   i = 0
   while i < len(myText):
      myFinalText.append(myText[i])
      i = i + 3
   while r < height:
      while c < width:
         index = (r*width) + c
         if not isEdge(width, height, index):
            r1Val = int(myFinalText[index-width-1]) + 2*int(myFinalText[index-width]) + int(myFinalText[index-width+1])
            r2Val = 2*int(myFinalText[index-1]) + 4*int(myFinalText[index]) + 2*int(myFinalText[index+1])
            r3Val = int(myFinalText[index+width-1]) + 2*int(myFinalText[index+width]) + int(myFinalText[index+width+1])
            redVal = int((r1Val + r2Val + r3Val)/16)
            printFile.write(str(redVal) + " " + str(redVal) + " " + str(redVal) + "\n")
         else:
            printFile.write(str(myFinalText[index]) + " " + str(myFinalText[index]) + " " + str(myFinalText[index]) + "\n")
         c = c + 1
      r = r+1
      c = 0
   printFile.close()

def outline(myText, header, width, height):
   count = 0
   printFile = open(filename + "Outline.ppm", "w+")
   printFile.write(header + "\n" + width + "\n" + height + "\n255\n")
   r, c = 0, 0
   myFinalText = []
   width, height = int(width), int(height)
   i = 0
   threshold = 5
   while i < len(myText):
      myFinalText.append(myText[i])
      i = i + 3
   while r < height:
      while c < width:
         index = (r*width) + c
         if not isEdge(width, height, index):
            gx1Val = -1*int(myFinalText[index-width-1]) + int(myFinalText[index-width+1])
            gx2Val = -2*int(myFinalText[index-1]) + 2*int(myFinalText[index+1])
            gx3Val = -1*int(myFinalText[index+width-1]) + int(myFinalText[index+width+1])
            gxVal = int((gx1Val + gx2Val + gx3Val)/16)

            gy1Val = -1*int(myFinalText[index-width-1]) + -2*int(myFinalText[index-width]) + -1*int(myFinalText[index-width+1])
            gy3Val = int(myFinalText[index+width-1]) + 2*int(myFinalText[index+width]) + int(myFinalText[index+width+1])
            gyVal = int((gy1Val + gy3Val)/16)

            g = abs(gxVal) + abs(gyVal)

            if g > threshold:
               printFile.write("225 0 0\n")
               count = count + 1
            else:
               printFile.write(str(myFinalText[index]) + " " + str(myFinalText[index]) + " " + str(myFinalText[index]) + "\n")
         else:
            printFile.write(str(myFinalText[index]) + " " + str(myFinalText[index]) + " " + str(myFinalText[index]) + "\n")
         c = c + 1
      r = r+1
      c = 0
   print(str(count / len(myFinalText) * 100) + "%")
   printFile.close()

def outline2(myText, header, width, height):
   count = 0
   printFile = open(filename + "Outline2.ppm", "w+")
   printFile.write(header + "\n" + width + "\n" + height + "\n255\n")
   r, c = 0, 0
   myFinalText = []
   width, height = int(width), int(height)
   i = 0
   threshold = 10
   while i < len(myText):
      myFinalText.append(myText[i])
      i = i + 3
   while r < height:
      while c < width:
         index = (r*width) + c
         if not isEdge(width, height, index):
            gx1Val = -1*int(myFinalText[index-width-1]) + int(myFinalText[index-width+1])
            gx2Val = -2*int(myFinalText[index-1]) + 2*int(myFinalText[index+1])
            gx3Val = -1*int(myFinalText[index+width-1]) + int(myFinalText[index+width+1])
            gxVal = int((gx1Val + gx2Val + gx3Val)/16)

            gy1Val = -1*int(myFinalText[index-width-1]) + -2*int(myFinalText[index-width]) + -1*int(myFinalText[index-width+1])
            gy3Val = int(myFinalText[index+width-1]) + 2*int(myFinalText[index+width]) + int(myFinalText[index+width+1])
            gyVal = int((gy1Val + gy3Val)/16)

            g = abs(gxVal) + abs(gyVal)

            if g > threshold:
               printFile.write("225 0 0\n")
               count = count + 1
               #print(g)
            else:
               printFile.write("255 255 255\n")
         else:
            printFile.write("255 255 255\n")
         c = c + 1
      r = r+1
      c = 0
   print(str(count / len(myFinalText) * 100) + "%")
   printFile.close()

   
def reblur(myText, header, width, height):
   printFile = open(filename + "ReBlur.ppm", "w+")
   printFile.write(header + "\n" + width + "\n" + height + "\n255\n")
   r, c = 0, 0
   myFinalText = []
   width, height = int(width), int(height)
   i = 0
   while i < len(myText):
      myFinalText.append(myText[i])
      i = i + 3
   while r < height:
      while c < width:
         index = (r*width) + c
         if not isEdge(width, height, index):
            r1Val = int(myFinalText[index-width-1]) + 2*int(myFinalText[index-width]) + int(myFinalText[index-width+1])
            r2Val = 2*int(myFinalText[index-1]) + 4*int(myFinalText[index]) + 2*int(myFinalText[index+1])
            r3Val = int(myFinalText[index+width-1]) + 2*int(myFinalText[index+width]) + int(myFinalText[index+width+1])
            redVal = int((r1Val + r2Val + r3Val)/16)
            printFile.write(str(redVal) + " " + str(redVal) + " " + str(redVal) + "\n")
         else:
            printFile.write(str(myFinalText[index]) + " " + str(myFinalText[index]) + " " + str(myFinalText[index]) + "\n")
         c = c + 1
      r = r+1
      c = 0
   printFile.close()
def voting(myText, header, width, height):
   printFile = open(filename + "Votes.ppm", "w+")
   printFile.write(header + "\n" + width + "\n" + height + "\n255\n")
   myCompareText = open(filename + "ReBlur.ppm").read().split()
   r, c = 0, 0
   myFinalText = []
   myFinalCompareText = []
   width, height = int(width), int(height)
   i = 0
   while i < len(myText):
      myFinalText.append(myText[i+1])
      myFinalCompareText.append(myCompareText[i])
      i = i + 3
   votes = [0]*(int(len(myFinalCompareText)))
   print(len(votes))
   while r < height:
      while c < width:
         index = (r*width) + c
         if not isEdge(width, height, index):
            if int(myFinalText[index]) == 0:
               gxVal = calcGX(myFinalCompareText, index, width)
               gyVal = calcGY(myFinalCompareText, index, width)
               theta = float(atan2(gyVal, gxVal))
               #print(index)
               votes = placeVotes(r, c, theta, votes, width, height)
         c = c + 1
      r = r+1
      c = 0
   print(len(votes))
   for i in range(0, len(votes)):
      #print(votes[i])
      if votes[i] > 25:
         printFile.write("0 0 0\n")
      else:
         printFile.write(str(255 - 10*votes[i]) + " " + str(255 - 10*votes[i]) + " " + str(255 - 10*votes[i]) + "\n")
         #printFile.write(str(votes[i]) + " 0 0\n")
   printFile.close()

def placeVotes(r, c, theta, votes, width, height):
   #descend
   rTemp = float(r)
   cTemp = float(c)
   index = int((rTemp*width)+cTemp)
   while not isEdge(width, height, index):
      votes[index] = votes[index]+1
      xComp = float(-1.0*(2.0**0.5)*cos(theta))
      yComp = float(-1.0*(2.0**0.5)*sin(theta))
##      xComp = float(-1.0*cos(theta))
##      yComp = float(-1.0*sin(theta))
      
      rTemp = rTemp + xComp
      cTemp = cTemp + yComp
   
      index = int(rTemp)*width+int(cTemp)
   #ascend
   rTemp = float(r)
   cTemp = float(c)
   index = int((rTemp*width)+cTemp)
   while not isEdge(width, height, index):
      votes[index] = votes[index]+1
      xComp = float((2.0**0.5)*cos(theta))
      yComp = float((2.0**0.5)*sin(theta))
##      xComp = float(cos(theta))
##      yComp = float(sin(theta))
      rTemp = rTemp + xComp
      cTemp = cTemp + yComp
      index = int(rTemp)*width+int(cTemp)
   return votes 
   
def thin(myText, header, width, height):
   printFile = open(filename + "Thin.ppm", "w+")
   printFile.write(header + "\n" + width + "\n" + height + "\n255\n")
   myCompareText = open(filename + "ReBlur.ppm").read().split()
   for i in range(0, 4):
      myCompareText.pop(0)
   r, c = 0, 0
   myFinalText = []
   myFinalCompareText = []
   width, height = int(width), int(height)
   i = 0
   while i < len(myText):
      myFinalText.append(myText[i+1])
      myFinalCompareText.append(myCompareText[i])
      i = i + 3
   while r < height:
      while c < width:
         index = (r*width) + c
         if not isEdge(width, height, index):
            if int(myFinalText[index]) == 0:
               gxVal = calcGX(myFinalCompareText, index, width)
               gyVal = calcGY(myFinalCompareText, index, width)
               print(gxVal, gyVal)
               theta = atan2(gyVal, gxVal)

               curr = abs(gxVal) + abs(gyVal)
               if theta == -1*pi or theta == pi:
                  print("n s")
                  second = abs(calcGX(myFinalCompareText, index - width, width)) + abs(calcGY(myFinalCompareText, index - width, width))
                  third = abs(calcGX(myFinalCompareText, index + width, width)) + abs(calcGY(myFinalCompareText, index + width, width))
                  print(second, third)
               elif theta > -1*pi and theta < 0:
                  print("se nw")
                  second = abs(calcGX(myFinalCompareText, index - width+1, width)) + abs(calcGY(myFinalCompareText, index - width+1, width))
                  third = abs(calcGX(myFinalCompareText, index + width-1, width)) + abs(calcGY(myFinalCompareText, index + width-1, width))
                  print(second, third)
               elif theta == 0:
                  print("e w")
                  second = abs(calcGX(myFinalCompareText, index -1, width)) + abs(calcGY(myFinalCompareText, index -1, width))
                  third = abs(calcGX(myFinalCompareText, index +1, width)) + abs(calcGY(myFinalCompareText, index +1, width))
                  print(second, third)
               elif theta > 0 and theta < pi:
                  print("nw se")
                  second = abs(calcGX(myFinalCompareText, index - width+1, width)) + abs(calcGY(myFinalCompareText, index - width+1, width))
                  third = abs(calcGX(myFinalCompareText, index + width-1, width)) + abs(calcGY(myFinalCompareText, index + width-1, width))
                  print(second, third)
               else:
                  print("ERROR ERROR ERROR")
               if max(curr, second, third) == curr:
                  printFile.write("255 0 0\n")
               else:
                  printFile.write("255 255 255\n")
            else:
               printFile.write("255 255 255\n")

         else:
            printFile.write("255 255 255\n")
         c = c + 1
      r = r+1
      c = 0
   printFile.close()
def calcGY(myText, index, width):
   gy1Val = -1*int(myText[index-width-1]) + int(myText[index-width+1])
   gy2Val = -2*int(myText[index-1]) + 2*int(myText[index+1])
   gy3Val = -1*int(myText[index+width-1]) + int(myText[index+width+1])
   #gxVal = int((gx1Val + gx2Val + gx3Val)/16)
   gyVal = int((gy1Val + gy2Val + gy3Val))
   return gyVal

def calcGX(myText, index, width):
   gx1Val = -1*int(myText[index-width-1]) + -2*int(myText[index-width]) + -1*int(myText[index-width+1])
   gx3Val = int(myText[index+width-1]) + 2*int(myText[index+width]) + int(myText[index+width+1])
   #gyVal = int((gy1Val + gy3Val)/16)
   gxVal = int((gx1Val + gx3Val))
   return gxVal
main()
  


