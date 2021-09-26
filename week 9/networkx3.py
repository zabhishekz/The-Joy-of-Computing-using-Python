# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:28:47 2021

@author: Abhishek
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(10)
nx.draw(G)
plt.show()