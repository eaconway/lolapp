import os
import requests
import random

from services import *

from flask import Flask, jsonify, render_template, request #used for subbing html elements
from flask_debugtoolbar import DebugToolbarExtension
from pprint import pprint

RIOT_API_KEY = os.environ["RIOT_API_KEY"]
DEBUG = 'PROD' not in os.environ

example_text = """Iceman2163 joined the lobby
Icegirl2163 joined the lobby
Imaqtpie joined the lobby
Vincent joined the lobby"""

app = Flask(__name__)

app.secret_key = os.environ['FLASK_SECRET_KEY']
app.debug = DEBUG
toolbar = DebugToolbarExtension()
toolbar.init_app(app)


# TODO: replace this
def get_summoners(summoner_names):
    ROLES = {'ADC', 'Support', 'Mid', 'Jungle', 'Top'}
    summoners = []
    for name in summoner_names:
        primary_role = random.choice(list(ROLES))
        secondary_role = random.choice(list(ROLES - {primary_role}))
        summoner = {
            'name': name,
            'level': random.randint(10,40),
            'primaryRole': primary_role,
            'secondaryRole': secondary_role,
        }
        summoners.append(summoner)
    return summoners

@app.route('/', methods=['GET', 'POST'])
def home():
    context = dict()
    if request.method=='POST':
        lobby_text = request.form.get('lobby_text', '')
        context['lobby_text'] = lobby_text
        parsed_names = parse_text(lobby_text)
        if parsed_names:
            summoners = get_summoners(parsed_names)
            context['summoners'] = summoners
    return render_template('index.html', **context)

if __name__ =='__main__':
    app.run()
