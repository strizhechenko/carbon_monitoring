# coding: utf-8

""" алертинг с помощью сторонних тулз """
import subprocess


def execute(val, string):
    """вызывает указанный в конфиге бинарик и отдаёт ему строку ошибки/owner"""
    subprocess.call([val.get('exe'), string] + val.get('custom_params', []))
