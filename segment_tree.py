class SegTree():
    # Segment Tree with n nodes
    # Custom operator, taking iterable, not necessarily commutative

    def __init__(self, a, op=sum):  # op takes iterable
        self.n = len(a)
        self.tree = [0]*self.n + a
        self.op = op
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.op([self.tree[i << 1], self.tree[i << 1 | 1]])

    def update(self, i, val):
        j = self.n+i
        self.tree[j] = val
        while j > 1:
            j >>= 1
            self.tree[j] = self.op([self.tree[j << 1], self.tree[j << 1 | 1]])

    def op_range(self, l, r):  # op on interval [l,r)
        l = self.n + l
        r = self.n + r
        if self.op is min:
            resl, resr = 10**18, 10**18
        elif self.op is max:
            resl, resr = -10**18, -10**18
        else:
            resl, resr = 0, 0
        while l < r:
            if l & 1:
                resl = self.op([resl, self.tree[l]])
                l += 1
            l >>= 1
            if r & 1:
                r -= 1
                resr = self.op([self.tree[r], resr])
            r >>= 1
        return self.op([resl, resr])


# Example for sum, max and min
print('Sum:')
s = SegTree([1, 5, 7, 8, 2, 9])
print(s.tree)
print(s.op_range(1, 6))
print(s.op_range(2, 5))
s.update(1, 101)
print(s.tree)
print(s.op_range(1, 6))
print(s.op_range(2, 5))

print('Max:')
t = SegTree([1, 5, 7, 8, 2, 9], op=max)
print(t.tree)
print(t.op_range(1, 6))
print(t.op_range(2, 5))
t.update(1, 101)
print(t.tree)
print(t.op_range(1, 6))
print(t.op_range(2, 5))

print('Min:')
u = SegTree([1, 5, 7, 8, 2, 9], op=min)
print(u.tree)
print(u.op_range(1, 6))
print(u.op_range(2, 5))
u.update(1, -2)
print(u.tree)
print(u.op_range(1, 6))
print(u.op_range(2, 5))
