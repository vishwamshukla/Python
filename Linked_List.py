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
            
    def reverseLLbyelements(self):
        p = self.first
        i=0
        A =[]
        while(p is not None):
            A.append(p.data)
            p=p.next
            i+=1
        p=self.first
        i=i-1
        while(p is not None):
            p.data = A[i]
            i-=1
            p=p.next
    def reverseLLbyLinks(self):
        p=self.first
        q=None
        r = None
        while(p is not None):
            r=q
            q=p
            p=p.next
            q.next=r
        self.first=q    
        
    def concate(self,list2):
        p = self.first
        second = list2.first
        while(p.next is not None):
            p = p.next
        p.next = second
        second = None
        
    def merge(self,list2):
        p = self.first
        q = list2.first
        
        if(p.data < q.data):
            third = last = p
            p=p.next
            third.next = None
        else:
            third = last=q
            q=q.next
            third.next = None
            
        while(p and q):
            if(p.data < q.data):
                last.next = p
                last = p
                p=p.next
                last.next = None
            else:
                last.next = q
                last = q
                q = q.next
                last.next = None
        if(p is not None):
            last.next = p
        elif(q is not None):
            last.next = q        
          
    def checkLoop(self):
        p=q=self.first
        
        while(p and q and p is not q):
            p=p.next 
            q=q.next
            if(q):
                q=q.next
        if(p == q):
            print("Loop found")
        else:
            print("No loop found in the Linked list")
            
    def checkLoop2(self):
        slow = fast = self.first
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        if slow ==fast:
            print("Loop found")
        else:
            print("Loop not found")
ll = LinkedList()
ll1 = LinkedList()

# n = int(input("How many you like to add?"))
# for i in range(n):
#     data = int(input("Enter data"))
#     ll.append(data)
ll.insert(0,10)
ll.insert(1,30)
ll.insert(2,50)
ll.insert(3,60)
ll.insert(4,70)

2
ll1.insert(0,80)
ll1.insert(1,99)
ll1.insert(2,110)
ll1.insert(3,122)
# ll.count()
# ll.sum()
# ll.max()
# ll.min()
# ll.search(60)
# ll.sortedInsert(35)
#ll.delete(4)

#print(ll.CheckifLLisSorted())
#ll.removeDups()

#ll.reverseLLbyelements()
#ll.display()

#ll.reverseLLbyLinks()

#ll.concate(ll1)
#ll.display()
ll.merge(ll1)
ll.display()
ll.checkLoop2()