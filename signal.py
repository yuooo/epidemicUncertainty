# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:12:49 2018

@author: jessicahoffmann
"""

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