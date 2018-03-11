from __future__ import division
from scipy import integrate
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

# Various Channel functions given by: http://neurdon.wpengine.com/2011/01/26/neural-modeling-with-python-part-2/
# Channels change according to input currents, and therefore, you need to be able to calculate them 
alphaN = vectorize(lambda v: 0)
betaN  = lambda v: 0
dn   = lambda v: 0

alphaM = vectorize(lambda v: 0.1*(-(v) + 25.0)/((exp((-(v) + 25.0)/10.0) - 1)) if (v) != 25.0 else 1.0)
betaM  = lambda v: 4.0*(exp(-v/18.0))
dm   = lambda v: alphaM((v))/(alphaM((v)) + betaM(v))

alphaH = lambda v: 0.07*exp(-(v)/20)
betaH  = lambda v: 1.0/(exp((-(v) + 30.0)/10.0) + 1.0)
dh   = lambda v: alphaH((v))/(alphaH((v)) + betaH((v)))

#Misc variables for HH model
Vr = -65      	# In mV
C = 1      		# In uF/cm2
gNa = 120   	# In mS/cm2
gK = 36     	# In mS/cm2
gL = 0.3    	# In mS/cm2
VNa = 0    		# Reverse Sodium Potential In mV
VK = -12    	# Reverse Potassium Potential In mV
VL = 10.613 	# Reverse Leak Channel Potential In mV

I = 10			#Input Current

m = (dm(Vr))   
h = (dh(Vr))
n = (dn(Vr))

T = 75
dT = 0.001
currTime = arange(0, T+dT, dT)

VArray = zeros(len(currTime))
VArray[0] = Vr 


for i in range(len(currTime)):
	m += (alphaM(VArray[i-1])*(1.0 - m) - betaM(VArray[i-1])*m) * dT
	h += (alphaH(VArray[i-1])*(1.0 - h) - betaH(VArray[i-1])*h) * dT
	n += (alphaN(VArray[i-1])*(1.0 - n) - betaN(VArray[i-1])*n) * dT
	VArray[i] = VArray[i-1] + (I - gNa * m**3 * h * (VArray[i-1] - VNa) - gK * n**4 * (VArray[i-1] - VK) - gL * (VArray[i-1] - VL))/C * dT

plt.plot(currTime, VArray)
plt.title("Simulation - Pronase in HH Neuron")
plt.ylabel("Membrane Potential in mv")
plt.xlabel("Time in miliseconds")
plt.show()
