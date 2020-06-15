from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 2
    real=(-b)/(2*a)
    imaginary= sqrt(-r)/(2*a)
    x1=complex(real,imaginary)
    x2=complex(real,imaginary)
    print("There are 2 imaginary roots")
    print(x1,x2)
    
exit()
	
    

	
    
