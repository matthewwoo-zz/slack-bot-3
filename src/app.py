from flask import Flask, request

from src.errors import Error
from src.models.bots.bot import Bot

app = Flask(__name__)
app.secret_key = "123"
# app.config.from_object('config')

from src.models.bots.views import bot_blueprint
app.register_blueprint(bot_blueprint, url_prefix="/bot")

if __name__ == '__main__':
    app.run(port=4999, debug=True)


# token=4wZgtfCemPr0FCHdl9DKgObD&team_id=T1042HMJB
# team_domain=929broderick&\
# service_id=34895149248&\
# channel_id=C103W0BRC&channel_name=general&\
# timestamp=1460758091.000022&\
# user_id=U103W08NA&\
# user_name=matthew\
# text=instapaper&trigger_word=instapaper