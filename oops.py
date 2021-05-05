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
class Student:                     #outer class
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
    def show(self):
        print(self.name,self.rollno)
        
    
    class Laptop:                  #inner class
        def __init__(self):
            self.brand="Dell"
            self.cpu="i5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)
    
s1 = Student("Vishwam",20)
s2 = Student("Shukla",23)

s1.show()
s2.show()

lap1 = Student.Laptop()
lap2 = Student.Laptop()

lap1.show()