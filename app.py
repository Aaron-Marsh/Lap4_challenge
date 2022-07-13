from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import shortMethods as sm

url_list = [{'url': 'https://www.youtube.com/watch?v=pTFZFxd4hOI&t=582s&ab_channel=ProgrammingwithMosh', 'short_url': 'https://ltl-url.herokuapp.com/you-gyc'}]

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/shorten', methods = ['GET', 'POST'])
def short():
    if request.method == 'POST':
        new_url_pair = {'url': request.form['url']}
        # print(type(new_url_pair))
        # url_type = request.form['url-type']
        short_url = sm.shorten_url(request.form['url'])
        new_url_pair['short_url'] = short_url
        url_list.append(new_url_pair)

        return render_template('result.html')
    else:
        print('else')

@app.route('/url_list', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(url_list)
    # elif request.method == "POST":
        # new_url_pair = request.json
        # last_id = url_list[-1]['id']
        # new_url['id'] = last_id + 1
        # url_list.append(new_url)
        # return f"{new_url['name']} was created", 201
