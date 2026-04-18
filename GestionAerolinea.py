"""Sistema de Gestión de Aerolínea - Programación 1 - Grupo 4"""


#aviones
aviones_modelo     = ["A320", "A320", "A320", "A320", "A350", "Boeing 777"]
aviones_tipo       = ["continental", "continental", "continental", "continental", "intercontinental", "intercontinental"]
aviones_capacidad  = [180, 180, 180, 180, 300, 300]
aviones_disponible = [True, True, True, True, True, True]

#vuelos
vuelos_origen  = []
vuelos_destino = []
vuelos_tipo    = []
vuelos_avion   = []

#funcion para mostrar la lista de aviones disponibles
def mostrar_flota():
    print("Flota de aviones:")
    for i in range(len(aviones_modelo)):
        if aviones_disponible[i]:
            estado = "Disponible"
        else:
            estado = "Ocupado"
        print(f"[{i+1}] {aviones_modelo[i]} - {aviones_tipo[i]} - {aviones_capacidad[i]} asientos - {estado}")
        

#funcion paara asignar aviones por tipo de ruta 
def asignar_avion(tipo_ruta):
    for i in range(len(aviones_modelo)):
        if aviones_tipo[i] == tipo_ruta and aviones_disponible[i]:
            return i
    return -1



#funcion para crear los vuelos 

def crear_vuelo():
    print("Crear vuelo")
    origen = input("Origen: ")
    destino = input("Destino: ")

    print("1- Continental")
    print("2- Intercontinental")
    opcion = input("Opcion: ")
    
    print("Elegir tipo de vuelo")
    
    if opcion == "1":
        tipo = "continental"
    elif opcion == "2":
        tipo = "intercontinental"
    else:
        print("Opcion invalida")
        return

    indice = asignar_avion(tipo)

    if indice == -1:
        print("No hay aviones disponibles")
        return

    aviones_disponible[indice] = False

    vuelos_origen.append(origen)
    vuelos_destino.append(destino)
    vuelos_tipo.append(tipo)
    vuelos_avion.append(indice)

    print("Vuelo creado correctamente")
     
crear_vuelo()

