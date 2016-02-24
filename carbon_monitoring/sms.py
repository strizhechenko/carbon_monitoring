# coding: utf-8

import os
from urllib2 import urlopen

def sms(val, string):
    """ отправляет смс на smsc, нужно экспортнуть SMS_LOGIN/SMS_PASSWORD """
    sms_login = os.environ.get('SMS_LOGIN')
    sms_pass = os.environ.get('SMS_PASSWORD')
    owner = val.get('phone')
    url_tmplt = "http://smsc.ru/sys/send.php?login=%s&psw=%s&phones=%s&mes=%s"
    urlopen(url_tmplt % (sms_login, sms_pass, owner, string))
