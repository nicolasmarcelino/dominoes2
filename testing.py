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

reachable = DirectedDFS(g, [1])

for v in range(g.V):
    if reachable.marked(v):
        ## adicionar +1 pra considerar de 1 a n
        print(v, "is reachable from source(s)")

derrubados = 0
for v in range(g.V):
    if reachable.marked(v):
        derrubados += 1
print("derrubados:", derrubados)

'''
print(derrubados)
1 -> [2]
2 -> [3, 4]
3 -> [5]
4 -> [1]
5 -> [7]
6 -> [7]
7 -> []

1
7 7 1
1 2
2 4
2 3
3 5
4 1
5 7
6 7
'''