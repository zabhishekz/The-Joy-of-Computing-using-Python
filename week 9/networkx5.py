# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:47:53 2021

@author: Abhishek
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.barabasi_albert_graph(50,2)
nx.draw(G)
plt.show()

nx.write_gexf(G,"Analysis1.gexf")