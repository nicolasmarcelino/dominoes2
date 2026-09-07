"""

https://open.kattis.com/problems/dominoes2

Sample input
1
3 2 1
1 2
2 3
2

Sample output
2

"""

from digraph import Digraph
from directed_dfs import DirectedDFS

testes = int(input())

while testes:

    derrubados = 0
    total_dominos, total_enfileirados, total_empurrados = input().split()
    total_dominos, total_enfileirados, total_empurrados = int(total_dominos), int(total_enfileirados), int(total_empurrados)

    g = Digraph(total_dominos) ## mapeando dominós em um grafo

    while total_enfileirados:

        x, y = input().split()
        x, y = int(x), int(y)

        g.add_edge(x - 1, y - 1)  ## mapeando sequência de enfileiramento

        total_enfileirados = total_enfileirados - 1
    
    while total_empurrados:
        derrubado_manualmente = int(input())

        reachable = DirectedDFS(g, [derrubado_manualmente - 1]) ## inicia DFS a partir
        
        for v in range(g.V):
            if reachable.marked(v):
                derrubados += 1

        total_empurrados = total_empurrados - 1
    
    print(derrubados)

    testes = testes - 1

