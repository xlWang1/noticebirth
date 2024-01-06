# _*_ coding: UTF-8 _*_
# @Time     :2024/1/2 19:19
# @Author   :xiaolong wang
# @File     :pushwheather.py
import pushweather
import Schedule
import time
def start_run():

    pushweather.GetWxToken()
    pushweather.GetWheatherInfo(['嘉兴市南湖区', '成都市武侯区'])
    Schedule.Comparison()

if __name__ == '__main__':
    start_run()



