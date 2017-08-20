#!/usr/bin/env python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def static_page():
    return render_template('index.html')

@app.route('/', methods = ['GET'])
def api_respond():
    data = {'message':"This is a reply from Flask"}
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
