# coding: utf-8
"""
Проверяет значения метрик.
Если состояние изменилось - вызывает соответствующее событие.
При наступлении события проверяется как давно алертило по нему в последний раз,
если достаточно давно - добавляется в список событий о которых нужно алертить.
Затем события агрегируются по получателям и отсылаются им скопом.
"""

import os
import sys
from carbon_monitoring.alert import alert
from carbon_monitoring.metrics import metrics_load, eval_state
from carbon_monitoring.influxdb import QUERY

__author__ = 'Oleg Strizhechenko <oleg.strizhechenko@gmail.com>'

def process_metric(metric):
    """ обработка одной метрики """
    value = QUERY(metric)
    state = eval_state(metric, value)
    print "%s: %d (%s)" % (metric['name'], value, state)
    if not state == 'OK' and '--dry' not in sys.argv:
        alert(metric, state, value)

def main():
    """ проход по всем метрикам """
    metrics = metrics_load(os.environ.get('METRICS'))
    for metric in metrics:
        process_metric(metric)


if __name__ == '__main__':
    main()
