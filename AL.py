import guppy
from guppy import hpy
import time

import sys
from collections import defaultdict 


class Heap(): 

	def __init__(self): 
		self.array = [] 
		self.size = 0
		self.pos = [] 

	def newMinHeapNode(self, v, dist): 
		minHeapNode = [v, dist] 
		return minHeapNode 


	def swapMinHeapNode(self, a, b): 
		t = self.array[a] 
		self.array[a] = self.array[b] 
		self.array[b] = t 

	def minHeapify(self, idx): 
		smallest = idx 
		left = 2 * idx + 1
		right = 2 * idx + 2

		if left < self.size and self.array[left][1] <self.array[smallest][1]: 
			smallest = left 

		if right < self.size and self.array[right][1] <self.array[smallest][1]: 
			smallest = right 

		if smallest != idx: 

			self.pos[ self.array[smallest][0] ] = idx 
			self.pos[ self.array[idx][0] ] = smallest 

			self.swapMinHeapNode(smallest, idx) 

			self.minHeapify(smallest) 

	def extractMin(self): 

		if self.isEmpty() == True: 
			return


		root = self.array[0] 

		lastNode = self.array[self.size - 1] 
		self.array[0] = lastNode 

		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1

		self.size -= 1
		self.minHeapify(0) 

		return root 

	def isEmpty(self): 
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist): 


		i = self.pos[v] 

		self.array[i][1] = dist 

		while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 

			self.pos[ self.array[i][0] ] = (i-1)/2
			self.pos[ self.array[(i-1)//2][0] ] = i 
			self.swapMinHeapNode(i, (i - 1)//2 ) 

			i = (i - 1) // 2; 

	def isInMinHeap(self, v): 

		if self.pos[v] < self.size: 
			return True
		return False


def printArr(parent, n): 
	for i in range(1, n): 
		print ("% d - % d" % (parent[i], i))


class Graph(): 

	def __init__(self, V): 
		self.V = V 
		self.graph = defaultdict(list) 

	# Adds an edge to an undirected graph 
	def addEdge(self, src, dest, weight): 


		newNode = [dest, weight] 
		self.graph[src].insert(0, newNode) 


		newNode = [src, weight] 
		self.graph[dest].insert(0, newNode) 


	def PrimMST(self): 
		# Get the number of vertices in graph 
		V = self.V 
		
		# key values used to pick minimum weight edge in cut 
		key = [] 
		
		# List to store contructed MST 
		parent = [] 

		# minHeap represents set E 
		minHeap = Heap() 


		for v in range(V): 
			parent.append(-1) 
			key.append(sys.maxsize) 
			minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) ) 
			minHeap.pos.append(v) 

		# Make key value of 0th vertex as 0 so 
		# that it is extracted first 
		minHeap.pos[0] = 0
		key[0] = 0
		minHeap.decreaseKey(0, key[0]) 

		# Initially size of min heap is equal to V 
		minHeap.size = V; 

		# In the following loop, min heap contains all nodes 
		# not yet added in the MST. 
		while minHeap.isEmpty() == False: 

			# Extract the vertex with minimum distance value 
			newHeapNode = minHeap.extractMin() 
			u = newHeapNode[0] 

			# Traverse through all adjacent vertices of u 
			# (the extracted vertex) and update their 
			# distance values 
			for pCrawl in self.graph[u]: 

				v = pCrawl[0] 
 
				if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
					key[v] = pCrawl[1] 
					parent[v] = u 

					# update distance value in min heap also 
					minHeap.decreaseKey(v, key[v]) 

		printArr(parent, V) 


h = hpy()
graph = Graph(9) 
graph.addEdge(0, 1, 1) 
graph.addEdge(0, 7, 1) 
graph.addEdge(1, 2, 1) 
graph.addEdge(1, 7, 1) 
graph.addEdge(2, 3, 1) 
graph.addEdge(2, 8, 1) 
graph.addEdge(2, 5, 1) 
graph.addEdge(3, 4, 1) 
graph.addEdge(3, 5, 1) 
graph.addEdge(4, 5, 1) 
graph.addEdge(5, 6, 1) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 1) 
graph.addEdge(7, 8, 1) 
graph.PrimMST() 


heap1 = hpy()
time_start = time.time()
compu = graph.PrimMST()
time_end = time.time()
cal = time_end - time_start
print("*******----------********\n")
print("\n\n Memory consumed -----",heap1.heap())
print("Prims complete graph", "time taken for particular nodes = ",cal)