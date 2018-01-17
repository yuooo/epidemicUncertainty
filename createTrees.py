# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:46:44 2018

@author: jessicahoffmann
"""
from math import *

""" Returns the adjencency matrix of a binary tree of size n = 2^(k+1) - 1 """
def CreateTrees(k):
    n = 2**(k+1) - 1
    adj = [[] for _ in xrange(n)]
    for i in xrange(1, n):
        adj[i].append((i - 1) // 2)
    for i in xrange(n // 2):
        adj[i].append(2*i + 1)
        adj[i].append(2*i + 2)
    return adj
    
#print CreateTrees(1)
#print CreateTrees(2)
#print CreateTrees(5)
    
def PrintTreeState(state, size_number=1):
    n_nodes = len(state)
    k = int(log(n_nodes, 2))
    n_space = n_nodes*size_number
    i_state = 0
    for i in xrange(k+1):
        n_space = (n_space - size_number) // 2
        s = ""
        for j in xrange(2**i):
            s += " " * n_space
            s += str(state[i_state])
            s += " " * (n_space + size_number)
            i_state += 1
        print(s)
        
        
#state0 = [0]*15    
#state1 = [1,1,0,0,1,0,0,0,0,0,0,0,0,0,0]
#PrintTreeState(state0)
#PrintTreeState(state1)