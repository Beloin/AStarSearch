# Atividade de Busca

1. Comparativo Dijkstra x A*. Pegue um problema aleatório composto de algumas cidades e calcule o melhor caminhos usando
   os dois algoritmos e mostre os tempos e as implementações.
1. Implemente a solução para o problema dos canibais e missionários.
1. Implemente uma solução para o problema do mosaico.

Para os algoritmos funcionarem, irei utilizar:

Para algoritmos Offline

- Lista de estados
- Mapa de Custos (Previamente conhecidos)

Para algoritmos online:

- Lista de estados
- Lista de custos (Adicionada em runtime)

# A* algorith

Important:

- In robotics, A* helps robots navigate obstacles and find optimal paths.
- Use heaps to store the paths.
- Uses Heuristic to find the shortest path

```
S = start  
E = end  
Sq1 = any point in the path  
Sq2 = any point in the path after Sq2  

f(n) = g(n) + h(n)  

h(n) -> Heuristic (estimated) cost of Sq2 to E  
g(n) -> Real cost of S to Sq2

```

A Priority Queue (Implemented with a Heap or AVL) can be used to fetch the nodes, in order to ease the looks for the
less costy operation.

The heuristic used depends on the problem:

- Map: Can be used Euclidian Distance
- Video-Games: Taxicab Distance

## Pseudocode

1. Add start node to PQ
2. While PQ is not empty:
    - pop the lowest value of the PQ as crr
    - if crr is meta, return the path to crr, else, continue
    - for each descendant of crr as d:
        - Calculate g(d) as c ( g(d) = g(crr) + cost(crr, d) )
        - If c is lower then the previously calculated g(d):
            - update the g(d) for d
            - update the f(d) for d
            - set the path of d to came from crr
            - Add d to PQ with f(d) value
3. return error

