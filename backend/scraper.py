from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_scraper(patente: str) -> str:
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")
    option.add_argument("--window-size=1920,1080")
    
    driver = Chrome(service=service, options=option)
    driver.implicitly_wait(10)
    driver.get("https://pasastesintag.cl/")

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]').click()

    driver.find_element("id", "inputPatente").send_keys(patente)
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/form/button').click()

    if driver.find_elements(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/span'):
        response = "Patente no encontrada o no posee multas."
    else:
        deuda = driver.find_element(By.XPATH, '//*[@id="contResumenBajo"]/section[2]/div[1]/div[2]/div[1]/p').text
        response =  f"La patente {patente} posee una deuda total de: {deuda}"

    print(response)

    driver.quit() 

    return response   