from data_structures.graph import WeightedGraph, Node
from data_structures.disjoint_set import DisjointSet


def kruskal(graph):
    sorted_edges = sorted(graph.edges(), key = lambda x:x[2])
    
    MST_edges = []
    nodes = DisjointSet(graph.node_count)
    while len(MST_edges) < (graph.node_count - 1):
        min_weight_edge = sorted_edges.pop(0)

        if (nodes.union(min_weight_edge[0].id, min_weight_edge[1].id) == True):
            MST_edges.append((min_weight_edge[0].id, min_weight_edge[1].id, min_weight_edge[2]))
        
    return MST_edges

if __name__ == '__main__':
    wgraph2 = WeightedGraph(6, True)
    wgraph2.addEdge(wgraph2.getNode(0), Node(1, "node_1"), 10)
    wgraph2.addEdge(wgraph2.getNode(0), Node(5, "node_5"), 8)
    wgraph2.addEdge(wgraph2.getNode(1), Node(3, "node_3"), 2)
    wgraph2.addEdge(wgraph2.getNode(2), Node(1, "node_1"), 1)
    wgraph2.addEdge(wgraph2.getNode(3), Node(2, "node_2"), -2)
    wgraph2.addEdge(wgraph2.getNode(4), Node(3, "node_3"), -1)
    wgraph2.addEdge(wgraph2.getNode(4), Node(1, "node_1"), -4)
    wgraph2.addEdge(wgraph2.getNode(5), Node(4, "node_4"), 1)
    


    print(wgraph2)
    wgraph2_mst = kruskal(wgraph2)
    print(wgraph2_mst)

    tot = 0
    for x in wgraph2_mst:
        tot += x[2]

    print('total cost:', tot)