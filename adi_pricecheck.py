from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

producturl="https://www.adidas.com/us/harden-vol.-6-shoes/GW1712.html?forceSelSize=M%209%20%2F%20W%2010"
#producturl = input ( "Please input product url : " )
alertprice = float ( input ( "please enter the price you need to be notify : $" ) )
print("Your link is: "+ producturl)
print ( f"Thank You, You'll be alerted if the price drop below ${alertprice}" )

def checkPrice(producturl) :
    try:
        driver = webdriver.Chrome ()
        driver.get ("https://www.adidas.com/us/harden-vol.-6-shoes/GW1712.html?forceSelSize=M%209%20%2F%20W%2010")
        producttitle=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div/h1/span').text
        productprice=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div').text
        prodprice = productprice.strip('$')
        if float(prodprice) < alertprice:
            print(f'{producttitle} price has dropped below alert price, its price now is {productprice}')
    except:
        print('The price is still over $'+str(alertprice))

def send_message(bot_message) :
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get ( send_text )
    return response.json ( )

#while(True):
#    checkPrice(producturl)
#    time.sleep(10)
checkPrice(producturl)
new_message = f'{producttitle} price has dropped below alert price, its price now is {productprice}. {producturl}'
send_message(new_message)
