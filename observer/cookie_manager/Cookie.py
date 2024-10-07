import os


class CookieManager:
    directory_path = None

    def __init__(self, path='cookie'):
        self.directory_path = path

    @staticmethod
    def convert_cookies(self):
        path = os.getcwd() + '\\cookie'
        files = os.listdir(path)
        for file in files:
            if file.title().lower().startswith('cookie'):
                # convert
                print(file.title())
                cookie_file = open(path + '\\' + file.lower().title(), 'r')
                cookies = cookie_file.readlines()
                print(cookies)
