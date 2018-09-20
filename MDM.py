#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def credenciais(self):
    print("Dados para login no Facebook")
    usuario = input("Digite seu e-mail ou usuário:")
    senha = input("Digite sua senha:")

    # go to the Facebook home page
    self.get("https://www.facebook.com")

    # Digita as credenciais de login
    inputEmail = self.find_element_by_name("email")

    inputEmail.send_keys("ds1523339@mailbox.org")

    inputPass = self.find_element_by_name("pass")

    inputPass.send_keys("aSd%5lKj&7kkk")

    # envia as credenciais de login
    inputPass.submit()

    # Aguarda o carregamento da página
    sleep(5)


def busca(self):
    buscaUser = input("Digite o nome do usuário para a busca:")

    # find the element that's name attribute is q (the Facebook search box)
    inputBusca = self.find_element_by_name("q")

    # type in the search
    inputBusca.send_keys(buscaUser)
    inputBusca.submit()


def printer(self):
    print(self.title)
    sleep(10)

def closer(self):
    self.quit()

# Create a new instance of the Firefox driver
pagina = webdriver.Firefox()
pagina.minimize_window()

credenciais(pagina)
busca(pagina)
printer(pagina)
closer(pagina)

# we have to wait for the page to refresh, the last thing that seems to be updated is the title
#WebDriverWait(driver, 10).until(EC.title_contains("Lula"))
#sleep(10)
#
