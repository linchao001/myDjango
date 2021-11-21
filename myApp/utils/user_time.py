# encoding: utf-8

from datetime import datetime

class UserTime:

    def __init__(self):
        self.format_1 = "%Y-%m-%d %H:%M:%S"

    def datetime_1(self):
        return datetime.now().strftime(self.format_1)

user_time = UserTime()