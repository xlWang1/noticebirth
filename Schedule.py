import datetime
import sxtwl
import smtplib
import email,ssl
from email.header import Header
from email.mime.text import MIMEText
import logging
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
def Comparison():
    tomorrow = getlunar_day()
    with open('./info.txt',encoding='utf-8') as f:
        for info in f:
            info = info.strip().split(',')
            name = info[0]
            month_and_day = info[1]

            if info[1] == tomorrow[5:]:
                date = str(datetime.date.today() + datetime.timedelta(days=1))
                sendmessage(name,month_and_day,date)
            else:
                print("nothing")

def sendmessage(name,month_and_day,date):
    with open('./授权码.txt', encoding='utf-8') as i:
        info = i.read()
        info = info.strip().split(',')
<<<<<<< HEAD
        EMAIL_ADDRESS = info[0] #发送人
        EMAIL_PASSWORD = info[1] #密码
        receive = info[2] #接受人
    mail_content = f"助手提醒：明天是{date},农历{month_and_day},{name}的生日~~"
    smtp_server = 'smtp.163.com'
    subject = "生日提醒"
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['subject'] = Header(subject, 'utf-8')
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receive
    smtp = smtplib.SMTP_SSL(smtp_server, 465)
    smtp.helo(smtp_server)
    smtp.ehlo(smtp_server)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    logging.info("Start send Email....")
    smtp.sendmail(EMAIL_ADDRESS, receive, msg.as_string())
    smtp.quit()
    logging.info("Send End!")

=======
        EMAIL_ADDRESS = info[0] #发送地址
        EMAIL_PASSWORD = info[1] #密码
        receive = info[2] #接受地址
    context = ssl.create_default_context()
    smtp = smtplib.SMTP_SSL("smtp.163.com", 465, context=context)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    subject = "邮件标题"
    body = "主体"
    msg = f"Subject: {subject}\n\n{body}"
>>>>>>> c531b845b6a7ec52ceb72dfe3a88cccf5684fd99
    

if __name__ == '__main__':
   Comparison()


