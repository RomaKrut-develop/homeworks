import requests

ip = "158.58.129.140"
url = "https://ipinfo.io/" + ip + "/geo"

response = requests.get(url)

r = response.json()

print(f"Country: {r["country"]}\nCity: {r["city"]}\nLot,lon: {r["loc"]}\nOrganisation: {r["org"]}")
