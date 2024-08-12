from flask import Flask, render_template, request
from gemini import user_chat_response
from waitress import serve
import requests
import os
import re


app = Flask(__name__)

@app.route('/')
@app.route('/index',methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)

def get_Chat_response(text):
    out =  user_chat_response(text)
    out = re.sub(r'\n',r'<br />',out)
    out = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', out)
    return out

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000) # Need Waitess to serve the file/ server