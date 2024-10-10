import os
import requests
import random
import pickle
import observer.cookie_manager.Cookie


class Downloader:
    link = None

    def __init__(self, link):
        self.link = link

    def download_video(self, cookies: list[dict]):
        path = os.getcwd() + '\\' + 'download_master' + '\\' + 'downloaded\\' + str(random.randint(1000000, 9999999)) + '.mp4'
        agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'}
        req = requests.Session()
        for cookie in cookies:
            req.cookies.set(
                name=cookie['name'],
                value=cookie['value'],
            )
        response = req.get(
            self.link,
            headers=agent
        )

        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)
            print('File downloaded successfully')
            return path
        else:
            print('Failed to download file')
            return None

