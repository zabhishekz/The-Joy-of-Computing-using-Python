# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:22:30 2021

@author: Abhishek
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

def add_edges():
    nodes=list(G.nodes())
    
    for s in nodes:
        for t in nodes:
            if s != t:
                r=random.random()
                if r<0.5:
                    G.add_edge(s,t)
                
    return G


#Create a directed graph
G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=add_edges()

#visualise the graph
nx.draw(G,with_labels=True)
plt.show()
