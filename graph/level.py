from queue import Queue

def get_levels(graph):
    nodes = graph.get_nodes()
    successors, predecessors = graph.get_relations()
    pred_count = { key: len(value) for key,value in predecessors.items() }

    queue = Queue()
    level_group = dict()
    level = dict()
    visited = set()

    for u in nodes:
        if not u in predecessors:
            queue.put(u)
            visited.add(u)
            level[u] = 0
            break

    while not queue.empty():
        u = queue.get()
        if not level[u] in level_group:
            level_group[level[u]] = []
        level_group[level[u]].append(u)
        if not u in successors: continue
        for v in successors[u]:
            pred_count[v] -= 1
            if pred_count[v] == 0 and not v in visited:
                queue.put(v)
                visited.add(v)
                level[v] = level[u]+1

    if len(visited) != len(nodes):
        return None

    return list(level_group.values())
