class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1


    
newDLL=DoublyLinkedList()
newDLL.append(40)
newDLL.append(30)
newDLL.append(20)
newDLL.append(10)
print(newDLL.head)
print(newDLL.head.next)
print(newDLL.tail)

#time complexity=O(1),O(1)