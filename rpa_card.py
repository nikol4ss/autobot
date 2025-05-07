import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utils.click import click
from utils.insert import input
from utils.log import log

def run_checkout_card():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    for _ in range(3):
        log("RUN", "CARD CHECKOUT")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.get("https://app.keedpay.com.br/checkout/6R3OzH3uj5h")
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/input', "luciano@grupocapsul.com.br")
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[1]/div[3]/div/input', "Luciano Emanuel")
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[1]/div[4]/div/input', '37999690698')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/input', '05407002')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/div/input', 'Rua Cardeal Arcoverde')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div/input', '1011')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[2]/div/input', 'TESTE')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/input', 'Pinheiros')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[6]/div[1]/div/input', 'São Paulo')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[6]/div[2]/div/input', 'SP')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[1]/div/input', 'teste')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[2]/div/div/input', 'teste')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[3]/div/div/input', '10866861602')
            input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[4]/div[2]/div/input', 'teste')
            click(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[10]/button')

            time.sleep(3)

        except Exception as e:
            log(f"ERROR {e}")

        finally:
            driver.quit()
            log("FINISHED", "CARD DONE")
            time.sleep(2)

if __name__ == "__main__":
    run_checkout_card()
