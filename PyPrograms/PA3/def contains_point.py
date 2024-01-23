   def contains_point(self, P): #if the self line contains point P, then it would return true
      """
      Return True if self contains point P, False otherwise.
      """
      y1 = other.Point.ycoord
      y2 = self.Point.ycoord 
      x1 = other.Point.xcoord
      x2 = self.Point.xcoord 
      deltaX = x1 - x2 
      deltaY = y1 - y2 
      
      if deltaX == 0 and deltaY == 0: #if points are same, on line 
         return True 
      
      elif deltaX == 0 and deltaY != 0 and self.slope != 0: 
         return False 

      elif deltaX == 0 and deltaY != 0 and self.slope == 0:
         return True

      m = deltaY / deltaX 
      
      if self.slope == m: 
         return True
      else: 
         return False 
    
      pass