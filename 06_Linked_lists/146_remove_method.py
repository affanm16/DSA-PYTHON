#remove method  removes a particular node
#pop method
#pop first method removes the first node and returns it
#set method takes the index and updates the value at that position
#get method when given index returns the value
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=Node(value)
        #for adding in empty linked list
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length += 1
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def insert(self,index,value):
        new_node=Node(value)
        if index<0 or index>self.length:
            return False
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        elif index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1

    def traverse(self):
        current_node=self.head
        while current_node is not None:     #or while current:
            print(current_node.value)
            current_node=current_node.next

    def search(self,target):
        current=self.head
        while current:
            if current.value==target:
                return True
        return False

    def get(self,index):
        if index<0 or  index>=self.length:
            return None
        current=self.head
        for _ in range(index):
            current=current.next
        return current
    


    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    

    def pop_first(self):
        popped_node=self.head
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            popped_node.next=None
        self.length-=1
        return popped_node.value


    def pop(self):
        popped_node=self.tail
        if self.length==0:
            return None
        if self.length==1:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
            self.length-=1
            return popped_node.value

    
    def remove(self,index):
        if index >= self.length or index<0:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        prev_node=self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node



    def __str__(self):
         temp_node=self.head
         result=''
         while temp_node is not None:   #none marks end of linked list
             result+=str(temp_node.value)
             if temp_node.next is not None:
                 result+=' -> '
             temp_node=temp_node.next
         return result
    


new_linked_list=LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.remove(1))
print(new_linked_list)


#time and space complexity for remove method O(n),O(1)