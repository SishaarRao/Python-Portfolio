#
#
#Neighbor data structure
class NeighborContainer2:
   name = ""
   fullName = ""
   x = 0
   y = 0
   neighbors = []

   def __init__(self, a, x, y):
      self.name = a
      self.x = x
      self.y = y
      self.neighbors = []
   
   def compare(self, a):# 1 = 1 letter in common 2 = more than one letter
      flag = 0
      for i in range (0, len(a)):
         if not a[i] == self.word[i]:
            flag = flag + 1
         if flag > 1:
            return 2
      return flag
	    
         
   
      
   
   


#
#
