#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 14:21:33 2023

@author: bwj
"""

#File for working on our Daisy World Model. We can try to use a github repository to all 
#work on this together! We'll use the equations from Watson and Lovelock 1983. 

import numpy as np
from scipy.integrate import odeint

#test edit 
#second edit

stef_boltz = 5.670374419e-8 # Stefan-Boltzman constant W⋅m−2⋅K−4
d = 1.49e11 #distance of the Earth from the Sun, in m
Lo = 3.846e26 #luminosity of the Sun, W
Ab = 0.3 #Albedo
emiss=0.996
k_to_c = 273
S = 917 #Solar Flux
death = 0.3 #death rate


'''
ab = area covered by black daisies
aw = area covered by white daisies
x = area of fertile ground with no daisies
P = proportion of planet that is fertile
    x = P - ab - aw

B = growth rate
T1 = local temperature
    B1 = 1-0.003265(22.5 - T1)**2
y = death rate
comparative growth of daisies:
    daw/dt = aw(XB - y)
    dab/dt = ab(XB - y)
Te = effective temperature planet radiates 

F =  total radiation lost to space
   
'''
#local temperature calculation


# function for differential equations
def dw_model(z,t,C,D):
    aw=z[0] #starting area for white daisies
    ab=z[1] #starting area for black daisies
    p = 1
    x_fertile = (p - ab - aw)
    c1 = 0.003265
    c2 = 22.5
    numerator = Lo*(1-Ab)
    denominator = 16*np.pi*d**2*stef_boltz
    temp_eff = numerator/denominator
    temp_eff = temp_eff**(1/4) 
    print(temp_eff)
    
       #calculate growth rate
    growth_rate = 1 - c1*(c2-temp_eff-k_to_c)**2
    print(growth_rate)
    dwdt = aw(x_fertile*growth - death)
    dbdt = ab(x_fertile*growth - death)
    #radiation lost to space. Not sure where this is used??
    F = stef_boltz(tem_eff + k_to_c)**4
    return [dwdt, dbdt]


# initial condition
z0 = [1,1]
# time points
t = np.linspace(0,10)
#t = [0,5,10]
# solve ODE
z_solved = odeint(model,z0,t,args=(C1,C2))

x_out = z_solved[:,0]
y_out = z_solved[:,1]
# plot results
plt.figure(num=1); plt.clf()
plt.plot(t,x_out,'k-h')
plt.plot(t,y_out,'r:o')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()