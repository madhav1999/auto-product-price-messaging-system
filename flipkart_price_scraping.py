from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier
from selenium.webdriver.support.ui import WebDriverWait
import time

PATH = "C:\Program Files (x86)\chromedriver_for_selenium.exe"
driver =  webdriver.Chrome(PATH)

driver.get("https://flipkart.com")
print(driver.title)

email = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
email.send_keys("YOUR_FLIPKART_ACCOUNT_LOGIN_ID")

password=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
password.send_keys("YOUR_FLIPKART_ACCOUNT_PASSWORD")

button=driver.find_element_by_xpath("[paste_your_xpath_of_your_product_in_cart]")

button.click()

cart=driver.find_element_by_xpath("[paste_your_xpath_of_your_product_in_cart]")
cart.send_keys(Keys.RETURN)
det=""
try:
	details = WebDriverWait(driver,10).until(
	     EC.presence_of_element_located((By.XPATH,"[paste_your_xpath_of_your_product_in_cart]"))
	)  
	det=details.text
	print(details.text)
except:
	print(details.text)
	
print(det[1:])
price=(int)(det[1:])
priceinitial=price
while (priceinitial<=price):
	try:
		details = WebDriverWait(driver,10).until(
		EC.presence_of_element_located((By.XPATH,"[paste_your_xpath_of_your_product_in_cart]"))
		)  
		price=(int)(details[1:])
	except:
		hello=''
finalprice=str(price)
notifier = ToastNotifier()
message = "the message is="+finalprice
notifier.show_toast(msg=message,duration=60)





 
time.sleep(5)
