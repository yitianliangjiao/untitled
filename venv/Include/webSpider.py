import urllib.request
import re
params = {'sortname': 'BGTIME','sortorder':'sortorder','xzqh':'130000','query':'','rp':'15','page':'1'}
data = bytes(urllib.parse.urlencode(params), encoding='utf8')
print(data)
response = urllib.request.urlopen('http://tzxm.hbzwfw.gov.cn/tzxmweb/main/gsxx', data=data)
pattern = re.compile(r'[0-9]{4}-[0-9]{6}-[0-9]{2}-[0-9]{2}-[0-9]{6}')
result = pattern.findall(response.read().decode('utf-8'))
result = set(result)
print(result)
print(len(result))