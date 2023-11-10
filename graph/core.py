from queue import Queue

class Node(str): pass

class Edge():
    def __init__(self,src,dest, weight = 0):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.data = dict()
    
    def get_data(self):
        return self.data

    def __str__(self):
        return f'({self.src}, {self.dest})'

class Graph:
    def __init__(self, directed = False):
        self.nodes = dict()
        self.edges = dict()
        self.directed = directed

    def get_nodes(self):
        nodes = self.nodes.values()
        return list(nodes)

    def add_node(self, label):
        if label in self.nodes:
            return False
        self.nodes[label] = Node(label)
        return True
    
    def get_node(self, label):
        if not label in self.nodes:
            return None
        return self.nodes[label]

    def remove_node(self, label):
        if not self.get_node(label):
            return False
        del self.nodes[label]
        del self.edges[node]

    def get_node_degree(self, label, default = None):
        if not label in self.nodes: return default
        if not label in self.edges: return 0
        return len(self.edges[label])

    def add_edge(self, src_label, dest_label):
        if self.get_edge(src_label, dest_label) \
           or not src_label in self.nodes \
           or not dest_label in self.nodes:
            return None
        if not src_label in self.edges:
            self.edges[src_label] = dict()
        edge = Edge(src_label,dest_label)
        self.edges[src_label][dest_label] = edge 
        if not self.directed:
            reverse = self.add_edge(dest_label, src_label)
            if reverse: reverse.data = edge.data
        return edge

    def get_edge(self, src_label, dest_label):
        try: return self.edges[src_label][dest_label]
        except: return None

    def remove_edge(self, src_label, dest_label):
        try:
            del self.edges[src_label][dest_label]
            return True
        except: return False

    def get_relations(self):
        successors = dict()
        predecessors = dict()
        for u in self.edges:
            successors[u] = []
            for v in self.edges[u]:
                if not v in predecessors: 
                    predecessors[v] = []
                successors[u].append(v)
                predecessors[v].append(u)
        return successors, predecessors

    @staticmethod
    def from_edgelist(file):
        graph = Graph()
        with open(file, 'r') as content:
            for index,line in enumerate(content):
                line = line.split()
                if len(line) < 2 or len(line) > 4:
                    return None
                graph.add_node(line[0])
                graph.add_node(line[1])
                if graph.add_edge(line[0], line[1]) and len(line) > 2:
                    edge = graph.get_edge(line[0], line[1])
                    edge.weight = float(line[2])
        return graph
