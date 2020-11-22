class WG:
    # weighted graph, adj list for dijkstra below
    def __init__(self,V):
        self.V=V
        self.adj=[[] for i in range(V)]

    def add_edge(self,v,w,weight):
        self.adj[v].append((w,weight))
        self.adj[w].append((v,weight))
    
    


import heapq
def dijk(g, start_v=0):
    INF = 10e18
    d = [INF] * g.V
    seen = [False] * g.V
    prev = [-1] * g.V
    d[start_v] = 0
    q = [(0,start_v)]

    while(len(q)>0):
        a = heapq.heappop(q)[1]
        seen[a] = True
        for u in g.adj[a]:
            b = u[0]
            if seen[b]: continue
            w = u[1]
            if d[b] > d[a]+w:
                d[b] = d[a]+w
                prev[b] = a
                heapq.heappush(q,(d[b],b))

    return d, prev


g = WG(4)
g.add_edge(1,2,10)
g.add_edge(0,2,5)
g.add_edge(2,3,3)
print(dijk(g))


 