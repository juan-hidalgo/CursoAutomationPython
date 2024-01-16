# Data-Test en tienda.claro.com.ar
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tienda.claro.com.ar")

# busco elemento por data-test

txt_titulo = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]')
assert "Moto E13 64GB" == txt_titulo.text()
