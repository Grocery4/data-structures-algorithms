from data_structures.graph import WeightedGraph
from queue import PriorityQueue

def prim(graph, src):
    cost = {node:999 for node in graph.nodes}
    # parent could be substituted by a mst set of edges
    parent = {node:None for node in graph.nodes}
    visited = {node:False for node in graph.nodes}

    cost[src] = 0
    pq = PriorityQueue()
    pq.put((cost[src], src.id))

    while len(pq.queue) != 0:
        node = graph.getNode(pq.get()[1])
        for adj in graph.adjacent(node):
            if visited[adj] == False:
                print(f'{node=}, {adj=}')
                if cost[adj] > graph.getWeight(node, adj):
                    cost[adj] = graph.getWeight(node, adj)
                    parent[adj] = node
                else:
                    print('skipped!')
                pq.put((cost[adj], adj.id))

        visited[node] = True

    return parent


if __name__ == '__main__':
    wgraph = WeightedGraph(7, False)
    wgraph.addEdge(wgraph.getNode(0), wgraph.getNode(1), 2)
    wgraph.addEdge(wgraph.getNode(0), wgraph.getNode(2), 3)
    wgraph.addEdge(wgraph.getNode(0), wgraph.getNode(3), 3)
    wgraph.addEdge(wgraph.getNode(1), wgraph.getNode(2), 4)
    wgraph.addEdge(wgraph.getNode(1), wgraph.getNode(4), 3)
    wgraph.addEdge(wgraph.getNode(2), wgraph.getNode(3), 5)
    wgraph.addEdge(wgraph.getNode(2), wgraph.getNode(4), 1)
    wgraph.addEdge(wgraph.getNode(2), wgraph.getNode(5), 6)
    wgraph.addEdge(wgraph.getNode(3), wgraph.getNode(5), 7)
    wgraph.addEdge(wgraph.getNode(4), wgraph.getNode(5), 8)
    wgraph.addEdge(wgraph.getNode(5), wgraph.getNode(6), 9)

    print(wgraph)

    print(prim(wgraph, wgraph.getNode(0)))
