from flask import Flask, render_template, request
from gemini import user_query_gemini
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sigma')
def sigma():
    return render_template('sigma.html')


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