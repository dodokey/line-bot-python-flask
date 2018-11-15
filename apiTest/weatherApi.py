# connect api
import sys
sys.path.append('..')
import requests
import json
try:
    from apiTest.authorizationkey import *
except:
    from authorizationkey import *


def whatIsTheWeather(time, location):
    header = {'authorizationkey': weatherKey,
              'locationName': location,
              'elementName': 'Wx,PoP,MinT,MaxT,CI'}
    r = requests.get(
        'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001', params=header)
    data = r.content.decode("utf-8")
    z = json.loads(data)
    WxData = z['records']['location'][0]["weatherElement"][0]
    PoPData = z['records']['location'][0]["weatherElement"][1]
    MinTData = z['records']['location'][0]["weatherElement"][2]
    CITData = z['records']['location'][0]["weatherElement"][3]
    MaxTData = z['records']['location'][0]["weatherElement"][4]

    # ==return dict something: weather, minTemperature, warning
    weather = WxData['time'][time]['parameter']['parameterName']
    rainProbability = PoPData['time'][time]['parameter']['parameterName']
    minTemperature = MinTData['time'][time]['parameter']['parameterName']
    MaxTemperature = MaxTData['time'][time]['parameter']['parameterName']
    bodyfeel = CITData['time'][time]['parameter']['parameterName']

    returnData = {}
    returnData['weather'] = weather
    returnData['rainProbability'] = rainProbability
    returnData['minT'] = minTemperature
    returnData['MaxT'] = MaxTemperature
    returnData['bodyfeel'] = bodyfeel
    # ==return dict something: weather, minTemperature, warning
    return returnData
    #目前天氣, 最低溫, 警告訊息


if __name__ == '__main__':
    weatherAnswer = whatIsTheWeather(2, '新竹市')
    print('好呀好呀 \n' + '新竹市'+'稍晚的天氣是\n'+weatherAnswer['weather']+'\n氣溫是'+weatherAnswer['minT'] +
          '到'+weatherAnswer['MaxT']+'度C\n降雨機率'+weatherAnswer['rainProbability'] + '％\n(｡◕∀◕｡)')
