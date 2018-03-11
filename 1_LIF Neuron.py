import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from pylab import *

I = 1.5 #Input Current, in Amps - Edit this to change input current

T = 200 #Time to simulate, in ms
dT = 0.1 #the dT time step in dV/dT
VArray = zeros((T/dT) + 1) #Array of membrane potentials, for plotting later
Vt = 1 #Threshold, in V
Vr = 0.0 #Reset potential, in mV
initialV = 0.0 #Initial Membrane Potential = Formula is change in mV
R = 1.0 #Membrane resistance, in kOhms
C = 10 #Capacitance in uF
tauM = R*C #Membrane time constant, in miliseconds

currentChangeInPotential = float(10.0) #Change in current membrane potential - Used in array

counter = 0.0
for i in range(0, len(VArray)) :
	currentChangeInPotential = (-1*VArray[i-1] + R*I)
	VArray[i] = VArray[i-1] + currentChangeInPotential/tauM*dT
	if(VArray[i] >= Vt):
		VArray[i] = Vr

#Plotting Code
currTime = arange(0, T+dT, dT) 
plt.plot(currTime, VArray)
plt.xlabel('Time in miliseconds')
plt.ylabel('Membrane Potential in Volts')
plt.title('Simulation - LIF Neuron')
plt.ylim([0,4])
plt.show()