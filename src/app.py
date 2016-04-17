from flask import Flask, request

from src.errors import Error
from src.models.bots.bot import Bot

app = Flask(__name__)
app.secret_key = "123"
# app.config.from_object('config')

# from src.models.bots.views import bot_blueprint
# app.register_blueprint(bot_blueprint, url_prefix="/bot")
@app.route("/bot_call", methods=['POST'])
def get_channel_info():
    if request.method == 'POST':
        try:
            channel = request.form['channel_id']
            user_id = request.form['user_id']
            user = request.form['user_name']
        except:
            raise Error.ParameterError("Parameters are not correct")
        try:
            Bot(channel_id=channel, reply_user_id=user_id, reply_user_name=user).post_message()
        except:
            raise Error.MessageError("Message is incorrect")
        return (get_messages(channel), 200)

def get_messages(channel):
    Bot().get_last_messages(channel)


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