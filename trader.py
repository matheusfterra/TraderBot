import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()
api_token = 'bjrXBRkA1w34VkJlZpe2pXuD9y2rzOn10wN72jtbmJOx3EQChNtCdU15vBOH'

# https://www.worldtradingdata.com/documentation?python#single-day-history

# url = 'https://api.worldtradingdata.com/api/v1/stock'
# params = {
#   'symbol': 'SNAP,TWTR,VOD.L',
#   'api_token': api_token
# }
# response = requests.request('GET', url, params=params)
#
# data=response.json()

# print(data['data'][0]['market_cap'])

url = 'https://api.worldtradingdata.com/api/v1/forex_single_day'
params = {
  'base': 'USD',
  'date': '2019-01-02',
  'api_token': 'bjrXBRkA1w34VkJlZpe2pXuD9y2rzOn10wN72jtbmJOx3EQChNtCdU15vBOH'
}
response = requests.request('GET', url, params=params)
data=response.json()
print(data)