# -*- coding:utf-8 -*-
import sys
import json
import urllib2 as request

### Const

### Sub Function
def get_weather(locale):
  #  try :
    
    if locale == "tokyo":
        api_req = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22tokyo%2C%20jp%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    elif locale == "manila":
        api_req = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22manila%2C%20ph%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    response = request.urlopen(api_req)
    weather_uni = response.read()
    response.close()
    weather = json.loads(weather_uni)
  #  weather = pywapi.get_weather_from_yahoo(locale)
  #  weather = pywapi.get_weather_from_google(locale)
  #  weather = pywapi.get_weather_from_noaa('KJFK')
  #  except:
  #      print "Failed to get Web API response"
  #      quit()
    return weather["query"]["results"]["channel"]
    
def cal_temp(temp_f):
    temp = 5 * (temp_f - 32) / 9
    return temp

def print_weather(weather,num):
    if 0 <= num and num <= 4:
        high_f = weather['item']['forecast'][num]['high']
        low_f = weather['item']['forecast'][num]['low']
        txt = weather['item']['forecast'][num]['text']
        city = weather['location']['city']
        
        high = cal_temp(int(high_f))
        low = cal_temp(int(low_f))

        print "%s : \"%s\" 最高気温 %d℃ 最低気温 %d℃" % (city.encode('utf-8'), txt.encode('utf-8'), high, low)


def set_date(num):
    date = ""
    if num == 0:
        date = "今日"
    elif num == 1:
        date = "明日"
    elif num == 2:
        date = "明後日"
    else:
        date = str(num) + "日後"
    return date

def print_date(num):
    if num < 0:
        print "もの寂しげに過去をみるな、それは二度と戻って来ないのだから。抜け目なく現在を収めよ、それは汝だ。影のような未来に向って進め、怖れずに雄々しい勇気をもって。"
        quit()
    elif num > 4:
        print "過去は変えられない。だが未来は変えられる。だから今を大切にしよう"
        quit()
    date = set_date(num)
    print "===== %sの天気 =====" % date


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) > 2:
        print "Usage : python %s filename" % argv[0]
        quit()
    elif len(argv) == 2:
        num = int(argv[1])
    else:
        num = 0

    # URL : https://weather.com/weather/today/l/JAXX0085:1:JA
    manila_locale="RPXX0017"
    tokyo_locale="JAXX0085"

    # Get webinfo
    tokyo_weather = get_weather("tokyo")
    manila_weather = get_weather("manila")
    
    # print date
    print_date(num)
    # print weather
    print_weather(manila_weather,num)
    print_weather(tokyo_weather,num)

#    print json.dumps(tokyo_weather, separators=(',',':'), indent=4)
