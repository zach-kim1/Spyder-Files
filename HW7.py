# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:03:30 2020

@author: zkim2
"""

#%% Load Packages - should be at the start of any code
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
import CoolProp.CoolProp as cp   # for thermodynamics state lookups

#%% Problem 2

fl= 'Propane'

#Conversions
PaPerBar = 100000

#Knowns
mf= 0.5 #kg/s
p1 = 1 #bar
T1= 300 #K
p2= 20  #bar
T2= 430 #K
#Adiabatic Compressor 

#Actual Compressor
h1= cp.PropsSI('H','P',p1*PaPerBar,'T',T1, fl) #J/kg
h2= cp.PropsSI('H','P',p2*PaPerBar,'T',T2, fl) #J/kg
W = -mf*(h1-h2)  #J/kg

#Isentropic Compressor
s1 = cp.PropsSI('S','P',p1*PaPerBar,'T',T1, fl) #J/kg*k
h2s= cp.PropsSI('H','P',p2*PaPerBar,'S',s1, fl) #J/kg
Ws = -mf*(h1-h2s)

#Efficiency
n = Ws/W
print('Problem 2 Answers:')
print('--------------')
print('Work Required = {:.2f} kJ/kg'.format(W/1000)) # output Work to screen
print('Efficency = {:.2f}'.format(n)) # output Work to screen
print('--------------')

#%% Problem 3

fl ='Water'

#Conversions
PaPerMPa = 1000000
PaPerkPa= 1000

#Knowns
mf= 150 #kg/s
p1= 18 #MPa
T1= 500 #C
p2= 7 #kPa
p3= p2 #kPa
p4= p1 #MPa

#Turbine

h1= cp.PropsSI('H','P',p1*PaPerMPa,'T',T1, fl) #J/kg
s1= cp.PropsSI('S','P',p1*PaPerMPa,'T',T1, fl) #J/kg*K
h2 = cp.PropsSI('H','P',p2*PaPerkPa,'S',s1, fl) #J/kg
WoutTurbine= mf*(h1-h2) #J/s

#Condensor
x=0
s2=s1
h3= cp.PropsSI('H','P',p3*PaPerkPa,'Q',x, fl) #J/kg
T3= cp.PropsSI('T','P',p3*PaPerkPa,'Q',x, fl) #C
QoutCondensor= mf*(h2-h3) #J/kg
s3= (-(QoutCondensor/T3)/mf)+s2

#Pump
s4= s3 #J/kg
h4= cp.PropsSI('H','P',p4*PaPerMPa,'S',s4, fl) #J/kg
WinPump=-mf*(h3-h4)

#Boiler
QinBoiler=-mf*(h4-h1)

#Efficiency
n=(WoutTurbine-WinPump)/QinBoiler
print('\nProblem 3 Answers:')
print('--------------')
print('Net Power = {:.2f} kJ/kg'.format((WoutTurbine-WinPump)/1000)) # output Work to screen
print('Rate of HEat Transfer to Steam Through Boiler = {:.2f} kJ/kg'.format(QinBoiler/1000)) # output Work to screen
print('Efficiency = {:.2f}'.format(n)) # output Work to screen
print('--------------')

#%% Problem 4

fl ='Water'

#Conversions
PaPerMPa = 1000000

#Knowns
p1= 0.008 #MPa
T3= 210 #C
p4= 0.7 #MPa

#State 1 (sat liquid)
x1=0
T1 = cp.PropsSI('T','P',p1*PaPerMPa,'Q',x1, fl) #K
s1 = cp.PropsSI('S','P',p1*PaPerMPa,'Q',x1, fl) #J/kg *K
h1 = cp.PropsSI('H','P',p1*PaPerMPa,'Q',x1, fl) #J/kg

#Work of Pump
n = 0.8
p2s = p4
s2s = s1
h2s = cp.PropsSI('H','P',p2s*PaPerMPa,'S',s2s, fl) #J/kg
WinPerMass= (h2s-h1)/n

#State 2
p2 = p4
h2 = WinPerMass + h1
T2 = cp.PropsSI('T','P',p2*PaPerMPa,'H',h2, fl) #K
s2 = cp.PropsSI('S','P',p2*PaPerMPa,'H',h2, fl)

#State 3
p3 = p4
s3 = cp.PropsSI('S','P',p3*PaPerMPa,'T',T3+273, fl) #J/kg*K
h3 = cp.PropsSI('H','P',p3*PaPerMPa,'T',T3+273, fl) #J/kg

#State 4
h4 = (0.85*h2) + (0.15 * h3) #J/kg
s4 = cp.PropsSI('S','P',p4*PaPerMPa,'H',h4, fl) #J/kg* K
T4 = cp.PropsSI('T','P',p4*PaPerMPa,'H',h4, fl) #K


# Phase of water
Tsat4 = cp.PropsSI('T','P',p4*PaPerMPa,'Q',0, fl)
x = cp.PropsSI('Q','P',p4*PaPerMPa,'T',T4, fl)
