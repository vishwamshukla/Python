class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.first = Node(None)
        self.last = Node(None)
        self.first.next = self.last
        self.last.next = self.first
        
    def add(self,data):
        p = Node(data)
        
        if self.first.data is None:
            self.first = p
            self.last = p
            p.next = self.first
        else:
            self.last.next = p
            self.last = p
            self.last.next = self.first
            
    def display(self):
        p = self.first
        if p is None:
            print("Linked list is empty")
            return
        else: 
            print(p.data)
            while(p.next is not self.first):
                p=p.next
                print(p.data)
    def delete(self,index):
        if index ==1:
            p=self.first
            self.first = self.first.next
            p=None
        elif(index >1):
            p =self.first
            q = None
            for i in range(index -1):
                q=p
                p=p.next
            q.next = p.next
            p = None

c1 = CircularLinkedList()
c1.add(10)
c1.add(20)
c1.add(30)
c1.add(40)

c1.delete(1)
c1.display()