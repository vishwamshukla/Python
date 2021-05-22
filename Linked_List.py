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
        #self.DisplayRecursive(self.first)   #To display LL in recursive fashion
    def insert(self,index,data):
        p = Node(data)
        t= self.first
        if(index==0):
            p.next = self.first
            self.first = p
        else:
            for i in range(index-1):
                t = t.next
            p.next = t.next
            t.next = p
    def DisplayRecursive(self, current):
        if current is None:
            return
        else:
            print(current.data, end = " ")
            self.DisplayRecursive(current.next)
    def count(self):
        p = self.first
        count = 0
        while(p is not None):
            count+=1
            p = p.next
        print(count)
    
    def sum(self):
        p = self.first
        sum=0
        while(p is not None):
            sum+=p.data
            p=p.next
        print(sum)
    def max(self):
        max = -32768
        p=self.first
        while(p is not None):
            if(p.data > max):
                max = p.data
            else:
                p = p.next
        print(max)
        
    def min(self):
        min = 32768
        p=self.first
        while(p is not None):
            if(p.data < min):
                min = p.data
            else:
                p = p.next
        print(min)
        
    def search(self, key):
        p = self.first
        while(p is not None):
            if(key == p.data):
                print("Found")
            p = p.next
        print("Not Found")
ll = LinkedList()
# n = int(input("How many you like to add?"))
# for i in range(n):
#     data = int(input("Enter data"))
#     ll.append(data)
ll.insert(0,10)
ll.insert(1,20)
ll.insert(2,30)
ll.insert(3,40)
ll.insert(3,50)    
ll.display()
ll.count()
ll.sum()
ll.max()
ll.min()
ll.search(60)