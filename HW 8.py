# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:12:01 2020

@author: zkim2
"""


#%% Load Packages - should be at the start of any code
import CoolProp.CoolProp as cp   # for thermodynamics state lookups
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
#%% Problem

fl= 'Air'

# Conversions
PaPerBar = 100000

#Knowns
mf= 500 #kg/s

#State 1
p1 = 3 #bar
T1 = 293 #K 
h1 =  cp.PropsSI('H','P',p1*PaPerBar,'T',T1, fl) #J/kg
