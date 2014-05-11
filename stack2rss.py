#!/usr/bin/env python

from datetime import datetime
from flask import Flask, render_template, render_template_string, request, url_for
from json import load
import PyRSS2Gen
import requests

def timestamp(ts):
    pass

def translate(text):
    pass

app = Flask(__name__)
app.jinja_env.globals.update(timestamp=timestamp, translate=translate)

# Load the list of types and the fields to use
with open('types.json', 'r') as f:
    types = load(f)

def process_item(item, type_):
    """Expand the templates for the specified item."""
    params = {}
    for k, v in type_.items():
        params[k] = render_template_string(v, **item)
    return PyRSS2Gen.RSSItem(**params)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/<path:method>')
def method(method):
    """Display the specified API method as an RSS feed."""
    params = dict(request.args)
    params.update({
        'filter': '!)*M9.fSWn.729PmhIC)EmDAcZu2fDM.QX6OES2lJ9SKGJ.6y.efUtoqwdSIDfwDgj.DHrkL.1(4eDh4-_i07kVX)0VlzJ(T5kQpKZ5d_ZAAfWnyeErxmuCe46PAnssLSJya4.)bZMfhwY3P(wCBvL',
    })
    data = requests.get('http://api.stackexchange.com/2.2/%s' % method, params=params).json()
    type_ = types[data['type']]
    feed = PyRSS2Gen.RSS2(
        title='Stack2RSS Custom Feed',
        link=request.url_root,
        description='A custom RSS feed for the "/%s" Stack Exchange API method.' % method,
        lastBuildDate=datetime.now(),
        items=[process_item(i, type_) for i in data['items']]
    )
    return str(feed.to_xml())

if __name__ == '__main__':
    app.debug = True
    app.run()
