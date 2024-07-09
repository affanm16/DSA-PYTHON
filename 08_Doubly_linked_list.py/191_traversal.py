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
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=None
            self.tail=None
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1

    def traverse(self):
        current_node=self.head
        while current_node:
            print(current_node.value)
            current_node=current_node.next

         




    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result +='<=>'
            temp_node=temp_node.next
        return result


    
newDLL=DoublyLinkedList()
newDLL.append(40)
newDLL.append(30)
newDLL.append(20)
newDLL.append(10)
print(newDLL)
newDLL.prepend(0)
print(newDLL)
newDLL.traverse()

#O(n),O(1)