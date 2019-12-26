# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from datetime import datetime
from lektor.types import DateType, DateTimeType
from jinja2 import Undefined

def current_date():
    return datetime.now().date()

def compare_dates(dt1, dt2):
    # check if dt1 > dt2
    return dt1 >= dt2

class CompareDatesPlugin(Plugin):
    name = 'Compare Dates'
    description = u'Add your description here.'

    def dt1_greater_dt2(self, dt1, dt2):
        # check if dt1 > dt2
        return dt1 >= dt2

    def on_process_template_context(self, context, **extra):
        def test_function():
            return 'Value from plugin %s' % self.name
        context['test_function'] = test_function

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['current_date'] = current_date
        self.env.jinja_env.filters['compare_dates'] = compare_dates

        self.env.jinja_env.globals.update({
            'current_date': current_date,
            'compare_dates': compare_dates
        })
