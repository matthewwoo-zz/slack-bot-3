import requests
import src.common.constants as UserConstants

class User(object):
    def __init__(self, username=None, password=None):
        self.username = UserConstants.INSTAUSERNAME if username is not None else username
        self.password = UserConstants.INSTAPASSWORD if password is not None else password

    def add_article_to_instapaper():
        resp = requests.post("https://www.instapaper.com/api/add", {"username": UserConstants.INSTAEMAIL,
                                                                    "password": UserConstants.INSTAPASSWORD,
                                                                    "url": UserConstants.INSTAURL
                                                                    })
        print resp.status_code
        print resp.headers
        print resp.json()

    def save_to_mongo(self):
        pass







