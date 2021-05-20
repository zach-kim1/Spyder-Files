# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:21:15 2020

@author: zkim2
"""

#%% Load Packages - should be at the start of any code
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
from scipy.integrate import quad
import CoolProp.CoolProp as cp   # for thermodynamics state lookups
from astropy.table import QTable, Table, Column
from astropy import units as u
import math
#%%

fl = 'Ammonia'

# Conversions
PaPerBar = 100000

#Knowns
p1 = 10     #bar
x1 = 0.7    #quality of 1
m = 3       #kg

#State 1
D1 = cp.PropsSI('D','P',p1*PaPerBar,'Q',x1, fl)     # kg/m^3
v1= 1/D1                                            #m^3/kg
T1 = cp.PropsSI('T','P',p1*PaPerBar,'Q',x1, fl)     # K
u1 = cp.PropsSI('U','P',p1*PaPerBar,'Q',x1, fl) /1000    # kJ/kg

#State 2
v2=v1
x2=1

T2 = cp.PropsSI('T','D',D1,'Q',x2, fl)     # K
u2 = cp.PropsSI('U','D',D1,'Q',x2, fl) /1000   # kJ/kg
p2 = cp.PropsSI('P','D',D1,'Q',x2, fl) /PaPerBar    # Pa

#State 3
p3=p1
T3=T2

D3 = cp.PropsSI('D','P',p3*PaPerBar,'T',T3, fl)     #kg/m^3
v3=1/D3                                             #m^3/kg
u3 = cp.PropsSI('U','P',p3*PaPerBar,'T',T3, fl) /1000    # kJ/kg


#Process 1 to 2
"Trying to get an integral to work"
#def integrand(x):
#    return p1
#W12,err = quad (integrand, v1, v2)
#print('Win/m = {:f} (+-{:g}) kJ/kg'.format(W12,err))

W12 = m*p1*(v2-v1)      #kj
Q12 = m*(u2-u1) + W12   #kj

#Proces 2 to 3
Q23 = 500               #kj
W23 = Q23 - m*(u3-u2)   #kj

#Process 3 to 1
W31 = m*(p3*PaPerBar)*(v1-v3)/1000  #kj
Q31 = m*(u1-u3) + W31               #kj

#Wnet and Qin
Wnet= W12 + W23 + W31
"Calculates Qin based on Q's from each process"
QVal= [Q12, Q23, Q31]
i = 0
Qin=0
while (i < len(QVal)):
    if(QVal[i] > 0):
        Qin += QVal[i]
        i+=1
    else:
        i +=1      

#Thermal Efficiency
n = Wnet/Qin

print("Looked Up Table")
a = [1, 2, 3]
b = [round(p1,3),round(p2,3),round (p3,3)]
c = [round (v1,3),round (v2,3),round (v3,3)]
d = [round (T1,3),round (T2,3),round (T3,3)]
e = [round (u1,3),round (u2,3),round (u3,3)]
t= Table([a,b,c,d,e], names=('State',' P (bar) ',' v (m^3/kg)', ' T (K) ',' u(kj/kg) '))

print(t)

print("\n")

#Work Q 

l = ['1->2', '2->3', '3->1', 'Wnet', 'Efficiency']
w = [round(W12,3),round(W23,3),round (W31,3), '-', '-']
q = [round (Q12,3),round (Q23,3),round (Q31,3), '-', '-']
t = ['-', '-', '-', round (Wnet,3), '-']
E = ['-','-','-', '-', round(n,3)]
z= Table([l,w,q,t,E], names=('-',' Wout (kj) ',' Qin (kj)','--','---'))

print(z)

         