from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#import org.openqa.selenium.keys

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()
time.sleep(1)
driver.get("https://www.mercadolibre.com.co/#from=homecom")
cookies = driver.find_element(
    By.XPATH, '/HTML/body/div[2]/div[1]/div[2]/button[1]')
time.sleep(1)
# cookies.click()
tema = "PORTATILES LENOVO GAMER"

busqueda = driver.find_element(By.XPATH, '/html/body/header/div/form/input')
busqueda.click()
busqueda.send_keys(tema)

# click en la lupa de busqueda
buscar = driver.find_element(By.XPATH, '/html/body/header/div/form/button/div')
buscar.click()
time.sleep(1)

#descripcionpc=driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/ol/li[1]/div/div/div[1]/a/div/div/div/div/div/img')
# descripcionpc.click()

descripcionpc = driver.find_element(
    By.XPATH, '/html/body/main/div/div[2]/section/ol/li[1]/div/div/div[2]/div[1]/a/h2').text
preciopc = driver.find_element(
    By.XPATH, '/html/body/main/div/div[2]/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text

print("-------PRIMER PRODUCTO EN CONSOLA-------")
print(preciopc)
print(descripcionpc)

time.sleep(3)

busquedaDos = driver.find_element(By.XPATH, '/html/body/header/div/form/input')
busquedaDos.click()
busquedaDos.clear()
busquedaDos.send_keys("Mouse Gamer")

busquedaDos = driver.find_element(
    By.XPATH, '/html/body/header/div/form/button/div')
busquedaDos.click()

entrarProduct = driver.find_element(
    By.XPATH, '/html/body/main/div/div[2]/section/ol/li[1]/div/div/div[1]/a/div/div/div/div/div/img')
entrarProduct.click()
time.sleep(4)

driver.quit()
