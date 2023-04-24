from flask import Flask, render_template, request, session
from chatbot import *
import openai
from twilio.twiml.messaging_response import MessagingResponse


openai.api_key = "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"

app = Flask(__name__)
app.secret_key = os.urandom(24)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)


@app.route("/", methods=["POST","GET"])
def index():
    if "chat_log" not in session:
        session["chat_log"] = None

    chatgpt_response = ""
    
    if request.method == "POST":
        user_input = request.form.get("user_input","none")
        chatgpt_response, session["chat_log"] = askgpt(user_input, session["chat_log"])

    return render_template("index.html", chatgpt_response=chatgpt_response)


@app.route("/sms", methods=["POST"])
def bot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')

    answer, chat_log = askgpt(incoming_msg, chat_log)
    session['chat_log'] = chat_log

    r = MessagingResponse()
    r.message(answer)
    return str(r)









