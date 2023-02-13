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
#hey guys, hope your Monday is going well :)