# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:49:50 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
import CoolProp.CoolProp as cp   # for thermodynamics state lookups

#%% 3.1.2


fl = 'Water'

# Conversions
PaPerBar = 100000

#Knowns
mf= 500 #kg/s

#State 1
p1 = 200 #bar
T1 = cp.PropsSI('T','P',p1*PaPerBar,'Q',1, fl) +200 #K 
s1 =  cp.PropsSI('S','P',p1*PaPerBar,'T',T1, fl) #J/kg*K
h1 =  cp.PropsSI('H','P',p1*PaPerBar,'T',T1, fl) #J/kg

#Isentropic Efficiecny of Turbine @ State 2
p2= 0.2 #bar
nTurbine=0.85
s2s = s1
h2s= cp.PropsSI('H','P',p2*PaPerBar,'S',s2s, fl)
h2 =  h1 - nTurbine*(h1-h2s) #J/kg

#State 2
Wout = mf*(h1-h2)
s2 = cp.PropsSI('S','P',p2*PaPerBar,'H',h2, fl)
T2 = cp.PropsSI('T','P',p2*PaPerBar,'H',h2, fl)


#State 3 (sat liquid)
p3 =  0.2 #bar
x3 = 0 #quality
T3 =  cp.PropsSI('T','P',p3*PaPerBar,'Q',x3, fl) #K
s3 =  cp.PropsSI('S','P',p3*PaPerBar,'Q',x3, fl) #J/kg*K   
h3 =  cp.PropsSI('H','P',p3*PaPerBar,'Q',x3, fl)  #J/K


#State 4
p4= 200 #bar
s4s = s3
h4s = cp.PropsSI('H','P',p4*PaPerBar,'S',s4s, fl)

#%% Ploting

IsenEffMin = .75
IsentEffMax = 1
nn = 26 # number of temperature entries in array
sigmaArr = np.linspace(IsenEffMin,IsentEffMax,nn)    

# Setup a loop to calculate Win and T2 for different values of entropy production
Wnet_array = np.empty(nn)
ThermalEff_array = np.empty(nn)
h4_array = np.empty(nn)
Qin_array = np.empty(nn)
for (i,IsenEff) in enumerate(sigmaArr):
    h4_array[i] = (((h4s-h3)/IsenEff) +h3 )/1000 
    Wnet_array[i] = (Wout/1000) - (mf*(h4_array[i] - (h3/1000)))
    Qin_array[i] = (mf*((h1/1000)-h4_array[i]))
    ThermalEff_array[i] = ((Wnet_array[i])/(Qin_array[i]))

# Plot!
plt.figure(1)
plt.clf()
plt.plot(sigmaArr,Wnet_array,'-r')
plt.xlabel(' Isentropic Efficiency of Pump')
plt.ylabel('Net Power Output (kJ/s)')
plt.title('Net Power Output v.s. Varying Pump Efficiency ')

# Plot!
plt.figure(2)
plt.clf()
plt.plot(sigmaArr,ThermalEff_array,'-r')
plt.xlabel(' Isentropic Efficiency of Pump')
plt.ylabel('Thermal Eff ')
plt.title('Cycle Thermal Efficiency v.s. Varying Pump Efficiency ')
