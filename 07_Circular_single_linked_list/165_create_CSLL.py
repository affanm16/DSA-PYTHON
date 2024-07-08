class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    #creating single valued CSLL
    def __init__(self):
        new_node=Node(value)
        new_node.next=new_node
        self.head=new_node
        self.tail=new_node
        self.length=1

csslinkedlist=CircularSinglyLinkedList()
