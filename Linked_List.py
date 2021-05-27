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
        
    def sortedInsert(self,data):
        t = Node(data)
        if(self.first == None):
            self.first = t
        else:
            p = self.first
            q = None
            while(p is not None and p.data < data):
                q = p
                p=p.next
            t.next = q.next
            q.next = t
    def delete(self,index):
        if(index < 1 and index > self.count()):
            print("Something is wrong")
        if(index ==1):
            p = self.first
            self.first = self.first.next
            p = None
        elif(index > 1):
            p = self.first
            q = None
            for i in range(index -1):
                q = p
                p = p.next
            q.next = p.next
            p = None
    def CheckifLLisSorted(self):
        x = -32768
        p = self.first
        while(p is not None):
            if(x > p.data):
                return False
            else:
                x = p.data
                p = p.next
        return True
    def removeDups(self):
        p = q = self.first
        while p is not None:
            while q.next is not None:   # check second.next here rather than second
                if q.next.data == q.data:   # check second.next.data, not second.data
                    q.next = q.next.next   # cut second.next out of the list
                else:
                    q = q.next   # put this line in an else, to avoid skipping items
            p = q = q.next
                    
ll = LinkedList()
# n = int(input("How many you like to add?"))
# for i in range(n):
#     data = int(input("Enter data"))
#     ll.append(data)
ll.insert(0,10)
ll.insert(1,10)
ll.insert(2,30)
ll.insert(3,40)
ll.insert(4,50)
# ll.count()
# ll.sum()
# ll.max()
# ll.min()
# ll.search(60)
# ll.sortedInsert(35)
#ll.delete(4)
ll.display()
print(ll.CheckifLLisSorted())
ll.removeDups()
ll.display()