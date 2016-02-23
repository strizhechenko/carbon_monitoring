# coding: utf-8
""" всё связанное с метриками """
import os
import json


def eval_state(metric, value):
    """ вычисляет состояние метрики """
    if metric.get('error')(value):
        return 'ERROR'
    if metric.get('warning')(value):
        return 'WARNING'
    return 'OK'


def metric_load(filename):
    """ возвращает dict с описанием метрики и лямбдами для варнингов """
    with open(filename) as config:
        metric = json.load(config)
        for key in ('warning', 'error'):
            metric[key] = eval(metric[key])
        metric['name'] = filename.split('/')[-1].replace('.json', '')
        return metric
    raise IOError(u'Проклятые англичане спиздили файл, пока мы его читали')


def metrics_load(directory):
    """ возвращает список dict'ов с описаниями метрик """
    metrics = []
    for config in [f for f in os.listdir(directory) if f.endswith('.json')]:
        metrics.append(metric_load('metrics/' + config))
    return metrics
