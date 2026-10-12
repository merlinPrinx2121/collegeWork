"""
Calculating Potential Energy for a uniform gravitational field
Formula: PE = mgh
"""






# Physical Constants
g = 9.81 # m/s^2

# Defining the function to calculate the Potential Energy
def calcPE(mass, height):
    return mass * height * g


try:
    mass = float(input("Enter the mass of the object (kg): "))
    height = float(input("Displacement of the object along the normnal of gravitational field level curves from the zero potential energy level (m): "))
    PE = calcPE(mass, height)
    print(f"Potential Energy: {PE:.2f} joules")
except ValueError:
    print("Enter numeric value!")