# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:34:46 2020

@author: Lenovo
"""

import pandas as pd
import networkx as nx

data=pd.read_csv("20200101.csv")
G=nx.DiGraph()

for index, row in data.iterrows():
    G.add_edge(row["origin"],row["destination"])

NG=G.to_undirected()
test=G.degree()
print(test)
'''
# temporal
average_clustering
transitivity
global_efficiency
reciprocity

'''
'''
# spatial
closeness_centrality
average_neighbor_degree
degree_centrality
pagerank
hits
degree
'''
