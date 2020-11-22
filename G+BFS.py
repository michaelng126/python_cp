class G:
    # Graph adj list + connected components
    def __init__(self,V):
        self.V=V
        self.adj=[[] for i in range(V)]

    def dfs_help(self,temp,v,vtd):
        vtd[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if vtd[i] == False:
                temp =self.dfs_help(temp,i,vtd)
        return temp
    
    def add_edge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def deg(self,v):
        return len(self.adj(v))
    
    def conn_comp(self):
        vtd=[False for i in range(self.V)]
        cc=[]
        for v in range(self.V):
            if vtd[v] == False:
                temp = []
                cc.append(self.dfs_help(temp,v,vtd))
        return cc


g = G(100)
g.add_edge(1,2)

# BFS from 0
from collections import deque

visited = [0 for i in range(N)]
visited[0] = 1
queue = deque([0])

while queue:
    s = queue.popleft()

    for v,w in g.adj[s]:
        if visited[v] == 0:
            visited[v] = 1
            # do things e.g. with the vertices, or with edge just traversed
            queue.append(v)