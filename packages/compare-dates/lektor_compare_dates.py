# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from datetime import datetime
from lektor.types import DateType, DateTimeType

def current_datetime():
    return datetime.now()

def compare_dates(dt1, dt2):
    # check if dt1 > dt2
    return dt1 >= dt2

class CompareDatesPlugin(Plugin):
    name = u'Compare Dates'
    description = u'Generate the current datetime with current_datetime, or see if one date is >= another with compare_dates'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['current_datetime'] = current_datetime
        self.env.jinja_env.filters['compare_dates'] = compare_dates

        self.env.jinja_env.globals.update({
            'current_datetime': current_datetime,
            'compare_dates': compare_dates
        })
