# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:06:25 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
import CoolProp.CoolProp as cp   # for thermodynamics state lookups

#%% 3.1.1

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


#State 2
p2 = 0.2 #bar
s2s =  s1 #J/kg*K
h2s = cp.PropsSI('H','P',p2*PaPerBar,'S',s2s, fl) #J/kg

#State 3 (Will be sat liquid)
p3 =  0.2 #bar
x3 = 0 #quality
T3 =  cp.PropsSI('T','P',p3*PaPerBar,'Q',x3, fl) #K
s3 =  cp.PropsSI('S','P',p3*PaPerBar,'Q',x3, fl) #J/kg*K   
h3 =  cp.PropsSI('H','P',p3*PaPerBar,'Q',x3, fl)  #J/K
 

#Isentropic Efficiecny of Pump
nPump=0.85
s4s = s3
p4 = 200 #bar
h4s= cp.PropsSI('H','P',p4*PaPerBar,'S',s4s, fl)
h4 = h3+((h4s-h3)/nPump)

#State 4
p4= 200 #bar
Win = -mf*(h3-h4)
s4 = cp.PropsSI('S','P',p4*PaPerBar,'H',h4, fl) #J/kg*K
T4 = cp.PropsSI('T','P',p4*PaPerBar,'H',h4, fl)

#Qin Boiler
Qin = -mf*(h4-h1) #J/s


#%% Ploting

IsenEffMin = .75
IsentEffMax = 1
nn = 26 # number of temperature entries in array
sigmaArr = np.linspace(IsenEffMin,IsentEffMax,nn)    

# Setup a loop to calculate Win and T2 for different values of entropy production
Wnet_array = np.empty(nn)
ThermalEff_array = np.empty(nn)
h2_array = np.empty(nn)
for (i,IsenEff) in enumerate(sigmaArr):
    h2_array[i] = (h1 - (IsenEff*(h1-h2s)))/1000  # kj/kg
    Wnet_array[i] = (((h1/1000)-h2_array[i])*mf) - (Win/1000)
    ThermalEff_array[i] = (Wnet_array[i]/(Qin/1000))
    
    
# Plot!
plt.figure(1)
plt.clf()
plt.plot(sigmaArr,Wnet_array,'-r')
plt.xlabel(' Isentropic Efficiency of Turbine')
plt.ylabel('Net Power Output (kJ/s)')
plt.title('Net Power Output v.s. Varying Turbine Efficiency ')

# Plot!
plt.figure(2)
plt.clf()
plt.plot(sigmaArr,ThermalEff_array,'-r')
plt.xlabel(' Isentropic Efficiency of Turbine')
plt.ylabel('Cycle Thermal Eff ')
plt.title('Cycle Thermal Efficiency v.s. Varying Turbine Efficiency ')
