import time
from utils.insert import input
from utils.click import click
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

while(True):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://app.keedpay.com.br/checkout/N0i54RNsgq4")

    time.sleep(5)

    #---- person ----
    email = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/input', "teste@gmail.com")
    name = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[1]/div[3]/div/input', "teste123")
    phone = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[1]/div[4]/div/input', '99999999999')

    #---- delivery ----
    cep = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/input', '35588000')
    andress = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/div/input', 'Rua dos guaranis')
    number = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div/input', '111')

    complement = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[4]/div[2]/div/input', 'Perto do test2')

    district = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/input', 'TesteBairro')
    city = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[6]/Qdiv[1]/div/input', 'TesteCidade')
    state = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div[6]/div[2]/div/input', 'TesteEstado')

    #---- payment ----
    cpf_cnpj = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/div/input', '11111111111111')
    button = click(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[8]/button')
    cpf_cnpj = input(driver, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/div/input', '11111111112222')

    time.sleep(5)
    driver.quit()
