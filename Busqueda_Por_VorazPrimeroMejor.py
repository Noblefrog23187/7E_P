import random  # Importa el módulo random para generar números aleatorios

def busqueda_voraz(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    cola = [(inicio, [inicio], 0)]  # Lista de prioridad para almacenar los nodos, el camino seguido hasta el momento y sus costos

    while cola:
        nodo_actual, camino_actual, costo_actual = cola.pop(0)  # Tomamos el primer elemento de la lista
        if nodo_actual == objetivo:
            print("Objetivo a alcanzar:", nodo_actual)
            print("Mejor camino:", " -> ".join(camino_actual))
            return True
        if nodo_actual not in visitados:
            print("Reconociendo terreno:", nodo_actual)
            visitados.add(nodo_actual)
            # Agregamos los nodos vecinos, el camino y sus costos a la cola
            vecinos = grafo[nodo_actual]
            vecinos.sort(key=lambda x: x[1])  # Ordenamos los vecinos por sus costos
            for vecino, costo in vecinos:
                if vecino not in visitados:
                    cola.append((vecino, camino_actual + [vecino], costo))
    print("No se encontro el objetivo.")
    return False

# Grafo con nombres de lugares en la ciudad
grafo = {
    'Casa': [('La Perla', 7), ('Plaza del Sol', 5), ('Terraza Oblatos', 3)],
    'La Perla': [('Terraza Belenes', 4), ('CUCEA', 6), ('CUCS', 3)],
    'Plaza del Sol': [('CUCS', 3)],
    'Terraza Oblatos': [('Transito', 2), ('Centro Historico', 5)],
    'Terraza Belenes': [('Plaza Galerias', 9)],
    'CUCEA': [('Real Center', 3), ('Casa de Marifer <3', 4)],
    'CUCS': [('Andares', 7)],
    'Transito': [('CETI', 1)],
    'Centro Historico': [('CETI', 8)],
    'Plaza Galerias': [],
    'Real Center': [],
    'Casa de Marifer <3': [],
    'Andares': [],
    'CETI': []
}

# Llamamos a la función de búsqueda con el nodo de inicio 'Casa' y el nodo objetivo 'CETI'
busqueda_voraz(grafo, 'Casa', 'CETI')
