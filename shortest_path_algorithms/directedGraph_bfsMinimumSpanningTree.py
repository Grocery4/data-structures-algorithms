from data_structures.graph import Graph

def unweightedGetMinimumSpanningTree(graph):
    queue = []
    parent = {node:None for node in graph.nodes}
    distance_covered = {node:0 for node in graph.nodes}
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
        


if __name__ == '__main__':
    graph = Graph(6, True)
    graph.removeNode(0)
    graph.addEdge(graph.getNode(1), graph.getNode(2))
    graph.addEdge(graph.getNode(1), graph.getNode(3))
    graph.addEdge(graph.getNode(2), graph.getNode(3))
    graph.addEdge(graph.getNode(2), graph.getNode(4))
    graph.addEdge(graph.getNode(2), graph.getNode(5))
    graph.addEdge(graph.getNode(3), graph.getNode(2))
    graph.addEdge(graph.getNode(3), graph.getNode(4))
    graph.addEdge(graph.getNode(3), graph.getNode(5))
    graph.addEdge(graph.getNode(5), graph.getNode(4))
    print(unweightedGetMinimumSpanningTree(graph))


    graph2 = Graph(6, True)
    graph2.addEdge(graph.getNode(1),graph.getNode(2))
    graph2.addEdge(graph.getNode(1),graph.getNode(3))
    graph2.addEdge(graph.getNode(2),graph.getNode(4))
    graph2.addEdge(graph.getNode(4),graph.getNode(5))
    graph2.addEdge(graph.getNode(3),graph.getNode(5))
    graph2.removeNode(0)
    print(unweightedGetMinimumSpanningTree(graph2))


    # Example: create a third graph with more nodes to test unweightedSpanningTree()
    graph3 = Graph(11, True)
    graph3.addEdge(graph3.getNode(1), graph3.getNode(2))
    graph3.addEdge(graph3.getNode(1), graph3.getNode(3))
    graph3.addEdge(graph3.getNode(2), graph3.getNode(4))
    graph3.addEdge(graph3.getNode(3), graph3.getNode(4))
    graph3.addEdge(graph3.getNode(4), graph3.getNode(5))
    graph3.addEdge(graph3.getNode(5), graph3.getNode(6))
    graph3.addEdge(graph3.getNode(6), graph3.getNode(7))
    graph3.addEdge(graph3.getNode(7), graph3.getNode(8))
    graph3.addEdge(graph3.getNode(8), graph3.getNode(9))
    graph3.addEdge(graph3.getNode(9), graph3.getNode(10))
    graph3.addEdge(graph3.getNode(3), graph3.getNode(7))
    graph3.addEdge(graph3.getNode(2), graph3.getNode(8))
    graph3.removeNode(0)
    print(unweightedGetMinimumSpanningTree(graph3))
