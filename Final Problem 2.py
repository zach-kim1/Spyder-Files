# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:25:46 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import CoolProp.CoolProp as cp   # for thermodynamics state lookups
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
#%% 

fl= 'Water'

# Conversions
PaPerBar = 100000

mf = 200

#State 1
p1 = 100 #bar 
T1 = 520 #C
h1 = cp.PropsSI('H','P',p1*PaPerBar,'T', T1+273, fl)
s1 = cp.PropsSI('S','P',p1*PaPerBar,'T', T1+273, fl)

#State 2
p2 = 15 #bar 
T2 = 280 #C
h2 = cp.PropsSI('H','P',p2*PaPerBar,'T', T2+273, fl)
s2 = cp.PropsSI('S','P',p2*PaPerBar,'T', T2+273, fl)

#State 3
p3 = 15 #bar 
T3 = 500 #C
h3 = cp.PropsSI('H','P',p3*PaPerBar,'T', T3+273, fl)
s3 = cp.PropsSI('S','P',p3*PaPerBar,'T', T3+273, fl)

#State 4 ideally so s4 = s3
p4 = 0.7 #bar 
s4 = s3
h4 = cp.PropsSI('H','P',p4*PaPerBar,'S',s4, fl)
T4 = cp.PropsSI('T','P',p4*PaPerBar,'S',s4, fl)
Q4 = cp.PropsSI('Q','P',p4*PaPerBar,'S',s4, fl)
#State 5 sat liquid
p5 = 0.7 #bar 
x=0
T5 = cp.PropsSI('T','P',p5*PaPerBar,'Q', x, fl) #C
h5 = cp.PropsSI('H','P',p5*PaPerBar,'Q', x, fl)
s5 = cp.PropsSI('S','P',p5*PaPerBar,'Q', x, fl)

#State 6 ideal so s6 =s5
p6 = 100 #bar 
s6 = s5
T6 = cp.PropsSI('T','P',p6*PaPerBar,'S', s6, fl) #C
h6 = cp.PropsSI('H','P',p6*PaPerBar,'S', s6, fl)


Wout12 = mf*(h1 -h2)
Wout34 = mf*(h3-h4)
Win56= mf*(h6-h5)
Qin61 = mf*(h1-h6)
Qin23 = mf*(h3-h2)

Wnet= Wout12+Wout34-Win56 #J/s = W
WnetMW = Wnet/1000000

QinNet = Qin61 + Qin23 

n = Wnet/QinNet 

s2s=s1
h2s = cp.PropsSI('H','P',p2*PaPerBar,'S', s2s, fl)
nTurbine = (h1-h2)/(h1-h2s)
