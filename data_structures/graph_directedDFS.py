from graph import Graph
import random

class StatusCodes:
    UNEXPLORED = 0
    EXPLORING = 1
    VISITED = 2


# STATUS CODES:
# 0 = not visited
# 1 = exploring
# 2 = visited

# u,v are ids of the node
# is v descendant of u?
def isDescendant(parent, u, v):
    tmp = v

    # while tmp hasn't ascended to root id
    while tmp != -1:
        if tmp == u:
            return True

        tmp = parent[tmp]
        
    return False


def categorizeEdges(graph, edges, id, status, parent):

    root = graph.getNode(id)

    status[root.id] = StatusCodes.EXPLORING
    
    # if there are no adjacent nodes, there are no edges to add to the dict,
    # which means that `edges` will not be modified.
    if len(graph.adjacency_list[root]) == 0:
        status[root.id] = StatusCodes.VISITED
        return edges

    for adj_node in graph.adjacency_list[root]:
        # analyze
        if status[adj_node.id] == StatusCodes.UNEXPLORED:
            status[adj_node.id] = StatusCodes.EXPLORING
            parent[adj_node.id] = id

            print(adj_node.id)

            edges["tree"].append((id, adj_node.id))
            categorizeEdges(graph, edges, adj_node.id, status, parent)


        elif status[adj_node.id] == StatusCodes.EXPLORING:
            edges["back"].append((id, adj_node.id))

        elif status[adj_node.id] == StatusCodes.VISITED:
            if isDescendant(parent, id, adj_node.id):
                edges["fwd"].append((id, adj_node.id))
                print(id, adj_node.id)
            else:
                edges["cross"].append((id, adj_node.id))
        
    status[root.id] = StatusCodes.VISITED
    return edges
        


# GRAPH INIT
g = Graph(11, True)
# Statically generate random edges (no duplicates, no self-loops)
# Create a simple cycle: 0 -> 1 -> 2 -> ... -> 10 -> 0
for i in range(len(g.nodes)):
    u = g.getNode(i)
    v = g.getNode((i + 1) % len(g.nodes))
    g.addEdge(u, v)
# Add a forward edge: 0 -> 3 (from lower to higher node, not consecutive)
g.addEdge(g.getNode(0), g.getNode(3))
# Add a back edge: 4 -> 1 (from one branch to another, not ancestor/descendant)
g.addEdge(g.getNode(4), g.getNode(1))
# Add a forward edge: 8 -> 11 (from one branch to another, not ancestor/descendant)
g.addNode(11,11)
g.addEdge(g.getNode(2), g.getNode(11))
g.addEdge(g.getNode(8), g.getNode(11))
g.adjacency_list[g.getNode(2)][0], g.adjacency_list[g.getNode(2)][1] = g.adjacency_list[g.getNode(2)][1], g.adjacency_list[g.getNode(2)][0] 
g.addEdge(g.getNode(7),g.getNode(5))
# print(g)


status = [StatusCodes.UNEXPLORED for _ in range(g.node_count)]
parent = [-1 for _ in range(g.node_count)]
edges = {
    "tree":[],
    "back":[],
    "fwd":[],
    "cross":[]
}


print(categorizeEdges(g, edges=edges, id=4, status=status, parent=parent))