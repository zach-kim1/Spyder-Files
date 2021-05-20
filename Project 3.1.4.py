# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:34:28 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import CoolProp.CoolProp as cp   # for thermodynamics state lookups
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
#%% 3.1.4 

fl= 'Water'

# Conversions
PaPerBar = 100000

#Knowns
mf= 500 #kg/s

#State 1
p1 = 200 #bar
T1 = cp.PropsSI('T','P',p1*PaPerBar,'Q',1, fl) #K 
s1 =  cp.PropsSI('S','P',p1*PaPerBar,'T',639, fl) #J/kg*K
h1 =  cp.PropsSI('H','P',p1*PaPerBar,'T',639, fl) #J/kg

#Isentropic Efficiecny of Turbine @ State 2
p2= 0.2 #bar
nTurbine=0.92
s2s = s1
h2s= cp.PropsSI('H','P',p2*PaPerBar,'S',s2s, fl)
h2 =  h1 - nTurbine*(h1-h2s) #J/kg

#State 2
Wout = mf*(h1-h2)
s2 = cp.PropsSI('S','P',p2*PaPerBar,'H',h2, fl)
T2 = cp.PropsSI('T','P',p2*PaPerBar,'H',h2, fl)

#State 3 (Will be sat liquid)
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
Win = -mf*(h3-h4)
s4 = cp.PropsSI('S','P',p4*PaPerBar,'H',h4, fl) #J/kg*K
T4 = cp.PropsSI('T','P',p4*PaPerBar,'H',h4, fl)


#Qin Boiler
Qin = -mf*(h4-h1) #J/s

#%% With a T1 = 650 C
fl = 'Water'

# Conversions
PaPerBar = 100000

#Knowns
mf= 500 #kg/s

#State 1
p16 = 200 #bar
T16 = 650+273 #K 
s16 =  cp.PropsSI('S','P',p16*PaPerBar,'T',T16, fl) #J/kg*K
h16 =  cp.PropsSI('H','P',p16*PaPerBar,'T',T16, fl) #J/kg

#Isentropic Efficiecny of Turbine @ State 2
p26= 0.2 #bar
nTurbine6=0.92
s2s6 = s16
h2s6= cp.PropsSI('H','P',p26*PaPerBar,'S',s2s6, fl)
Wout6 = mf*((h16-h2s6)*nTurbine6)

#State 2
p26 = 0.2 #bar
h26 =  h16-(Wout6/mf) #J/kg
s26 = cp.PropsSI('S','P',p26*PaPerBar,'H',h26, fl)
T26 = cp.PropsSI('T','P',p26*PaPerBar,'H',h26, fl)
Qin16 = -mf*(h4-h16) #J/s

Wnet6= Win - Wout6


#%% T-s diagram for process

Tcrit= int(cp.PropsSI("Tcrit","Water")) #K
TempArr = np.linspace(278,Tcrit,Tcrit-278+1) 
sLiquid_array = np.empty(Tcrit-278+1)
sVapor_array = np.empty(Tcrit-278+1)
for (i,T) in enumerate(TempArr):
    sLiquid_array[i] = cp.PropsSI('S','T',T,'Q',0, fl) #J/kg*k
    sVapor_array[i] = cp.PropsSI('S','T',T,'Q',1, fl) #J/kg*k

plt.figure(1)
plt.clf()
plt.plot(sVapor_array,TempArr,'-r')
plt.plot(sLiquid_array,TempArr,'-r')
plt.xlabel('Entropy (J/kg/K)')
plt.ylabel('Temperature (K)')


smin = 500 #J/kg/K
smax = 8500.0 #J/kg/K
nn = 500 # number of entropy entries in array
entropy = np.linspace(smin,smax,nn) 
isobarTemp1_array = np.empty(nn)
isobarTemp2_array = np.empty(nn)
for (i,s) in enumerate(entropy):
    isobarTemp1_array[i] = cp.PropsSI('T','P',p1*PaPerBar,'S',s, fl)
    isobarTemp2_array[i] = cp.PropsSI('T','P',p2*PaPerBar,'S',s, fl)
    
    
plt.plot(entropy,isobarTemp1_array,'g--')
plt.plot(entropy,isobarTemp2_array,'b--')


plt.plot(s1,T1, 'd')
plt.plot(s2,T2, 'd')
plt.plot(s3,T3, 'd')
plt.plot(s4,T4, 'd')
plt.ylim(200, 700)
plt.title('Temperature v.s. Entropy with T1 = Tsat ')
plt.legend(('Vapor Dome','Vapor Dome','200 bar','0.2 Bar'))

plt.figure(2)
plt.clf()
plt.plot(sVapor_array,TempArr,'-r')
plt.plot(sLiquid_array,TempArr,'-r')
plt.plot(entropy,isobarTemp1_array,'g--')
plt.plot(entropy,isobarTemp2_array,'b--')
plt.ylim(200, 1000)
plt.xlabel('Entropy (J/kg/K)')
plt.ylabel('Temperature (K)')
plt.plot(s16,T16, 's')
plt.plot(s26,T26, 's')
plt.plot(s3,T3, 's')
plt.plot(s4,T4, 's')
plt.title('Temperature v.s. Entropy with T1 = 650 C ')
plt.legend(('Vapor Dome','Vapor Dome','200 bar','0.2 Bar'))
