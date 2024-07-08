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
# print(new_linked_list)
new_linked_list.prepend(-10)
# print(new_linked_list)
new_linked_list.insert(0,90)
# print(new_linked_list)

new_linked_list.traverse()

#time and space complexity O(n),O(1)