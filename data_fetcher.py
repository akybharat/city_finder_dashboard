import config as cfg
import requests, json
url = cfg.url

def get_data():
  city_list = []
  response = requests.get(url).json()
  for i in response['list']:
    city_list.append(i['name'].lower())
  return list(set(city_list))

def city_details(start_letter):
    city_list = get_data()
    city_out = [ city for city in city_list if city.startswith(start_letter.lower())]
    return city_out, len(city_out)
