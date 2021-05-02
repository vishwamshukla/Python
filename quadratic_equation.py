import cmath

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

print("Equation is "+ str(a) +"X^2"+" + "+str(b)+"x"+" + "+ str(c)+" = 0")

inner_value = (b**2) - (4*a*c)


s1 = (-b - cmath.sqrt(inner_value)) / 2*a
s2 = (-b + cmath.sqrt(inner_value)) / 2*a

print("Solutions of the Quadratic equation are {0} and {1}". format(s1, s2))