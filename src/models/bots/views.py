from flask import Blueprint, request

from src.models.bots.bot import Bot
import src.errors as Error

bot_blueprint = Blueprint('bot', __name__)

@bot_blueprint.route('/instapaper', methods=['POST'])
def get_instapaper_information():
    def get_instapaper_information():
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
        return ('', 200)


