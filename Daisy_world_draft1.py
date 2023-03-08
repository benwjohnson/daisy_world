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
#%%Looking for the Te temperature 

m=emiss*Lo*(1-Ab)
h= m/ stef_boltz
o= math.sqrt(math.sqrt(h))

Te= o - 273
print(Te)

