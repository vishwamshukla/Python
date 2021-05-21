class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def append(self,data):
        if self.last is None:
            self.first = Node(data)
            self.last = self.first
        else:
            self.last.next = Node(data)
            self.last = self.last.next
    def display(self):
        temp = self.first
        while temp is not None:
            print(temp.data)
            temp = temp.next
    
ll = LinkedList()
n = int(input("How many you like to add?"))
for i in range(n):
    data = int(input("Enter data"))
    ll.append(data)
ll.display()