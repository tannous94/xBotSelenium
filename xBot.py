from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

from accounts import usernames
from accounts import passwords

########################################################################################
############################# Settings to Change #######################################
########################################################################################

twitter_login_page = "https://twitter.com/i/flow/login"
tweet_url = "https://twitter.com/RareApepesNFT/status/1741059055874088998"
twitter_page = "https://twitter.com/AntonioPhoenix5/"
max_reaction = 2
max_accounts = 2

##################################### CONSTANTS ########################################

uname_xpath = "//input[@type='text']"
next_button_xpath = "//div[@role='button']"
passwd_xpath = "//input[@type='password']"
login_xpath = "//div[@role='button']"
lower_bar_xpath = "//div[@data-testid='BottomBar']"
accept_cookies_xpath = "//div[@role='button']"
like_xpath = "//div[@data-testid='like']"
retweet_xpath = "//div[@data-testid='retweet']"
confirm_retweet_xpath = "//div[@data-testid='retweetConfirm']"
reply_textbox_xpath = "//div[@role='textbox']"
reply_button_xpath = "//div[@data-testid='tweetButtonInline']"
follow_button_xpath = "//div[@data-testid='placementTracking']"

########################################################################################

options = webdriver.ChromeOptions()
#this option will remove the message 'chrome is being controlled..'
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

#this will forbid it from closing immediately - can remove this if i want browser to exit after doing its goal!
options.add_experimental_option("detach", True)

#this will run the desired webpage - in this case twitter login page
driver = webdriver.Chrome(options=options)

def launchBrowser(user_uname, user_passwd, uid):
    if uid == 0:
        driver.close()
        driver.quit()
    driver_login = webdriver.Chrome(options=options)
    driver_login.get(twitter_login_page)

    #makes 1 second delay for the page to load in order to be able to get <input> tag
    driver_login.implicitly_wait(2)

    #finds the textbox for username and fills it with uname
    username = driver_login.find_element(By.XPATH, uname_xpath)
    username.send_keys(user_uname)

    #clicks on Next button
    all_buttons = driver_login.find_elements(By.XPATH, next_button_xpath)
    all_buttons[-2].click()

    #finds the textbox for password and fills it with password
    passwd = driver_login.find_element(By.XPATH, passwd_xpath)
    passwd.send_keys(user_passwd)

    #clicks on Login button
    login_button = driver_login.find_elements(By.XPATH, login_xpath)
    login_button[-1].click()

    driver_login.implicitly_wait(2)

    #this searches for the cookies and accepts them all
    #if uid == 0:
    bottom_bar = driver_login.find_elements(By.XPATH, lower_bar_xpath)
    buttons_in_bottom = bottom_bar[0].find_elements(By.XPATH, accept_cookies_xpath)
    buttons_in_bottom[0].click()

    #saving cookies - login credintials for faster login
    pickle.dump(driver_login.get_cookies() , open("cookies/cookies" + str(uid) + ".pkl","wb"))
    driver_login.close()
    driver_login.quit()

    
def likeTweet(uid):
    #don't know why but need to get page before and after loading cookies in order for the cookies to work
    driver.get(tweet_url)

    #loading cookies that were saved before
    cookies = pickle.load(open("cookies/cookies" + str(uid) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    #loading page again - either refresh or call same page
    #driver.get("https://twitter.com/SkeletonFamCNFT/status/1665426613532540928")
    driver.refresh()
  
    #waiting for the page to load
    driver.implicitly_wait(2)

    #this will click on the like button
    # the reason we use 0 as an index is because there are more than one like button in the page
    # and 0 simply means the first one which is usually the one for the main tweet
    like = driver.find_elements(By.XPATH, like_xpath)
    like[0].click()

    #waits 2 seconds in same spot
    #time.sleep(2)

    #closes browser
    #driver.close()


def retweetTweet(uid):
    #don't know why but need to get page before and after loading cookies in order for the cookies to work
    driver.get(tweet_url)

    #loading cookies that were saved before
    cookies = pickle.load(open("cookies/cookies" + str(uid) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    #loading page again - either refresh or call same page
    #driver.get("https://twitter.com/SkeletonFamCNFT/status/1665426613532540928")
    driver.refresh()
  
    #waiting for the page to load
    driver.implicitly_wait(2)

    #same idea as like
    retweet = driver.find_elements(By.XPATH, retweet_xpath)
    retweet[0].click()

    driver.implicitly_wait(2)

    #this will choose the repost option
    repost = driver.find_element(By.XPATH, confirm_retweet_xpath)
    repost.click()

    #waits 2 seconds in same spot
    time.sleep(2)

    #closes browser
    #driver.close()


def commentTweet(uid):
    #don't know why but need to get page before and after loading cookies in order for the cookies to work
    driver.get(tweet_url)

    #loading cookies that were saved before
    cookies = pickle.load(open("cookies/cookies" + str(uid) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    #loading page again - either refresh or call same page
    #driver.get("https://twitter.com/SkeletonFamCNFT/status/1665426613532540928")
    driver.refresh()
  
    #waiting for the page to load
    driver.implicitly_wait(2)

    #same idea as like
    comment = driver.find_element(By.XPATH, reply_textbox_xpath)
    comment.send_keys("NIICE")

    driver.implicitly_wait(2)

    type_comment = driver.find_element(By.XPATH, reply_button_xpath)
    type_comment.click()

    #waits 2 seconds in same spot
    time.sleep(2)

    #closes browser
    #driver.close()


def follow(uid):
    #don't know why but need to get page before and after loading cookies in order for the cookies to work
    driver.get(twitter_page)

    #loading cookies that were saved before
    cookies = pickle.load(open("cookies/cookies" + str(uid) + ".pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
        driver.add_cookie(cookie)

    #loading page again - either refresh or call same page
    #driver.get("https://twitter.com/SkeletonFamCNFT/status/1665426613532540928")
    driver.refresh()
  
    #waiting for the page to load
    driver.implicitly_wait(2)

    #same idea as like, 1 because the follow button is the 2nd and the index 0 (which is the 1st button) is something else
    follow_me = driver.find_element(By.XPATH, follow_button_xpath)
    follow_me.click()

    #waits 2 seconds in same spot
    time.sleep(2)

    #closes browser
    #driver.close()

###########################################################################################################################
    
#### NO NEEED FROM HERE / JUST FOR EDUCATION:
# not important, just prints out cookie in normal date format
def cookieRead():
    #don't know why but need to get page before and after loading cookies in order for the cookies to work
    driver.get(twitter_page)

    #loading cookies that were saved before
    cookies = pickle.load(open("cookies/cookies.pkl", "rb"))
    for cookie in cookies:
        expiry = cookie.get('expiry', None)
        if expiry:
            cookie['expiry'] = int(expiry * 1000)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expiry)))
        driver.add_cookie(cookie)

    #loading page again - either refresh or call same page
    #driver.get("https://twitter.com/SkeletonFamCNFT/status/1665426613532540928")
    driver.refresh()


def logout():
    #This doesn't work, and probably don't need, we can make the browser exit when it finishes it's faster :)
    logout = driver.find_element(By.XPATH, "//div[@data-testid='UserAvatar-Container-ConanCod1']")
    logout.click()


#from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get("http://www.google.com")

# Get cookies to a json file:
#Path('cookies.json').write_text(
#    json.dumps(driver.get_cookies(), indent=2)
#)

# retrieve cookies from a json file
#for cookie in json.loads(Path('cookies.json').read_text()):
#    driver.add_cookie(cookie)

#driver.quit()
################### UNTIL HERE ######################################

def main():
    # make mass logins to save their cookies
    for j in range(max_accounts):
        #launchBrowser(usernames[j], passwords[j], j)
        pass

    # then run any of the following methods for each operation:

    for i in range(max_reaction):
        #likeTweet(i)
        retweetTweet(i)
        #commentTweet(i)
        #follow(i)
        pass


    #cookieRead()
    
    #this doesn't work: (and not needed for now)
    #logout()
    

if __name__ == "__main__":
    main()