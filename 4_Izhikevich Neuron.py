import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from pylab import *

#These specific values simulate the Izhikevich Tonic Spiking Neuron
#To simulate other type of Izhikevich neurons, change these values
#Parameters received from wikipedia
a = 0.02 	#A variable
b = 0.2
c = -65
d = 6
v = -70 	#Initial membrane potential
u = 0 		#Initial Membrane Recovery Variable
I = 15
T = 200.0 	#Duration for Simulation
dT = 0.1	#dT for which to integrate

VArray = zeros(int((T/dT) + 1.0))
UArray = zeros(int((T/dT) + 1))
currTime = arange(0, T+dT, dT) 

for i in range(len(currTime)) :
	v += (0.04*v**2 + 5*v + 140 - u + I)*dT
	u += (a*(b*v - u))*dT
	if(v >= 30):
		VArray[i] = 30
		v = c
		u += d
	else: 
		VArray[i] = v
		UArray[i] = u


plt.plot(currTime, VArray)
plt.plot(currTime, UArray)
plt.title("Simulation - Izhikevich Tonic Spiking Neuron")
plt.xlabel("Time in miliseconds")
plt.ylabel("Membrane Potential in Volts")
plt.show()