from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

producturl="https://www.adidas.com/us/daily-3.0-shoes/FW7050.html"
#producturl = input ( "Please input product url : " )
alertprice = float ( input ( "please enter the price you need to be notify : $" ) )
print("Your link is: "+ producturl)
print ( f"Thank You, You'll be alerted if the price drop below ${alertprice}" )

def checkPrice(producturl) :
    try:
        driver = webdriver.Chrome ()
        driver.get ("https://www.adidas.com/us/daily-3.0-shoes/FW7050.html")
        producttitle=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/h1/span').text
        productprice=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div').text
        if float(productprice) < alertprice:
            print(f'{productprice} price has dropped below alert price, its price now is ${productprice}')
    except:
        print('The price is still over $'+str(alertprice))

#def send_message(bot_message) :
#    bot_token = '5***************8'
#    bot_chatID = 'BotTest'
#    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
#    response = requests.get ( send_text )
#    return response.json ( )

#while(True):
#    checkPrice(producturl)
#    time.sleep(10)
checkPrice(producturl)
