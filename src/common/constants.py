
import os

TOKEN = os.environ.get('TOKEN')
USERNAME = os.environ.get('USERNAME')
CHANNEL = os.environ.get('CHANNEL')
BOTNAME = os.environ.get('BOTNAME')
REPLY_USER_ID = os.environ.get('REPLY_USER_ID')
REPLY_USER_NAME = os.environ.get('REPLY_USER_NAME')
WIT_HEADERS = {'Authorization': '{}'.format(os.environ.get('WIT_TOKEN'))}


