from flask import Blueprint, request

from src.models.bots.bot import Bot
import src.errors as Error

bot_blueprint = Blueprint('bots', __name__)

@bot_blueprint.route('/instapaper', methods=['POST'])
def get_instapaper_information():
    try:
        channel = request.form['channel_id']
        user_id = request.form['user_id']
        user = request.form['user']

        print channel
        print user_id
        print user

    except:
        raise Error.ParameterError("Parameters are not correct")

    try:
        print request.get_data()
        Bot(channel_id=channel, reply_user_id=user_id, reply_user_name=user).post_message()
    except:
        pass

    print request.get_data()

    return ('', 200)


# @bot_blueprint.route('/instapaper', methods=['POST'])
# def get_instapaper_information():
#     if request.method == 'POST':
#         print request.get_data()
#         channel = request.form['channel_id']
#         token = request.form['token']
#         channel = request.form['channel_id']
#         user_id = request.form['user_id']
#         user = request.form['user']
#
#
#         # Bot(channel_id=channel, reply_user_id=user_id, reply_user_name=user).post_message()
#     return ('', 200)

