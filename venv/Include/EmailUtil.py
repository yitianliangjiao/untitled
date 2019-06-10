# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import configparser

class DbBean:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read('resource/demo.conf')
        self.myEmailHost = conf.get('myemail', 'myEmailHost')
        self.myEmailAccount = conf.get('myemail', 'myEmailAccount')
        self.myEmailPassword = conf.get('myemail', 'myEmailPassword')

    def sendEmail(self,sender,receivers,msg,subject):
        try:
            cc = sender
            toaddrs = [receivers] + [cc]
            print(toaddrs)
            message = MIMEText(msg, 'plain', 'utf-8')
            message['From'] = "<%s>" % sender
            message['To'] = "<%s>" % receivers
            message['Subject'] = Header(subject, 'utf-8')
            message['Cc'] = "<%s>"  % sender
            smtpObj = smtplib.SMTP(self.myEmailHost,25)
            smtpObj.set_debuglevel(1)
            smtpObj.login(self.myEmailAccount, self.myEmailPassword)
            smtpObj.sendmail(sender, toaddrs, message.as_string())
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


sender = '15732136845@163.com'
receivers = '1945623989@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
subject = '抓紧参加这次会议'
d = DbBean()
d.sendEmail(sender,receivers,message,subject)


