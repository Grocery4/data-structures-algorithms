# ALGORITHM DESCRIPTION
# BFS is the other way to traverse a graph
# it consists in using a stack to traverse spanning tree level-by-level
# instead of going depth first.. heh.. get it?
# each time a node is visited its children are added to the stack before being flagged as marked

from data_structures.graph import Graph

def BFS(graph):
    stack = []
    visited = [False for _ in range(graph.node_count)]

    first_iter = True
    stack.append(graph.getNode(0))
    while(len(stack) != 0):
        
        node = stack.pop(0)
        if visited[node.id] == False:
            for adj in graph.adjacent(node):
                stack.append(adj)
            
            print(node)
            visited[node.id] = True
        print(stack)


if __name__ == '__main__':
    g = Graph(11, False)
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
    
    BFS(g)