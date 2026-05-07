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