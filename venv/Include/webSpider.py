import urllib.request
import re
import time
from DBUtil import  DbBean
page = 1
o = DbBean()
while(page<3):
    time.sleep(1)
    params = {'sortname': 'BGTIME', 'sortorder': 'sortorder', 'xzqh': '130000', 'query': '', 'rp': '15', 'page': page}
    data = bytes(urllib.parse.urlencode(params), encoding='utf8')
    print(data)
    response = urllib.request.urlopen('http://tzxm.hbzwfw.gov.cn/tzxmweb/main/gsxx', data=data)
    pattern = re.compile(r'[0-9]{4}-[0-9]{6}-[0-9]{2}-[0-9]{2}-[0-9]{6}')
    result = pattern.findall(response.read().decode('utf-8'))
    result = set(result)
    for code in result:
        print(code)
        projson = {"procode": code}
        o.add(projson, "t_pro")
    page+=1
