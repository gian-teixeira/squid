from core import Graph

def vertex_cover(graph):
    successors, predecessors = graph.get_relations()
    nodes = sorted(graph.nodes, 
                   key = lambda node : -graph.get_node_degree(node, -1))
    excluded = set()
    cover = set()

    for base in nodes:
        if not base in successors: continue
        #if base in excluded: 
        for neighbor in successors[base]:
            if base in excluded and \
               not neighbor in excluded: continue
            excluded.add(neighbor)
        cover.add(base)

    return cover
