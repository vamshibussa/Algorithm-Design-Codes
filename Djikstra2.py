#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:26:20 2019

@author: vamshi
"""

import time
import sys
import random
import pdb

def rand():
    return random.randint(1, nodes)

class Node:
    def __init__ (self,ver, w):
        self.ver = ver
        self.w = w
        self.next = None
        
class FirstNode:
    def __init__(self,v, cur = 1):
        if v!=1:
            self.down = FirstNode(v-1, cur+1)
        else:
            self.down = None
        self.node = cur
        self.next = None
        
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.head = FirstNode(vertices)
        
    def weight(self):
        return rand()
        
    def addEdge(self, u, v, w):
        temp1 = self.head
        while(temp1.node != u):
            temp1 = temp1.down
        #temp1 = temp1.next
        while(temp1.next != None):
            temp1 = temp1.next
        temp2 = Node(v, w)
        temp1.next = temp2
        temp3 = self.head
        while(temp3.node != v):
            temp3 = temp3.down
        #temp3 = temp3.next
        while(temp3.next != None):
            temp3 = temp3.next
        temp4 = Node(u,w)
        temp3.next = temp4
#        self.graph[u][v]=w
#        self.graph[v][u]=w
    
    def generateSparse(self, n):
        #pdb.set_trace()
        arr = [0]
        random_val = rand()
        while len(arr) != (n+1):
           if random_val not in arr:
               arr.append(random_val)
           random_val = rand()
        print("\nrandom array", arr, "\n")
        for i in range(1,n):
            self.addEdge(arr[i],arr[i+1],self.weight())
            
    def generateComplete(self, n):
        for i in range(1,n+1):
            for j in range(i+1, n+1):
                self.addEdge(i, j, self.weight())
                
    def printGraph(self):
        #pdb.set_trace()
        temp = self.head
        for i in range(1, self.V+1):
            print("Source node : ",temp.node)
            print("vertice\t\tweight")
            temp1 = temp.next
            while temp1 != None:
                print(temp1.ver, "\t\t", temp1.w)
                temp1 = temp1.next
            temp = temp.down
            
    def findWeight(self,u,v):
        #pdb.set_trace()
        flag = 1
        temp = self.head
        while(temp.node != u):
            temp = temp.down
        temp = temp.next
        while(temp.ver != v):
            if temp.next == None:
                flag = 0
                break
            temp = temp.next
        if flag:
            return temp.w
        else:
            return 0


def printSolution(g, dist, src):
        print("Vertex \tDistance from Source ", src)
        for node in range(1, g.V+1):
            print(node, "\t", dist[node])
                
def minDistance(g, dist, sptSet):
        #pdb.set_trace()
        # Initilaize minimum distance for next node
        minimum = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(1, g.V+1):
            if dist[v] < minimum and sptSet[v] == False:
                minimum = dist[v]
                min_index = v

        return min_index

def dijkstra(g, src):
        #pdb.set_trace()
        dist = [sys.maxsize] * (g.V+1)
        dist[src] = 0
        sptSet = [False] * (g.V+1)

        for cout in range(1, g.V+1):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = minDistance(g, dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(1, g.V+1):
                if g.findWeight(u,v) > 0 and sptSet[v] == False and dist[v] > dist[u] + g.findWeight(u,v):
                    dist[v] = dist[u] + g.findWeight(u,v)

        printSolution(g, dist, src)

nodes = 300

start = time.time()

g1 = Graph(nodes)
g1.generateComplete(nodes)
g1.printGraph()
for i in range(1, nodes+1):
    dijkstra(g1, i)
    
#g2 = Graph(nodes)
#g2.generateSparse(nodes)
#g2.printGraph()
#for i in range(1, nodes+1):
#    dijkstra(g2, i)
#pdb.set_trace()

print("\n\nElapsed time : ", time.time() - start, " seconds")

##input for test case 1
#nodes=8
#g3 = Graph(nodes)
#g3.addEdge(1,4,29)
#g3.addEdge(2,7,11)
#g3.addEdge(2,6,11)
#g3.addEdge(3,4,12)
#g3.addEdge(3,6,5)
#g3.addEdge(3,7,5)
#g3.addEdge(4,5,5)
#g3.addEdge(4,7,13)
#g3.addEdge(5,7,7)
#g3.addEdge(5,8,11)
#g3.addEdge(6,8,17)
#g3.printGraph()
#dijkstra(g3, 1)
#dijkstra(g3, 7)
#
##input for test case 2
#nodes=12
#g4 = Graph(nodes)
#g4.addEdge(1,2,11)
#g4.addEdge(1,3,14)
#g4.addEdge(1,5,8)
#g4.addEdge(1,7,29)
#g4.addEdge(1,8,28)
#g4.addEdge(1,11,14)
#g4.addEdge(2,3,12)
#g4.addEdge(2,5,6)
#g4.addEdge(3,4,18)
#g4.addEdge(3,5,13)
#g4.addEdge(3,9,25)
#g4.addEdge(3,6,13)
#g4.addEdge(3,12,16)
#g4.addEdge(4,7,27)
#g4.addEdge(4,8,17)
#g4.addEdge(4,9,9)
#g4.addEdge(4,10,25)
#g4.addEdge(5,12,22)
#g4.addEdge(6,8,15)
#g4.addEdge(6,9,5)
#g4.addEdge(8,9,5)
#g4.addEdge(8,10,9)
#g4.addEdge(9,11,25)
#dijkstra(g4, 2)
#dijkstra(g4, 12)
