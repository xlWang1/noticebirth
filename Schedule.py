import datetime
import sxtwl
def gettoday():
    today = str(datetime.date.today())
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])
    today = str(today_year)+'-'+str(today_month)+'-'+str(today_day)
    print("今天是" + today)
    person = []
    with open('./info.txt',encoding='utf-8') as f:
        for info in f:
            info = info.strip().split(',')
            name = info[0]
            month_and_day = info[1]
            this_birthday = str(today_year-1)+month_and_day
            this_birthday = getsolar(this_birthday)
            print(this_birthday)
            if today == this_birthday:
                person.append([name,today_day])
                print(person)
                return person
def getsolar(lunar_day):
    year = int(lunar_day[:4])
    month = int(lunar_day[4:6])
    day = int(lunar_day[6:])
    lunar_day = sxtwl.fromLunar(year,month,day)
    solar_date = "%d-%d-%d" % (lunar_day.getSolarYear(), lunar_day.getSolarMonth(), lunar_day.getSolarDay())
    return solar_date

if __name__ == '__main__':
    # print(getsolar('20231123'))
    gettoday()

