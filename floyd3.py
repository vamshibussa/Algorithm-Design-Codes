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


def get_index(i,j,n):
    if i <= j:
        return (n*(n-1))/2 - (n-1)*(n-i-1)/2 + j - i - 1
    else:
        return (n*(n-1))/2 - (n-1)*(n-i-1)/2 + i - j - 1

def converting_2d_to_1d(graph_2d,size):
    length = int((size*size - size)/2)
    result = []
    for i in range(0,size):
        for j in range(0,size):
            if i < j:
                result.append(graph_2d[i][j])
    return result


comp_size = 5
gengraph_size = 8

graph = comp(comp_size)
graph = weight(graph,20)
print(graph)

graph2 = comp(comp_size)
graph2 = weight(graph2,20)
print(graph2)

t_case1_1D = converting_2d_to_1d(t_case1,8)
t_case2_1D = converting_2d_to_1d(t_case2,12)
#print(graph_1D)

#print(graph1_1D)

def floyd(graph_1d,size):
    length = len(graph_1d)
    d_array = graph_1d.copy()
    p_array = np.zeros((length))
    for k in range(0,size):
        for i in range(0,size):
            for j in range(0,size):
                if (1!=j):
                    index_i_k = int(get_index(i,k,size))
                    index_i_j = int(get_index(i,j,size))
                    index_j_k = int(get_index(j,k,size))
                    if d_array[index_i_k] + d_array[index_i_j] + d_array[index_j_k]:
                        p_array[index_i_j] = k
                        d_array[index_i_j] = d_array[index_i_k] + d_array[index_j_k]
                        pass
    return[d_array,p_array]


def path_finder(a_array,first,last,size):
    index = int(get_index(first,last,size))
    if a_array[index] != 0:
        path_finder(a_array,first,int(a_array[first][last]))
        print(int(a_array[first][last]+1))
        path_finder(a_array,int(a_array[first][last],last))
         


















































