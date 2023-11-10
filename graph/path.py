from queue import Queue, PriorityQueue

def get_path(graph, src, dest):
    successors, predecessors = graph.get_relations()

    u = None
    parent = dict()
    visited = set()
    queue = Queue()

    queue.put(src)
    visited.add(src)
    parent[src] = None

    while not queue.empty():
        u = queue.get()
        visited.add(u)
        if u is dest: break
        if not u in successors: continue
        for v in successors[u]:
            if v in visited: continue
            parent[v] = u
            queue.put(v)

    if u is not dest: 
        return None
    
    path = []
    while parent[u]:
        edge = graph.get_edge(parent[u],u) 
        path.append(edge)
        u = parent[u]
    path.reverse()

    return path

def dijkstra(graph, src):
    successors, predecessors = graph.get_relations()
    
    u = None
    parent = dict()
    visited = set()
    nearest = PriorityQueue()
    dist = dict()

    dist[src] = 0
    nearest.put((0,src))

    while u := nearest.get()[1] and dist[u] < float('inf'):
        visited.add(u)
        for v in successors[u]:
            if not dist.get(v) \
               and dist[v] > dist[u] + graph.get_edge(u,v).weight:
                dist[v] = dist[u] + graph.get_edge(u,v).weight
                queue.put((dist[v],v))


            
