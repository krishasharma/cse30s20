#------------------------------------------------------------------------------
# Krisha Sharma 
# krvsharm
# CSE 30-02 Spring 2021
# lines.py
# Definition of the Point and Line classes.
#------------------------------------------------------------------------------
import math


#------------------------------------------------------------------------------
# Do not change the definition of the Point class, other than to define 
# the function join() at the end.
#------------------------------------------------------------------------------
class Point(object):
   """Class representing a Point in the x-y coordinate plane."""

   def __init__(self, x, y):
      """Initialize a Point object."""
      self.xcoord = x
      self.ycoord = y
   # end

   def __str__(self):
      """Return the string representation of a Point."""
      return '({}, {})'.format(self.xcoord, self.ycoord)
   # end

   def __repr__(self):
      """Return the detailed string representation of a Point."""
      return 'geometry.Point({}, {})'.format(self.xcoord, self.ycoord)
   # end

   def __eq__(self, other):
      """
      Return True if self and other have the same coordinates, False otherwise.
      """
      eqx = (self.xcoord==other.xcoord)
      eqy = (self.ycoord==other.ycoord)
      return eqx and eqy
   # end

   def distance(self, other):
      """Return the distance between self and other."""
      diffx = self.xcoord - other.xcoord
      diffy = self.ycoord - other.ycoord
      return math.sqrt( diffx**2 + diffy**2 )
   # end

   def norm(self):
      """Return the distance from self to the origin (0, 0)."""
      return self.distance(Point(0,0))
   # end

   def midpoint(self, other):
      """Return the midpoint of the line segment from self to other."""
      midx = (self.xcoord + other.xcoord)/2
      midy = (self.ycoord + other.ycoord)/2
      return Point(midx, midy)
   # end

   #---------------------------------------------------------------------------
   # Fill in the definition of this function, belonging to the Point class.
   #---------------------------------------------------------------------------
   def join(self, other):
      """
      If self==other return None. Otherwise return the line passing through 
      self and other.
      """

      m = (self.ycoord  - other.ycoord)/(self.xcoord - other.xcoord)
      P = Point(self.xcoord, self.ycoord)
      if self == other: 
         return None
         if self.xcoord == other.xcoord: 
            if self.slope == str('infinity'):
               return Line(self.xcoord, self.slope)
      else:  
         return Line(P, m)
      pass
   # end     

# end


#------------------------------------------------------------------------------
# Fill in the definitions of each method in the Line class.
#------------------------------------------------------------------------------
class Line(object):
   """Class representing a Line in the x-y coordinate plane."""
   #P = point 
   #m = slope
   #b = y intercept 
   #y = mx+b
   def __init__(self, P, m):
      """Initialize a Line object."""
      self.Point = P
      self.slope = m
      #b = self.P.xcoord 
      pass
   # end

   def __str__(self):
      """Return a string representation of a Line."""
      x = self.Point.xcoord
      y = self.Point.ycoord 
      return 'Line through ({}, {}) of slope {}'.format(x, y, self.slope)
      pass
   # end

   def __repr__(self):
      """ Return a detailed string representation of a Line."""
      x = self.Point.xcoord
      y = self.Point.ycoord 
      return 'lines.Line(point=({}, {}), slope={})'.format(x, y, self.slope)
      pass
   # end

   def __eq__(self, other):
      """
      Return True if self and other are identical Lines, False otherwise.
      """

      if self.slope == other.slope: 
         if self.Point.xcoord  - other.Point.xcoord == 0 and self.slope == str('infinity'):
            return True 
         elif self.Point.xcoord  - other.Point.xcoord == 0 and self.slope != str('infinity'):
            return False 
         m = (self.Point.ycoord  - other.Point.ycoord)/(self.Point.xcoord - other.Point.xcoord)
         if self.slope == m: 
            return True 
      return False 
      pass

   # end

   def parallel(self, other):
      """
      Return True if self and other are parallel lines, False otherwise.
      """

      m1 = self.slope 
      m2 = other.slope 
      if m1 == m2:
         return True
      return False 
      pass
   # end

   def perpendicular(self, other): #when the slopes are the negative reciprocals and they intersect at a 90 degree angle 
      """
      Return True if self and other are perpendicular lines, False otherwise.
      """

      m1 = self.slope
      m2 = other.slope
      if m1 == str('infinity') and m2 == 0: 
         return True 
      if m2 == str('infinity') and m1 == 0: 
         return True 
      if m2 == 0:
         return False
      if m1 == -1 * (1/m2):
         return True 
      else:
         return False 
      pass
   # end

   def contains_point(self, P): #if the self line contains point P, then it would return true
      """
      Return True if self contains point P, False otherwise.
      """
      
      if (P.xcoord - self.Point.xcoord)  == 0 and (P.ycoord - self.Point.ycoord) == 0: #if points are same, on line 
         return True 
      
      elif (P.xcoord - self.Point.xcoord)  != 0 and (P.ycoord - self.Point.ycoord) == 0 and self.slope == 0:
         return True

      elif (P.xcoord - self.Point.xcoord)  == 0 and (P.ycoord - self.Point.ycoord) != 0 and self.slope == str('infinity'): #vertical line 2/0 = inf
         return True 

      elif (P.xcoord - self.Point.xcoord)  != 0 and (P.ycoord - self.Point.ycoord) == 0 and self.slope != 0: 
         return False 

      #m = (P.ycoord - self.Point.ycoord) / (P.xcoord - self.Point.xcoord)  
      m = (self.Point.ycoord  - P.ycoord)/(self.Point.xcoord - P.xcoord)
      
      if self.slope == m: 
         return True

      else: 
         return False 
   
      pass

   # end

   def intersect(self, other): # Get help with this one too
      """
      If self and other are parallel, return None.  Otherwise return their
      Point of intersection.
      """

      if self.slope == other.slope or self.slope == "infinity" and other.slope == "infinity": #if the slopes of the lines self and other are the same
         return None    
      elif self.slope == "infinity": #no while loop
         y = other.slope * self.Point.xcoord + (other.Point.ycoord - (other.slope * other.Point.xcoord)) 
         return Point(self.Point.xcoord, y)
      elif other.slope == "infinity": #no while loop
         y = self.slope * other.Point.xcoord + (self.Point.ycoord - (self.slope * self.Point.xcoord)) 
         return Point(other.Point.xcoord, y)
      else: 
         x = ((other.Point.ycoord - (other.slope * other.Point.xcoord)) - (self.Point.ycoord - (self.slope * self.Point.xcoord))) / (self.slope - other.slope)
         y = other.slope * x + (other.Point.ycoord - (other.slope * other.Point.xcoord))
         return Point(x, y) 
      pass 

   def parallel_line(self, P): # y- intercept changes
      """Returns the Line through P that is parallel to self."""
      return Line(P, self.slope)
      pass
   # end

   def perpendicular_line(self, P):
      """Returns the Line through P that is perpendicular to self."""
      if self.slope == str('infinity'):
         m = 0 
         return Line(P, m)
      if self.slope == 0: 
         m = str('infinity')
         return Line(P, m)
      else: 
         m = -1 / (self.slope) 
         return Line(P, m) 
      pass
   # end

# end


#------------------------------------------------------------------------------
# Do not change functon main(). Its role is just to test all of the above.
# Actually you can change it during your own independent testing, but return
# it to exactly this state before you submit the project.
#------------------------------------------------------------------------------
def main():

   P = Point(1, 3)
   Q = Point(3, 3)
   R = Point(1, 1)
   S = Point(3, 1)
   T = Point(4, 3)
   U = Point(5, 5)
   V = Point(2, 2)
   W = Point(2, 5)
   X = Point(2, -1)

   A = Line(P, -1)
   B = Line(R, 1)
   C = S.join(T) #points_to_line(S, T)
   D = Line(W, 'infinity')
   E = Line(Q, 0)
   F = C.parallel_line(P)

   print()
   print('A =', A)
   print(repr(A))
   print()
   print('B =', B)
   print(repr(B))
   print()
   print('C =', C)
   print(repr(C))
   print()
   print('D =', D)
   print(repr(D))
   print()
   print('E =', E)
   print(repr(E))
   print()
   print('F =', F)
   print(repr(F))

   print()
   print(B.intersect(C)==U)
   print(A.intersect(B)==V)
   print(D.intersect(C)==X)
   print(D.intersect(Line(T,'infinity'))==None)
   print(A.perpendicular(B))
   print(D.perpendicular(E))
   print(A.parallel(B.perpendicular_line(Q)))
   print(A.contains_point(S))
   print(B.contains_point(U))
   print(C.contains_point(X))
   print(F.contains_point(W))

   print()

# end

#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end
