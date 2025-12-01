Feature: Validar si una persona puede votar

  Scenario: Persona con edad suficiente
    Given que la persona tiene 20 años
    When se verifica si puede votar
    Then el resultado debe ser "Sí puede votar"

  Scenario: Persona menor de edad
    Given que la persona tiene 15 años
    When se verifica si puede votar
    Then el resultado debe ser "No puede votar"
