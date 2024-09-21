
def Busq_Ancho(graph, start, goal):
    visited = set()  # Para poner los nodos visitados
    stack = [(start, [start])]  # Cantidad de nodos a explorar, con el nodo inicial y su camino hasta ese punto

    while stack:  # Mientras existan nodos por visitar
        node, path = stack.pop()  # Tomar el último nodo de la fila
        if node not in visited:  # Si el nodo no ha sido visitado
            visited.add(node)  # Marcar el nodo como visitado
            if node == goal:  # Si el nodo es el objetivo
                return path  # Devolver el camino hasta ese nodo
            # Extender la fila con los nodos vecinos y sus caminos
            stack.extend((neighbor, path + [neighbor]) for neighbor in graph[node])

    return None  # Si no se encuentra un camino hasta el objetivo, devolver None

# Ejemplo de uso
graph = {
    'Casa': ['Trabajo', 'Plaza Patria'],
    'Trabajo': ['Casa', 'Colomos', 'Escuela'],
    'Plaza Patria': ['Casa', 'Oxxo'],
    'Colomos': ['Trabajo'],
    'Escuela': ['Trabajo', 'Oxxo'],
    'Oxxo': ['Plaza Patria', 'Escuela']
}

start = 'Casa'
goal = 'Escuela'
camino = Busq_Ancho(graph, start, goal)

print("Camino recorido de casa a escuela : ", camino)
