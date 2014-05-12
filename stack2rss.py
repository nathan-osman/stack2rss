#!/usr/bin/env python

from datetime import datetime
from email import utils
from flask import Flask, render_template, render_template_string, request, url_for
from json import load
import requests

from feed import RSSFeed

def timestamp(ts):
    """Formats timestamps as RFC822 dates."""
    return utils.formatdate(ts)

def translate(text):
    """Converts this_type_of_text to This Type of Text."""
    return ' '.join([p.capitalize() for p in text.split('_')])

app = Flask(__name__)
app.jinja_env.globals.update(timestamp=timestamp, translate=translate)

# Load the config file
with open('config.json', 'r') as f:
    config = load(f)

# Load the list of types and the fields to use
with open('types.json', 'r') as f:
    types = load(f)

def process_item(item, type_):
    """Expand the templates for the specified item."""
    params = {}
    for k, v in type_.items():
        value = render_template_string(v, **item)
        if value:
            params[k] = value
    return params

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html', version='2.2')

@app.route('/<version>/<path:method>')
def method(version, method):
    """Display the specified API method as an RSS feed."""
    params = dict(request.args)
    params.update({
        'filter': '-cMqQU)2Ngv7r(VTGLvhKZnEIDGH09-IxaIfPU3vLaIXPO*dlV0SQg3._npJh3Qj1ah(aRM8jjRvI_xG9OPgURzV(xF.qBi6I1C-r4h088reO*6s-cXlFwv0lvo2(n4o-CVp4K5XZtXS_jePvw2r4H',
        'key': config['key'],
    })
    data = requests.get('http://api.stackexchange.com/%s/%s' % (
        version,
        method,
    ), params=params).json()
    type_ = types[data['type']]
    feed = RSSFeed(
        'Stack2RSS Custom Feed',
        'A custom RSS feed for the "/%s" Stack Exchange API method.' % method
    )
    for i in data['items']:
        feed.append_item(**process_item(i, type_))
    return feed.get_xml()

if __name__ == '__main__':
    app.debug = True
    app.run()
