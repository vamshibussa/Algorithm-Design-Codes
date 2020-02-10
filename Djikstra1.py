#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from guppy import hpy
import numpy as np
import random
import pdb
import time

t_case1 = np.zeros((8,8))

for i in range(0,8):
    for j in range(0,8):
        t_case1[i][j] = 10000


t_case1[0][3] = 29
t_case1[3][0] = 29
t_case1[3][4] = 5
t_case1[4][3] = 5
t_case1[4][7] = 11
t_case1[7][4] = 11
t_case1[7][5] = 17
t_case1[5][7] = 17
t_case1[3][2] = 12
t_case1[2][3] = 12
t_case1[3][6] = 13
t_case1[6][3] = 13
t_case1[2][6] = 5
t_case1[6][2] = 5
t_case1[1][6] = 11
t_case1[6][1] = 11
t_case1[4][6] = 7
t_case1[6][4] = 7
t_case1[2][5] = 5
t_case1[5][2] = 5
t_case1[5][1] = 11
t_case1[1][5] = 11

t_case2 = np.zeros((12,12))

for i in range(0,12):
    for j in range(0,12):
        t_case2[i][j] = 10000

t_case2[9][7] = 9
t_case2[7][7] = 9
t_case2[9][3] = 25
t_case2[9][3] = 25
t_case2[7][5] = 15
t_case2[5][7] = 15
t_case2[7][8] = 5
t_case2[8][7] = 5
t_case2[7][0] = 28
t_case2[0][7] = 28
t_case2[7][3] = 17
t_case2[3][7] = 17
t_case2[3][8] = 7
t_case2[8][3] = 7
t_case2[3][2] = 18
t_case2[2][3] = 18
t_case2[6][3] = 27
t_case2[6][0] = 29
t_case2[0][6] = 29
t_case2[0][10] = 14
t_case2[10][0] = 14
t_case2[0][2] = 14
t_case2[2][0] = 14
t_case2[0][1] = 11
t_case2[1][0] = 11
t_case2[0][4] = 8
t_case2[4][0] = 8
t_case2[8][5] = 5
t_case2[5][8] = 5
t_case2[8][10] = 25
t_case2[10][8] = 25
t_case2[8][2] = 25
t_case2[2][8] = 25
t_case2[5][2] = 13
t_case2[2][5] = 13
t_case2[2][1] = 12
t_case2[1][2] = 12
t_case2[2][11] = 16
t_case2[11][2] = 16
t_case2[2][4] = 13
t_case2[4][2] = 13
t_case2[1][4] = 6
t_case2[4][1] = 6
t_case2[4][11] = 22
t_case2[11][4] = 22

def Random(n):
    return random.randint(1,n)

def comp(n):
    g_return_c = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            g_return_c[i][j] = 1
            g_return_c[j][i] = 1
    return g_return_c

def gengraph(n):
    p = []
    for i in range(0,n):
        p.append(i)
        pass
    q = []
    edges = []
    
    first_input = p[Random(len(p))-1]
    q.append(first_input)
    
    for i in range(0,n-1):
        second_input = p[Random(len(p))-1]
        p.remove(second_input)
        
        joined = q[Random(len(q))-1]
        
        edges.append([second_input,joined])
        
        q.append(second_input)
        q.sort
        pass
    g_return = np.zeros((n,n))
    for item in edges:
        g_return[item[0]][item[1]] = 1
        g_return[item[1]][item[0]] = 1
    return g_return

def weight(graph,value):
    for i in range(0,graph.shape[0]):
        for j in range(i,graph.shape[0]):
            if i == j:
                graph[i][j] = 10000
            if graph[i][j] == 0:
                graph[i][j] = 10000
            if graph[i][j] == 1:
                graph[i][j] = Random(value)
                graph[j][i] = graph[i][j]
                pass
    return graph

def dijkstra(graph_2d,n,start):
    a = []
    length = []
    distance = []
    start = start - 1 
    F = []
    edges = []
    
    for i in range(0,n):
        a.append(start)
        length.append(graph_2d[start][i])
        distance.append(graph_2d[start][i])
        pass
    length[start] = -1
    for steps in range(0,n-1):
        minimum = 10000
        for i in range(0,n):
            if length[i]>= 0 and length[i]<minimum:
                minimum = length[i]
                vclose = i
        edge = [a[vclose],vclose]
        F.append(edge)
        
        for i in range(0,n):
            if length[vclose] + graph_2d[vclose][i] < length[i]:
                length[i] = length[vclose] + graph_2d[vclose][i]
                distance[i] = length[vclose] + graph_2d[vclose][i]
                a[i] = vclose
        length[vclose] = -1
    for item in F:
        item[0] += 1
        item[1] += 1
    return[F,a,distance]

def path_finder(a_list,first,last):
    found = False
    result = []
    first -= 1
    last -= 1
    while found == False:
        result.append(last + 1)
        last = a_list[last]
        if last == first:
            result.append(last + 1)
            break
    result.reverse()
    return result



''' Test case 1

one = dijkstra(t_case1, 8, 1)
edges = one[0]
a = one[1]
length = one[2]


path = path_finder(a , 1 , 8)
print("minimum spanning tree edges", edges)
print("shortest path from 1  to 8", path)
print("length of the path is",length[7])


one = dijkstra(t_case1, 8, 7)
edges = one[0]
a = one[1]
length = one[2]


path = path_finder(a , 7 , 8)
print("minimum spanning tree edges", edges)
print("shortest path from 1  to 8", path)
print("length of the path is",length[7])


Test case 2

one = dijkstra(t_case2, 12, 2)
edges = one[0]
a = one[1]
length = one[2]


path = path_finder(a , 2 , 8)
print("minimum spanning tree edges", edges)
print("shortest path from 1  to 8", path)
print("length of the path is",length[7])


one = dijkstra(t_case2, 12, 12)
edges = one[0]
a = one[1]
length = one[2]


path = path_finder(a , 12 , 10)
print("minimum spanning tree edges", edges)
print("shortest path from 1  to 8", path)
print("length of the path is",length[10])

comp_size = 5
gengraph_size = 5

graph = comp(comp_size)
graph = weight(graph,20)
#print(graph)

graph2 = gengraph(gengraph_size)
graph2 = weight(graph2,20)
#print(graph2)
'''

h = hpy()
g = [10,50,100,200,300,400,500,1000]
for graph_sizes in g:
    graph = comp(graph_sizes)
    graph = weight(graph,20)
    #print(graph)
    graph2 = gengraph(graph_sizes)
    graph2 = weight(graph2,20)
    #print(graph2)
    
    
    heap1 = hpy()
    time_start = time.time()
    for i in range(0,graph_sizes):
        compu = dijkstra(graph,graph_sizes,i)
    time_end = time.time()
    cal = time_end - time_start
    print("*******----------********\n")
    print("\n\n Memory consumed -----",heap1.heap())
    print("Dijkstra complete graph",graph_sizes, "time taken for particular nodes = ",cal)
    
    heap2 = hpy()
    time_start = time.time()
    for i in range(0,graph_sizes):
        compu = dijkstra(graph2,graph_sizes,i)
    time_end = time.time()
    cal = time_end - time_start
    print("*******----------********\n")
    print("\n\n Memory consumed -----",heap2.heap())
    print("Dijkstra complete graph",graph_sizes, "time taken for particular nodes = ",cal)
    
print("*************--------***************")
    
    
    

































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        












































