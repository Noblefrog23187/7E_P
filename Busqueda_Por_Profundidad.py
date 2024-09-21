def Busq_Prof(graph, start, goal):
    visited = set()  # Conjunto para mantener los nodos visitados
    stack = [(start, [start])]  # fila de nodos a explorar, con el nodo inicial y su camino hasta ese punto

    while stack:  # Mientras la fila no esté vacía
        node, path = stack.pop()  # Tomar el último nodo de la fila
        if node not in visited:  # Si el nodo no ha sido visitado
            visited.add(node)  # Marcar el nodo como visitado
            if node == goal:  # Si el nodo es el objetivo
                return path  # Devolver el camino hasta ese nodo
            # Extender la fila con los nodos vecinos y sus caminos
            stack.extend((neighbor, path + [neighbor]) for neighbor in graph[node])

    return None  # Si no se encuentra un camino hasta el objetivo, devolver None

# Ejemplo de uso
grafo = {
    'Escuela': ['Edificio_B', 'Cafeteria_B'],
    'Edificio_B': ['Escuela', 'Edificio_G', 'Edificio_L'],
    'Cafeteria_B': ['Escuela', 'Edificio_L'],
    'Edificio_G': ['Edificio_B'],
    'Edificio_L': ['Edificio_B', 'Cafeteria_B']
}

start = 'Escuela'
goal = 'Edificio_L'

camino = Busq_Prof(grafo, start, goal)

print("Rutina a la llegada a la escuela ", camino)
