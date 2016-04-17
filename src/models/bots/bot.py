import json
import re
import time

import datetime as datetime
import time

import requests
from slackclient import SlackClient
import src.common.constants as BotConstants
from src.models.articles.article import Article


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
        sc = SlackClient(self.bot_token)
        sc.api_call(
            "chat.postMessage", channel=self.channel_id, text="Hello <@{}|{}> grabbing your instapaper links :newspaper:!".format(self.reply_user_id, self.reply_user_name),
            username=self.username, as_user="false", icon_emoji=':robot_face:'
        )

    def get_messages(self, channel, start_time=None):
        sc = SlackClient(self.bot_token)
        start_time = time.time()- 90061 if start_time is None else start_time
        json_data = sc.api_call("channels.history", channel=channel, oldest = start_time)
        message_dump =json.dumps(json_data)
        message_dict = json.loads(message_dump)
        for test in message_dict['messages']:
            print 'title_link' in test

    def get_last_messages(self, channel):
        sc = SlackClient(self.bot_token)
        json_data = sc.api_call("channels.history", channel=channel, count=10)
        message_dump = json.dumps(json_data)
        message_dict = json.loads(message_dump)
        for test in message_dict['messages']:
            if 'attachments' in test:
                x = test['attachments'][0]['from_url']
                Article().save_to_instapaper(url=x)
                print x


    def get_links(self):
        pass

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
