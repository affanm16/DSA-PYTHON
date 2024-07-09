
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
    
class CircularDLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __str__(self):
        result = ''
        currentNode = self.head
        while currentNode:
            result += str(currentNode.value)
            currentNode = currentNode.next
            if currentNode == self.head: 
                break
            result += ' <-> '
        return result
    

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1   

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1   

    def traverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
            if currentNode == self.head:
                break    
    def reverse_traverse(self):
        currentNode = self.tail
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.prev
            if currentNode == self.tail:
                break
    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        currentNode = None
        if index < self.length // 2:
            currentNode = self.head
            for i in range(index):
                currentNode = currentNode.next
        else:
            currentNode = self.tail
            for i in range(self.length - 1, index, -1):
                currentNode = currentNode.prev

        return currentNode

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

new_cdl=CircularDLL()
new_cdl.append(10)
new_cdl.append(20)
new_cdl.append(30)
new_cdl.append(40)
# print(new_cdl)
# new_cdl.prepend(-10)
print(new_cdl)
new_cdl.set_value(2,23)
print(new_cdl)

