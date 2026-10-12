"""
Calculating Kinetic Energy
Formula: KE = \frac{1}{2}mv^2

"""





# Defining the function to calculate the kinetic energy
def calcKE(mass, speed):
    return 0.5 * mass * speed**2 


try:
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    
    print(f"Kinetic Energy: {calcKE(mass, velocity)} joules")
except ValueError:
    print("Please enter a float!")