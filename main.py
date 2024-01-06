# _*_ coding: UTF-8 _*_
# @Time     :2024/1/2 19:19
# @Author   :xiaolong wang
# @File     :pushwheather.py
import pushweather
import Schedule
import time
def start_run(city,info_add,author_add):
    try:
        pushweather.GetWxToken()
        pushweather.GetWheatherInfo(city)
    except Exception as err1:
        print(err1)
    try:
        Schedule.Comparison(info_add,author_add)
    except Exception as err2:
        print(err2)

if __name__ == '__main__':
    info_add = './info.txt'
    author_add = './authorization.txt'
    city = ['嘉兴市南湖区', '成都市武侯区']
    start_run(city,info_add,author_add)



