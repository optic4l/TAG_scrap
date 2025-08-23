from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os
from dotenv import load_dotenv


load_dotenv()

def main():
    
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    
    driver = Chrome(service=service, options=option)
    driver.implicitly_wait(10)
    driver.get("https://pasastesintag.cl/")

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]').click()

    driver.find_element("id", "inputPatente").send_keys(os.getenv("PATENTE"))
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/form/button').click()

    

    response = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/span').text

    if('no registra deuda' not in response.lower()):
        telegram_message(f'El vehiculo con patente {os.getenv("PATENTE")} no registra deuda')
    else:
        telegram_message(f'El vehiculo con patente {os.getenv("PATENTE")} registra deuda')
    

    time.sleep(2)  # Wait for the page to load
    driver.quit()  # Close the browser after use

def telegram_message(message: str):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=data)
    print("Mensaje enviado a Telegram")

if __name__ == "__main__":
    main()
    pass