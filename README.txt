Formats:

n = 2^k: # nodes
tau: time step
state: list of size n, state[i] == 1 iff node i is infected
adj: n*? adjacency list
mu: probability of infection along an edge between an infected and a non-infected node
delta: maximum probability of curing a node
rit: budget attributed to node i at time t
r: maximum budget
deltait: probability of curing node i at time t