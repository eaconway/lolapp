import os
import requests

from services import *

from flask import Flask, jsonify, render_template, request #used for subbing html elements
from pprint import pprint

RIOT_API_KEY = os.environ["RIOT_API_KEY"]

example_text = """Iceman2163 joined the lobby
Icegirl2163 joined the lobby
Imaqtpie joined the lobby
Vincent joined the lobby"""

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	context = dict()
	if request.method=='POST':
		##lobby_text = request.form['lobby_text']
		parsed_names = parse_text(example_text)
		#url = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(summoner_name, RIOT_API_KEY)
		#response = requests.get(url)
		#user_data = response.json()
		#context["summoner_names"]=user_data
		get_data(parsed_names[0])
		#for name in parsed_names:
		#	get_data(name)
		context["summoner_names"]=parsed_names

	return render_template('index.html', **context)

if __name__ =='__main__':
	app.run(debug=True)
