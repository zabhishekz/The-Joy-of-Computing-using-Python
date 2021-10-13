# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:48:17 2021

@author: Abhishek
"""

import networkx as nx

U=nx.Graph() #Undirected
G=nx.DiGraph() #directed

G.add_nodes_from([i for i in range(5)])
print(G.nodes())

G.add_edge(1,2)

print(G.edges())
print(G.out_edges())
print(G.in_edges())

print(G.out_edges(1))
print(G.in_edges(1))

G.add_edge(0,3)
G.add_edge(2,3)
G.add_edge(3,2)
G.add_edge(3,4)
G.add_edge(4,1)

print(G.out_edges(2))
print(G.out_edges(3))
print(G.in_edges(3))