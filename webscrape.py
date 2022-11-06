from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

producturl = input ( "Please input product url : " )
alertprice = float ( input ( "please enter the price you need to be notify : $" ) )
print("Your link is: "+ producturl)
print ( f"Thank You, You'll be alerted if the price drop below ${alertprice}" )

def checkPrice(producturl) :
    try:
        driver = webdriver.Chrome ()
        driver.get ( producturl )
        producttitle=driver.find_element(By.ID,'productTitle').text
        productprice=driver.find_element(By.CLASS_NAME,'apexPriceToPay').text.removeprefix('$')
        if float(productprice) <= alertprice:
            send_message(f'{producttitle}\nprice has dropped below alert price, its price now is ${productprice}')
    except:
        print('The price is still over $'+str(alertprice))

def send_message(bot_message) :
    bot_token = '<token>'
    bot_chatID = 'BotTest'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get ( send_text )
    return response.json ( )

while(True):
    checkPrice(producturl)
    time.sleep(10)
