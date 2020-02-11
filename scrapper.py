import requests
from bs4 import BeautifulSoup
import smtplib
import time

LINK = "https://www.amazon.es/echo-dot-3-generacion-altavoz-inteligente-con-alexa-tela-de-color-antracita/dp/B07PHPXHQS/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1JIIATQ84WB18&keywords=alexa&qid=1573644957&sprefix=alexa%2Caps%2C176&sr=8-1"
#pass = "quobiydiferonann"
def send_email(price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('andrestascon@gmail.com','quobiydiferonann')
    subject = "Price is ",price," LOL, Low AF!"
    body = "Check amazon link ",LINK

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("andrestascon@gmail.com", "andrestascon@gmail.com", msg)
    print("Email has been sent!")
    server.quit()

def check_price():

    URL = LINK

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    price = soup2.find(id="priceblock_ourprice").get_text().strip()
    price_selected = price[0:5] #Coger de 0 a 5 numeros 34,99 son 5 caracteres
    price_selected = price_selected.replace(",",".")
    double_price = float(price_selected)
    print(double_price)
    if double_price <= 25.99:
        print ("Price is low AF!")
        send_email(double_price)

while(True):

    check_price()
    sleep(1800)