# _*_ coding: UTF-8 _*_
# @Time     :2024/1/2 19:19
# @Author   :xiaolong wang
# @File     :pushwheather.py
import pushweather
import Schedule
import time
def start_run(city):
    try:
        pushweather.GetWxToken()
        pushweather.GetWheatherInfo(city)
    except Exception as err1:
        print(err1)
    try:
        Schedule.Comparison()
    except Exception as err2:
        print(err2)

if __name__ == '__main__':
    start_run(['嘉兴市南湖区', '成都市武侯区'])



