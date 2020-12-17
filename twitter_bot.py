from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="_YOUR_DRIVER_PATH_")
        self.username = "_TWITTER_USER_NAME_GOES_HERE_"
        self.password = "_TWITTER_PASSWORD_GOES_HERE_"
        self.webpage = "https://twitter.com/home"

    def sign_in(self):
        self.driver.get(self.webpage)
        print("connected to Twitter")
        time.sleep(1)
        print(">>> attempt to log in")
        time.sleep(1)
        print(">>> user input")
        time.sleep(1)
        user_input = self.driver.find_element_by_css_selector(
            "#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > "
            "div.css-1dbjc4n.r-13qz1uu > "
            "form > div > div:nth-child(6) > label > div > "
            "div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x.r-1inuy60.r-ou255f.r-vmopo1 > div > input")
        user_input.send_keys(self.username)
        print(">>> user entered")
        time.sleep(1)
        print(">>> password input")
        time.sleep(1)
        user_pass = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        user_pass.send_keys(self.password)
        print(">>> password entered")
        time.sleep(1)
        user_pass.send_keys(Keys.ENTER)
        print("wait...")
        time.sleep(5)

        print(">>> log in successful")

    def tweet(self, message):
        print(">>> compose tweet")
        compose_tweet = self.driver.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                      /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                      /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                      /div/div/div''')
        print(">>> bot.preparing msg")
        compose_tweet.send_keys(message)

        print(">>> click tweet")
        time.sleep(2)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_btn.click()
        print(">>> bot.message sent")

    def quit(self):
        self.driver.quit()
