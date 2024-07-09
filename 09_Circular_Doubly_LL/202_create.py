class Node:
    def __init__(self,value):
        self.value=None
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
class CircularDLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

new_cdl=CircularDLL()
print(new_cdl)
