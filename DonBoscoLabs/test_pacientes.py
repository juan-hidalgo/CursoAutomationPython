# US: Cargar usuarios en la base de datos utilizando la interfaz
# DataSet funcional
# https://donboscolabs.com.ar
# usr: mimail@gmail.com
# psw: laboratorio1

import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   # Alias for "Expected Condition"

from metodos import escribir_id, click_link, click_id, visitar_url, espera_implicita
from selectores import obtener_selectores

driver = webdriver.Chrome()
espera_implicita(driver)
visitar_url(driver,"https://www.donboscolabs.com.ar/")
click_link(driver,"Login")
escribir_id(driver,"username","mimail@gmail.com")
escribir_id(driver,"password","laboratorio1")
click_id(driver,"loginButton")
click_link(driver,"Pacientes")

driver.find_element(By.CSS_SELECTOR, ".table-primary:nth-child(1) > td:nth-child(4) img").click()

escribir_id(driver,"nombre","Pablo")
escribir_id(driver,"domicilio","Santa Fe 5023")
click_id(driver,"updateButton")

espera_explicita = WebDriverWait(driver,4)
alerta = espera_explicita.until(EC.alert_is_present())
alerta = driver.switch_to.alert # foco en la ventana del alert
assert alerta.text == "Los datos se actualizaron correctamente" # aserción de respuesta de la alerta
alerta.accept()
time.sleep(4)

click_link(driver,"Volver")
click_link(driver,"Volver")
click_link(driver,"Inicio")

driver.quit()