# coding: utf-8
"""
Проверяет значения метрик.
Если состояние изменилось - вызывает соответствующее событие.
При наступлении события проверяется как давно алертило по нему в последний раз,
если достаточно давно - добавляется в список событий о которых нужно алертить.
Затем события агрегируются по получателям и отсылаются им скопом.
"""

import os
# import sys
# import json
from time import time, sleep
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from carbon_monitoring.alert import alert
from carbon_monitoring.metrics import metrics_load, eval_state
from carbon_monitoring.influxdb import QUERY

__author__ = 'Oleg Strizhechenko <oleg.strizhechenko@gmail.com>'


logging.basicConfig(level=logging.WARN,
                    format='%(created)d - %(name)s: %(message)s')


def process_metric(metric, storage):
    """ обработка одной метрики """
    value = QUERY(metric)
    state = eval_state(metric, value)
    data = (metric['name'], value, state)
    logging.warning("query: %s", data)
    if not state == 'OK':  # and '--dry' not in sys.argv:
        storage.append(data)


def process_alerts(metric, storage, data):
    """ обработка алярмов (группировка) """
    alerts = set([tuple(m) for m in storage if m[0] == metric.get('name')])
    for __alert in alerts:
        if data['last'] + data['rate'] > int(time()):
            continue
        logging.warning('alert! %s %d', str(__alert), data['rate'])
        data['last'] = int(time())
        alert(metric, __alert[2], __alert[1])


def main():
    """ проход по всем метрикам """
    sched = BlockingScheduler()
    storage = []
    metrics = metrics_load(os.environ.get('METRICS'))
    for metric in metrics:
        trigger = IntervalTrigger(**metric.get('check_freq'))
        sched.add_job(process_metric, trigger, args=(metric, storage))
        sleep(0.2)
    for metric in metrics:
        for data in metric.get('alerts').values():
            data['last'] = int(time())
            trigger = IntervalTrigger(**metric.get('check_freq'))
            sched.add_job(process_alerts, trigger, args=(metric, storage, data))
            sleep(0.2)
    sched.start()


if __name__ == '__main__':
    main()
