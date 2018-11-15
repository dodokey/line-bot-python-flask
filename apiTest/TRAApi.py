from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint
import json
try:
    from apiTest.authorizationkey import *
except:
    from authorizationkey import *


class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'),
                          ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }


def checkStationID(stationName):
    a = Auth(TRAapp_id, TRAapp_key)

    response = request(
        'get', 'http://ptx.transportdata.tw/MOTC/v2/Rail/TRA/Station?$format=JSON', headers=a.get_auth_header())
    z = json.loads(response.content.decode("utf-8"))
    print(type(z))
    for zz in z:
        if zz['StationName']['Zh_tw'] == stationName:
            print(zz['StationID'])


if __name__ == '__main__':
    checkStationID('新竹')
    # a = Auth(app_id, app_key)

    # response = request(
    #     'get', 'http://ptx.transportdata.tw/MOTC/v2/Rail/TRA/Station?$format=JSON', headers=a.get_auth_header())
    # z = json.loads(response.content.decode("utf-8"))
    # for zz in z:
    #     # if zz['StationID'] == '1421':
    #     #     print(zz)
    #     #     print('==========')
    #     if zz['StationName']['Zh_tw'] == '員林':
    #         print(zz['StationID'])
    #         print('==========')
    #     # zz['StationName']['Zh_tw'] for zz in z if zz['StationID'] == '1421'
    # # print(zz for zz in z if zz['StationID'] == '1421')
