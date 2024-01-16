# US: Cargar usuarios en la base de datos utilizando la interfaz
# DataSet funcional
# usr: mimail@gmail.com
# psw: laboratorio1

import time
import json
from selectores import obtener_selectores
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #Alias for "Expected Condition"

try:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://donboscolabs.com.ar")

    # Trabajo con archivo data.json
    with open('CursoAutomationPython/DonBoscoLabs/data.json','r') as mi_archivo:
        lector = json.load(mi_archivo)
    # Obtención de los elementos mediante selectores - Página de inicio
    lnk_login = driver.find_element(By.LINK_TEXT,"Login")
    # Ejecución de las acciones sobre los elementos - Página de inicio
    lnk_login.click()
    # Obtención de selectores
    login_screen = obtener_selectores()
    
    for renglon in lector:
        var_usuario = renglon['user']
        var_clave = renglon['password']
                
    # Obtención de los elementos mediante selectores - Página de login
        txt_user = driver.find_element(By.ID,login_screen['txt_usuario'])
        txt_pass = driver.find_element(By.ID,login_screen['txt_clave'])
        btn_login = driver.find_element(By.ID,login_screen['btn_login'])

    # Ejecución de las acciones sobre los elementos - Página de login
        txt_user.clear()
        txt_user.send_keys(var_usuario)
        txt_pass.clear()
        txt_pass.send_keys(var_clave)
        btn_login.click()

    # Espera explícita de 4 seg puntualmente para el evento
        espera_explicita = WebDriverWait(driver,4)
        alerta = espera_explicita.until(EC.alert_is_present()) 

    # Mensaje de error de la ventana login de usuario (alert por sistema del browser)
        alerta = driver.switch_to.alert
        assert alerta.text == "Usuario o Clave inválida"
        alerta.accept()

except AssertionError:
    print("Ocurrió un error de assertion")
    driver.quit()
except FileNotFoundError:
    print("No se encontró el archivo")
    driver.quit()
except Exception:
    print("Ocurrió un error")
    driver.quit()

# Cierre de sesión
time.sleep(4)
driver.quit()