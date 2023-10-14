import squid.base as sq
import squid.cpm as cpm
import sys

vertex_list, edge_list = sq.Graph.readEdgeList(sys.argv[1])
graph = sq.Graph(nodes = vertex_list,
              edges = edge_list,
              weighted = True)

minTime, maxTime, criticalPath = cpm.CPM(graph)

formatLine = "%10s %10s %10s %10s"
print(formatLine%("node", "minTime", "maxTime", "slack"))
for node in sorted(graph.getNodes(), key = lambda node : int(str(node))):
    print(formatLine%(node.label, minTime[node], maxTime[node], 
                      maxTime[node] - minTime[node]))

print("\nCritical Path :", end = " ")
sq.Graph.show(criticalPath)

cpm.plotCP(graph, imagepath = 'critical_path.png')