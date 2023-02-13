#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 08:41:42 2018

@author: benjohnson
"""

#practice  ODE integration 

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

C1=4
C2=5
# function that returns dy/dt
def model(z,t,C,D):
    x=z[0]
    y=z[1]
    k = -0.3
    dxdt = k*(-C+x)
    dydt = k-D*y
    
    return [dxdt, dydt]

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
#Alex was here