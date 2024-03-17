from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle

from config import *

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
    
def testLogin(uname):
    driver.get(tweet_url)
    
    cookies = pickle.load(open("logs/cookies" + str(uname) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    driver.refresh()
    #print(driver.get_cookies())


def main():
    testLogin("josiah_bar16596")
    

if __name__ == "__main__":
    main()