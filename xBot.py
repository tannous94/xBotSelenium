from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

from login import *
from config import *
from accounts import usernames
from accounts import passwords

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
    
def likeTweet(uname):
    driver.get(tweet_url)

    cookies = pickle.load(open("logs/cookies" + str(uname) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    driver.refresh()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, like_xpath)))
    like = driver.find_elements(By.XPATH, like_xpath)
    like[0].click()


def retweetTweet(uname):
    driver.get(tweet_url)

    cookies = pickle.load(open("logs/cookies" + str(uname) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    driver.refresh()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, retweet_xpath)))
    retweet = driver.find_elements(By.XPATH, retweet_xpath)
    retweet[0].click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, confirm_retweet_xpath)))
    repost = driver.find_element(By.XPATH, confirm_retweet_xpath)
    repost.click()


def commentTweet(uname):
    driver.get(tweet_url)

    cookies = pickle.load(open("logs/cookies" + str(uname) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    driver.refresh()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, reply_textbox_xpath)))    
    comment = driver.find_element(By.XPATH, reply_textbox_xpath)
    comment.send_keys("NIICE")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, reply_button_xpath)))  
    type_comment = driver.find_element(By.XPATH, reply_button_xpath)
    type_comment.click()


def follow(uname):
    driver.get(twitter_page)

    cookies = pickle.load(open("logs/cookies" + str(uname) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    driver.refresh()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, follow_button_xpath)))
    follow_me = driver.find_element(By.XPATH, follow_button_xpath)
    follow_me.click()


def main():
    
    for j in range(40, max_accounts):
        #createLoginSession(usernames[j], passwords[j])
        pass

    for i in range(max_reaction):
        #likeTweet(usernames[i])
        #retweetTweet(usernames[i])
        #commentTweet(usernames[i])
        #follow(usernames[i])
        pass
    

if __name__ == "__main__":
    main()