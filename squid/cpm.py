from squid.base import *
import matplotlib.pyplot as plt
import numpy as np
from queue import Queue

def getNodesLevel(graph : Graph):
    """ Implementation of Demoucron's algorithm. Returns the
        number of layers that need to be removed to make each
        vertex to have no predecessors. If there is a cicle, 
        returns None. """
    queue = Queue()
    incidentEdges = dict()
    level = dict()
    taken = len(graph.getNodes())

    for node in graph.getNodes():
        incidentEdges[node] = len(graph.getPredecessors(node))
        if incidentEdges[node] == 0: 
            queue.put(node)
            level[node] = 0

    while not queue.empty():
        currentNode = queue.get()
        for adjacent in graph.getSuccessors(currentNode):
            if incidentEdges[adjacent] == 0: return None
            incidentEdges[adjacent] -= 1
            if incidentEdges[adjacent] == 0: 
                queue.put(adjacent)
                level[adjacent] = level[currentNode]+1
        taken -= 1

    if taken > 0: return None
    return dict(sorted(level.items(), key = lambda item: item[1]))
# ===== #

def CPM(graph : Graph):
    """ Gets the minimum and the maximum time for each state
        (vertex) and the critical activities (edges). """
    minTime = defaultdict(lambda : 0)
    maxTime = defaultdict(lambda : 10000)
    criticalPath = list()

    def getMinTime(node):
        for adjacent in graph.getPredecessors(node):
            edgeWeight = graph.getEdges((adjacent,node)).weight
            if minTime[node] < minTime[adjacent] + edgeWeight:
                minTime[node] = minTime[adjacent] + edgeWeight

    def getMaxTime(node):
        for adjacent in graph.getSuccessors(node):
            edgeWeight = graph.getEdges((node,adjacent)).weight
            if maxTime[node] > maxTime[adjacent] - edgeWeight:
                maxTime[node] = maxTime[adjacent] - edgeWeight
        if maxTime[node] == minTime[node]:
            criticalPath.insert(0,node)

    level = list(getNodesLevel(graph).keys())
    endState = graph.getNodes(level[-1])
    for node in level: getMinTime(node)
    maxTime[endState] = minTime[endState]
    for i in range(len(level)): getMaxTime(level[-1-i])

    return minTime, maxTime, criticalPath
# ===== #

def plotCP(graph, 
           hSpacing = 20, 
           vSpacing = 20, 
           nodeSize = 20,
           imagepath = None):
    """ Plots the graph with focus on the critical path. """
    level = getNodesLevel(graph)
    layer = defaultdict(lambda : list())
    minTime, maxTime, criticalPath = CPM(graph)

    def recursiveRelevel(node):
        maxPredecessorLevel = 0
        for parent in graph.getPredecessors(node):
            if not graph.getEdges((parent,node)).weight: continue
            maxPredecessorLevel = max(maxPredecessorLevel,level[parent])
        level[node] = maxPredecessorLevel + 1
        for adjacent in graph.getSuccessors(node):
            recursiveRelevel(adjacent)

    for node in level: 
        recursiveRelevel(node)
        layer[level[node]].append(node)
    
    fig, ax = plt.subplots(figsize = (8,8))
    nodePosition = dict()
    hOffset = 0
    vOffset = 0

    for index in layer:
        vOffset = (len(layer[index])-1)*vSpacing / 2
        for node in layer[index]:
            nodePosition[node] = np.array([hOffset, vOffset])
            vOffset -= vSpacing
        hOffset += hSpacing

    for i,node in enumerate(level):
        for next in graph.getSuccessors(node):
            weight = graph.getEdges((node,next)).weight
            start = nodePosition[node]
            end = nodePosition[next]

            plt.plot([start[0],end[0]], [start[1],end[1]],
                     color = 'black', 
                     linestyle = 'solid' if weight else 'dashed',
                     label = weight,
                     linewidth = 1 if maxTime[next] - minTime[node] != weight
                                 else 3)
        plt.plot(nodePosition[node][0], nodePosition[node][1], 'o',
                 markersize = nodeSize, 
                 color = 'red' if node in criticalPath else 'black' )
        plt.annotate(str(node),
                     nodePosition[node],
                     textcoords="offset points",
                     xytext=(0,0),
                     ha = 'center',
                     va = 'center',
                     color = 'white',
                     size = nodeSize*0.7)

    if ax.get_ylim() < ax.get_xlim():
        xlim = np.array(ax.get_xlim())
        len_xlim = xlim[1] - xlim[0]
        ax.set_ylim(xlim - np.array((len_xlim/2),(len_xlim/2)))
    elif ax.get_xlim() < ax.get_ylim():
        ylim = np.array(ax.get_ylim())
        len_ylim = ylim[1] - ylim[0]
        ax.get_xlim(ylim - np.array((len_ylim/2),(len_ylim/2)))
    
    plt.title('Critical path')
    plt.axis('off')

    if imagepath is not None:
        plt.savefig(imagepath)
    plt.show()
# ===== #