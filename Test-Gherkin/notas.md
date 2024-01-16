Vimos un  Scenario Outline, pero podría ser solamente Scenario si no usamos variables.

    Scenario Outline: Test del titulo
        Given ingreso a la web Don Bosco
        When compruebo que el titulo es "<mi_titulo>"
        Then cierro el navegador

    Examples:
    | mi_titulo      | 
    | Don Juan       |
    | Don Bosco Labs |
    | Don Pepe Labs  |

Si se usan más de una variable se utiliza este formato:
    
    Examples:
    | mi_titulo      | mi_otra_var |
    | Don Juan       | 1254        |
    | Don Bosco Labs | 555         |
    | Don Pepe Labs  | 0000        |