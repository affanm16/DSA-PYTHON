class Node:
    def __init__(self,value):
        self.value=value
        self.next=None




class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=new_node
#time and space complexity =O(1),

new_linked_list=LinkedList(20)
print(new_linked_list)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)




