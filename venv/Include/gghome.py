import requests
import json

longtime = 900
minnum = 3

remoteUrl = "https://gongjiao.xiaojukeji.com/api/transit/line/location?from=webapp&wsgsig=dd03-NDQT5%2Fr2kA66DZ90c%2FW%2BBdYLWqx2052BadX1dFZKWqx1C1TID%2FNMAk%2F3n961CPUDgktBDUq2na94dwO80ln1Adk3nFIAf5YAcA7eehPKnAa6f5Ta"
UserAgent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
params = {"line_stops":"27780929343910022:27780929999380022:0","city":"22","imei":"-1327242286385646123","channel":"1200","pages":6,"oid":"-1327242286385646123","token":"bPaEu8v5c7PcIeQZbI3wzk44ezX06B6heEMzPy0xssgkzEvKwzAMAOG7zFoEybJsR7f5H-lj40JLVyF3LyWrWQx8O1NJfNFFEaaRJsxCuqqqMJ20HmuJEa0PtyrMSn5XkCD8nPkly_BiVYd5q6248E92YSN3Xo_3828j7RAupEWsEWvTLlxJLLoX8zZqINxO8k7q8QkAAP__","lng":"114.50497119761405","lat":"38.04392867553338"}
r = requests.get(
        remoteUrl,
        params,
        headers={
            'User-Agent': UserAgent})
print(r.text)
rjson = json.loads(r.text)
buses = rjson.get("location")[0].get("buses")
gbus = 0
for index in range(len(buses)):
    bus = buses[index]
    if(bus.get("time")>=0 and bus.get("time")<=longtime):
        gbus = gbus+1
        print(bus)
if(gbus >= minnum):
    print(666)
else:
     print(gbus)