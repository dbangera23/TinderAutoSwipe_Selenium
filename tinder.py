import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
print("Opened facebook. Please enter username")
a = driver.find_element_by_id('email')
a.send_keys(input())
print("Email Id entered. Please enter password")
b = driver.find_element_by_id('pass')
b.send_keys(input())
print("Password entered...")
c = driver.find_element_by_id('loginbutton')
c.click()
driver.get('http://tinder.com')
print("Facebook Login complete. lets go to tinder")
time.sleep(5)
print("Clicking on sign into facebook")
driver.find_element_by_xpath("//*[@id=\"modal-manager\"]/div/div/div[2]/div[1]/div/div[3]/button[1]/span").click();
time.sleep(2)
try:
    print("Clicking on tutorial prompts")
    driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div[1]/div[1]/div/button/span/span").click()
    print("Prompt 1")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/main/div/button/span/span").click()
    print("Prompt 2")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]/span/span").click()
    print("Prompt 3")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]/span/span").click()
    print ("Prompt 4")
except:
    pass
print("Should be ready to start swiping")
actions = ActionChains(driver)
time.sleep(5)
print("Swipe till there are no more profiles")
try:
    #Stop swiping by catching the exception of not finding a profile. closes browser
    while driver.find_element_by_xpath("//*[@id=\"content\"]/div/span/div/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[3]/div[1]"):
        time.sleep(2)
        actions.send_keys(Keys.ARROW_RIGHT)
except:
    print("No more profile found. Quitting")
    driver.quit()

