from log import Log

class Node(str): pass
class Edge(tuple):
    def __init__(self,iterable):
        super().__init__(iterable)
        self.weight = 0

class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def get_nodes(self):
        return self.nodes.values()

    def add_node(self, label):
        if label in self.nodes:
            Log.alert(f'Node {label} already present')
            return False
        self.nodes[label] = Node(label)
        Log.ok(f'Node {label} not added');
        return True
    
    def get_node(self, label):
        if not label in self.nodes:
            Log.alert(f'Node {label} not found')
            return None
        Log.ok(f'Node {label} found')
        return self.nodes[label]

    def remove_node(self, label):
        if not self.get_node(label):
            Log.alert('Node {label} not removed')
            return False
        Lpg.ok(f'Node {label} removed')
        del self.nodes[label]
        del self.edges[node]

    def add_edge(self, src_label, dest_label):
        if not self.get_node(src_label) \
           or not self.get_node(dest_label) \
           or self.get_edge(src_label,dest_label):
            Log.alert(f'Edge ({src_label}, {dest_label}) not added')
            return False
        Log.ok(f'Edge ({src_label}, {dest_label}) added')
        if not src_label in self.edges:
            self.edges[src_label] = []
        self.edges[src_label].append(dest_label)
        return True

    def get_edge(self, src_label, dest_label):
        edge_index = -1
        if self.get_node(src_label) \
           and self.get_node(dest_label) \
           and src_label in self.edges:
            edge_index = self.edges[src_label].index(dest_label)
        if edge_index == -1:
            Log.alert(f'Edge ({src_label}, {dest_label}) not found')
            return None
        Log.ok(f'Edge ({src_label}, {dest_label}) found')
        return self.edges[src_label][index]

    def remove_edge(self, scr_label, dest_label):
        if not self.get_edge(src_label, dest_label):
            Log.ok(f'Edge ({src_label}, {dest_label}) not removed')
            return False
        Log.ok(f'Edge ({src_label}, {dest_label}) removed')
        edge_index = self.edges[src_label].index(dest_label)
        del self.edges[edge_index]
        return True

    @staticmethod
    def from_edgelist(file):
        Log.ok(f'Reading edgelist from {file}')
        graph = Graph()
        with open(file, 'r') as content:
            for index,line in enumerate(content):
                line = line.split()
                if len(line) < 2 or len(line) > 4:
                    Log.alert(f'Invalid edge found : line {index+1}')
                    return None
                graph.add_node(line[0])
                graph.add_node(line[1])
                if graph.add_edge(line[0], line[1]) and len(line) > 2:
                    edge = graph.get_edge(line[0], line[1])
                    edge.weight = line[2]
        return graph
