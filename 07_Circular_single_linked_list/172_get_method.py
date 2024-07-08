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
    def insert(self,index,value):
        new_node=Node(value)
        if index>self.length or index <0:
            raise Exception("Index out of range")
        if index==0:
            if self.head is None:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        elif index==self.length:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        else:
            temp_node=self.head
            for  _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
            self.length+=1
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
            if current==self.head:
                break
    def search(self,target):
        current=self.head
        while current is not None:
            if current.value==target:
                return True
            current=current.next
            if current==self.head:
                break
        return False




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
cslinkedlist.traverse()
print(cslinkedlist.search(20))
#o(n),O(1)