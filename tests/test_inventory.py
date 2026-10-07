import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_visualizacion_productos():
    # Inicializamos el navegador
    driver = webdriver.Firefox()
    
    # Tiempo de espera explícito que tendrá el driver
    wait = WebDriverWait(driver, 5)

    try:
        # MÓDULO LOGIN
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

        # MÓDULO INVENTORY (CATÁLOGO)
        # Buscamos la presencia de productos en el inventario
        productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        # Sacamos la longitud de cuantos productos hay en el inventario
        products = len(productos)
        assert products > 0

        # Imprimimos/listamos el nombre y precio del primer producto
        primer_producto = productos[0]

        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name")
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price")

        assert nombre_producto.text == "Sauce Labs Backpack"
        assert precio_producto.text == "$29.99"

    finally:
        # Cerramos el navegador
        driver.quit()


def test_visualizacion_elementos():
    # Inicializamos el navegador
    driver = webdriver.Firefox()
        
    # Tiempo de espera explícito que tendrá el driver
    wait = WebDriverWait(driver, 5)
    
    try:
        # MÓDULO LOGIN
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

        # MÓDULO INVENTORY (CATÁLOGO)
        # Verificamos que los elementos importantes de la interfaz esten presentes (menú, filtro, icono carrito)
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

        icono_carrito = driver.find_element(By.ID, "shopping_cart_container")
        assert icono_carrito.is_displayed()

    finally:
        # Cerramos el navegador
        driver.quit()


def test_agregar_producto_al_carrito():
    # Inicializamos el navegador
    driver = webdriver.Firefox()
            
    # Tiempo de espera explícito que tendrá el driver
    wait = WebDriverWait(driver, 5)
        
    try:
        # MÓDULO LOGIN
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
    
        # MÓDULO INVENTORY (CATÁLOGO)
        # Buscamos la presencia de productos en el inventario
        productos = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        # Sacamos la longitud de cuantos productos hay en el inventario
        products = len(productos)
        assert products > 0

        # Identificamos el botón de agregar al carrito (del primer producto)
        add_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")

    finally:
        # Cerramos el navegador
        driver.quit()