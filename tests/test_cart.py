import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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

        # Hacemos el evento click en ese botón de agregar al carrito
        add_cart.click()

        # Verificamos que el producto se haya añadido al carrito
        badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

        assert badge.text == "1"

        print(f"Se ha añadido el producto al carrito correctamente")

    finally:
        # Cerramos el navegador
        driver.quit()


def test_verificar_item_carrito():
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
    
        # Hacemos el evento click en ese botón de agregar al carrito
        add_cart.click()

        # Verificamos que nos lleve a la URL del carrito
        assert "/cart.html" in driver.current_url
    
        # Verificamos que el producto este en el carrito
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        carrito.click()

        producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
        print("El producto esta visible en el carrito")
    
    finally:
        # Cerramos el navegador
        driver.quit()


def test_eliminar_producto_del_carrito():
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
    
        # Hacemos el evento click en ese botón de agregar al carrito
        add_cart.click()
    
        # Verificamos que el producto se haya añadido al carrito
        badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    
        assert badge.text == "1"

        # Ubicamos el botón de remove del primer producto para eliminarlo del carrito
        remove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        remove.click()

        # Verificamos que se haya eliminado de carrito
        contador = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    finally:
        # Cerramos el navegador
        driver.quit()