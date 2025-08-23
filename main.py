from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATENTE = "jt0789"

def main():
    
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    
    driver = Chrome(service=service, options=option)
    driver.implicitly_wait(10)
    driver.get("https://pasastesintag.cl/")

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/button[1]').click()

    driver.find_element("id", "inputPatente").send_keys(PATENTE)
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/form/button').click()

    

    response = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/span').text

    print('no registra deuda' in response.lower())
    

    time.sleep(2)  # Wait for the page to load
    driver.quit()  # Close the browser after use

if __name__ == "__main__":
    main()
    pass