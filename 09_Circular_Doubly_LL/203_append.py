class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
class CircularDLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0


    

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1    

new_cdl=CircularDLL()
new_cdl.append(10)
new_cdl.append(20)
new_cdl.append(30)
new_cdl.append(40)
print(new_cdl)

