# _*_ coding: UTF-8 _*_
# @Time     :2024/1/2 19:19
# @Author   :xiaolong wang
# @File     :pushwheather.py
import pprint

import requests
import json
import time
import datetime
template_id = 'YeKkyl96XmYJOZ7RbAZeht_Eb1WljzzQDl-f9Ma2KYU'
def GetWheatherInfo(city_name):
    global city
    city = city_name
    cityinfourl = f'https://geoapi.qweather.com/v2/city/lookup?location={city}&key=a39074eb6541477cbb1b2c1dfd738481'
    city_id= requests.get(cityinfourl).json()['location'][0]['id']#'101270101'
    wheather_url = f'https://devapi.qweather.com/v7/weather/3d?location={city_id}&key=a39074eb6541477cbb1b2c1dfd738481'
    wheather_data= requests.get(wheather_url).json()['daily'][0]
    #预报日期
    date = wheather_data['fxDate']
    #天气状况
    textDay = wheather_data['textDay']
    #日出时间
    sunrise = wheather_data['sunrise']
    #日落时间
    sunset = wheather_data['sunset']
    #最高气温
    tempMax = wheather_data['tempMax']
    #最低气温
    tempMin = wheather_data['tempMin']
    #风向
    windDirDay = wheather_data['windDirDay']
    #风力
    windScaleDay = wheather_data['windScaleDay']
    #降雨量
    precip = wheather_data['precip']
    global wheather_info
    wheather_info = [date,city,textDay,sunrise,sunset,tempMax,tempMin,windDirDay,windScaleDay,precip]

def GetWxToken():
    global appid,secret
    appid = 'wxbe3dd6f4aaddc86f'
    secret = 'cc79700d7668dcf42590795d94051f00'
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
    global tokendata
    tokendata = requests.get(url).json()['access_token']

def SendMessage(open_id):
    sendMessage_url=f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={tokendata}"
    messagedata = {
        "touser": open_id,
        "template_id": template_id,
        "appid": appid,
        "topcolor": "#FF0000",
        "data":{
            'date':{
                    "value":wheather_info[0],
                    "color": "#6B6A66"
                    },
            'city':{
                    "value":wheather_info[1],
                    "color": "#F9AD08"
                    },
            'textDay':{
                    "value":wheather_info[2],
                    "color": "#F9AD08"
                    },
            'sunrise':{
                    "value":wheather_info[3],
                    "color": "#F9AD08"
                    },
            'sunse':{
                    "value":wheather_info[4],
                    "color": "#F9AD08"
                    },
            'tempMax':{
                    "value":wheather_info[5]+"度",
                    "color": "#F9AD08"
                    },
            'tempMIN':{
                    "value":wheather_info[6]+"度",
                    "color": "#6B6A66"
                    },
            'windDirDay':{
                    "value":wheather_info[7],
                    "color": "#F9AD08"
                    },
            'windScaleDay':{
                    "value":wheather_info[8]+"级",
                    "color": "#F9AD08"
                    },
            'precip':{
                    "value":wheather_info[9]+"毫米",
                    "color": "#F9AD08"
                    },
            'zhuyu':{
                    "value":"你今天也要开心哦~~",
                    "color": "#6B6A66"
                    }
        }
    }

    resp = requests.post(sendMessage_url, data=json.dumps(messagedata)).json()
    print(resp)

if __name__ == '__main__':
    GetWheatherInfo('成都')
    GetWxToken()
    SendMessage('o4qtq6wS9zthnKP8z5f74e1m_vrI')



