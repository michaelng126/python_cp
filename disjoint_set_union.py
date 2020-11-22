class DSU():
    # Disjoint Set Union/Union Find
    # n vertices, zero indexed
    # cc = connected components

    def __init__(self, n):
        self.n = n
        self.link = list(range(n))
        self.size = [1]*n

    def find(self, x):
        while (x != self.link[x]):
            x = self.link[x]
        return x

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a

    def size(self, x):
        return self.size[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.link) if i == x]

    def cc_count(self):
        return len(self.roots())

    def ccs(self):
        return [self.members(r) for r in self.roots()]


# Example code
d = DSU(5)
d.unite(1, 2)
d.unite(0, 3)
d.unite(0, 4)
print(d.ccs())
print(d.cc_count())
print(d.roots())
