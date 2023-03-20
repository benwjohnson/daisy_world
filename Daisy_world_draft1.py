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
import math

#test edit 
#second edit

stef_boltz = 5.670374419e-8 # Stefan-Boltzman constant W⋅m−2⋅K−4
d = 1.49e11 #distance of the Earth from the Sun, in m
Lo = 3.846e26 #luminosity of the Sun, W
Ab = 0.3 #Albedo
emiss=0.996
k_to_c = 273
S= 917 #Solar flux constant



#%% Equations
'''
Equations for comparative growth of daisies
daw/dt= aw(xB - y)
dab/dt = ab (xB-y) 
aw= area covered by white daises
ab= area covered by black daises
B= growth rate per unit of time
B- 1-0.003265(22.5 - T1)^2
x= area of fertile ground not covered by daisies
Y= death rate per unit of time
x= p - ab - aw where p= proportion of the planet covered in
in fertile ground.
Local T1 is 0 when local T is 5C and 40C.
Locat T1 is 1 when local T is 22.5C

Te= sqrt.(4)(SLo-(1-Ab))/stef_bltz - 273
'''

def dw_model(z,t,Lo,Ab,stef_boltz):
    aw=z[0] #starting area for white daisies
    ab=z[1] #starting area for black daisies
    
    p = 1
    x_fertile = p - aw - ab
    death_rate = 0.3
    
    numerator = Lo*(1-Ab)
    denominator = 16*np.pi*d**2*stef_boltz
    temp_eff = numerator/denominator
    temp_eff = temp_eff**(1/4) 
    print(temp_eff)
   
    #calculate growth rate
    c1 = 0.003265
    c2 = 22.5
    growth_rate = 1 - c1*(c2-temp_eff-273)**2
    print(growth_rate)
    
    #here are the differential equations
    dwdt = aw*(x_fertile*growth_rate - death_rate)
    dbdt = ab*(x_fertile*growth_rate - death_rate)
    
    return [dwdt, dbdt]

#%% Attempt to run the code
C = (Lo,Ab,stef_boltz)
t = np.linspace(0,10,num=10)
z0 = [0.5,0.5]

fun = odeint(dw_model,z0,t,args=(Lo,Ab,stef_boltz))


#%%Looking for the Te temperature 

m=S*Lo*(1-Ab)
h= m/ stef_boltz
o= math.sqrt(math.sqrt(h))

Te= o - 273
print(Te)

#And the equation for effective temperature
numerator = Lo*(1-Ab)
denominator = 16*np.pi*d**2*stef_boltz
temp_eff = numerator/denominator
temp_eff = temp_eff**(1/4)
print(temp_eff)
#%%
'''
f= total radiation lost to space
q=SL/stef_boltz
q=0, local temp = mean temp. meaning perfect conuction from high to lower temp. 
'''
F= (stef_boltz)*(Te+273)**4
print(F)
#%%
'''
q= solar energy that is absorbed and distributed to ground, black, and white daises.
q= SLo/ setf_boltz
'''
q= (S*Lo)/stef_boltz
print(q)
