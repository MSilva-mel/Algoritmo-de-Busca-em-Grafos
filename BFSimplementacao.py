import matplotlib.pyplot as plt #biblioteca de ilustração do grafo
import networkx as nx #

class No:
    #Representa um nó de uma lista encadeada
    def __init__(self, valor):
        self.valor = valor #Valor q armazena um nó
        self.proximo = None # referêmcia para o pr[oximo nó

class Fila:
    #Fila implementada com lista encadeada
    def __init__(self):
        self.inicio = None  # primeiro da fila
        self.fim = None     # ultimo da fila

    def esta_vazia(self):
        #Verifica se a fila está vazia.
        return self.inicio is None

    def enfileirar(self, valor): #FIFO
        #Adiciona um elemento ao final da fila
        novo_no = No(valor)
        if self.fim is None:  # Fila está vazia
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no #ultimo aponta para o novo nó
            self.fim = novo_no  #atualiza o fim para o novo

    def desenfileirar(self):
        #Remove um elemento do início da fila
        if self.esta_vazia():
            raise Exception("A fila está vazia!")
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:  # A fila ficou vazia
            self.fim = None
        return valor

def bfs_encontrar(grafo, inicio, alvo):
    #BFS para encontrar um nó específico
    visitados = set()         # conjunto para rastrear os nós visitados
    fila = Fila()             # fila para gerenciar o caminhamento
    caminho = []              # lista para armazenar o caminho percorrido
    visitados.add(inicio)     # marca o nó inicial como visitado
    fila.enfileirar(inicio)   # adiciona o inicial na fila

    while not fila.esta_vazia():
        # Remove o primeiro nó da fila euquanto o grafo n estover vazio
        no_atual = fila.desenfileirar()
        caminho.append(no_atual)

        # Verifica se encontrou o alvo
        if no_atual == alvo:
            print(f"Nó '{alvo}' encontrado!")
            return caminho

        # Adiciona os vizinhos não visitados à fila
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.enfileirar(vizinho)

    print(f"Nó '{alvo}' não encontrado!")
    return caminho

def desenhar_grafo(grafo, caminho):
    #Desenha o grafo e destaca o caminho percorrido
    G = nx.Graph() #cria uma instância de grafo não direcionado
    for vertice, vizinhos in grafo.items():
        for vizinho in vizinhos:
            G.add_edge(vertice, vizinho) #adiciona arestas

    pos = nx.spring_layout(G)  # Layout do grafo
    plt.figure(figsize=(10, 8))

    # Desenhar todos os nós e arestas
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="black", font_weight="bold")

    # Destacar o caminho percorrido
    caminho_arestas = [(caminho[i], caminho[i+1]) for i in range(len(caminho) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=caminho_arestas, width=3, edge_color="red")
    nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color="red", node_size=700)

    plt.title("Caminhamento no Grafo (BFS)", fontsize=16)
    plt.show()

# Grafo com 15 vértices
grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G', 'H'],
    'D': ['A', 'I'],
    'E': ['B', 'J'],
    'F': ['B', 'K', 'L'],
    'G': ['C'],
    'H': ['C'],
    'I': ['D'],
    'J': ['E'],
    'K': ['F'],
    'L': ['F']
}

# Configuração de busca
inicio = 'A'
alvo = input("Digite o nó que deseja encontrar: ").strip().upper()
#strip elimina espaços na resposta e upper coloca a resposta para maiúsculo

# Executar BFS e desenhar o grafo
caminho_percorrido = bfs_encontrar(grafo, inicio, alvo)
print("Caminho percorrido:", " -> ".join(caminho_percorrido))
desenhar_grafo(grafo, caminho_percorrido)