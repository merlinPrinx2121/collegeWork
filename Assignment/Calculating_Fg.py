"""
Calculating Gravitational Force
Formula: |F| = Gm1m2/r^2
"""




# Physical Constants
G = 6.67 * 1e-11 # kg-1 m3 s-2


# Defining a function returning the force acting between particles separated by a distance r and having masses m1 and m2
def calcF(m1, m2, r):
    return G*m1*m2 / (r**2)


try:
    m1 = float(input("Enter the mass of first particle (kg): "))
    m2 = float(input("Enter the mass of second particle (kg): "))
    distance = float(input("Enter the distance between particles (m): "))
    
    print(f"Gravitational Force: {calcF(m1, m2, distance)} N")
except ValueError:
    print("Please enter numeric value!")
