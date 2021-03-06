# class Computer:    #Class computer is created with method Config
    
#     def __init__(self,cpu, ram):
#         self.cpu = cpu
#         self.ram = ram    
#     def config(self):
#         print("Config for the pc is ", self.cpu, self.ram)
        

# com1 = Computer(2,4)  # object of the class computer
# com2 = Computer(5,6)
# # Computer.config(com1)
# # Computer.config(com2)

# com1.config()
# com2.config()


# class Student:
    
#     def __init__(self):
#         self.name = "Vishwam"
#         self.age = 21
#     def compare(self, other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
# s1 = Student()
# s1.age = 22
# s2 = Student()

# if s1.compare(s2):
#     print("They are same")
# else:
#     print("Not same")

# print(s1.name)
# print(s2.name)


# class Car:
#     wheels = 4     #class variable
#     def __init__(self):
#         self.mil = 10          #instance variable
#         self.com = "BMW"       #instance variable
        
# c1 = Car()
# c2 = Car()
# Car.wheels = 5
# print(c1.com,c1.mil,c1.wheels)

# class Student:
#     school = "MIT"
    
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#     def avg(self):       #instance method
#         return (self.m1+self.m2+self.m3)/3
#     @classmethod
#     def info(cls):       #class method
#         return cls.school
#     @staticmethod        #static method
#     def infoStatic():
#         print("This is the MIT college")
# s1 = Student(11,22,33)
# s2 = Student(22,33,44)

# print(s1.avg())
# print(s2.avg())
# print(Student.info())
# Student.infoStatic()

#Class inside a class 
# class Student:                     #outer class
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()
#     def show(self):
#         print(self.name,self.rollno)
        
    
#     class Laptop:                  #inner class
#         def __init__(self):
#             self.brand="Dell"
#             self.cpu="i5"
#             self.ram=8
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
    
# s1 = Student("Vishwam",20)
# s2 = Student("Shukla",23)

# s1.show()
# s2.show()

# lap1 = Student.Laptop()
# lap2 = Student.Laptop()

# lap1.show()

#inheritance
# class A:               #Parent class or Super class
#     def feature1(self):
#         print("Feature 1 is working")
#     def feature2(self):
#         print("Feature 2 is working")
#  #Single level        
# class B(A):            #Child class or Sub class
#     def feature3(self):
#         print("Feature 3 is working")
#     def feature4(self):
#         print("Feature 4 is working")

# #Multilevel Inheritance        
# class C(B):            #Child class or Sub class
#     def feature5(self):
#         print("Feature 5 is working")
#     def feature6(self):
#         print("Feature 6 is working")
 
#  #Multiple Inheritance       
# class C(A,B):            #Child class or Sub class
#     def feature5(self):
#         print("Feature 5 is working")
#     def feature6(self):
#         print("Feature 6 is working")
# a1 = A()
# a1.feature1()
# a1.feature2()

# b1=B()
# b1.feature2()

# c1=C()
# c1.feature1()


#Constructors and Super class 
# class A:    
#     #Parent class or Super class
    
#     def __init__(self):   #Constructors
#         print("In A init")
    
#     def feature1(self):
#         print("Feature 1-A is working")
#     def feature2(self):
#         print("Feature 2 is working")
#  #Single level        
# class B:            #Child class or Sub class
    
#     def __init__(self):
#         print("In B init")
#     def feature3(self):
#         print("Feature 3 is working")
#     def feature4(self):
#         print("Feature 4 is working")
# #MRO(Method resolution order)  
# class C(A,B):
#     def __init__(self):
#         super().__init__()  #will call init of A class first(goes from left to right C->A->B)
#         print("In C init")
#     def feat(self):
#         super().feature2()
# a1 = C()
# a1.feat()




#Polymorphism (Poly- Many, Morph - Form) 

#Duck typing

# class PyCharm:
#     def execute(self):
#         print("Compile")
#         print("Run")
# class Laptop:
#     def code(self,ide):
#         ide.execute()
        
# ide=PyCharm()
# lap1 = Laptop()
# lap1.code(ide)


#operator overloading



# a=1
# b=3

# print(int.__add__(a,b))  #behind the scene of print(a+b)

class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        
        return s3
        
s1=Student(2,2)
s2 = Student(3,4)

s3 = s1+s2  #-> Student.__add__(s1,s2)

print(s3.m1 -1)