import json
import re
import time

import datetime as datetime
from slackclient import SlackClient
import src.common.constants as BotConstants


class Bot(object):
    def __init__(self, bot_token=BotConstants.TOKEN,
                 bot_username=BotConstants.BOTNAME,
                 channel_id=None,
                 reply_user_id=None,
                 reply_user_name=None):

        self.bot_token = bot_token
        self.username = bot_username
        self.channel_id = channel_id if channel_id is not None else BotConstants.CHANNEL
        self.reply_user_id = reply_user_id if reply_user_id is not None else BotConstants.REPLY_USER_ID
        self.reply_user_name = reply_user_name if reply_user_name is not None else BotConstants.REPLY_USER_NAME

    #2016-04-16_update
    # def __repr__(self):
    #     print "{}, {}".format(self.token, self.username)

    def post_message(self):
        sc = SlackClient(self.token)
        sc.api_call(
            "chat.postMessage", channel=self.channel_id, text="Hello <{}> from Python!".format(self.reply_user_id),
            username=self.username, as_user="false", icon_emoji=':robot_face:'
        )

    def get_mesages(self, start_time=None):
        self.start_time = datetime.time() - datetime.timedelta(days=1) if start_time is None else start_time
        sc = SlackClient(self.token)
        x = sc.api_call("channels.history", channel=BotConstants.CHANNEL, oldest = start_time)
        print x

    def json(self):
        return



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
