import requests
from lxml import etree
import time
remoteUrl = 'https://cn.bing.com/'
UserAgent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'


def get_img_url():
    r = requests.get(
        remoteUrl,
        headers={
            'User-Agent': UserAgent})
    print(r.status_code)
    result = r.text
    html = etree.HTML(result)
    imgurl = html.xpath('//*[@id="bgLink"]//@href')
    return remoteUrl + imgurl[0]


def getfilefromurl(fileurl):
    r = requests.get(
        fileurl,
        headers={
            'User-Agent': UserAgent})
    local = time.strftime("%Y.%m.%d")
    print(local)
    f = open('E:\wallPaper\%s.jpg' % '555', 'wb')
    f.write(r.content)
    f.close()
getfilefromurl(get_img_url())

