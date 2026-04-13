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

mostrar_flota()


