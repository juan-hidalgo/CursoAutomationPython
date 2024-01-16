import time
from behave import given, when, then
from selenium import webdriver

@given('ingreso a la web Don Bosco')
def step_given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.donboscolabs.com.ar")

@when('compruebo que el titulo es "{var_titulo}"')
def step_when(context,var_titulo):
    time.sleep(4)
    titulo_web = context.driver.title
    assert titulo_web == var_titulo

@then('cierro el navegador')
def step_then(context):
    context.driver.close()