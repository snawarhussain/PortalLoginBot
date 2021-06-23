from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


##<<<================================================>>>##

#enter the link to the website you want to automate login.
website_link=""
#enter your login username
username=""
#enter your login password
password=""

##<<<================================================>>>##
#enter the element for username input field
element_for_username="textfield"
#enter the element for password input field
element_for_password="textfield2"
#enter the element for submit button
element_for_submit="login_button"
##<<<================================================>>>###browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
#browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)	#uncomment this line,for chrome users
browser.get((website_link))	

#try:
browser.find_element_by_xpath("//span[@class='close']").click()
username_element = browser.find_element_by_name(element_for_username)
username_element.send_keys(username)		
password_element  = browser.find_element_by_name(element_for_password)
password_element.send_keys(password)
signInButton = browser.find_element_by_xpath("//a[@id='login_button']")
signInButton.click()
	
	#### to quit the browser uncomment the following lines ####
	# time.sleep(3)
	# browser.quit()
	# time.sleep(1)
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)
#except Exception:
	#### This exception occurs if the element are not found in the webpage.
#	print("Some error occured :(")
#	Exception
	#### to quit the browser uncomment the following lines ####
	# browser.quit()
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)