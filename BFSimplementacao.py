import matplotlib.pyplot as plt
import networkx as nx

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, valor):
        novo_no = No(valor)
        if self.fim is None:
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            raise Exception("A fila está vazia!")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return valor

def bfs_caminho_curto(grafo, inicio, alvo):
    visitados = set()
    predecessores = {inicio: None}
    fila = Fila()
    fila.enfileirar(inicio)
    visitados.add(inicio)

    fila_desejados = []  # Fila dos nós desejados
    predecessores_lista = []  # Lista de predecessores

    while not fila.esta_vazia():
        no_atual = fila.desenfileirar()

        fila_desejados.append(no_atual)  # Adiciona o nó atual na fila dos desejados

        if no_atual == alvo:
            break

        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.enfileirar(vizinho)
                predecessores[vizinho] = no_atual

    # Reconstruir o caminho mais curto
    caminho = []
    atual = alvo
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]

    caminho.reverse()  # Inverter para começar no nó de início

    # Preencher a lista de predecessores para cada nó visitado
    for visita in caminho:
        predecessores_lista.append(predecessores[visita])

    return caminho, fila_desejados, predecessores_lista

def desenhar_grafo(grafo, caminho):
    G = nx.Graph()
    for vertice, vizinhos in grafo.items():
        for vizinho in vizinhos:
            G.add_edge(vertice, vizinho)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))

    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="black", font_weight="bold")

    # Destacar o caminho mais curto em amarelo
    caminho_arestas = [(caminho[i], caminho[i+1]) for i in range(len(caminho) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=caminho_arestas, width=3, edge_color="yellow")
    nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color="yellow", node_size=700)

    plt.title("Caminho Mais Curto no Grafo (BFS)", fontsize=16)
    plt.show()

# Grafo com 7 vértices, exemplo similar ao seu
grafo = {
    '0': ['1', '2', '3'],
    '1': ['0', '4', '5','3'],
    '2': ['0', '6', '9'],
    '3': ['0', '7','4'],
    '4': ['1', '8','2'],
    '5': ['1', '9'],
    '6': ['2', '10'],
    '7': ['3', '11'],
    '8': ['4'],
    '9': ['5','1'],
    '10': ['6'],
    '11': ['7'],
    '12': ['3','4','5']
}

# Configuração de busca
inicio = '0'
alvo = input("Digite o nó que deseja encontrar: ").strip().upper()

# Executar BFS e obter o caminho mais curto, fila e predecessores
caminho, fila_desejados, predecessores_lista = bfs_caminho_curto(grafo, inicio, alvo)

# Exibir a fila dos desejados e predecessores
print(f"Fila dos desejados: {', '.join(fila_desejados)}")
print(f"Predecessores: {', '.join([str(p) if p is not None else 'None' for p in predecessores_lista])}")

# Exibir o caminho mais curto
print(f"Caminho mais curto: {' -> '.join(caminho)}")

# Exibir o grafo com o caminho em amarelo
desenhar_grafo(grafo, caminho)
