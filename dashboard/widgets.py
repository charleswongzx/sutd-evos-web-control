# -*- encoding: utf-8 -*-
from dashing.widgets import NumberWidget
from dashing.widgets import KnobWidget
from random import randint

users = randint(50, 100)


class SpeedWidget(KnobWidget):
    title = 'Speed'

    def get_value(self):

        return stat.o


class NewClientsWidget(NumberWidget):
    title = 'New Users'

    def get_value(self):
        global users
        users += 1
        return users

    def get_detail(self):
        global users
        return '{} actives'.format(users/3)

    def get_more_info(self):
        global users
        return '{} fakes'.format(users/10)
