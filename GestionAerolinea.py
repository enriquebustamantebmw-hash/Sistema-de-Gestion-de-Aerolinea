"""Sistema de Gestion de Aerolinea - Programacion 1 - Grupo 4"""

aviones = [
    {"id": 1, "modelo": "A320", "tipo": "continental", "capacidad": 180, "disponible": True},
    {"id": 2, "modelo": "A320", "tipo": "continental", "capacidad": 180, "disponible": True},
    {"id": 3, "modelo": "A320", "tipo": "continental", "capacidad": 180, "disponible": True},
    {"id": 4, "modelo": "A320", "tipo": "continental", "capacidad": 180, "disponible": True},
    {"id": 5, "modelo": "A350", "tipo": "intercontinental", "capacidad": 300, "disponible": True},
    {"id": 6, "modelo": "Boeing 777", "tipo": "intercontinental", "capacidad": 300, "disponible": True}
]

vuelos = []
pasajeros = []
reservas = []


def mostrar_flota():
    """Muestra la flota de aviones con su estado de disponibilidad."""
    print("\nFlota de aviones:")
    for avion in aviones:
        if avion["disponible"]:
            estado = "Disponible"
        else:
            estado = "Ocupado"

        print("ID:", avion["id"])
        print("Modelo:", avion["modelo"])
        print("Tipo:", avion["tipo"])
        print("Capacidad:", avion["capacidad"], "asientos")
        print("Estado:", estado)
        print("-------------------------")
        
def asignar_avion(tipo_ruta):
    """busca un avion disponible segun el tipo de ruta."""

    for avion in aviones:
        if avion["tipo"] == tipo_ruta and avion["disponible"]:
            return avion

    return None    

def crear_vuelo():
    """permite crear un vuelo y asignar un avion disponible."""

    print("\nCrear vuelo")
    origen = input("Origen: ")
    destino = input("Destino: ")

    print("1- Continental")
    print("2- Intercontinental")
    opcion = input("Opcion: ")

    if opcion == "1":
        tipo = "continental"
    elif opcion == "2":
        tipo = "intercontinental"
    else:
        print("Opcion invalida")
        return

    avion = asignar_avion(tipo)

    if avion == None:
        print("No hay aviones disponibles para ese tipo de ruta")
        return

    avion["disponible"] = False

    vuelo = {
        "origen": origen,
        "destino": destino,
        "tipo": tipo,
        "avion": avion["modelo"],
        "capacidad": avion["capacidad"],
        "asientos_disponibles": avion["capacidad"]
    }

    vuelos.append(vuelo)

    print("Vuelo creado correctamente")

def mostrar_vuelos():
    """muestra todos los vuelos creados"""

    if len(vuelos) == 0:
        print("No hay vuelos registrados")
        return

    print("\nLista de vuelos:")

    for i in range(len(vuelos)):
        print("Vuelo", i + 1)
        print("Origen:", vuelos[i]["origen"])
        print("Destino:", vuelos[i]["destino"])
        print("Tipo:", vuelos[i]["tipo"])
        print("Avion:", vuelos[i]["avion"])
        print("Asientos disponibles:", vuelos[i]["asientos_disponibles"])
        print("-------------------------")
        
def menu():
    """se muestra el menu principal del sistema."""

    opcion = ""

    while opcion != "0":
        print("\nSistema de Gestion de Aerolinea")
        print("1- Ver flota")
        print("2- Crear vuelo")
        print("3- Ver vuelos")
        print("4- Registrar pasajero")
        print("5- Ver pasajeros")
        print("0- Salir")

        opcion = input("Opcion: ")

        if opcion == "1":
            mostrar_flota()
        elif opcion == "2":
            crear_vuelo()
        elif opcion == "3":
            mostrar_vuelos()
            
        elif opcion == "4":
            registrar_pasajero()
        elif opcion == "5":
            mostrar_pasajeros()
        elif opcion == "0":
            print("Fin del sistema")
        else:
            print("Opcion invalida")
            


def buscar_pasajero_por_dni(dni):
    """Busca a un pasajero por Dni """

    for pasajero in pasajeros:
        if pasajero["dni"] == dni:
            return pasajero

    return None


def registrar_pasajero():
    """Registra un pasajero validando que el dni no este repetido"""

    print("\nRegistrar pasajero")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")

    if buscar_pasajero_por_dni(dni) != None:
        print("Ya existe un pasajero registrado con ese dni")
        return

    pasajero = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    }

    pasajeros.append(pasajero)

    print("Pasajero registrado correctamente")


def mostrar_pasajeros():
    """Muestra la lista de pasajeros registrados."""

    if len(pasajeros) == 0:
        print("No hay pasajeros registrados")
        return

    print("\nLista de pasajeros:")

    for i in range(len(pasajeros)):
        print("Pasajero", i + 1)
        print("Nombre:", pasajeros[i]["nombre"])
        print("Apellido:", pasajeros[i]["apellido"])
        print("DNI:", pasajeros[i]["dni"])
        print("-------------------------")
        
menu()