import pathlib
import pickle
from selenium import webdriver

#chrome_driver_path = "C:\Program Files (x86)\chromedriver.exe"
chrome_driver_path = str(pathlib.Path.cwd() / 'chromedriver.exe')
import time
import random
from secrets import fb_username,fb_password, phone_number

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)


    def save_cookies(self):
        with open("cookies.pkl",'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)


    def load_cookies(self):
        with open("cookies.pkl", 'rb') as cookies_file:
            cookies = pickle.load(cookies_file)
            for cookie in cookies:
                print(cookie)
                self.driver.add_cookie(cookie)


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


    def manual_login(self):

        print("logging in to tinder...")

        self.driver.get('https://tinder.com')

        # open login menu
        initial_login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        initial_login_btn.click()

        # account for latency
        time.sleep(.5)

        # login with phone number
        phone_number_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        phone_number_btn.click()

        # Hang until user input
        input("This is a placeholder until a method to defeat captcha is found\nPress ENTER when done.")

        print("saving cookies...")
        self.save_cookies()

        print("Done.")


    def like(self):
        self.driver.get('https://tinder.com/app/recs')
        time.sleep(.5)
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        #self.driver.get('https://tinder.com/app/recs')
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()


    def auto_swipe(self):
        now = time.time()
        future = now + 15
        while time.time() < future:
            time.sleep(.5)
            decider = random.randint(1,11)
            if decider < 10:
                self.like()
            else:
                self.dislike()
            pass



    def handle_match_popup(self):
        self.driver.get('https://tinder.com/app/recs')
        popup_close_btn = self.driver.find_element_by_xpath('')
        popup_close_btn.click()

if __name__ == '__main__':
    bot = TinderBot()
    bot.manual_login()
"""
    try:
        bot.auto_swipe()
    except(Exception):
        bot.manual_login()
    bot.like()
    #bot.auto_swipe()
"""