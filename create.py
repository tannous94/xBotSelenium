from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.funcaptchaproxyless import *
import time
import pickle
import random

from names import names
from config import *

ad_block_path = r"D:\xBotTwitter\5.20.0_0"

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("detach", True)
options.add_argument("load-extension=" + ad_block_path)
options.add_argument("--start-maximized")

email_driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=options)

# this is to allow time to close adblocker tab -_-
time.sleep(4)

def createAcc():
    first_name = names[random.randint(2, 505)]
    sur_name = names[random.randint(2, 505)]
    user_uname = first_name + " " + sur_name
    user_passwd = "T159753t"

    driver.get("https://x.com")
    email_driver.get("https://generator.email/")

    WebDriverWait(email_driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='email_ch_text']")))
    email = email_driver.find_element(By.XPATH, "//span[@id='email_ch_text']").text

    # accept all cookies - if needed in some countries
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, lower_bar_xpath)))
    bottom_bar = driver.find_elements(By.XPATH, lower_bar_xpath)
    buttons_in_bottom = bottom_bar[0].find_elements(By.XPATH, accept_cookies_xpath)
    buttons_in_bottom[0].click()

    signup = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='signupButton']")))
    signup.click()
    
    fname = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
    fname.send_keys(user_uname)
    
    # this is for USA - or some other countries - switch between email and phone
    # driver.find_elements(By.XPATH, "//div[@role='button']")[1].click()
    # driver.implicitly_wait(2)
    
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
    driver.implicitly_wait(2)

    month = Select(driver.find_elements(By.XPATH, "//select")[0])
    month.select_by_index(random.randint(2,11))
    driver.implicitly_wait(2)

    day = Select(driver.find_elements(By.XPATH, "//select")[1])
    day.select_by_index(random.randint(2,26))
    driver.implicitly_wait(2)

    year = Select(driver.find_elements(By.XPATH, "//select")[2])
    year.select_by_index(random.randint(27,35))

    time.sleep(1)
    signupnext = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='ocfSignupNextLink']")))
    signupnext.click()

    # Next before captcha - also if needed in some countries
    nextmore = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='ocfSettingsListNextButton']")))
    nextmore.click()

    # waits for captcha and code arrival
    time.sleep(10)
    email_driver.find_elements(By.TAG_NAME, "button")[2].click() 
    code = email_driver.find_elements(By.TAG_NAME, "h1")[0].get_attribute("innerHTML").split(" ")[0]

    while not code.isnumeric():
        time.sleep(10)
        email_driver.find_elements(By.TAG_NAME, "button")[2].click() 
        code = email_driver.find_elements(By.TAG_NAME, "h1")[0].get_attribute("innerHTML").split(" ")[0]

    driver.find_element(By.XPATH, "//input[@name='verfication_code']").send_keys(code)
    time.sleep(1)
    driver.find_elements(By.XPATH, "//div[@role='button']")[1].click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(user_passwd)

    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']").click()

    # picture upload you can change the send_keys value to any path of file you want
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']")))
    driver.find_element(By.XPATH, "//input[@data-testid='fileInput']").send_keys(r"C:\Users\Tannous\Pictures\5516.jpg")

    apply = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='applyButton']")))
    apply.click()

    upload = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='ocfSelectAvatarNextButton']")))
    upload.click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
    uname = driver.find_element(By.XPATH, "//input[@name='username']").get_attribute("value")
    f = open("accs.txt", "a")
    f.write(f"{uname}\n")
    f.close()

    # saving cookies for login session in order to use them later without logging in
    pickle.dump(driver.get_cookies() , open("logs/cookies" + str(uname) + ".pkl","wb"))
   

def main():
    createAcc()
    

if __name__ == "__main__":
    main()