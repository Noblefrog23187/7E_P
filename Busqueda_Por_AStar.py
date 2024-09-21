def ao_estrella(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    frontera = [(inicio, [inicio], 0)]  # Lista de prioridad para almacenar los nodos, el camino seguido hasta el momento y sus costos

    while frontera:
        # Seleccionamos el nodo de la frontera con el menor costo estimado
        nodo_actual, camino_actual, costo_actual = min(frontera, key=lambda x: x[2])
        frontera.remove((nodo_actual, camino_actual, costo_actual))
        
        if nodo_actual == objetivo:
            print("Objetivo alcanzado:", nodo_actual)
            print("Camino seguido:", " -> ".join(camino_actual))
            return True
        
        visitados.add(nodo_actual)
        # Expandimos el nodo actual y añadimos los nodos vecinos a la frontera
        for vecino, costo in grafo[nodo_actual]:
            if vecino not in visitados:
                nuevo_camino = camino_actual + [vecino]
                nuevo_costo = costo_actual + costo
                frontera.append((vecino, nuevo_camino, nuevo_costo))
    
    print("No se encontro el objetivo.")
    return False

# Grafo con los nombres de los lugares
grafo = {
    'Casa': [('La perla', 7), ('Plaza del sol', 5), ('Terraza Oblatos', 8)],
    'La perla': [('Terraza Belenes', 4), ('CUCEA', 6), ('CUCS', 3)],
    'Plaza del sol': [('CUCS', 3)],
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

# Llamada a la función de búsqueda con 'Casa' como inicio y 'CETI' como objetivo
ao_estrella(grafo, 'Casa', 'CETI')
