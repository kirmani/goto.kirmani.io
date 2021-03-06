#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Sean Kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.
import os

from forms import ShortLinkForm
from flask import Flask,redirect
from flask import render_template
from python import tools
from python import shortlink
import json

SHORT_LINK_DATA_FILE = os.path.join(os.path.dirname(__file__),
    'data/shortlinks.json')

app = Flask(__name__)
app.secret_key = 'kirmani_io_secret_key'

@app.route('/', methods=['GET', 'POST'])
def hello():
  form = ShortLinkForm()
  if form.validate_on_submit():
    if not tools.IsValidUrl(form.url.data):
      return 'Invalid URL'
    short_links = _LoadShortLinks()
    if form.short_link.data in short_links:
      return 'Shortlink already exists.'
    short_links[form.short_link.data] = {
        shortlink.Shortlink.URL: form.url.data,
        shortlink.Shortlink.COUNT: 0
    }
    _WriteShortLinks(short_links)
    return 'Shortlink added.'
  return render_template('index.html', form=form)

@app.route('/<shortlink_query>')
def RedirectShortLink(shortlink_query=None):
  short_links = _LoadShortLinks()
  if shortlink_query not in short_links:
    return 'Shortlink not found'
  short_links[shortlink_query][shortlink.Shortlink.COUNT] += 1
  _WriteShortLinks(short_links)
  return redirect(short_links[shortlink_query][shortlink.Shortlink.URL],
      code=302)

def _LoadShortLinks():
  try:
    with open(SHORT_LINK_DATA_FILE, 'r+') as f:
      return json.load(fp=f)
  except IOError:
    return {}

def _WriteShortLinks(data):
  j = json.dumps(data, indent=4)
  with open(SHORT_LINK_DATA_FILE, 'w') as f:
    f.write(j)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 33507))
  app.debug = True;
  app.run(host='0.0.0.0', port=port)
