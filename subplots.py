import matplotlib.pyplot as plt
import numpy as np


# Independent Variable
t = np.linspace(0, 10, 500)


# Parameters
A = 5 # m
phi = 2 # rad
f = 0.13 # s-1

y1 = A * np.sin(2* np.pi * f * t + phi) # Sine wave
y2 = A * np.cos(4 * np.pi * f * t + 2 * phi) # cosine wave

y_net = y1 + y2 # superimposed wave of cosine and sine wave


# Defining the figure and axes
msc = [
       ['sine', 'superimposed'],
       ['cosine', 'superimposed']
]
fig = plt.figure(figsize=(12, 10), facecolor='#c0fad8')
ax = fig.subplot_mosaic(msc)


# Adding properties to the axes
ax['sine'].set_title("Representing the sine function")
ax['cosine'].set_title("Representing the cosine function")
ax['superimposed'].set_xlabel("t -->")
ax['superimposed'].set_ylabel("Wave function -->")
ax['superimposed'].set_title("Superimposed the two waves: ")


# Toggling grid 'on'
ax['sine'].grid(True)
ax['cosine'].grid(True)
ax['superimposed'].grid(True, color='pink')




# Plotting lines
line_sine = ax['sine'].plot(t,
    y1,
    linestyle='--',
    lw=4,
    color='green',
    label="Sine Function")

line_cosine = ax['cosine'].plot(t,
    y2,
    linestyle='--',
    lw=4,
    color='#faaa39',
    label='Cosine Function')

line_Superposed = ax['superimposed'].plot(t,
    y_net,
    lw = 5,
    color='red',
    label='Superimposed Function')


# Plot properties
ax['sine'].legend()
ax['cosine'].legend()
ax['superimposed'].legend()


plt.show()