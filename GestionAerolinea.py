"""Sistema de Gestion de Aerolinea - Programacion 1 - Grupo 4"""

from functools import reduce

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
        print("6- Realizar reserva")
        print("7- Ver reservas")
        print("8- Ver aviones disponibles")
        print("9- Ver vuelos continentales")
        print("10- Ver modelos de aviones")
        print("11- Ver capacidad total")
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
        elif opcion == "6":
            realizar_reserva()
        elif opcion == "7":
            mostrar_reservas()
        elif opcion == "8":
            mostrar_aviones_disponibles()
        elif opcion == "9":
            mostrar_vuelos_continentales()
        elif opcion == "10":
           mostrar_modelos_aviones()
        elif opcion == "11":
         mostrar_capacidad_total()
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
        


def mostrar_vuelos_con_numero():
    """muestra los vuelos con un numero para poder seleccionarlos"""

    if len(vuelos) == 0:
        print("No hay vuelos registrados")
        return

    for i in range(len(vuelos)):
        print(i + 1, "-", vuelos[i]["origen"], "->", vuelos[i]["destino"], "-", vuelos[i]["avion"])


def realizar_reserva():
    """realiza una reserva asociando un pasajero a un vuelo"""

    if len(vuelos) == 0:
        print("No hay vuelos registrados")
        return

    if len(pasajeros) == 0:
        print("No hay pasajeros registrados")
        return

    dni = input("DNI del pasajero: ")
    pasajero = buscar_pasajero_por_dni(dni)

    if pasajero == None:
        print("Pasajero no encontrado")
        return

    mostrar_vuelos_con_numero()

    try:
        numero_vuelo = int(input("Seleccione el numero de vuelo: "))
    except ValueError:
        print("Debe ingresar un numero")
        return

    if numero_vuelo < 1 or numero_vuelo > len(vuelos):
        print("Numero de vuelo invalido")
        return

    vuelo = vuelos[numero_vuelo - 1]

    if vuelo["asientos_disponibles"] <= 0:
        print("El vuelo esta completo")
        return

    vuelo["asientos_disponibles"] = vuelo["asientos_disponibles"] - 1

    reserva = {
        "dni": pasajero["dni"],
        "pasajero": pasajero["nombre"] + " " + pasajero["apellido"],
        "origen": vuelo["origen"],
        "destino": vuelo["destino"],
        "avion": vuelo["avion"]
    }

    reservas.append(reserva)

    print("Reserva realizada correctamente")


def mostrar_reservas():
    """muestra todas las reservas realizadas."""

    if len(reservas) == 0:
        print("No hay reservas registradas")
        return

    print("\nLista de reservas:")

    for i in range(len(reservas)):
        print("Reserva", i + 1)
        print("Pasajero:", reservas[i]["pasajero"])
        print("DNI:", reservas[i]["dni"])
        print("Vuelo:", reservas[i]["origen"], "->", reservas[i]["destino"])
        print("Avion:", reservas[i]["avion"])
        print("-------------------------")
        


def mostrar_aviones_disponibles():
    """muestra solo los aviones disponibles usando filter"""

    disponibles = list(filter(lambda avion: avion["disponible"], aviones))

    if len(disponibles) == 0:
        print("No hay aviones disponibles")
        return

    print("\nAviones disponibles:")
    for avion in disponibles:
        print("ID:", avion["id"], "-", avion["modelo"], "-", avion["tipo"])


def mostrar_vuelos_continentales():
    """muestra solo los vuelos continentales usando filter"""

    continentales = list(filter(lambda vuelo: vuelo["tipo"] == "continental", vuelos))

    if len(continentales) == 0:
        print("No hay vuelos continentales")
        return

    print("\nVuelos continentales:")
    for vuelo in continentales:
        print(vuelo["origen"], "->", vuelo["destino"], "-", vuelo["avion"])
        
def mostrar_modelos_aviones():
    """muestra los modelos de aviones usando map"""

    modelos = list(map(lambda avion: avion["modelo"], aviones))

    print("\nModelos de aviones:")
    for modelo in modelos:
        print(modelo)

def mostrar_capacidad_total():
    """uso reduce para mostrar la capacidad total de la flota de aviones"""

    capacidades = list(map(lambda avion: avion["capacidad"], aviones))
    total = reduce(lambda acumulador, capacidad: acumulador + capacidad, capacidades)

    print("Capacidad total de la flota:", total, "asientos")
    
menu()