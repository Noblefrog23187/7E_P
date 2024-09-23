# Nombre del archivo que contendr� las preguntas y respuestas
archivo_db = 'preguntas_respuestas.txt'

# Funci�n para cargar las preguntas y respuestas del archivo
def cargar_respuestas():
    respuestas = {}
    try:
        with open(archivo_db, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Dividir la l�nea en pregunta y respuesta
                pregunta, respuesta = linea.strip().split('|')
                respuestas[pregunta] = respuesta
    except FileNotFoundError:
        # Si el archivo no existe, simplemente devolver un diccionario vac�o
        pass
    return respuestas

# Funci�n para guardar una nueva pregunta y respuesta en el archivo
def guardar_respuesta(pregunta, respuesta):
    with open(archivo_db, 'a', encoding='utf-8') as archivo:
        archivo.write(f"{pregunta}|{respuesta}\n")

# Funci�n para agregar respuestas predeterminadas al archivo si no existen
def agregar_respuestas_predeterminadas(respuestas):
    respuestas_predeterminadas = {
        'Como te llamas?': 'Me llamo Chatbot.',
        'Como estas?': 'Bien, gracias. Y tu?',
        'Bien tambien': 'Me alegra. Hay algo mas de lo que quieras saber?',
    }

    # A�adir solo las que no existan ya en el diccionario cargado
    nuevas_respuestas = 0
    for pregunta, respuesta in respuestas_predeterminadas.items():
        if pregunta not in respuestas:
            guardar_respuesta(pregunta, respuesta)
            nuevas_respuestas += 1

# Funci�n para buscar una respuesta en el diccionario
def buscar_respuesta(respuestas, pregunta):
    return respuestas.get(pregunta, None)

# Funci�n principal
def chatbot():
    print("Bienvenido! Hazme una pregunta o escribe 'salir' para terminar.")
    
    # Cargar las respuestas desde el archivo
    respuestas = cargar_respuestas()

    # Agregar respuestas predeterminadas si es necesario
    agregar_respuestas_predeterminadas(respuestas)
    
    while True:
        pregunta = input("\nTu pregunta: ").strip()
        
        if pregunta.lower() == 'salir':
            break
        
        # Buscar respuesta en el diccionario cargado
        respuesta = buscar_respuesta(respuestas, pregunta)
        
        if respuesta:
            print(f"Respuesta: {respuesta}")
        else:
            print("No tengo una respuesta para esa pregunta.")
            nueva_respuesta = input("Te gustaria agregar una respuesta para esta pregunta? (si/no): ").strip().lower()
            if nueva_respuesta == 'si':
                respuesta_usuario = input("Escribe la respuesta: ").strip()
                guardar_respuesta(pregunta, respuesta_usuario)
                respuestas[pregunta] = respuesta_usuario  # A�adir la respuesta al diccionario en memoria
                print("Respuesta agregada exitosamente.")
            else:
                print("Pregunta no agregada.")
    
    print("Adios!")

# Ejecutar el chatbot
if __name__ == '__main__':
    chatbot()

