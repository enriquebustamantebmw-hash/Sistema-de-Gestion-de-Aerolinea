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

mostrar_flota()
crear_vuelo()