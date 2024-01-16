# Acá se guardan los nombres de los selectores a utilizar 
# por pantalla y los devuelve cuando se los solicita - definiendo una función

def obtener_selectores():
    selectores_login = {
        "txt_usuario" : "username",
        "txt_clave" : "password",
        "btn_login" : "loginButton"
    }
    return selectores_login
