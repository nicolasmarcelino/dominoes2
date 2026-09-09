from digraph import Digraph
from directed_dfs import DirectedDFS

g = Digraph(7)
g.add_edge(0, 1)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 6)
g.add_edge(5, 6)
print(g.adj)
reachable = DirectedDFS(g, [2, 3])
print(reachable._marked)
print(reachable.count)
