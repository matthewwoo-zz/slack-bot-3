import requests
import src.common.constants as InstaContants


class Article(object):
    def __init__(self, url=None, email=None, psw=None):
        self.url = "" if url is None else url
        self.email = InstaContants.INSTAEMAIL if email is None else email
        self.psw = InstaContants.INSTAPASSWORD if psw is None else psw

    def save_to_instapaper(self, url):
        requests.post("https://www.instapaper.com/api/add", data=self.json(url))

    def json(self, url):
        return {
            "username": self.email,
            "password": self.psw,
            "url": url
        }


