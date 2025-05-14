from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ruta_controlador = r"C:\Users\danie\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
servicio = Service(executable_path=ruta_controlador)
opciones = webdriver.ChromeOptions()
opciones.add_argument("--start-maximized")

navegador = webdriver.Chrome(service=servicio, options=opciones)

try:
    navegador.get("https://www.youtube.com/watch?v=7KJpxXYvSeg")
    espera = WebDriverWait(navegador, 40)

    likes = espera.until(EC.presence_of_element_located((
        By.XPATH,
        '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]'
    )))
   
    like = likes.text.strip()
    print("Likes:", like)

    
    print("URL del video:", navegador.current_url)

finally:
    time.sleep(5)
    navegador.quit()





