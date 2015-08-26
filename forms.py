#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Sean Kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.

from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required

class ShortLinkForm(Form):
  short_link = TextField('ShortLink', validators=[Required()])
  url = TextField('URL', validators=[Required()])
