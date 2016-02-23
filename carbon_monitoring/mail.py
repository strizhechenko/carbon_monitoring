# coding: utf-8
""" всё связанное с отправкой почты"""
import os
from smtplib import SMTP
from email.mime.text import MIMEText


def email_send(msg, server, port, password):
    """непосредственно отправка почты"""
    smtp = SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(msg['From'], password)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.close()


def email(alert_data, string):
    """export  <EMAIL> <EMAIL_PASSWORD> [<EMAIL_SERVER> <EMAIL_PORT>]"""
    msg = MIMEText(string, _charset='utf-8')
    msg['Subject'] = alert_data.get('subject', "ALARM! Проблема!")
    msg['From'] = os.environ.get('EMAIL', alert_data['email'])
    msg['To'] = alert_data['email']
    server = os.environ.get('EMAIL_SERVER', 'smtp.gmail.com')
    port = os.environ.get('EMAIL_PORT', '25')
    email_send(msg, server, port, os.environ.get('EMAIL_PASSWORD'))
