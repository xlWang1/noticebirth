import datetime
import sxtwl
import smtplib
import email,ssl
from email.message import EmailMessage
def getlunar_day():
    tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
    solar_day = tomorrow
    year = int(solar_day[:4])
    month = int(solar_day[5:7])
    day = int(solar_day[8:])
    solar_day = sxtwl.fromSolar(year,month,day)
    lunar_date_tomorrow = "%d-%s%d-%d" % (solar_day.getLunarYear(),
                        '闰' if solar_day.isLunarLeap() else '', solar_day.getLunarMonth(), solar_day.getLunarDay())
    return lunar_date_tomorrow
def gettoday():
    tomorrow = getlunar_day()
    person = []
    with open('./info.txt',encoding='utf-8') as f:
        for info in f:
            info = info.strip().split(',')
            name = info[0]
            month_and_day = info[1]
            if info[1] == tomorrow[5:]:
                person.append([name,str(datetime.date.today() + datetime.timedelta(days=1))])
        print(person)
        return person

def sendmessage():
    with open('./授权码.txt', encoding='utf-8') as i:
        info = i.read()
        info = info.strip().split(',')
        EMAIL_ADDRESS = info[0]
        EMAIL_PASSWORD = info[1]
        receive = info[2]
    context = ssl.create_default_context()
    smtp = smtplib.SMTP_SSL("smtp.163.com", 465, context=context)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    sender = EMAIL_ADDRESS


if __name__ == '__main__':
    # gettoday()
    sendmessage()

