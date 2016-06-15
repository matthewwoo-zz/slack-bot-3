import calendar
import json
import re
import time
import urllib2
import uuid

from datetime import datetime
import time

import requests
from slackclient import SlackClient
import src.common.constants as BotConstants
from src.models.articles.article import Article


class Bot(object):
    def __init__(self, bot_token=BotConstants.TOKEN,
                 bot_username=BotConstants.BOTNAME,
                 session_id=None,
                 channel_id=None,
                 reply_user_id=None,
                 reply_user_name=None):
        self.bot_token = bot_token
        self.username = bot_username
        self.session_id = uuid.uuid4() if session_id is None else session_id
        self.channel_id = channel_id if channel_id is not None else BotConstants.CHANNEL
        self.reply_user_id = reply_user_id if reply_user_id is not None else BotConstants.REPLY_USER_ID
        self.reply_user_name = reply_user_name if reply_user_name is not None else BotConstants.REPLY_USER_NAME


    def query_wit(self, text=None):
        if text == '':
            self.get_messages()
            return 200
        elif 'article' in text or 'articles' in text:
            self.get_messages()
            return 200
        else:
            text = text.encode('utf-8')
        encode_text = urllib2.quote(text)
        data_url = 'https://api.wit.ai/converse?v=20160330&session_id={}&q={}'.format(self.session_id, encode_text)
        data = requests.post(data_url, headers=BotConstants.WIT_HEADERS)
        json_data = json.loads(data.text)
        if 'datetime' in json_data['entities']:
            start_time = json_data['entities']['datetime'][0]['value']
            start_time = calendar.timegm(datetime.strptime(start_time[:23], '%Y-%m-%dT%H:%M:%S.%f').timetuple())
            self.get_messages(channel=self.channel_id, start_time=start_time)
        else:
            self.fail_message()
        return 200

    def success_message(self, num_articles):
        sc = SlackClient(self.bot_token)
        sc.api_call(
            "chat.postMessage", channel=self.channel_id,
            text="Hello <@{}|{}> just grabbed {} new articles for you :newspaper:!".format(self.reply_user_id, self.reply_user_name, num_articles),
            username=self.username, as_user="false", icon_emoji=':instapaper:'
        )
        return 200

    def fail_message(self):
        sc = SlackClient(self.bot_token)
        sc.api_call(
            "chat.postMessage", channel=self.channel_id,
            text="Sorry <@{}|{}> not sure if I can do that".format(self.reply_user_id, self.reply_user_name),
            username=self.username, as_user="false", icon_emoji=':instapaper:')
        return 200

    def get_messages(self, channel=None, start_time=None):
        channel = self.channel_id if channel is None else channel
        sc = SlackClient(self.bot_token)
        if start_time == None:
            json_data = sc.api_call("channels.history", channel=channel, count=10)
        else:
            json_data = sc.api_call("channels.history", channel=channel, oldest=start_time)
        message_dump = json.dumps(json_data)
        message_dict = json.loads(message_dump)
        num_articles = 0
        for msg in message_dict['messages']:
            if 'attachments' in msg:
                x = msg['attachments'][0]['from_url']
                Article().save_to_instapaper(url=x)
                print x
                num_articles += 1
        return self.success_message(num_articles=num_articles)


    def get_links(self):
        pass

    def json(self):
        return