# coding: utf-8
""" всё связанное с influxdb """

import os
import json
from urllib import urlencode
from urllib2 import urlopen

DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = int(os.environ.get('DB_HOST', 8086))


def get_result(metric, db_host, db_port):
    """ забирает последнее значение из базы """
    db_name = metric.get('db_name', os.environ.get('DB_NAME', '_default'))
    query_tmplt = 'SELECT value FROM %s WHERE %s limit 1'
    _query = {
        'db': db_name,
        'q':  query_tmplt % (metric['name'], metric['filter']),
        'pretty': 'true',
    }
    url = "http://%s:%d/query?%s" % (db_host, db_port, urlencode(_query))
    return urlopen(url).read()


def parse_result(data):
    """ выдёргивает из ответа influxdb само значение """
    res = json.loads(data).get('results')
    if not res:
        print 'no results in response'
        return None
    series = res[0].get('series')
    if not series:
        print 'no series in result'
        return None
    value = series[0].get('values')
    if not value:
        print 'no value in series'
        return None
    return value[0][1]

QUERY = lambda metric: parse_result(get_result(metric, DB_HOST, DB_PORT))
