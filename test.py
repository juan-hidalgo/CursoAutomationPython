import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.emaras.com.ar")
driver.maximize_window()
driver.find_element(By.NAME, "usuario").send_keys("prueba")
driver.find_element(By.NAME, "clave").send_keys("12345")
driver.find_element(By.ID, "btnIngresar").click()
time.sleep(5)
