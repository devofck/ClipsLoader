import pickle


class CookieManager:
    directory_path = None

    def __init__(self, path='cookie'):
        self.directory_path = path

    def get_actual_cookies(self, filename) -> dict:
        with open(self.directory_path + '\\' + filename, 'rb') as data:
            return pickle.load(data)
