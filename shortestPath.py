from distanceFunction import distance
from sys import maxsize
from python_tsp.exact import solve_tsp_dynamic_programming

import numpy as np

class pathFinder:
    def graphGenerator(self,chosen_cities):
        #initialize a graph of the required size
        num_nodes = len(chosen_cities)
        g = []
        for i in range(0,num_nodes):
            g.append([0]*num_nodes)
        #initialize distances
        for i in range(0,num_nodes):
            for j in range(0,num_nodes):
                g[i][j] = distance(chosen_cities[i].lat, chosen_cities[i].long, chosen_cities[j].lat, chosen_cities[j].long)
        return g


    def pathGenerator(self, graph):
        dist_mat = np.array(graph)
        perm, dist = solve_tsp_dynamic_programming(dist_mat)
        return (dist, perm)
