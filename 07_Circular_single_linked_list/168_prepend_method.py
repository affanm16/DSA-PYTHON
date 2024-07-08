#append method adds a single element at theend



class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1

    def prepend(self,value):
            new_node=Node(value)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            else:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
            self.length+=1



    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
            result+='->'
        return result





cslinkedlist=CircularSinglyLinkedList()

cslinkedlist.prepend(0)
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
print(cslinkedlist)
cslinkedlist.prepend(100)
print(cslinkedlist)


# print(cslinkedlist.head.value)
# print(cslinkedlist.head.next.value)

#time complexity of prepend method O(1) 
#space complexity of prepend method  O(1)