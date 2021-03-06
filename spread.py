# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:45:16 2018

@author: jessicahoffmann
"""
import random
from createTrees import *

""" Returns the updated states of the graph given by its adjacency matrix adj,
with probability of contamination along an edge = mu. """
def OneSpreadStep(state, adj, mu):
    state_after_spread = list(state)
    for i in xrange(len(adj)):
        for j in adj[i]:
            if state[i] == 1 and state[j] == 0:
                state_after_spread[j] = int(random.random() < mu)
    return state_after_spread

def OneCureStep(state, index_to_cure, deltait):  
    state_after_cure = list(state)
    for i_cured in index_to_cure:
        if state_after_cure[i_cured] == 1:
            state_after_cure[i_cured] = int(random.random() < 1-deltait) 
    return state_after_cure 
 
#%%    
#adj = CreateTrees(3)
#print(t)
#state1 = [1,1,0,0,1,0,0,0,0,0,0,0,0,0,0]
#state2 = OneSpreadStep(state1, adj, 0.5)
#PrintTreeState(state1)
#PrintTreeState(state2)