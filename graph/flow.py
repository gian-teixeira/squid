from queue import Queue
from level import get_levels
from path import get_path

def max_flow(graph):
    levels = get_levels(graph)
    src = levels[0][0]
    end = levels[-1][0]
    max_flow = 0

    while path := get_path(graph, src, end):
        local_flow = path[0].weight
        for edge in path:
            local_flow = min(local_flow, edge.weight)
        for edge in path:
            reverse = graph.get_edge(edge.dest,edge.src)
            if not reverse:
                reverse = graph.add_edge(edge.dest, edge.src)
            reverse.weight += local_flow
            edge.weight -= local_flow
            if edge.weight == 0:
                graph.remove_edge(edge.src, edge.dest)
        max_flow += local_flow
    
    return max_flow
