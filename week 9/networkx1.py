# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 14:54:43 2021

@author: Abhishek
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)
print(G.nodes())
print(G.edges())
nx.draw(G)
plt.show()