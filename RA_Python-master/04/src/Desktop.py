# -*- coding: utf-8 -*-

import subprocess


class Desktop(object):
    __notifier_util = 'notify-send'
    __xsel_util = 'xsel'

    @classmethod
    def send_notification(cls, title, body):
        subprocess.call((cls.__notifier_util, title, body))

    @classmethod
    def get_selection(cls):
        return subprocess.check_output([cls.__xsel_util, '-o']).decode()
