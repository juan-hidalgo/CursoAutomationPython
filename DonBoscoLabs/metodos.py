# Modularizamos para el POM (page object model)

from selenium.webdriver.common.by import By


def visitar_url(driver, url):
    driver.get(url)
    driver.maximize_window()


def escribir_id(driver, elemento, texto):
    driver.find_element(By.ID, elemento).click()
    driver.find_element(By.ID, elemento).clear
    driver.find_element(By.ID, elemento).send_keys(texto)


def click_link(driver, elemento):
    driver.find_element(By.LINK_TEXT, elemento).click()


def click_id(driver, texto):
    driver.find_element(By.ID, texto).click()


def espera_implicita(driver):
    driver.implicitly_wait(4)
