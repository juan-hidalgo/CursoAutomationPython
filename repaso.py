import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Creación de la sesión en el navegador seleccionado
driver = webdriver.Chrome()

# Actualización del driver (desde la consola): pip install --upgrade selenium

# Ingreso a la página
driver.get("https://institutoweb.com.ar/test/login.html")

# Maximización de la ventana del navegador
driver.maximize_window()

# Obtención de los elementos mediante selectores
txt_usuario = driver.find_element(By.ID, "tuusuario")
txt_clave = driver.find_element(By.ID, "tuclave")
txt_mail = driver.find_element(By.ID, "tumail")
btn_ingresar = driver.find_element(By.CSS_SELECTOR, "body > form > button:nth-child(8)")

# Ejecución de las acciones sobre los elementos
txt_usuario.send_keys("Mi_Usuario")
txt_clave.send_keys("Mi_clave_12345")
txt_mail.send_keys("mail@mail.com")
time.sleep(5)
btn_ingresar.click()
time.sleep(2)

# Obtención de los elementos mediante selectores de la página siguiente
link_volver = driver.find_element(By.ID, "volver")
title_ok = driver.find_element(By.CSS_SELECTOR, "body > h3")

# Assertion - Análisis de respuesta - Verificación = Acceso correcto!
# Verificar que la variable tenga en su texto, el contenido "Acceso correcto!"
# Tras ejecutar, controlar desde la consola
assert "Acceso correcto!" == title_ok.text, "Acceso INCORRECTO"
print("El test continúa")

# Vuelta desde esta página siguiente y pausa de la espera final
# Ejecución de las acciones sobre los elementos de la página siguiente
link_volver.click()
time.sleep(2)

# Cierre del navegador
driver.quit
