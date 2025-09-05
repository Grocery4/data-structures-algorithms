class DisjointSet:
    def __init__(self, n):
        # Initially, each node is its own parent (self root)
        self.parent = [i for i in range(n)]
        self.rank = [0] * n  # can also use size
    
    def find(self, x):
        """Find the root of x with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # compress path
        return self.parent[x]

    def union(self, x, y):
        """Union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            print("same group union attempted.")
            return  # already in the same set
        
        # attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True