from flask import Flask, request

from src.models.bots.bot import Bot

app = Flask(__name__)
app.secret_key = "jose"

@app.route('/instapaper', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        Bot().post_message()
    if request.method == 'GET':
        Bot().post_message()


if __name__ == '__main__':
    app.run(port=4999, debug=True)