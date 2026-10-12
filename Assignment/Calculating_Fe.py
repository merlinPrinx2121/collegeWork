"""
Calculating Electric Force between two Particles
Formula: Fe = kq1q2/(r^2)
"""







# Physical Constant
k = 8.99 * 1e9


# Defining the function calculating the Columbic Electrostatic Force between charge particles
def calcFe(q1, q2, r):
    return k * q1 * q2 / (r**2)


try:
    charge1 = float(input("Enter the charge on the first particle (C) : "))
    charge2 = float(input("Enter the charge on the second particle (C) : "))
    distance = float(input("Enter the distance between the two particles (m) : "))
    Fe = calcFe(charge1, charge2, distance)
    
    print(f"Electric Force: {Fe:.2f} N")
except ValueError:
    print("Enter Numeric Value!")