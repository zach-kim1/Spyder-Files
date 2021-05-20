# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:17:28 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import CoolProp.CoolProp as cp   # for thermodynamics state lookups
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
#%% Problem 3

fl= 'Air'

# Conversions
PaPerBar = 100000
m3percm3 = 1/1000000

m = 0.000580747 #kg

p1= 1 #Bar
T1 = 300 #K
V1 = 500 #cm^3

u1 =  cp.PropsSI('U','P',p1*PaPerBar,'T',T1, fl) #J/kg
s1 =  cp.PropsSI('S','P',p1*PaPerBar,'T',T1, fl) #J/kg*K


s2 = s1 
V2 = 50 #cm^3
D2 = m/ (V2 * m3percm3) #kg/m^3
u2 =  cp.PropsSI('U','D',D2,'S',s2, fl) #J/kg
T2 =  cp.PropsSI('T','D',D2,'S',s2, fl) #J/kg
P1 =  cp.PropsSI('P','D',D2,'S',s2, fl) #J/kg


T3= 1900 #K 
D3= D2
u3 =  cp.PropsSI('U','D',D3,'T',T3, fl) #J/kg
P3 =  cp.PropsSI('P','D',D3,'T',T3, fl) #J/kg
s3 =  cp.PropsSI('S','D',D3,'T',T3, fl) #J/kg

s4 = s3 
V4 = 500 #cm^3
D4 = m/ (V4 * m3percm3) #kg/m^3
u4 =  cp.PropsSI('U','D',D4,'S',s4, fl) #J/kg
T4 =  cp.PropsSI('T','D',D4,'S',s4, fl) #J/kg
P4 =  cp.PropsSI('P','D',D4,'S',s4, fl) #J/kg

Win = m*(u2-u1)
Wout = -1*m*(u4-u3)
Wnet = Win - Wout

Qin = m*(u3-u2)
Qout= -1*m*(u1-u4)

n = Wnet/Qin