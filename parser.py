import networkx as nx
import matplotlib.pyplot as plt
import core
import cover

gml = nx.read_gml('sjdr.gml')
graph = core.Graph(directed = False);

for label in gml.nodes: graph.add_node(label)
for edge in gml.edges: 
    src, dest = edge
    name = gml.get_edge_data(src, dest)['name']

    added_edge = graph.add_edge(src, dest)
    added_edge.get_data()['name'] = name

nx.draw(gml)
plt.savefig('teste.png')


print(len(gml.edges))
print(sum(len(graph.edges[node]) for node in graph.nodes if node in graph.edges))
cover = cover.vertex_cover(graph)
covered = set()
for node in cover:
    if not node in graph.edges: continue
    for adj in graph.edges[node]:
        covered.add((node,adj))
print(len(covered))
