# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:24:48 2020

@author: Andrew
"""
import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for doing math (matlab like commands)
import CoolProp.CoolProp as cp   # for thermodynamics state lookups

#heat exchanger, pressure doesn't change
#known
fl = 'water'
m1 = 500 #kg/s
PaPerBar = 100000
p1 = 200*PaPerBar
t1 = 650 + 273.15
eff = 0.92

h1 = cp.PropsSI('H','P',p1,'T', t1, fl)
s1 = cp.PropsSI('S','P',p1,'T', t1, fl)

print("Pressure 1 (Bar):", p1/PaPerBar)
print("Temperature 1 (K):", t1)
print("Enthalpy 1 (kJ/kg):", h1/1000)
print("Entropy 1 (kJ/(kg*K)):", s1/1000)
print("Mass Rate (kg/s):", m1)



s2s = s1
p3 = 60 * PaPerBar #pressure 3
p2 = p3 #Same as pressure 3
p2s = p2
h2s = cp.PropsSI('H','S',s2s,'P', p2s, fl)
h2 = h1 - 0.92*(h1-h2s) #0.92 = (h1-h2)/(h1-h2s)
m2 = m1
m2b = 0.05 * m2
m2a = 0.95 * m2

s2 = cp.PropsSI('S','H',h2,'P', p2, fl)
t2 = cp.PropsSI('T','H',h2,'P', p2, fl)

print("Pressure 2 (Bar):", p2/PaPerBar)
print("Temperature 2 (K):", t2)
print("Enthalpy 2 (kJ/kg):", h2/1000)
print("Entropy 2 (kJ/(kg*K)):", s2/1000)
print("Mass Rate 2 (kg/s):", m2)
print("Mass Rate 2a (kg/s):", m2a)
print("Mass Rate 2b (kg/s):", m2b)




m3 = m2a
t3 = 670 + 273.15 #Max Temperature
p3 = 60 * PaPerBar
s3 = cp.PropsSI('S','P',p3,'T', t3, fl)
h3 = cp.PropsSI('H','P',p3,'T', t3, fl)
Qin = -m3 * (h3-h2)

print("Pressure 3 (Bar):", p3/PaPerBar)
print("Temperature 3 (K):", t3)
print("Enthalpy 3 (kJ/kg):", h3/1000)
print("Entropy 3 (kJ/(kg*K)):", s3/1000)
print("Mass Rate 3 (kg/s):", m3)




m4 = m3
p4 = 15 * PaPerBar #given. All pressures in and out of open feed is equal so p4 = p7 = p9 = p10
s4s = s3
p4s = p4
h4s = cp.PropsSI('H','P',p4s,'S', s4s, fl)
h4 = h3 - 0.92*(h3-h4s)
t4 = cp.PropsSI('T','P',p4,'H', h4, fl)
s4 = cp.PropsSI('S','P',p4,'H', h4, fl)
m4b = 0.13 * m1 #y = 13% from first question #y * m1 #y * mtotal = y * mtotal
m4a = m4 - m4b
print("Pressure 4 (Bar):", p4/PaPerBar)
print("Temperature 4 (K):", t4)
print("Enthalpy 4 (kJ/kg):", h4/1000)
print("Entropy 4 (kJ/(kg*K)):", s4/1000)
print("Mass Rate 4 (kg/s):", m4)
print("Mass Rate 4a (kg/s):", m4a)
print("Mass Rate 4b (kg/s):", m4b)




s5s = s4
p6 = 0.2 * PaPerBar #Condenser
p5 = p6
p5s = p5
h5s = cp.PropsSI('H','S',s5s,'P', p5s, fl)
h5 = h4 - 0.92*(h4-h5s)
s5 = cp.PropsSI('S','H',h5,'P', p5, fl)
t5 = cp.PropsSI('T','H',h5,'P', p5, fl)
m5 = m4a
print("Pressure 5 (Bar):", p5/PaPerBar)
print("Temperature 5 (K):", t5)
print("Enthalpy 5 (kJ/kg):", h5/1000)
print("Entropy 5 (kJ/(kg*K)):", s5/1000)
print("Mass Rate 5 (kg/s):", m5)




p6 = 0.2 * PaPerBar #Condenser
t6 = cp.PropsSI('T','P',p6,'Q', 0, fl)
s6 = cp.PropsSI('S','P',p6,'Q', 0, fl)
h6 = cp.PropsSI('H','P',p6,'Q', 0, fl)
m6 = m5
print("Pressure 6 (Bar):", p6/PaPerBar)
print("Temperature 6 (K):", t6)
print("Enthalpy 6 (kJ/kg):", h6/1000)
print("Entropy 6 (kJ/(kg*K)):", s6/1000)
print("Mass Rate 6 (kg/s):", m6)




p7 = p4 #lecture
s7s = s6
p7s = p7
h7s = cp.PropsSI('H','S',s7s,'P', p7s, fl)
h7 = ((h7s-h6)/0.92) + h6 #pump formula
t7 = cp.PropsSI('T','P',p7,'H', h7, fl)
s7 = cp.PropsSI('S','P',p7,'H', h7, fl)
m7 = m6
print("Pressure 7 (Bar):", p7/PaPerBar)
print("Temperature 7 (K):", t7)
print("Enthalpy 7 (kJ/kg):", h7/1000)
print("Entropy 7 (kJ/(kg*K)):", s7/1000)
print("Mass Rate 7 (kg/s):", m7)





m8 = m2b
p8 = p2 #given
t8 = cp.PropsSI('T','P',p8,'Q', 0, fl) - 273.15 + 25 + 273.15 #25 degrees celsius above saturation
s8 = cp.PropsSI('S','P',p8,'T', t8, fl)
h8 = cp.PropsSI('H','P',p8,'T', t8, fl)
print("Pressure 8 (Bar):", p8/PaPerBar)
print("Temperature 8 (K):", t8)
print("Enthalpy 8 (kJ/kg):", h8/1000)
print("Entropy 8 (kJ/(kg*K)):", s8/1000)
print("Mass Rate 8 (kg/s):", m8)




p9 = p4
h9 = h8 #throttling device, problem lecture. its a trap so 0 = m(h1- h2)
t9 = cp.PropsSI('T','P',p9,'H', h9, fl)
s9 = cp.PropsSI('S','P',p9,'H', h9, fl)
m9 = m8
print("Pressure 9 (Bar):", p9/PaPerBar)
print("Temperature 9 (K):", t9)
print("Enthalpy 9 (kJ/kg):", h9/1000)
print("Entropy 9 (kJ/(kg*K)):", s9/1000)
print("Mass Rate 9 (kg/s):", m9)


#m4b(h4b) + m7(h7) + m9(h9) - m10(h10) = 0
m10 = m1 #since m10 = m11
h10 = (m4b * (h4) + m7 * (h7) + m9 * (h9)) / m10
p10 = p4
t10 = cp.PropsSI('T','P',p10,'H', h10, fl)
s10 = cp.PropsSI('S','P',p10,'H', h10, fl)
print("Pressure 10 (Bar):", p10/PaPerBar)
print("Temperature 10 (K):", t10)
print("Enthalpy 10 (kJ/kg):", h10/1000)
print("Entropy 10 (kJ/(kg*K)):", s10/1000)
print("Mass Rate 10 (kg/s):", m10)

p11 = p1 #Since p12 = p1, p11 = p1

s11s = s10
p11s = p11
h11s = cp.PropsSI('H','S',s11s,'P', p11s, fl)
h11 = ((h11s-h10)/0.92) + h10 #pump formula
t11 = cp.PropsSI('T','P',p11,'H', h11, fl)
s11 = cp.PropsSI('S','P',p11,'H', h11, fl)
m11 = m1 #mass rate doesn't change through closed feed so same as m12
print("Pressure 11 (Bar):", p11/PaPerBar)
print("Temperature 11 (K):", t11)
print("Enthalpy 11 (kJ/kg):", h11/1000)
print("Entropy 11 (kJ/(kg*K)):", s11/1000)
print("Mass Rate 11 (kg/s):", m11)



#m2b(h2b-h8) + m11(h11-h12) use to solve for h12
h12 = ((m2b*(h2-h8))/m11)+ h11
p12 = p1 #heat exchanger, pressure doesn't change
m12 = m1 #dont change through boilers
t12 = cp.PropsSI('T','P',p12,'H', h12, fl)
s12 = cp.PropsSI('S','P',p12,'H', h12, fl)
print("Pressure 12 (Bar):", p12/PaPerBar)
print("Temperature 12 (K):", t12)
print("Enthalpy 12 (kJ/kg):", h12/1000)
print("Entropy 12 (kJ/(kg*K)):", s12/1000)
print("Mass Rate 12 (kg/s):", m12)



#massflowmin = .01
#massflowmax = .21
#nn = 21 # number of temperature entries in array
#sigmaArr = np.linspace(massflowmin,massflowmax,nn)   

#Wnet_array = np.empty(nn)
#ThermalEff_array = np.empty(nn)
#h2_array = np.empty(nn)
#for (i,IsenEff) in enumerate(sigmaArr):
#    h2_array[i] = (h1 - (IsenEff*(h1-h2s)))/1000  # kj/kg
#    Wnet_array[i] = (Win/1000) - ((h1/1000)-h2_array[i])*mf
#    ThermalEff_array[i] = -1*(Wnet_array[i]/(Qin/1000))

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
isobar200_array = np.empty(nn)
isobar60_array = np.empty(nn)
isobar15_array = np.empty(nn)
isobar0_2_array = np.empty(nn)

for (i,s) in enumerate(entropy):
    isobar200_array[i] = cp.PropsSI('T','P',200*PaPerBar,'S',s, fl)
    isobar60_array[i] = cp.PropsSI('T','P',60*PaPerBar,'S',s, fl)
    isobar15_array[i] = cp.PropsSI('T','P',15*PaPerBar,'S',s, fl)
    isobar0_2_array[i] = cp.PropsSI('T','P',0.2*PaPerBar,'S',s, fl)

plt.plot(entropy,isobar200_array,'g--')
plt.plot(entropy,isobar60_array,'b--')
plt.plot(entropy,isobar15_array,'c--')
plt.plot(entropy,isobar0_2_array,'y--')
plt.ylim(200, 1200)

plt.plot(s1,t1, 'd')
plt.plot(s2,t2,'d')
plt.plot(s3,t3,'d')
plt.plot(s4,t4,'d')
plt.plot(s5,t5,'d')
plt.plot(s6,t6,'d')
plt.plot(s7,t7,'d')
plt.plot(s8,t8,'d')
plt.plot(s9,t9,'d')
plt.plot(s10,t10,'d')
plt.plot(s11,t11,'d')
plt.plot(s12,t12,'d')
plt.title('Temperature v.s. Entropy')
plt.legend(('Vapor Dome','Vapor Dome','200 bar','60 Bar','15 Bar','0.2 Bar'))
