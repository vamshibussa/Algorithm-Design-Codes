#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from guppy import hpy
import time
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
            return 100000
        
    def updateWeight(self,u,v,new_w):
        #pdb.set_trace()
        flag = 0
        temp = self.head
        while(temp.node != u):
            temp = temp.down
        temp = temp.next
        while(temp.ver != v):
            if temp.next == None:
                flag = 1
                break
            temp = temp.next
        if flag:
            temp2 = Node(v, new_w)
            temp.next = temp2
        else:
            temp.w = new_w
        
        
def printSolution(g):
    #print("Solution matrix")
    for i in range(1,g.V+1):
        print("Vertex \tDistance from Source ", i)
        for j in range(1,g.V+1):
            if i==j:
                print(j, "\t", 0)
            else:
                ind4 = g.findWeight(i,j)
                print(j, "\t", ind4)
        print("\n")

def floyd(g):
    #dist = list(map(lambda i : list(map(lambda j : j, i)), g.graph))
    #pdb.set_trace()
    #dist = list(map(lambda i : i, g.graph))
    #pdb.set_trace()
    for k in range(1,g.V+1):
        for i in range(1,g.V+1):
            for j in range(1,g.V+1):
                ind1 = g.findWeight(i,j)
                ind2 = g.findWeight(i,k)
                ind3 = g.findWeight(k,j)
                if i!=j:
                    new_w = min(ind1, ind2+ind3)
                    g.updateWeight(i,j,new_w)
    #pdb.set_trace()
    printSolution(g)
    
nodes = 5

start = time.time()
h = hpy()

g1 = Graph(nodes)
g1.generateComplete(nodes)
g1.printGraph()
floyd(g1)
print("\n\n Memory consumed --- complete graph", h.heap())

#h = hpy()

g2 = Graph(nodes)
g2.generateSparse(nodes)
#print("\n\n Memory consumed --- sparse graph", h.heap())
g2.printGraph()
floyd(g2)

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
#floyd(g3)

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
#floyd(g4)
