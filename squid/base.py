from collections import defaultdict
from typing import *

class Node():
    def __init__(self, label, 
                 item : dict = None):
        self.label = label
        if not item: item = defaultdict(lambda : None)
        self.item = item

    def __getitem__(self, __name):
        return self.item[__name]
    
    def __setitem__(self, __name, value):
        self.item[__name] = value
    
    def __str__(self):
        return str(self.label)
    
    def getLabel(self):
        return self.label

class Edge():
    def __init__(self, 
                 src : Node, 
                 dest : Node, 
                 weight : float = 0,
                 item : dict = None):
        self.src = src
        self.dest = dest
        self.weight = weight
        if not item: item = dict()
        self.item = item
    
    def reversed(self):
        return Edge(self.dest,self.src,self.weight,self.item.copy())
    
    def __getitem__(self, __name: str):
        return self.item[__name]
    
    def __setitem__(self, __name: str, value):
        self.item[__name] = value
    
    def __str__(self):
        if self.weight: (f'({str(self.src)},{str(self.dest)},{self.weight})')
        return (f'({str(self.src)},{str(self.dest)})')

class Graph:
    def __init__(self, 
                 nodes : list = list(),
                 edges : list[tuple] = list(),
                 directed : bool = True,
                 weighted : bool = False):
        
        if not weighted: edges = [(src,dest,0) for src,dest in edges]
        if not directed: edges += [(dest,src,weight) for src,dest,weight in edges]

        self.nodes = {label : Node(label) for label in set(nodes)}
        self.edges = defaultdict(lambda : list())
        self.successors : Dict[Node,List[Node]] = defaultdict(lambda : list())
        self.predecessors : Dict[Node,List[Node]] = defaultdict(lambda : list())

        for src,dest,weight in edges:
            src = self.nodes[src]
            dest = self.nodes[dest]

            e = Edge(src,dest,float(weight))
            self.edges[tuple((src,dest))].append(e)
            self.successors[src].append(dest)
            self.predecessors[dest].append(src)
            
    def getNodes(self, label = None):
        if not label: return self.nodes.values()
        if type(label) == list():
            return [self.getNodes(l) for l in label]
        return self.nodes[str(label)]
    
    def getEdges(self, pair = None):
        if not pair: return self.edges.values()
        edges = self.edges[tuple(pair)]
        if len(edges) == 0: return None
        if len(edges) == 1: return edges[0]
        return edges
    
    def getSuccessors(self, node):
        if type(node) == Node: return self.successors[node]
        else: return self.successors[self.getNodes(node)]
    
    def getPredecessors(self, node):
        if type(node) == Node: return self.predecessors[node]
        else: return self.predecessors[self.getNodes(node)]

    @staticmethod
    def show(list : list):
        print("[", " ".join([str(item) for item in list]), "]")

    @staticmethod
    def readEdgeList(filePath : str):
        nodes = set()
        edges = list()
        with open(filePath) as file:
            for line in file:
                e = tuple(line.split())
                nodes.add(e[0])
                nodes.add(e[1])
                edges.append(e)
        return list(nodes), edges