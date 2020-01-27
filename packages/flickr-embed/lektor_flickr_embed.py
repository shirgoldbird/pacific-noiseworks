# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.types import Type
import re

def create_responsive_embed(embed_html):
    return re.sub(r'="([0-9]+)"', '="100%"', embed_html)

# Wrapper with an __html__ method prevents
# Lektor from escaping HTML tags.
class HTML(object):
    def __init__(self, html):
        self.html = html

    def __html__(self):
        return self.html

class FlickrEmbedType(Type):
    widget = 'multiline-text'

    def value_from_raw(self, raw):
        return HTML(create_responsive_embed(raw.value or u''))

class FlickrEmbedPlugin(Plugin):
    name = u'Flickr Embeds'
    description = u'Adds Flickr embeds and field type to Lektor.'

    def on_setup_env(self, **extra):
        # Derives type name "flickrembed" from class name.
        self.env.add_type(FlickrEmbedType)
