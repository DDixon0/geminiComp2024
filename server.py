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
    # out = rep.replace('\n', '<br />')
    out = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', out)
    # print(out)
    return out
# @app.route('/sigma')
# def sigma():
#     return render_template('sigma.html')


#Handaling a route for requests 
# @app.route('/page')
# def get_data():
#     info = request.args.get('_____')
#     response_data = user_query_gemini(info)
#     handle the case where the querey response was not what we expected

#     return render_template(
#         "site.html",
#         item1=response_data['one'],
#         item2=response_data['two']['second'])

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000) # Need Waitess to serve the file/ server