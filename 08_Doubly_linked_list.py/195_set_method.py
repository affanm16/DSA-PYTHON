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
    def reverse_traverse(self):
        current_node=self.tail
        while current_node:
            print(current_node.value)
            current_node=current_node.prev
         
    def search(self,target):
        current_node=self.head
        index=0
        while current_node:
            if current_node.value==target:
                return index
            current_node=current_node.next
            index+=1
        return -1
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        if index< self.length//2:
            current_node=self.head
            for _ in range(index):
                current_node=current_node.next
        else:
            current_node=self.tail
            for _ in range(self.length-1,index,-1):
                current_node=current_node.prev
            return current_node
    def set(self,index,value):
        node=self.get(index)
        if node:
            node.value=value
            return True
        return False



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
newDLL.set(2,200)
print(newDLL)

#O(n),O(1)