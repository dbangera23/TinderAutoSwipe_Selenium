#!/usr/bin/env python3

import time

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Swiper():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")

    def fb_login(self):
        self.driver.get('https://www.facebook.com/')
        a = self.driver.find_element_by_id("0netrickp0ny0203@gmail.com")
        a.send_keys("")
        b = self.driver.find_element_by_id("741986532ffr")
        b.send_keys("")
        print("Password entered. Logging in.")
        c = self.driver.find_element_by_id('loginbutton')
        c.click()
        try:  # Check whether login was successful by finding the home button
            self.driver.find_element_by_id('u_0_c')
        except:
            return False
        return True

    def tinder_login(self):
        self.driver.get('http://tinder.com')
        time.sleep(5)
#        self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div/button/span/span").click()
#        print("done")
#        time.sleep(2)
        print("Clicking on sign in with Facebook.")
        self.driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[2]/div/div[3]/div[1]/button/span/span").click()
        print("done")
        time.sleep(2)
        print("Prompt 0")
        try:  # Selenium scripts open a testing environment in chrome. Every login acts like a brand new login. Must click through tutorial
            print("Dismissing tutorial prompts")
            self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/div[3]/button[1]/span/span").click()
            print("Prompt 1")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/div[3]/button[1]/span/span").click()
            print("Prompt 2")
            print("Ready to start swiping.")
            return True
        except:
            print('Something went wrong during login.')
            return False
        print("Ready to start swiping.")
        return True

    def swipe_tinder(self):
        actions = ActionChains(self.driver)
        time.sleep(30)
        print("Swipe until there are no more profiles.")
        try:
            # Stop swiping by catching the exception of not finding a profile. closes browser
            while self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[3]/div[1]"):
                actions.send_keys(Keys.ARROW_RIGHT).perform()
                time.sleep(2)
        except:
            time.sleep(20)
            try:
                while self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[3]/div[1]"):
                    actions.send_keys(Keys.ARROW_RIGHT).perform()
                    time.sleep(2)
            except:
                print("No more profiles found. Quitting.")
                self.driver.quit()

if __name__ == "__main__":
    swiper = Swiper()
    if(swiper.fb_login()):
        if swiper.tinder_login():
            swiper.swipe_tinder()
    else:
        print("Facebook login failed, Quitting")
        swiper.driver.quit()
