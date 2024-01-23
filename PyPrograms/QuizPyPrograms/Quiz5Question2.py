#Quiz5Question2.py

def Eccentricity(self, x):
    """Return the eccentricity of x."""
    # your code begins here
    # initialize
    undiscovered = set(self.vertices)  
    discovered   = Queue()             
    finished     = set()               
    for v in self.vertices:
        self._distance[v] = 'Infinity'
        self._predecessor[v] = None
    # end
    undiscovered.remove(x)        
    discovered.enqueue(x)         
    self._distance[x] = 0
    while not discovered.isEmpty():
        i = discovered.dequeue()     
        for y in self._adj[i]:
        if y in undiscovered:
            undiscovered.remove(y)       
            discovered.enqueue(y)     
            self._distance[y] = self._distance[x]+1  
            self._predecessor[y] = i                  
        # end
        # end
        finished.add(i)             
        maxValue = max(finished)
        print(maxValue)
    return maxValue
    # end
# end

