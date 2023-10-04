def transformar_nombre(nombre_completo):
    if isinstance(nombre_completo, str):
        nombres = nombre_completo.split()
        apellido = nombres[-1]
        nombre = " ".join(nombres[:-1])
        return f"{apellido}, {nombre}"
    else:
        return nombre_completo

# Función para obtener las estadísticas de un jugador
def obtener_estadisticas(jugador):
    driver = webdriver.Chrome(PATH, options=opciones)
    driver.get(url)
    time.sleep(3)

    # Aceptar cookies
    aceptar = driver.find_element(By.XPATH, '//*[@id="ez-accept-necessary"]')
    aceptar.click()

    # Variables de asignación predeterminadas
    wins = 'N/A'
    draws = 'N/A'
    losses = 'N/A'

    try:
        # Introducir el nombre del jugador
        texto = driver.find_element(By.XPATH, '//*[@id="data"]')
        texto.send_keys(jugador)
        texto.send_keys(Keys.ENTER)
        time.sleep(3)

        # Obtener las estadísticas
        wins = driver.find_element(By.XPATH, '//*[@id="about"]/div[1]/div[9]/div/h6').text
        draws = driver.find_element(By.XPATH, '//*[@id="about"]/div[1]/div[10]/div/h6').text
        losses = driver.find_element(By.XPATH, '//*[@id="about"]/div[1]/div[11]/div/h6').text

        driver.quit()  # Cerrar el navegador

    except:
        time.sleep(2)

    return {'Jugador': jugador, 'Wins': wins, 'Draws': draws, 'Losses': losses}

def extraer_porcentaje(cadena):
    patron = r'\((\d+\.\d+)\s%\)'
    resultado = re.search(patron, cadena)

    if resultado:
        porcentaje = resultado.group(1)
        return porcentaje

    return None
