import random

class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __str__(self):
        # return f"{self.id}:{self.value}"
        return f"{self.id}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Graph:
    def __init__(self, node_count, directed=False):
        self.node_count = node_count
        self.directed = directed
        # Use Node objects as keys
        self.nodes = [Node(i, f"node_{i}") for i in range(node_count)]
        self.adjacency_list = {node: [] for node in self.nodes}

    def getNode(self, id):
        for node in self.nodes:
            if node.id == id:
                return node
        return None

    def checkDuplicates(self, u, v):
        if self.directed:
            return v in self.adjacency_list[u]
        else:
            return v in self.adjacency_list[u] or u in self.adjacency_list[v]
    
    
    def addNode(self, id, value=None):
        if self.getNode(id) is not None:
            print('NODE ALREADY EXISTS.')
            return False
        
        node = Node(id, value if value is not None else str(id))
        self.adjacency_list[node] = []
        self.nodes.append(node)
        self.node_count += 1
        return True

    def removeNode(self, id):
        node = self.getNode(id)
        if node is None:
            print('NODE DOES NOT EXIST.')
            return False
        
        # remove all edges with node
        for k in list(self.adjacency_list.keys()):
            if node in self.adjacency_list[k]:
                self.removeEdge(k, node)

        # remove node
        self.adjacency_list.pop(node)
        self.nodes.remove(node)
        self.node_count -= 1
        return True

    def addEdge(self, u, v):
        if not self.checkDuplicates(u, v):
            self.adjacency_list[u].append(v)
            # If not directed it's gon be symmetrrical
            if not self.directed:
                self.adjacency_list[v].append(u)
            return True
        
        print('EDGE ALREADY EXISTS.')
        return False

    def removeEdge(self, u, v):
        if self.existsEdge(u, v):
            if not self.directed:
                self.adjacency_list[u].remove(v)
                self.adjacency_list[v].remove(u)
            else:
                self.adjacency_list[u].remove(v)
            
            return True
        print('EDGE DOES NOT EXIST')
        return False

    def existsEdge(self, u, v):
        return v in self.adjacency_list[u]

    def adjacent(self, node):
        return self.adjacency_list[node]

    def vertexes(self):
        return [node for node in self.adjacency_list.keys()]

    def edges(self):
        res = set()
        for key in self.adjacency_list.keys():
            for adj in self.adjacency_list[key]:
                if not self.directed:
                    if (adj, key) not in res:
                        res.add((key, adj))
                else:
                    res.add((key, adj))
        return res

    
    # dfs requires a is_visited boolean and a stack of nodes
    # stack can be either implicit(recursive + call stack)
    # or explicit(real stack)
    # - add elements to be visited in stack
    # - pop said element and add children to stack
    # - rinse and repeat.
    # assumes no multiple connected
    
    def dfs(self, id, visited):
        if visited[self.getNode(id)] == False:
            visited[self.getNode(id)] = True
            print(self.getNode(id))

            for adj in self.adjacency_list[self.getNode(id)]:
                self.dfs(adj.id, visited)

    def dfsFindCycle(self, id, parent,visited):
        
        if visited[self.getNode(id)] == False:
            visited[self.getNode(id)] = True
            print(self.getNode(id))

            if len(self.adjacency_list[self.getNode(id)]) == 1 and self.adjacency_list[self.getNode(id)][0].id == parent:
                return False
            
            for adj in self.adjacency_list[self.getNode(id)]:
                if adj.id != parent:
                    return self.dfsFindCycle(adj.id, id, visited)
        
        return True

    def dfsSpanningForest(self, id, visited, previous):
        if visited[self.getNode(id)] == False:
            visited[self.getNode(id)] = True
            print(self.getNode(id))
            for adj in self.adjacency_list[self.getNode(id)]:
                if visited[self.getNode(adj.id)] == False:
                    previous[self.getNode(adj.id)] = id
                    self.dfsSpanningForest(adj.id, visited, previous)

    def asciiGraph(self):
        print("Graph Representation (nodes and edges):")
        for u in self.adjacency_list:
            connections = " -- ".join(str(v) for v in self.adjacency_list[u])
            print(f"({u}) -- {connections}" if connections else f"({u})")

    def __str__(self):
        res = ''
        for node in self.adjacency_list.keys():
            res += '[' + str(node) + ']: '
            for adj in self.adjacency_list[node]:
                res += str(adj) + '\t'
            res += '\n'
        return res

if __name__ == '__main__':
    # g = Graph(10, directed=False)
    # edge_count = 15  # You can adjust the number of edges

    # Generate random edges
    # while len(g.edges()) < edge_count:
    #     u = random.choice(g.nodes)
    #     v = random.choice(g.nodes)
    #     if u != v:
    #         g.addEdge(u, v)

    # print(g)
    # visited_nodes = {node:False for node in g.nodes}
    # g.dfs(2, visited_nodes)

    # Generate a graph with multiple connected components
    g2 = Graph(10, directed=False)
    # First component (nodes 0-4)
    g2.addEdge(g2.getNode(0), g2.getNode(1))
    g2.addEdge(g2.getNode(1), g2.getNode(2))
    g2.addEdge(g2.getNode(2), g2.getNode(3))
    g2.addEdge(g2.getNode(3), g2.getNode(4))
    # Second component (nodes 5-9)
    # g2.addEdge(g2.getNode(5), g2.getNode(6))
    # g2.addEdge(g2.getNode(6), g2.getNode(7))
    # g2.addEdge(g2.getNode(7), g2.getNode(8))
    # g2.addEdge(g2.getNode(8), g2.getNode(9))
    # previous = {node:-1 for node in g2.nodes}

    visited_nodes = {node:False for node in g2.nodes}
    print(g2)
    print(g2.dfsFindCycle(0, -1, visited_nodes))
    # for v in g2.vertexes():
    #     if visited_nodes[g2.getNode(v.id)] == False:
    #         g2.dfsSpanningForest(v.id, visited_nodes, previous)

    # print(previous)

    # print("\nGraph with multiple connected components:")
    # print(g2)

    g3 = Graph(9, directed=False)
    # g3.addEdge(g3.getNode(0), g3.getNode(1))
    # g3.addEdge(g3.getNode(0), g3.getNode(2))
    # g3.addEdge(g3.getNode(2), g3.getNode(3))
    # g3.addEdge(g3.getNode(2), g3.getNode(4))
    g3.addEdge(g3.getNode(1), g3.getNode(5))
    g3.addEdge(g3.getNode(5), g3.getNode(6))
    g3.addEdge(g3.getNode(5), g3.getNode(7))
    g3.addEdge(g3.getNode(6), g3.getNode(8))
    g3.addEdge(g3.getNode(8), g3.getNode(7))
    
    print(g3)

    visited_nodes = {node:False for node in g3.nodes}
    previous = {node:-1 for node in g3.nodes}


    # for v in g3.vertexes():
    #     if visited_nodes[g3.getNode(v.id)] == False:
    #         g3.dfsSpanningForest(v.id, visited_nodes, previous)

    print(g3.dfsFindCycle(1, -1,visited_nodes))

    # g4: cyclic graph
    g4 = Graph(5, directed=False)
    g4.addEdge(g4.getNode(0), g4.getNode(1))
    g4.addEdge(g4.getNode(1), g4.getNode(2))
    g4.addEdge(g4.getNode(2), g4.getNode(3))
    g4.addEdge(g4.getNode(3), g4.getNode(0))  # This edge creates a cycle
    print("\ng4 (cyclic):")
    print(g4)
    visited_nodes_g4 = {node: False for node in g4.nodes}
    print("Cycle detected in g4:", g4.dfsFindCycle(0, -1, visited_nodes_g4))

    # g5: acyclic graph (tree)
    g5 = Graph(5, directed=False)
    g5.addEdge(g5.getNode(0), g5.getNode(1))
    g5.addEdge(g5.getNode(1), g5.getNode(2))
    g5.addEdge(g5.getNode(2), g5.getNode(3))
    g5.addEdge(g5.getNode(3), g5.getNode(4))
    print("\ng5 (acyclic):")
    print(g5)
    visited_nodes_g5 = {node: False for node in g5.nodes}
    print("Cycle detected in g5:", g5.dfsFindCycle(0, -1, visited_nodes_g5))