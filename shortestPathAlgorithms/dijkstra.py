from data_structures.graph import WeightedGraph, Node
import queue

# weighted
def getMinimumSpanningTree(graph):
    queue = []
    parent = {node:None for node in graph.nodes}

    distance_covered = {node:10000000000 for node in graph.nodes}
    visited = {node:False for node in graph.nodes}

    # init
    queue.append(graph.getNode(1))
    # bfs

    while(queue):
        node = queue.pop(0)

        if visited[node] == False:
            for adj in graph.adjacent(node):
                # works thanks to how bfs is structured
                if parent[adj] == None:
                    parent[adj] = node
                    distance_covered[adj] = distance_covered[parent[adj]] + 1
                queue.append(adj)
             
            visited[node] = True

    minimumSpanningTree = [(p,c) for c,p in parent.items() if p is not None]
    return minimumSpanningTree


# when choosing which node to explore, you prioritize the node 
# with smallest edge weight because that would mean always going for the least amount
# of resistance to another.

# Implements Dijkstra's algorithm for finding the shortest paths from a starting node to all other nodes in a weighted graph.
# The algorithm uses a priority queue to always expand the node with the smallest known distance.
# For each node, it updates the shortest known distance to its adjacent nodes if a shorter path is found.
# The function returns a list of parent-child relationships representing the shortest path tree, and a dictionary of distances.
"""
Finds the shortest paths from the starting node to all other nodes in a weighted graph using Dijkstra's algorithm.
Args:
    graph: A graph object that provides methods `nodes`, `getNode(node_id)`, `adjacent(node)`, and `getWeight(node1, node2)`.
    starting_id: The identifier of the starting node.
Returns:
    tuple:
        - List of (parent, child) tuples representing the shortest path tree.
        - Dictionary mapping each node to its shortest distance from the starting node.
"""

def dijkstra(graph, starting_id):
    distance = {node:999 for node in graph.nodes}
    parent = {node:None for node in graph.nodes}
    shortestpath = []

    pq = queue.PriorityQueue()
    
    root = graph.getNode(starting_id)
    distance[root] = 0  
    pq.put((0, root.id, root))
    
    # bfs-style navigation
    while len(pq.queue) != 0:

        node = graph.getNode(pq.get()[1])

        for adj in graph.adjacent(node):

            if distance[adj] > distance[node] + graph.getWeight(node, adj):
                distance[adj] = distance[node] + graph.getWeight(node, adj)
                parent[adj] = node

            pq.put((distance[adj], adj.id))

        print(node, distance[node])
        print(pq.queue)


    shortestpath = [(p,c) for c,p in parent.items() if p is not None]

    return shortestpath, distance
    
def bellman_ford(graph, starting_id):
    distance = {node:999 for node in graph.nodes}
    parent = {node:None for node in graph.nodes}
    shortestpath = []

    pq = queue.PriorityQueue()
    
    root = graph.getNode(starting_id)
    distance[root] = 0  
    pq.put((0, root.id, root))

    for i in range(graph.node_count-1):
        node = graph.getNode(pq.get()[1])
        if distance[node] != 999:

            for adj in graph.adjacent(node):

                if distance[adj] > distance[node] + graph.getWeight(node, adj):
                    distance[adj] = distance[node] + graph.getWeight(node, adj)
                    parent[adj] = node

                pq.put((distance[adj], adj.id))

        print(f'{i=}')
        print(node, distance[node])
        print(pq.queue)


    shortestpath = [(p,c) for c,p in parent.items() if p is not None]
    return shortestpath, distance

if __name__ == '__main__':
    wgraph = WeightedGraph(6, True)

    # Add edges using inherited addEdge method, passing WeightedNode objects
    wgraph.addEdge(wgraph.getNode(0), Node(1, "node_1"), 7)
    wgraph.addEdge(wgraph.getNode(0), Node(2, "node_2"), 9)
    wgraph.addEdge(wgraph.getNode(0), Node(5, "node_5"), 14)
    wgraph.addEdge(wgraph.getNode(1), Node(2, "node_2"), 10)
    wgraph.addEdge(wgraph.getNode(1), Node(3, "node_3"), 15)
    wgraph.addEdge(wgraph.getNode(2), Node(3, "node_3"), 11)
    wgraph.addEdge(wgraph.getNode(2), Node(5, "node_5"), 2)
    wgraph.addEdge(wgraph.getNode(3), Node(4, "node_4"), 6)
    wgraph.addEdge(wgraph.getNode(4), Node(5, "node_5"), 9)

    print(wgraph)
    # print(getMinimumSpanningTree(wgraph))
    # print(dijkstra(wgraph, 0))


    wgraph2 = WeightedGraph(6, True)
    wgraph2.addEdge(wgraph.getNode(0), Node(1, "node_1"), 10)
    wgraph2.addEdge(wgraph.getNode(0), Node(5, "node_5"), 8)
    wgraph2.addEdge(wgraph.getNode(1), Node(3, "node_3"), 2)
    wgraph2.addEdge(wgraph.getNode(2), Node(1, "node_1"), 1)
    wgraph2.addEdge(wgraph.getNode(3), Node(2, "node_2"), -2)
    wgraph2.addEdge(wgraph.getNode(4), Node(3, "node_3"), -1)
    wgraph2.addEdge(wgraph.getNode(4), Node(1, "node_1"), -4)
    wgraph2.addEdge(wgraph.getNode(5), Node(4, "node_4"), 1)
    print(wgraph2)


    print(bellman_ford(wgraph2, 0))
    # print(dijkstra(wgraph2, 0))