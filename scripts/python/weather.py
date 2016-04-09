# -*- coding:utf-8 -*-
import sys
import pywapi
import json

### Const

### Sub Function
def get_weather(locale):
    weather = pywapi.get_weather_from_yahoo(locale)
    return weather

def print_weather(weather,num):
    if 0 <= num and num <= 4:
        high = weather['forecasts'][num]['high']
        low = weather['forecasts'][num]['low']
        txt = weather['forecasts'][num]['text']
        city = weather['location']['city']
        print "%s : \"%s\" 最高気温 %s℃ 最低気温 %s℃" % (city.encode('utf-8'), txt.encode('utf-8'), high.encode('utf-8'), low.encode('utf-8'))


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
    tokyo_weather = get_weather(tokyo_locale)
    manila_weather = get_weather(manila_locale)
    
    # print date
    print_date(num)
    # print weather
    print_weather(manila_weather,num)
    print_weather(tokyo_weather,num)

#    print json.dumps(tokyo_weather, separators=(',',':'), indent=4)
