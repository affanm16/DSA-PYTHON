class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
new_node=Node(30)
print(new_node)

#time complexity=O(1),O(1)