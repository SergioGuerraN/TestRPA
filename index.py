from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#import org.openqa.selenium.keys

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()
time.sleep(1)
driver.get("https://www.viajesexito.com/")
paquetes = driver.find_element(
    By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a/p')
time.sleep(1)
paquetes.click()

ciudadDestino = "Punta "
destino = driver.find_element(
    By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input')
destino.click()
destino.send_keys(ciudadDestino)
time.sleep(1)

seleccionarCiudad = driver.find_element(By.XPATH, '/html/body/ul[21]/li[3]')
seleccionarCiudad.click()
time.sleep(2)

fechas = driver.find_element(
    By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]')
fechas.click()
time.sleep(1)

fechaSalida = driver.find_element(
    By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]')
fechaSalida.click()
time.sleep(1)

fechaRegreso = driver.find_element(
    By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]')
fechaRegreso.click()
time.sleep(1)

adultos = driver.find_element(
    By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p')
adultos.click()
time.sleep(1)

adicionarAdulto = driver.find_element(
    By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button/span')
adicionarAdulto.click()
time.sleep(1)

confirmarAdultos = driver.find_element(
    By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button')
confirmarAdultos.click()
time.sleep(3)

buscarViaje = driver.find_element(
    By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a/p')
buscarViaje.click()
time.sleep(30)

opcionesAvanzadas = driver.find_element(
    By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
opcionesAvanzadas.click()
time.sleep(2)


aerolienaA = "avi"
aerolinea = driver.find_element(
    By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
aerolinea.click()
aerolinea.send_keys(aerolienaA)
time.sleep(1)


aero = driver.find_element(By.XPATH, '/html/body/ul[3]/li[1]')
aero.click()

buscar2 = driver.find_element(
    By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscar2.click()
time.sleep(5)


driver.quit()
