import numpy as np
import matplotlib.pyplot as plt







# Our defined varuiables
x_values = np.arange(-10, 11, 0.23)
y_values = np.tan((x_values) + 3)


"""
# Using functions to generate the values of y
def myFunc(val):
    return val**3 - 4*val
y_values = [myFunc(val) for val in x_values]
"""



"""
# Creating a dummy error for x and y values
x_err = [0.1, 0.2, 0.1, 0, 0.3, 0.2, 0.4, 0.2, 0.1, 0.1]*2
y_err = [0.2, 0.4, 0.2, 0, 0.6, 0.2, 0.8, 0.4, 0.2, 0.2]*2
"""

# Defining our figure and adding an axes to it
fig = plt.figure(figsize=(6, 4), facecolor="#FFEFC4")
axs = fig.add_subplot(111)

# Adding a line to the axes
line1 = axs.scatter(x_values, y_values, marker='o', label='Y = X^2', s=3)

# Controlling the parameters of the axes
axs.set_title("Plotting y vs x: ")
axs.set_ylabel('-- y --> ')
axs.set_xlabel('-- x --> ')

# Adding the line status on the upper center position
plt.legend(loc='upper center', fontsize=15)

"""
# Adding the error bar to the plot showing the the region of values where the actual values could be found!
line_err = axs.errorbar(x_values, y_values, xerr=x_err, yerr=y_err, ecolor='red', fmt='none')
"""





plt.show()
