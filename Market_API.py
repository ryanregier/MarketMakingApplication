import requests
BASE = "http://127.0.0.1:80/"


def get_price(market_id):
    response = requests.get(BASE + str(market_id) + "/price")
    return response.json()['data']


def get_bid(market_id):
    response = requests.get(BASE + str(market_id) + "/bid")
    return response.json()['data']


def get_ask(market_id):
    response = requests.get(BASE + str(market_id) + "/bid")
    return response.json()['data']


def buy_best(market_id):
    response = requests.get(BASE + str(market_id) + "/sell")
    return response.json()['data']


def sell_best(market_id):
    response = requests.get(BASE + str(market_id) + "/buy")
    return response.json()['data']

