import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():
    # Inicializamos el navegador
    driver = webdriver.Firefox()

    # Tiempo de espera explícito que tendrá el driver
    wait = WebDriverWait(driver, 5)

    try:
        # Abrimos el navegador
        driver.get("https://www.saucedemo.com/")

        # Localizamos los inputs de nombre y contraseña, y el botón de login
        usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = wait.until(EC.presence_of_element_located((By.ID, "password")))
        btn_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

        # Enviamos los datos correctos a los inputs de nombre y contraseña, y el evento click al botón de login
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        btn_login.click()

        # Validamos que el usuario se encuentre en la URL del catálogo luego del click en el botón login
        assert "/inventory.html" in driver.current_url

        # Validamos el logo y el titulo que contiene la página en la que esta el usuario actualmente
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")

        assert logo.text == "Swag Labs"
        assert titulo.text == "Products"

    finally:
        # Cerramos el navegador
        driver.quit()


def test_login_credenciales_invalidas():
    # Inicializamos el navegador
    driver = webdriver.Firefox()
    
    # Tiempo de espera explícito que tendrá el driver
    wait = WebDriverWait(driver, 5)

    try:
        # Abrimos el navegador
        driver.get("https://www.saucedemo.com/")
    
        # Localizamos los inputs de nombre y contraseña, y el botón de login
        usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = wait.until(EC.presence_of_element_located((By.ID, "password")))
        btn_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    
        # Enviamos datos invalidos a los inputs de nombre y contraseña, y el evento click al botón de login
        usuario.send_keys("standard_user")
        password.send_keys("sauce_secreto") # contraseña inválida
        btn_login.click()

        # Validamos que la URL donde se encuentre en usuario sea la del login
        assert "https://www.saucedemo.com/" in driver.current_url
    
        # Validamos que el elemento de error de credenciales se haga visible 
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))

        assert error.text == "Epic sadface: Username and password do not match any user in this service"

    finally:
        # Cerramos el navegador
        driver.quit()


def test_login_campos_vacios():
    # Inicializamos el navegador
    driver = webdriver.Firefox()

    try:
        # Abrimos el navegador
        driver.get("https://www.saucedemo.com/")
        
        # Localizamos el botón de login
        btn_login = driver.find_element(By.ID, "login-button")
        
        # Enviamos el evento click al botón de login
        btn_login.click()

        # Validamos que la URL donde se encuentre el usuario sea la del login
        assert "https://www.saucedemo.com/" in driver.current_url

        # Validamos que muestre mensaje de error
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    
        assert error.text == "Epic sadface: Username is required"
        

    finally:
        # Cerramos el navegador
        driver.quit()