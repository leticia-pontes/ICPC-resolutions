import heapq

def dijkstra(grafo, inicio, aresta_excluida):
    """
    Encontra o caminho mais curto a partir do nó `inicio` no grafo, 
    ignorando a aresta `aresta_excluida`.
    
    :param grafo: Lista de adjacência representando o grafo.
    :param inicio: Nó de onde começar a busca.
    :param aresta_excluida: Aresta que deve ser ignorada na busca.
    :return: Lista com as distâncias mínimas a partir do nó `inicio`.
    """
    # Inicializa a distância para todos os nós como infinita
    distancias = [float('inf')] * len(grafo)
    distancias[inicio] = 0  # A distância do nó inicial para ele mesmo é 0
    fila_prioridade = [(0, inicio)]  # Fila de prioridade para Dijkstra (distância, nó)

    while fila_prioridade:
        # Extrai o nó com a menor distância conhecida
        distancia_atual, u = heapq.heappop(fila_prioridade)

        # Se a distância atual for maior que a registrada, ignora
        if distancia_atual > distancias[u]:
            continue

        # Explora todos os vizinhos do nó `u`
        for v, comprimento in grafo[u]:
            # Ignora a aresta que foi excluída
            if (u, v) == aresta_excluida or (v, u) == aresta_excluida:
                continue
            
            # Calcula a nova distância para o nó `v`
            nova_distancia = distancia_atual + comprimento
            # Se a nova distância for menor, atualiza e adiciona à fila
            if nova_distancia < distancias[v]:
                distancias[v] = nova_distancia
                heapq.heappush(fila_prioridade, (nova_distancia, v))
    
    return distancias

def main():
    # Leitura dos dados de entrada
    N, M = map(int, input().split())
    grafo = [[] for _ in range(N + 1)]  # Lista de adjacência do grafo
    arestas = []  # Lista para armazenar as arestas do grafo

    # Leitura das arestas do grafo
    for _ in range(M):
        U, V, L = map(int, input().split())
        grafo[U].append((V, L))  # Adiciona aresta de U para V
        grafo[V].append((U, L))  # Adiciona aresta de V para U (grafo não dirigido)
        arestas.append((U, V, L))  # Armazena a aresta para processamento futuro
    
    resultados = []
    # Processa cada aresta para encontrar o desvio mais curto
    for U, V, L in arestas:
        # Executa o algoritmo de Dijkstra a partir do nó U
        distancias_a_partir_de_U = dijkstra(grafo, U, (U, V))
        menor_distancia = distancias_a_partir_de_U[V]

        # Verifica se existe um caminho alternativo
        if menor_distancia == float('inf'):
            resultados.append(-1)  # Não é possível encontrar um caminho alternativo
        else:
            resultados.append(menor_distancia)
    
    # Imprime os resultados para cada aresta
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
