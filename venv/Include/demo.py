import urllib.request
from lxml import etree
import re

params = {'sortname': 'BGTIME', 'sortorder': 'sortorder', 'xzqh': '130000', 'query': '', 'rp': '15', 'page': '1'}
data = bytes(urllib.parse.urlencode(params), encoding='utf8')
print(data)
response = urllib.request.urlopen('http://tzxm.hbzwfw.gov.cn/tzxmweb/main/gsxx', data=data)
response = response.read().decode('utf-8')
html = etree.HTML(response)
html_title = html.xpath("//*[@id='listForm']//table[@class='ej_zjfw_list']//tr/td[2]//@title")
html_code = html.xpath("//*[@id='listForm']//table[@class='ej_zjfw_list']//tr/td[2]//a//@href")
pattern = re.compile(r'[0-9]{4}-[0-9]{6}-[0-9]{2}-[0-9]{2}-[0-9]{6}')
for index in range(len(html_title)):
    print(pattern.search(html_code[index]).group()+html_title[index])