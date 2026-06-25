import GestionAerolinea as sistema


def test_validar_dni_correcto():
    assert sistema.validar_dni("12345678") == True


def test_validar_dni_incorrecto():
    assert sistema.validar_dni("123ABC") == False


def test_validar_texto_correcto():
    assert sistema.validar_texto("Buenos Aires") == True


def test_validar_texto_incorrecto():
    assert sistema.validar_texto("Buenos Aires 123") == False


def test_asignar_avion_continental():
    avion = sistema.asignar_avion("continental")
    assert avion["tipo"] == "continental"