# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 09:46:08 2018

@author: jessicahoffmann
"""
import random
import numpy as np
import time
from math import *
from createTrees import *
from signal import *
from spread import *
from strategies import *
import matplotlib.pyplot as plt

#%% Parameters


tau = 0.1
k = 4
n_nodes = 2**(k+1) - 1
C = 4.
r = C*(k+1)
mu = 1 - exp(-tau)
delta = 1 - exp(-r*tau)
adj = CreateTrees(k)
p = 1
q = 0

  
#%% Impact of size for random curing
 
n_trials = 100
res = []
x = []
for i_k in range(6):
    s = 0
    start = time.time()
    adj = CreateTrees(i_k)
    n_nodes = 2**(i_k+1) - 1
    x.append(n_nodes)
    for _ in range(n_trials):
        s += NaiveCuring(adj)
    end = time.time() - start
    print "iteration {} lasted {}".format(i_k, end)
    res.append(s/n_trials)
    
#%%
plt.plot(x, res, 'ro')
plt.title("Time to cure as a function of the number of nodes, p=1, q=0, random strategy.")

#%% Impact of uncertainty for random curing

adj = CreateTrees(4)
delta = [0.5, 0.49, 0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.40]
res2 = []
it = 0
for delt in delta:
    it += 1
    start = time.time()
    p = 0.5 + delt
    q = 0.5 - delt
    s = 0
    for _ in range(n_trials):
        s += NaiveCuring(adj, False, p, q)
    end = time.time() - start
    print "iteration {} lasted {} for a result of {}".format(it, end, s/n_trials)
    res2.append(s/n_trials)
    
    
#%%
plt.plot([0.5-x for x in delta], [log(y) for y in res2])    
plt.title("Time to cure as a function of the probability of error, logscale, random strategy.\n")   
    
    
#%%