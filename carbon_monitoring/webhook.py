# coding: utf-8

""" отправка в чятик slack """
import json
from urllib2 import urlopen


def webhook(val, string):
    """ всего-то отправить текст urlopen'ом """
    hook = val.get('url')
    data = val.get('description')
    data['text'] = string
    urlopen(hook, data=json.dumps(data))
