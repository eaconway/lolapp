import string, os
import requests
from flask import request

RIOT_API_KEY = os.environ["RIOT_API_KEY"]

def parse_text(text):
	split_sums= text.splitlines()
	sum_names = []
	for summoner in split_sums:
		phrase_array= summoner.split(' ')
		sum_names.append(phrase_array[0])
	return sum_names

#parse_text(example_text)

def get_data(name):
	#for name in names:
	url = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, RIOT_API_KEY)
	response = requests.get(url)
	user_data = response.json()
	print(user_data)



#def get_best_role(name):
	#query the riot api with that name
	#store data in variable
	#analyze that data