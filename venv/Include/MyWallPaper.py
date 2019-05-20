import requests
from lxml import etree
import time
import os
import win32gui,win32con,win32api
remoteUrl = 'https://cn.bing.com/'
UserAgent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
imgpath = 'E:\wallPaper\%s.jpg'


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
    f = open(imgpath % local, 'wb')
    f.write(r.content)
    f.close()
def setWallPaper(filepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面，0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, filepath, 1 + 2)

getfilefromurl(get_img_url())
local = time.strftime("%Y.%m.%d")
setWallPaper(imgpath % local)

