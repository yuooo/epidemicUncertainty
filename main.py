# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 09:46:08 2018

@author: jessicahoffmann
"""

import numpy as np
import time
from createTrees import *
from strategies import *
from spread import *
import matplotlib.pyplot as plt

from math import *

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
    
    
#%% Blind strategy
from collections import deque
def RunDFS(adj):
    n_nodes = len(adj)
    visited = [0]*n_nodes
    node_order = []
    
    def DFS(current_node):
        visited[current_node] = 1
        for neighbor in adj[current_node]:
            if visited[neighbor] == 0:
                DFS(neighbor)
        node_order.append(current_node)
        
    DFS(0)
    return node_order
    
#adj1 = CreateTrees(3)
#PrintTreeState([0]*len(adj1))
#l = RunDFS(adj1)
#print l
#PrintTreeState(l, 2)
    
def BlindCuring(adj, r, verbose=False):
    n_nodes = len(adj)
    n_tail = int(r/4)
    state = [1]*n_nodes
    node_order = RunDFS(adj)
    to_cure = deque([])
    deltait = 1 - exp(-4*tau)
    mu = 1 - exp(-tau)
    n_iter = 0
    while (any(state)):
        for node in node_order:
            if verbose:
                print "curing node {}".format(node)
            # add element
            to_cure.append(node)
            # cure the nodes for enough time steps
            for _ in range(int(1/tau)):
                state = OneCureStep(state, to_cure, deltait)
#                print "after curing"
#                PrintTreeState(state)
                state = OneSpreadStep(state, adj, mu)
#                print "after spreading"
#                PrintTreeState(state)
                n_iter += 1
#            print "finished curing ", to_cure
            # remove if too many element
            if len(to_cure) > n_tail - 1:
                node_removed = to_cure.popleft()
                if verbose:
                    print "removing node {}".format(node_removed)
#            PrintTreeState(state)
        for _ in range(n_tail):
            if not(any(state)):
                break
            for i_cured in to_cure:
                for _ in range(int(1/tau)):
                    state = OneCureStep(state, to_cure, deltait)
                    state = OneSpreadStep(state, adj, mu)
                    n_iter += 1
    return n_iter
    
#%% plots
n_trials = 1
res3 = []
x = []
for i_k in range(8):
    s = 0
    start = time.time()
    adj = CreateTrees(i_k)
    n_nodes = 2**(i_k+1) - 1
    x.append(n_nodes)
    for _ in range(n_trials):
        s += BlindCuring(adj, 4*(n_nodes)**(3/4), verbose=False)
    end = time.time() - start
    print "iteration {} lasted {}, for a result of {}".format(i_k, end, s/n_trials)
    res3.append(s/n_trials)
    
#%%
#plt.plot(x, res, 'ro')
plt.plot(x, [log(y) for y in res3], 'bo')
#plt.plot(x, [log(y) for y in res3], 'bo')
plt.title("Time to cure as a function of the number of nodes, blind strategy.")