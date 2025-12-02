from pytest_bdd import scenarios, given, when, then, parsers

# Vincula el archivo .feature
scenarios("votar.feature")

def puede_votar(edad):
    return "Sí puede votar" if edad >= 18 else "No puede votar"

@given(parsers.parse("que la persona tiene {edad:d} años"))
def edad_persona(edad):
    return {"edad": edad}

@when("se verifica si puede votar")
def verificar(edad_persona):
    resultado = puede_votar(edad_persona["edad"])
    edad_persona["resultado"] = resultado
    return edad_persona

@then(parsers.parse('el resultado debe ser "{texto}"'))
def validar(edad_persona, texto):
    assert edad_persona["resultado"] == texto
