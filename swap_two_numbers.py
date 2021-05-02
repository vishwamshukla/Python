a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))

temp = a
a = b
b = temp

print("The value of a and b after swapping is {0} and {1} respectively".format(a,b))