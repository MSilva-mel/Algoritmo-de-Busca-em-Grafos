class Grafo:
    def _init_(self, vertices):
        self.vertices = vertices
        self.grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def imprimirSolucao(self, distancias=None):
        if distancias is not None:
            print("Vértice \t Distância da Origem")
            for vertice in range(self.vertices):
                print(vertice + 1, "\t\t", distancias[vertice])
        else:
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if self.grafo[i][j] > 0:
                        print(f"Vértice {i + 1} -> Vértice {j + 1} com peso {self.grafo[i][j]}")

    def menorDistancia(self, distancias, conjuntoSPT):
        minimo = 100
        indiceMinimo = -1
        for v in range(self.vertices):
            if distancias[v] < minimo and not conjuntoSPT[v]:
                minimo = distancias[v]
                indiceMinimo = v
        return indiceMinimo

    def dijkstra(self, origem):
        distancias = [100] * self.vertices
        distancias[origem] = 0
        finalizados = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.menorDistancia(distancias, finalizados)
            finalizados[u] = True

            for v in range(self.vertices):
                if (self.grafo[u][v] > 0 and not finalizados[v]
                        and distancias[v] > distancias[u] + self.grafo[u][v]):
                    distancias[v] = distancias[u] + self.grafo[u][v]

        self.imprimirSolucao(distancias)


g = Grafo(12)
g.grafo = [
    [0, 3, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [3, 0, 2, 0, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 2, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 4, 0, 6, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 6, 0, 1, 0, 0, 0, 4, 0, 0],
    [5, 0, 0, 0, 1, 0, 3, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 0, 3, 0, 1, 0, 0, 0, 6],
    [0, 0, 8, 0, 0, 0, 1, 0, 5, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 5, 0, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 7, 0, 3, 1],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 4],
    [0, 0, 0, 0, 0, 0, 6, 0, 0, 1, 4, 0],
]

g.imprimirSolucao()

print("\nResultados de Dijkstra:")
g.dijkstra(0)