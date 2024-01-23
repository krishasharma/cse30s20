#Quiz4Question2

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class List:
    def __init__(self):
        self.start_node = None

    def insert7(self, x, data):
        self.item = 7
        x = 2
        n = self.start_node
        print(n.next)
        while n is not None:
            x = 2 
            if n.item == x:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(self.item)
            new_node.next = n.next
            n.next = new_node
    # end
# end

