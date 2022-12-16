from collections import defaultdict,OrderedDict
from itertools import combinations
from collections.abc import MutableMapping

with open("16.txt","r") as f:
    lines=map(lambda x: x[:-1],f.readlines())


class Cache(MutableMapping):
    def __init__(self, maxlen):
        self._maxlen = maxlen
        self.d = OrderedDict()

    @property
    def maxlen(self): return self._maxlen

    def __getitem__(self, key):
        self.d.move_to_end(key)
        return self.d[key]

    def __setitem__(self, key, value):
        if key in self.d: self.d.move_to_end(key)
        elif len(self.d) == self.maxlen: self.d.popitem(last=False)
        self.d[key] = value

    def __delitem__(self, key): del self.d[key]

    def __iter__(self): return self.d.__iter__()

    def __len__(self): return len(self.d)



def prepos(s):
    n,r=s.replace('Valve ','').replace(' has flow rate','').replace(' tunnels lead to valves','').replace(' tunnel leads to valve','').split('=')
    r,l=r.split(';')
    l=l.replace(' ','').split(',')
    return n,int(r),l

arr = defaultdict(list)
adjdir = []
for line in lines:
    A,custo,adj = prepos(line)
    arr[A] = custo,adj
    if custo!=0: adjdir.append(A)
        
adjdir = set(adjdir)
cache = Cache(1000000)

def solve(t, nodo, aVisitar):
    if t == 0 or len(aVisitar) == 0: return 0
    key = (t, nodo, frozenset(aVisitar))
    if key in cache: return cache[key]
    custo, ladj = arr[nodo]
    M = 0
    if nodo in aVisitar and custo != 0:
        M = solve(t - 1, nodo, aVisitar - {nodo}) + custo * (t - 1)
    for adj in ladj:
        M =  max(M,solve(t - 1, adj, aVisitar))
    cache[key] = M
    return M

M = -1e9
for i in range(1,len(adjdir)):
    ma=M
    for a in combinations(list(adjdir), i):
        a = set(a)
        b = set(adjdir - set(a))
        M = max(M, solve(26, "AA", a) + solve(26, "AA", b))
    if M<ma:
        print(M)
        break
    