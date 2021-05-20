# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:40:10 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
import CoolProp.CoolProp as cp   # for thermodynamics state lookups

#%% 3.1.3


fl = 'Water'

# Conversions
PaPerBar = 100000

#Knowns
mf= 500 #kg/s

#State 1
p1 = 200 #bar


#Isentropic Efficiecny of Turbine @ State 2
p2= 0.2 #bar
nTurbine = 0.92

#State 2
p2= 0.2 #bar

#State 3 (sat liquid)
p3 =  0.2 #bar
x3 = 0 #quality
T3 =  cp.PropsSI('T','P',p3*PaPerBar,'Q',x3, fl) #K
s3 =  cp.PropsSI('S','P',p3*PaPerBar,'Q',x3, fl) #J/kg*K   
h3 =  cp.PropsSI('H','P',p3*PaPerBar,'Q',x3, fl)  #J/K

#Isentropic Efficiecny of Pump
nPump=0.92
s4s = s3
p4 = 200 #bar
h4s= cp.PropsSI('H','P',p4*PaPerBar,'S',s4s, fl)
h4 = h3+((h4s-h3)/nPump)

#State 4
p4= 200 #bar
WinPump = -mf*(h3-h4)
s4 = cp.PropsSI('S','P',p4*PaPerBar,'H',h4, fl) #J/kg*K
T4 = cp.PropsSI('T','P',p4*PaPerBar,'H',h4, fl)

#%% Ploting

T1Min = (cp.PropsSI('T','P',p1*PaPerBar,'Q',1, fl)) #K 
T1Max = 650+273
nn = T1Max -639 +1 # number of temperature entries in array
TempArr = np.linspace(639,T1Max,nn)    

# Setup a loop to calculate Win and T2 for different values of entropy production
Wnet_array = np.empty(nn)
ThermalEff_array = np.empty(nn)
Qin_array = np.empty(nn)

for (i,T1) in enumerate(TempArr):
    s1= cp.PropsSI('S','P',p1*PaPerBar,'T',T1, fl)
    h1= cp.PropsSI('H','P',p1*PaPerBar,'T',T1, fl)
    s2s = s1
    h2s=cp.PropsSI('H','P',p2*PaPerBar,'S',s2s, fl)
    h2 = h1-(nTurbine*(h1-h2s))
    WoutTurbine=mf*(h1-h2)
    
    Wnet_array[i] = (WoutTurbine/1000) - (WinPump/1000)
    
    Qin_array[i] = (mf*(h1-h4))/1000
    ThermalEff_array[i] = ((Wnet_array[i])/(Qin_array[i]))

plt.figure(1)
plt.clf()
plt.plot(TempArr,Wnet_array,'-r')
plt.xlabel(' Temperature (K)')
plt.ylabel('Net Power Output (kJ/s)')
plt.title('Net Power Output v.s. Varying Temperature ')

plt.figure(2)
plt.clf()
plt.plot(TempArr,ThermalEff_array,'-r')
plt.xlabel(' Temperature (K)')
plt.ylabel('Cycle Thermal Eff ')
plt.title('Thermal Efficiency v.s. Varying Temperature')

plt.figure(3)
plt.clf()
plt.plot(TempArr,Qin_array,'-r')
plt.xlabel(' Temperature (K)')
plt.ylabel('Heat Transfer In (kJ/s)')
plt.title('Heat Transfer In v.s. Varying Temperature')
