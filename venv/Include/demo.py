import urllib.request
from lxml import etree

params = {'sortname': 'BGTIME', 'sortorder': 'sortorder', 'xzqh': '130000', 'query': '', 'rp': '15', 'page': '1'}
data = bytes(urllib.parse.urlencode(params), encoding='utf8')
print(data)
response = urllib.request.urlopen('http://tzxm.hbzwfw.gov.cn/tzxmweb/main/gsxx', data=data)
response = response.read().decode('utf-8')
html = etree.HTML(response)
#html_data = html.xpath("//*[@id='listForm']/table/tr/td[3]/table[2]/tbody/tr[2]/td[2]")
html_data = html.xpath("//*[@id='listForm']//table[@class='ej_zjfw_list']//td//@title")
print (html_data)