#!/usr/bin/python3

# sudo apt-get install bottle
# server
from bottle import route, run
@route('/')
def home():
	return "It isn't fancy, but it's my home page"
run(host='localhost', port=9999)


# + index.html
# My <b>new</b> <i>home</i> page !!!
from bottle import route, run, static_file
@route('/')
def main():
	return static_file('index.html', root='.')
run(host='localhost', port=9999)

# URL connection
from bottle import route, run, static_file
@route('/')
def home():
	return static_file('index.html', root='.')
@route('/echo/<thing>')
def echo(thing):
	return "Say hello to my little friend: %s!" % thing
run(host='localhost', port=9999)

# bottle_test.py
import requests
resp = requests.get('http://localhost:9999/echo/Mothra')
if resp.status_code == 200 and \
   resp.text == 'Say hello to my little friend: Mothra!':
	print('It worked! That almost never happens!')
else:
	print('Argh, got this:', resp.text)


# sudo apt-get install flask
# server
from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def home():
	return app.send_static_file('index.html')
@app.route('/echo/<thing>')
def echo(thing):
	return "Say hello to my little friend: %s" % thing
app.run(port=9999, debug=True)

# templates/flask2.html
#<html>
# <head>
#  <title>Flask2 Example</title>
# </head>
#  <body>
#   Say hello to my little friend: {{ thing }}
#   Alas, it just destroyed {{ place }}!
#  </body>
# </html>

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/echo/<thing>/<place>')
def echo(thing):
	return render_template('flask2.html', thing=thing, place=place)
app.run(port=9999, debug=True)

# http://localhost:9999/echo?thing=Gorgo&place=Wilmerdingls
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/echo/')
def echo():
	thing = request.args.get('thing')
	place = request.args.get('place')
	return render_template('flask3.html', thing=thing, place=place)
app.run(port=9999, debug=True)
