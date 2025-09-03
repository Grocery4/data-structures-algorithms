import copy

from data_structures.graph import Graph


def topologicalSort(graph):
    c_graph = copy.deepcopy(graph)
    
    linear_dag = []

    while len(c_graph.nodes) != 0:
        for node in c_graph.nodes:
            if len(c_graph.getInEdges(node)) == 0:
                linear_dag.append(node)
                c_graph.removeNode(node.id)

    return linear_dag


def dfs_ts(graph, node, stack, visited_nodes):
    visited_nodes[node] = True
    for adj in graph.adjacency_list[node]:
        if visited_nodes[adj] == False:
            dfs_ts(graph, adj, stack, visited_nodes)
    stack.append(node)

def recursiveTopologicalSort(graph):
    print(graph.nodes)
    visited_nodes = {node:False for node in graph.nodes}
    stack = []

    for node in graph.nodes:
        if visited_nodes[node] == False:
            dfs_ts(graph, node, stack, visited_nodes)

    stack.reverse()
    return stack


if __name__ == '__main__':
    g5 = Graph(5, directed=True)
    g5.addEdge(g5.getNode(0), g5.getNode(1))
    g5.addEdge(g5.getNode(2), g5.getNode(1))
    g5.addEdge(g5.getNode(2), g5.getNode(4))
    g5.addEdge(g5.getNode(2), g5.getNode(3))
    g5.addEdge(g5.getNode(3), g5.getNode(1))
    g5.addEdge(g5.getNode(4), g5.getNode(1))

    print(g5)


    g5.nodes = g5.nodes[3:] + g5.nodes[:3]
    linear_dag = recursiveTopologicalSort(g5)
    print(linear_dag)