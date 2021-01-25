"""
TODO:
-----
1. Handle "It's a match" pop-ups
    > reference: https://www.youtube.com/watch?v=lvFAuUcowT4&list=PLEJ0LJh1b0EFxzszGPiWj806N9UinPR6U&index=4&ab_channel=CodeDripbyAaronJack @ 9:00
2. implement spawn_chatbot_instance()
    > research threading in Python

"""


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


    def open_page(self):
        self.load_cookies()
        self.driver.get('https://tinder.com/app/recs')


    def like(self):
        #self.driver.get('https://tinder.com/app/recs')
        time.sleep(.5)
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        #self.driver.get('https://tinder.com/app/recs')
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()


    def auto_swipe(self):
        swipes = 0
        liked = 0
        disliked = 0
        matches = 0

        now = time.time()
        future = now + 15
        while time.time() < future:
            #sleep_time = random.randint(1,4)
            # time.sleep(sleep_time)
            time.sleep(.5)
            decider = random.randint(1,11)
            try:
                if decider < 10:
                    self.like()
                    liked += 1
                    print()
                else:
                    self.dislike()
                    disliked += 1

                print("liked/disliked appropriately.")
                swipes += 1
                pass
            except(Exception):
                try:
                    self.handle_match_popup()
                    print("handled a match...")
                    matches += 1
                except:
                    try:
                        self.handle_super_like_popup()
                        print("handled a super like")
                    finally:
                        self.handle_TinderOnHomescreen_popup()
        print(f'swipes total: {swipes}\nliked: {liked}\ndisliked: {disliked}\nmatches: {matches}')





    def handle_match_popup(self):
        # self.driver.get('https://tinder.com/app/recs')
        popup_close_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
        popup_close_btn.click()

    def handle_super_like_popup(self):
        sl_popup_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[1]')
        sl_popup_btn.click()


    def handle_TinderOnHomescreen_popup(self):
        try:
            toh_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            toh_btn.click()
        except:
            print("clicked outside screen")
            outside_screen = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div')
            outside_screen.click()


    def interactive(self):
        while True:
            print("[1] Iterate autolike")
            print("[2] Message a sucka")
            print("[3] Exit")
            choice = input("> ")
            if choice == "1":
                while True:
                    try:
                        bot.auto_swipe()
                    finally:
                        print("~~~ Follow the stack trace, neo... ~~~")

                    cont = input("Auto-swipe again? y/n")
                    if cont.lower() != 'y':
                        break
            elif choice == "2":
                self.check_messages()
            elif choice == "3":
                exit()
            else:
                print("Invalid input!")


    def check_messages(self):
        # click into messages tab
        messages_tab = self.driver.find_element_by_xpath('//*[@id="messages-tab"]')
        messages_tab.click()

        message_list = self.driver.find_element_by_xpath('//*[@id="matchListWithMessages"]/div[2]')
        messages = self.driver.find_elements_by_class_name('messageListItem D(f) Ai(c) Pos(r)--s BdB--s Bdbc($c-divider) focus-background-style messageListItem--isNew')
        for message in messages:
            name = message.find_elements_by_class_name('messageListItem__name Fw($semibold) M(0)')
            print(name)


        # click out of messages when finished.
        # matches_tab = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
        # matches_tab.click()

    def spawn_chatbot_instance(self):
        ### IN PROGRESS ###
        # in: https://tinder.com/app/recs
        #
        message_list = self.driver.find_element_by_xpath('//*[@id="matchListWithMessages"]/div[2]')
        # list message opportunities
        # (at first) for the first five -- spawn off a chatbot thread




if __name__ == '__main__':
    bot = TinderBot()
    bot.manual_login()
    bot.interactive()
"""
    while True:
        try:
            bot.auto_swipe()
        finally:
            print("~~~ Follow the stack trace, neo... ~~~")

        cont = input("Continue? y/n")
        if cont.lower() != 'y':
            break
"""