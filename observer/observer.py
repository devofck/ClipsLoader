import time
from selenium import webdriver
from observer.cookie_manager.Cookie import CookieManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Observer:
    driver = None

    def __init__(self):
        manager = CookieManager()

        self.driver = webdriver.Firefox()
        self.driver.get('https://www.tiktok.com/')
        for cookie in manager.get_actual_cookies('data.pkl'):
            self.driver.add_cookie(cookie)
        self.driver.get('https://www.tiktok.com/foryou')
        time.sleep(10)

    @staticmethod
    def check_likes(tiktok_element: WebElement):
        likes = tiktok_element.find_elements(By.CLASS_NAME, 'css-vc3yj-StrongText')[0].text
        # reduction to numeric form
        if 'K' in likes:
            if '.' in likes:
                likes = likes.split('.')[0] + '000'
            else:
                likes = likes.replace('K', '') + '000'
        elif 'M' in likes:
            if '.' in likes:
                likes = likes.split('.')[0] + '000000'
            else:
                likes = likes.replace('M', '') + '000000'
        return int(likes) >= 100000

    def scrolling(self):
        target_class = 'css-1cps6d6-BaseGridLayout-DivVerticalGridLayout'
        elements = self.driver.find_elements(By.CLASS_NAME, target_class)
        count = 0
        while True:
            for tiktok in elements:
                tiktok.location_once_scrolled_into_view
                time.sleep(3)
                count += 1
                if self.check_likes(tiktok):
                    print('OK')
            elements = self.driver.find_elements(By.CLASS_NAME, target_class)[count:]
