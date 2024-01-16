import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Creación de la sesión en el navegador seleccionado
driver = webdriver.Chrome()

# https://institutoweb.com.ar/test/test2/selectmultiple.html
# https://institutoweb.com.ar/test/test2/select.html

# Ingreso a la página
driver.get("https://institutoweb.com.ar/test/test2/select.html")

# Maximización de la ventana del navegador
driver.maximize_window()

# Obtención de los elementos SELECT mediante selectores
select_element = driver.find_element(By.NAME, "selector")
mi_selector = Select(select_element)

# Ejecución de las acciones sobre los elementos - Ejemplos académicos
time.sleep(2)
select_element.send_keys("Esp")
time.sleep(2)
mi_selector.select_by_value("value2")
time.sleep(2)
mi_selector.select_by_index(2)
time.sleep(2)
mi_selector.select_by_visible_text("Colombia")
time.sleep(2)

# Cierre del navegador
driver.quit
