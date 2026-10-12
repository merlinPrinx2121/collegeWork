"""
Calculating Workdone by a constant force on a particle transversing in the same dimension at an angle theta
Formula: F dot d
"""

# Importing relevant function
import numpy as np





# Defining the function to calculate the Work Done
def calcWD(F, d, theta):
    return F * d * np.cos(theta)

try:
    Force = float(input("Enter the force acting on the particle (N) : "))
    displacement = float(input("Enter the displacement of particle (m) : "))
    theta = np.radians(float(input("Enter angle between the force acting on the particle and its displacement (deg): ")))
    WD = calcWD(Force, displacement, theta)
    
    print(f"Workdone by the Force: {WD:.2f} joules")
except ValueError:
    print("Please Enter Numeric Value!")