import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Creación de la sesión en el navegador seleccionado
driver = webdriver.Chrome()

# Ingreso a la página
driver.get("https://institutoweb.com.ar/test/test2/selectmultiple.html")

# Maximización de la ventana del navegador
driver.maximize_window()

# Obtención de los elementos mediante selectores
select_element = driver.find_element(By.ID, "selector")
multiple = Select(select_element)

# Ejecución de las acciones sobre los elementos - Ejemplos académicos
time.sleep(2)
multiple.select_by_value("value1")
time.sleep(2)
multiple.select_by_value("value2")
time.sleep(2)
multiple.deselect_all()
multiple.select_by_value("value3")
time.sleep(3)

# Cierre del navegador
driver.quit
