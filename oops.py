class Computer:    #Class computer is created with method Config
    
    def __init__(self,cpu, ram):
        self.cpu = cpu
        self.ram = ram    
    def config(self):
        print("Config for the pc is ", self.cpu, self.ram)
        

com1 = Computer(2,4)  # object of the class computer
com2 = Computer(5,6)
# Computer.config(com1)
# Computer.config(com2)

com1.config()
com2.config()