from core import Graph
from level import get_levels
from path import get_path, dijkstra
from flow import max_flow

graph = Graph.from_edgelist('./in.txt')
print(max_flow(graph))
