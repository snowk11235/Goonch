#import selenium
from selenium import webdriver
chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"

import time

from secrets import fb_username,fb_password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)

    def login_with_fb(self):
        self.driver.get('https://tinder.com')
        # self.driver.maximize_window()

        # open login menu
        initial_login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        initial_login_btn.click()

        #account for latency
        time.sleep(1)

        #login with facebook
        fb_login_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_login_btn.click()
        time.sleep(1)

        # switch to fb login pop-up
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        # proceed with fb pop-up login
        email_field = self.driver.find_element_by_xpath('//*[@id="email"]')
        pass_field = self.driver.find_element_by_xpath('//*[@id="pass"]')
        secondary_lgn_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')

        email_field.send_keys(fb_username)
        pass_field.send_keys(fb_password)
        secondary_lgn_btn.click()

        # switch back to base window
        self.driver.switch_to.window(base_window)

        #popup_1 = self.driver



if __name__ == '__main__':
    bot = TinderBot()
    bot.login_with_fb()