from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

from config import *

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("detach", True)

########################################################################################################
## THIS IS MOSTLY NOT NEEDED CAUSE WE ALREADY SAVE SESSION WHEN CREATING
## IF ACCOUNTS STOP WORKING AFTER A WHILE JUST CREATE NEW ONES
## WITH create.py
########################################################################################################
# Creates a login session for specific account and save its cookies
def createLoginSession(user_uname, user_passwd):
    driver_login = webdriver.Chrome(options=options)
    driver_login.get(twitter_login_page)

    WebDriverWait(driver_login, 20).until(EC.element_to_be_clickable((By.XPATH, uname_xpath)))
    username = driver_login.find_element(By.XPATH, uname_xpath)
    username.send_keys(user_uname)

    WebDriverWait(driver_login, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
    all_buttons = driver_login.find_elements(By.XPATH, next_button_xpath)
    all_buttons[-2].click()

    WebDriverWait(driver_login, 20).until(EC.element_to_be_clickable((By.XPATH, passwd_xpath)))
    passwd = driver_login.find_element(By.XPATH, passwd_xpath)
    passwd.send_keys(user_passwd)

    WebDriverWait(driver_login, 20).until(EC.element_to_be_clickable((By.XPATH, login_xpath)))
    login_button = driver_login.find_elements(By.XPATH, login_xpath)
    login_button[-1].click()

    WebDriverWait(driver_login, 30).until(EC.element_to_be_clickable((By.XPATH, lower_bar_xpath)))
    bottom_bar = driver_login.find_elements(By.XPATH, lower_bar_xpath)
    buttons_in_bottom = bottom_bar[0].find_elements(By.XPATH, accept_cookies_xpath)
    buttons_in_bottom[0].click()

    pickle.dump(driver_login.get_cookies() , open("logs/cookies" + str(user_uname) + ".pkl","wb"))
    driver_login.close()
    driver_login.quit()
