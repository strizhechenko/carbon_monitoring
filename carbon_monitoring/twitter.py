# coding: utf-8
""" всё что связано с твиттером """

from twitterbot_utils import Twibot


def twitter(alert_data, string):
    """ упоминает через твитор """
    bot = Twibot()
    bot.tweet(u"%s, %s" % (alert_data['username'], string))
