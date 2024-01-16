@test
Feature: Control del titulo de DonBoscoLabs

    Scenario Outline: Test del titulo
        Given ingreso a la web Don Bosco
        When compruebo que el titulo es "<mi_titulo>"
        Then cierro el navegador

    Examples:
    | mi_titulo      | 
    | Don Juan       |
    | Don Bosco Labs |
    | Don Pepe Labs  |