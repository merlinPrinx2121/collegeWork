"""
Calculating the roots of Quadratic Equations



let the quadratic equation be defined as:
    P(x) = ax^2 + bx + c
    where x = (-b +- sqrt(b^2 - 4ac))/2a
    
"""

import numpy as np






print("********** Quadratic Equation Solver ***********")
print("P(x) = ax^2 + bx + c")





# Defining the quadratic equation
def poly(a, b, c):
    print(f"The quadratic equation is: {a}x^2 + {b}x + {c}")
    D = b**2 - 4*a*c
    
    if (D>0):
        print("There are two real and distinct roots")
        x1 = (-b + np.sqrt(D))/2*a
        x2 = (-b - np.sqrt(D))/2*a
        print(f"Roots are: {x1}, {x2}")
    elif (D==0):
        print("There is only one real root")
        x = -b/(2*a)
        print(f"Root is: {x}")
    elif (D<0):
        print("Roots are conjugate complex pairs")
        print(f"Complex conjugate roots are: {-b/(2*a)} + i({(np.sqrt(-D))/(2*a)}) , {-b/(2*a)} - i({(np.sqrt(-D))/(2*a)})")



# Running the program:
try:
    # Coefficients of the quadratic equations
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    poly(a, b, c)
except ValueError:
    print("Invalid Equation. Please try again!")
    