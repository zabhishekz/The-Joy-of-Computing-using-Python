# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:47:43 2021

@author: Abhishek
"""

import networkx as nx
G=nx.barbell_graph(4,2)
nx.draw(G)

G=nx.complete_graph(4)
nx.draw(G)

G=nx.cycle_graph(5)
nx.draw(G)

G=nx.ladder_graph(5)
nx.draw(G)

G=nx.path_graph(6)
nx.draw(G)

G=nx.star_graph(5)
nx.draw(G)

G=nx.wheel_graph(4)
nx.draw(G)


G=nx.gnp_random_graph(5,0.5)
nx.draw(G)

G=nx.gnp_random_graph(5,0.)
nx.draw(G)