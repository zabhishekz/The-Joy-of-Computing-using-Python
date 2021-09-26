# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:40:53 2021

@author: Abhishek
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(50,0.3)
nx.draw(G)
plt.show()

print(G.nodes())
print(G.edges())
print(G.degree(0))