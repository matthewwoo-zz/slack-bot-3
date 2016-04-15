import json
import re
import time
from slackclient import SlackClient
import src.common.constants as BotConstants


class Bot(object):
    def __init__(self, token=None, username=None):
        self.token = BotConstants.TOKEN if token is None else None
        self.username = BotConstants.BOTNAME if username is None else None

    def __repr__(self):
        print "{}, {}".format(self.token, self.username)

    def post_message(self):
        sc = SlackClient(self.token)
        print sc.api_call("api.test")
        sc.api_call(
            "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
            username=self.username, as_user="false", icon_emoji=':robot_face:'
        )

    # def get_mesages(self):
    #     sc = SlackClient(self.token)
    #     sc.api_call("channels.history", channel=BotConstants.CHANNEL, count=100)
    #
    #     pass
    #
    #     '''
    #     pass list of json urls
    #     '''


    # def read(self):
    #     sc = SlackClient(self.token)
    #     if sc.rtm_connect():
    #         while True:
    #             new_evts = sc.rtm_read()
    #             for evt in new_evts:
    #                 try:
    #                     text = evt['text']
    #                 except:
    #                     pass
    #                 try:
    #                     pattern = re.compile(".{}.".format(username))
    #                     match = pattern.search(text)
    #                     user = match.group()
    #                     if user == BotConstants.USERNAME2:
    #                         Bot().post_message()
    #                 except:
    #                     pass
    #             time.sleep(1)
    #     else:
    #         print "Connection failed"
