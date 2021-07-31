import requests
BASE = "http://127.0.0.1:80/"
data = [{"name": "Bitcoin", "asset_type": "Cryptocurrency", "ticker": "BTC"}, {"name": "Ethereum", "asset_type": "Cryptocurrency", "ticker": "ETH"}, {"name": "Doge Coin", "asset_type": "Cryptocurrency", "ticker": "DOGE"}, {"name": "Cardano", "asset_type": "Cryptocurrency", "ticker": "ADA"}, {"name": "SushiSwap", "asset_type": "Cryptocurrency", "ticker": "SUSHI"}]
requests.patch(BASE + "market/0", {"name": "Test"})
for i in range(len(data)):
    response = requests.put(BASE + "market/" + str(i), data[i])
    print(response.json())
for i in range(len(data)):
    response = requests.get(BASE + "market/" + str(i))
    print(response.json())
response = requests.patch(BASE + "market/0", {"name": "FakeCoin"})
print(response)
response = requests.delete(BASE + "market/0")
print(response)
