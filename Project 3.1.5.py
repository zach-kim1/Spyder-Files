# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:53:00 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import CoolProp.CoolProp as cp   # for thermodynamics state lookups
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
#%% 3.1.5

fl= 'Water'

# Conversions
PaPerBar = 100000

#Knowns
mf= 500 #kg/s

#State 1
p1 = 200 #bar
T1 = 650 +273 #K 
s1 =  cp.PropsSI('S','P',p1*PaPerBar,'T',T1, fl) #J/kg*K
h1 =  cp.PropsSI('H','P',p1*PaPerBar,'T',T1, fl) #J/kg

#Isentropic Efficiecny of Turbine @ State 2
p2= 0.2 #bar
nTurbine=0.92
s2s = s1
h2s= cp.PropsSI('H','P',p2*PaPerBar,'S',s2s, fl)
Wout = mf*((h1-h2s)*nTurbine)

#State 2
p2 = 0.2 #bar
h2 =  h1-(Wout/mf) #J/kg
s2 = cp.PropsSI('S','P',p2*PaPerBar,'H',h2, fl)
T2 = cp.PropsSI('T','P',p2*PaPerBar,'H',h2, fl)


#State 3 (Will be sat liquid)
p3 =  0.2 #bar
x3 = 0 #quality
T3 =  cp.PropsSI('T','P',p3*PaPerBar,'Q',x3, fl) #K
s3 =  cp.PropsSI('S','P',p3*PaPerBar,'Q',x3, fl) #J/kg*K   
h3 =  cp.PropsSI('H','P',p3*PaPerBar,'Q',x3, fl)  #J/K
 
#Condensor (a and b)

Ta = 23 +273 #K (assume river water temperature of 23 C)
TempChange = 15 +273 #K
Tb= Ta + TempChange #K
pa = 1 #atm
pb = pa
PaPerATM= 101325
ha = cp.PropsSI('H','P',pa*PaPerATM,'T',Ta, fl) #J/K
hb = cp.PropsSI('H','P',pb*PaPerATM,'T',Tb, fl) #J/K

mcw = (mf*(h3-h2))/(ha-hb) #kg/s