# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:08:10 2018

@author: jessicahoffmann
"""

from math import *
from spread import *
from createTrees import *

#%%
import numpy as np

def Signal(state, p, q):
    n_nodes = len(state)
    signal_infected = np.random.choice(2, n_nodes, p=[1-p, p])
    signal_susceptible = np.random.choice(2, n_nodes, p=[1-q, q])
    np_state = np.array(state)
    signal_total = np_state * signal_infected + (1 - np_state) * signal_susceptible
    return signal_total
    
#state1 = [1,1,0,0,1,0,0,0,0,0,0,0,0,1,1]
#PrintTreeState(Signal(state1, 0.75, 0.25))  
#st = np.zeros(len(state1))
#for _ in range(100):
#    st += Signal(state1, 0.75, 0.25)
#PrintTreeState(state1)
#PrintTreeState(st.astype(int), 2)

#%%
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

""" This strategy cures uniformly the nodes which emits a positive signal, up
to k+1 node (so that each nodes receives at least budget C).
Efficient when the signal is good, not so much otherwise.""" 
def NaiveCuringStep(signal, state):
    index_ones = [i for i, j in enumerate(signal) if j == 1]
    n_signaling= len(index_ones)
    state_after_curing = list(state)
    # no signaling
    if n_signaling == 0:
        deltait = 1 - exp(-C*tau)
        random_index = np.random.choice(range(len(signal)), k+1, replace=False)
    # if too many nodes are signaling, choose k+1 randomly and cure them
    elif r/n_signaling < C:
        deltait = 1 - exp(-C*tau)
        random_index = np.random.choice(index_ones, k+1, replace=False)
        
    # else uniform spread
    else:
        deltait = 1 - exp(-r/n_signaling*tau)
        random_index = index_ones
    
    for i_index in random_index:
            state_after_curing[i_index] = int(random.random() < 1-deltait)
    
    return state_after_curing
    
def NaiveCuring(adj, verbose=False, infected_proba=p, susceptible_proba=q):
    state = [1]*(len(adj))
    n_iter = 0
    while any(state):
#        if n_iter > 100:
#            break
        signal = Signal(state, infected_proba, susceptible_proba)
        state = NaiveCuringStep(signal, state)
        if verbose:
            PrintTreeState(state)
            print "after curing, {} infected".format(sum(state))
        state = OneSpreadStep(state, adj, mu)
        if verbose:
            PrintTreeState(state)
            print "after spreading, {} infected".format(sum(state))
        n_iter += 1
    return n_iter
    
#%%













    
    
    