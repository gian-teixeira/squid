import squid.base as sq
import squid.cpm as cpm

vertex_list, edge_list = sq.Graph.readEdgeList('./crit.in')
graph = sq.Graph(nodes = vertex_list,
              edges = edge_list,
              weighted = True)

minTime, maxTime, criticalPath = cpm.CPM(graph)

formatLine = "%10s %10s %10s %10s"
print(formatLine%("node", "minTime", "maxTime", "slack"))
for node in graph.getNodes():
    print(formatLine%(node.label, minTime[node], maxTime[node], 
                      maxTime[node] - minTime[node]))

print("\nCritical Path :", end = " ")
sq.Graph.show(criticalPath)

cpm.plotCP(graph)