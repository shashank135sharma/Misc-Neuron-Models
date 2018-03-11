import numpy as np
import matplotlib.pyplot as plt
from pylab import *

interval = 0.01
inputCurrent = arange(1.01, 10+interval, interval)
firingRate = range(900)

R = 1.0 #Membrane resistance, in kOhms
C = 10 #Capacitance in uF
tauM = R*C #Membrane time constant, in miliseconds
Vt = 1 #Threshold, in V

for i in range(len(inputCurrent)):
	T =  tauM * (np.log(inputCurrent[i]/(inputCurrent[i]-Vt)))
	firingRate[i] = (1/T)*1000

plt.plot(inputCurrent, firingRate)
plt.title('Simulation - LIF Neuron')
plt.xlabel('Input Current in Volts')
plt.ylabel('Firing Rate')
plt.show()