# insertion in linked list
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
# print(new_linked_list.head.value)
# print(new_linked_list.tail.value)

#time and space complexity is O(1)


