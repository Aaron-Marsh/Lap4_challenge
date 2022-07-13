from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import Methods.shortMethods as sm

url_list = [{'url': 'https://www.youtube.com/watch?v=pTFZFxd4hOI&t=582s&ab_channel=ProgrammingwithMosh', 'short_url': 'you-gyc'}]

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/shorten', methods = ['GET', 'POST'])
def short():
    if request.method == 'POST':
        new_url_pair = {'url': request.form['url']}
        # print(type(new_url_pair))
        # url_type = request.form['url-type']
        if request.form['url-type'] == 'ltl-url':
            short_url = sm.shorten_url(request.form['url'])
        elif request.form['url-type'] == '4Letters':
            short_url = sm.gen_rand_word()
        elif request.form['url-type'] == 'sillySentence':
            short_url = sm.sillystring()


        new_url_pair['short_url'] = short_url
        url_list.append(new_url_pair)

        return render_template('result.html', url = new_url_pair['url'], short_url = short_url)
    else:
        print('else')

@app.route('/url_list', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(url_list)
 

@app.route('/<string:user_short_url>')
def redirect_url(user_short_url):
    try:
        for i in url_list:
            if user_short_url == i['short_url']:
                return redirect(i['url'], code=302)

        return render_template('notfound.html', short_url = user_short_url)
        # print('*****************************\n\n')
        # url_pair = next(pair for pair in url_list if pair['short_url'] == user_short_url)
        # print(url_pair)
        
    except:
        raise Exception(f'We do not have a url: {user_short_url}')
