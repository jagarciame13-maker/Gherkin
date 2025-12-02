from pytest_bdd import scenarios, given, when, then, parsers

# Cargar escenarios desde la carpeta tests
scenarios("votar.feature")

def puede_votar(edad):
    return "Sí puede votar" if edad >= 18 else "No puede votar"

# -----------------------
#       GIVEN
# -----------------------
@given(parsers.parse("que la persona tiene {edad:d} años"), target_fixture="contexto")
def given_edad(edad):
    return {"edad": edad}

# -----------------------
#        WHEN
# -----------------------
@when("se verifica si puede votar")
def when_verifica(contexto):
    resultado = puede_votar(contexto["edad"])
    contexto["resultado"] = resultado
    return contexto

# -----------------------
#        THEN
# -----------------------
@then(parsers.parse('el resultado debe ser "{texto}"'))
def then_resultado(contexto, texto):
    assert contexto["resultado"] == texto

