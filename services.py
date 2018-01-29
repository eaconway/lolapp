import string, os
import requests
from pprint import pprint
from flask import request

RIOT_API_KEY = os.environ["RIOT_API_KEY"]

def parse_text(text):
	split_sums= text.splitlines()
	sum_names = []
	for summoner in split_sums:
		phrase_array= summoner.split()
		sum_names.append(phrase_array[0])
	return sum_names

#parse_text(example_text)

def get_data(name):
	#for name in names:
	url = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, RIOT_API_KEY)
	response = requests.get(url)
	user_data = response.json()
	print(user_data)

def get_account_id(name):
	url = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name, RIOT_API_KEY)
	response = requests.get(url)
	user_data = response.json()
	return user_data["accountId"], user_data["id"], user_data["profileIconId"]

def get_recent_matches(account_id):
	url = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{}/recent?api_key={}".format(account_id, RIOT_API_KEY)
	response = requests.get(url)
	user_data = response.json()
	return user_data

def sort_roles(recent_matches):
	matches = recent_matches["matches"]
	pot_lanes = {}
	for match in matches:
		lane = match["lane"]
		if lane not in pot_lanes:
			pot_lanes[lane] = 0
		pot_lanes[lane]+=1
	sorted_items = sorted(pot_lanes.items(), key=lambda item: item[1], reverse=True)
	print (sorted_items[:2])


def wl_ratio(recent_matches):
	asdf

def get_summoner_icon(account_id):

def analyze_summoner(name):
	account_id, summoner_id, summoner_icon = get_account_id(name)
	get_summoner_icon(summoner_id)
	recent_matches = get_recent_matches(account_id)
	mp_roles = sort_roles(recent_matches)
	wl_ratio = win_loss_ratio(recent_matches)
	#pprint(recent_matches)


#def get_best_role(name):
	#query the riot api with that name
	#store data in variable
	#analyze that data