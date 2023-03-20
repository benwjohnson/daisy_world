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
o = 5.670374419 × 10−8 #Stefan's constant 

'''
ab = area covered by black daisies
aw = area covered by white daisies
x = area of fertile ground with no daisies
P = proportion of planet that is fertile
    x = P - ab - aw

B = growth rate
T1 = local temperature
    B1 = 1-0.003265(22.5 - T1)^2
y = death rate
comparative growth of daisies:
    daw/dt = aw(XB - y)
    dab/dt = ab(XB - y)
Te = effective temperature planet radiates 
   o =  
'''