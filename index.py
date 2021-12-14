import time
import requests
import ctypes
import os
import logging


def return_API():
    start = time.time()
    # time.sleep(1)
    try:
        response = requests.get(
            'https://restapi.amap.com/v3/weather/weatherInfo?city=420111&key=dfe3428e3e140ffd7bb365eb59c46f96&extensions=base')
        if response.status_code == 200:
            data = response.json()
            return (data['lives'][0].get('weather'))
    except Exception as e:
        exeTime = time.localtime()
        path = '.\\getErr {}-{}-{}-{}-{}-{}{}'.format(exeTime.tm_year, exeTime.tm_mon, exeTime.tm_mday, exeTime.tm_hour,
                                                      exeTime.tm_min, exeTime.tm_sec, '.txt')
        logging.basicConfig(filename=path, format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                            datefmt='%a %d %b %Y %H:%M:%S')
        logging.warning(e)
        end = time.time()
        if end - start > 10:
            return '晴'



def APItoWeatherCode():
    weather = return_API()
    weatherCode = 0
    if weather in ['晴', '少云']:
        weatherCode = 9
    elif weather == '晴间多云 ':
        weatherCode = 1
    elif weather in ['多云', '阴']:
        weatherCode = 5
    elif weather in ['有风', '平静', '微风', '和风', '清风']:
        weatherCode = 2
    elif weather in ['强风/劲风', '疾风', '大风', '烈风', '风暴', '狂爆风', '飓风', '热带风暴']:
        weatherCode = 7
    elif weather in ['霾', '中度霾', '重度霾', '严重霾', '浮尘', '扬沙', '沙尘暴', '强沙尘暴', '龙卷风', '雾', '浓雾', '强浓雾', '轻雾', '大雾', '特强浓雾']:
        weatherCode = 4
    elif '雷' not in weather and '雨' in weather:
        weatherCode = 6
    elif '雪' in weather:
        weatherCode = 8
    elif '雷' in weather:
        weatherCode = 3
    else:
        weatherCode = 9
    return weatherCode


while True:
    try:
        photoPath = os.getcwd() + '\\weatherJPG' + '\\' + str(APItoWeatherCode()) + '.jpg'
        # photoPath=os.getcwd()+'\\weatherJPG'+'\\3.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, photoPath, 0)
        time.sleep(3600)
    except Exception as e:
        exeTime = time.localtime()
        path = '.\\setErr {}-{}-{}-{}-{}-{}{}'.format(exeTime.tm_year, exeTime.tm_mon, exeTime.tm_mday, exeTime.tm_hour,
                                               exeTime.tm_min, exeTime.tm_sec, '.txt')
        logging.basicConfig(filename=path, format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                            datefmt='%a %d %b %Y %H:%M:%S')
        logging.warning(e)



