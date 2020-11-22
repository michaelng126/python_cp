# Graph (undirected), adjacency list form
# Connected Components via dfs
# Example BFS
# Example DFS

class G:
    # vertices zero indexed
    # connected components via dfs

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degree(self, v):
        return len(self.adj(v))

    def conn_comp(self):
        # find connected components via dfs
        vtd = [False for i in range(self.V)]
        cc = []
        for v in range(self.V):
            if vtd[v] == False:
                temp = []
                cc.append(self.conn_comp_dfs_help(v, vtd, temp))
        return cc

    def conn_comp_dfs_help(self, v, vtd, temp):
        vtd[v] = True
        temp.append(v)  # visit v
        for i in self.adj[v]:
            if vtd[i] == False:
                temp = self.conn_comp_dfs_help(i, vtd, temp)  # add each
        return temp


# Example Connected Components
N = 7
g = G(N)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(4, 5)
g.add_edge(0, 4)
g.add_edge(4, 6)

print('Connected components:')
print(g.conn_comp())


# Example BFS - find all distances from 0
N = 7
g = G(N)
g.add_edge(0, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(6, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)

from collections import deque

visited = set()

start = 0
# visit 0
visited.add(start)
queue = deque([start])

distances = [0 for i in range(N)]

while queue:
    s = queue.popleft()
    for v in g.adj[s]:
        if v not in visited:
            queue.append(v)
            # visit v
            visited.add(v)
            distances[v] = distances[s]+1

print('Distances in example BFS:')
print(distances)


# Example DFS - find a vertex connected to 0 with index 1 mod 4
N = 7
g = G(N)
g.add_edge(0, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(6, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 3)

visited = set()


def dfs(s):
    if s in visited:
        return
    visited.add(s)
    # visit v
    if s % 4 == 1:
        print(f'Vertex {s} found.')
    for v in g.adj[s]:
        dfs(v)


print('Example DFS:')
dfs(0)
