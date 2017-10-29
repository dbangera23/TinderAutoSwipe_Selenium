# TinderAutoSwipe_Selenium

Script set up to automatically swipe right on tinder.com

## Installation/Requirements

This app utilizes Python3, Selenium, and Chrome.

Python3 can be found here:
https://www.python.org/downloads/

Selenium can be found here:
http://www.seleniumhq.org/download/

A Chrome webdriver will be required with Selenium. This can be found here:
https://sites.google.com/a/chromium.org/chromedriver/downloads

## Usage

The code is set up to first start up facebook and allow user input for your facebook username and password.
After a sign in then it will go to tinder and attempt a sign in. Which should sign in if the facebook sign in worked.
Once signed into tinder since selenium starts up a testing environment we have to go through the tutorial every time.
After which the app swipes until it doesn't see a profile. At which point the script quits and closes the browser.
