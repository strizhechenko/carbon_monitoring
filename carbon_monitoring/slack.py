# coding: utf-8

""" отправка в чятик slack """
import os
import json
from urllib2 import urlopen


def slack(val, string):
    """ всего-то отправить текст urlopen'ом """
    hook = os.environ.get('SLACK_HOOK_URL')
    data = val.get('description')
    data['text'] = string
    urlopen(hook, data=json.dumps(data))
