# coding: utf-8
"""
всё связанное с алертами

поддерживаемые типы:
- twitter(username)
- email(email)
- sms(phone)
- webhook(url)
- execute(file)
- slack(channel)
"""

from carbon_monitoring.mail import email
from carbon_monitoring.twitter import twitter
from carbon_monitoring.slack import slack
from carbon_monitoring.webhook import webhook
from carbon_monitoring.sms import sms
from carbon_monitoring.execute import execute


def choose_alert_func(alert_type):
    """ отдаёт функцию с сигнатурой alert_data, string по строке-типу алерта"""
    if alert_type == 'twitter':
        return twitter
    if alert_type == 'email':
        return email
    if alert_type == 'slack':
        return slack
    if alert_type == 'webhook':
        return webhook
    if alert_type == 'sms':
        return sms
    if alert_type == 'execute':
        return execute
    raise NotImplementedError(alert_type)


def alert(metric, state, value):
    """ создание алертов """
    for val in metric.get('alerts').values():
        string = "%s: %s=%d" % (state, metric['name'], value)
        alert_func = choose_alert_func(val.get('type'))
        try:
            print val.get('type')
            alert_func(val, string)
        except Exception as error:
            print error
