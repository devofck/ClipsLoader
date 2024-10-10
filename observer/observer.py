import sys
import time
from selenium import webdriver
from observer.cookie_manager.Cookie import CookieManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from download_master.downloader import Downloader
from database.logic import Database

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
    def get_video_link(tiktok_element: WebElement):
        video_element = tiktok_element.find_element(By.TAG_NAME, 'video')
        return video_element.get_attribute('src')

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
        return int(likes)

    def scrolling(self):
        target_class = 'css-1cps6d6-BaseGridLayout-DivVerticalGridLayout'
        elements = self.driver.find_elements(By.CLASS_NAME, target_class)
        count = 0
        while True:
            for tiktok in elements:
                tiktok.location_once_scrolled_into_view
                time.sleep(3)
                count += 1
                likes = self.check_likes(tiktok)
                if likes > 100000:
                    print('OK')
                    link = self.get_video_link(tiktok)
                    downloader = Downloader(link)
                    path = downloader.download_video(self.driver.get_cookies())
                    base = Database()
                    base.add_video(path, likes)
            elements = self.driver.find_elements(By.CLASS_NAME, target_class)[count:]
