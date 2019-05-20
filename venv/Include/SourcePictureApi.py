import requests
import random
import json
searchURL = 'https://api.unsplash.com/photos?client_id=%s&page=%s&per_page=%s&order_by=%s'
client_id = '31a299e86e64a863b9cf644519dd6e0598fdd58cc17949a0a946d44e0375d206'
searchURL = searchURL % (client_id,1,10,'latest')
response = requests.get(searchURL)
print(u'正在从Unsplash上搜索图片...')
print(response.text)
#data = json.loads(response.text)
