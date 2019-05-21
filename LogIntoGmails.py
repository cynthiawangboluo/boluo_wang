from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

usernameStr = 'Type your username here'
passwordStr = 'Type your password here'

# fill in username and hit the next button
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, 'password')))
password.send_keys(passwordStr)
signInButton = browser.find_element_by_xpath("//span[contains(text(), 'Next')]")
signInButton.click()

time.sleep(10) # sleep for 10 seconds so you can see the results
browser.quit()
