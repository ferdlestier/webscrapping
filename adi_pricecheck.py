# This is a quick script to scrape data from the web and send a price alert message via a Telegram bot

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

# As an example I used a website with a shoe I looked at

producturl="https://www.adidas.com/us/harden-vol.-6-shoes/GW1712.html?forceSelSize=M%209%20%2F%20W%2010"
# Alternatively we can work with website inputs:
#producturl = input ( "Please input product url : " )
# You'll have to set the dollar amount you want to be notified in case the price goes under that threashold
alertprice = float ( input ( "please enter the price you need to be notify : $" ) )
print("Your link is: "+ producturl)
print ( f"Thank You, You'll be alerted if the price drop below ${alertprice}" )

# Creating the function that will do the webscrapping
def checkPrice(producturl) :
    try:
        driver = webdriver.Chrome ()
        driver.get ("https://www.adidas.com/us/harden-vol.-6-shoes/GW1712.html?forceSelSize=M%209%20%2F%20W%2010")
        producttitle=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[1]/h1/span').text
        productprice=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div').text
        prodprice = productprice.strip('$')
        if float(prodprice) < alertprice:
            print(f'{producttitle} price has dropped below alert price, its price now is {productprice}')
    except:
        print('The price is still over $'+str(alertprice))

# Defining the function that will send the message via Telegram
# Need to input your bot Chat ID and bot Token
def send_message(bot_message) :
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get ( send_text )
    return response.json ( )

# In order to set a while loop, you can use the following lines
#while(True):
#    checkPrice(producturl)
#    time.sleep(10)

# For a one time run, use these following lines:
checkPrice(producturl)
new_message = f'{producttitle} price has dropped below alert price, its price now is {productprice}. {producturl}'
send_message(new_message)
