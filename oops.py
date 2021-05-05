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


class Student:
    
    def __init__(self):
        self.name = "Vishwam"
        self.age = 21
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
s1 = Student()
s1.age = 22
s2 = Student()

if s1.compare(s2):
    print("They are same")
else:
    print("Not same")

print(s1.name)
print(s2.name)